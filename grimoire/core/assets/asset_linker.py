import typing
from enum import Enum
from typing import Union

from colored import Style
from glm import ivec2, ivec3

from .asset import Asset, AssetMeta
from ..generator.module import Module
from ..logger import LoggingLevel


class AssetLinker(Module):

    @Module.main
    def link_assets(self):
        for asset_type in (
            asset_type_loading_bar := self.log.progress(Asset.types, "")
        ):
            # skip child types since they already appear in their parents
            if len(asset_type.parent_types) > 0:
                continue

            asset_type_loading_bar.set_description(
                self.log.format(
                    text=f"Linking {asset_type.type_name}", level=LoggingLevel.INFO
                )[:-1]
            )

            for obj in asset_type.all():
                self.log.info(f"{Style.reset}Linking {obj.name}")
                self.link_asset(obj)

        # call on link
        for asset_type in Asset.types:
            # skip child types since they already appear in their parents
            if len(asset_type.parent_types) > 0:
                continue

            for obj in asset_type.all():
                obj.on_link()

    # This allows for fields that are annotated with Asset types that are filled with string types on loading jsons to be instead
    # swapped out for the actual Asset object.
    def link_asset(self, asset: Asset):
        for field_name, field_type in asset.get_annotations().items():
            value = getattr(asset, field_name)
            setattr(
                asset,
                field_name,
                self._get_linked_field(asset, value, field_name, field_type),
            )

    def _get_linked_field(self, asset: Asset, value, field_name: str, field_type: type):
        # If the type is an asset, link it
        if isinstance(field_type, AssetMeta) and isinstance(value, str):
            return field_type.find(value)

        # If the type is a list link the items in that list
        if self._type_eq(field_type, "list") and hasattr(field_type, "__args__"):
            t1 = field_type.__args__[0]

            if not isinstance(value, list):
                self.log.error(
                    f"Could not link {asset.name}.{field_name} - is not list type!"
                )
                return value

            return [
                self._get_linked_field(asset, item, f"{field_name}[{i}]", t1)
                for (i, item) in enumerate(value)
            ]

        # If the type is a dict, link the items in that dict
        if self._type_eq(field_type, "dict") and hasattr(field_type, "__args__"):
            t1 = field_type.__args__[0]
            t2 = field_type.__args__[1]

            if not isinstance(value, dict):
                self.log.error(
                    f"Could not link {asset.name}.{field_name} - is not dict type!"
                )
                return value

            return {
                self._get_linked_field(
                    asset, key, f"{field_type}{{key {i}}}", t1
                ): self._get_linked_field(asset, val, f"{field_type}{{value {i}}}", t2)
                for (i, (key, val)) in enumerate(value.items())
            }

        # If the type is a union, link to the first type in that union
        if (
            (
                typing.get_origin(field_type) is not None
                and typing.get_origin(field_type).__name__ == "UnionType"
            )
            or self._type_eq(field_type, "Optional")
        ) and hasattr(field_type, "__args__"):
            t1 = field_type.__args__[0]
            return self._get_linked_field(asset, value, field_name, t1)

        # If the type is an enum, find the right field in that enum
        if Enum in field_type.__mro__ and isinstance(value, str):
            return field_type[value.upper()]

        # IF the type is an ivec2, construct it
        if self._type_eq(field_type, "ivec2") and isinstance(value, list):
            return ivec2(*value)

        # IF the type is an ivec3, construct it
        if self._type_eq(field_type, "ivec3") and isinstance(value, list):
            return ivec3(*value)

        # Otherwise return own type
        return value

    def _type_eq(self, tp, name):
        return tp == name or (hasattr(tp, "__name__") and tp.__name__ == name)
