from typing import Optional


class AssetValidationState:
    def __init__(
        self,
        missing_args: Optional[list[tuple[str, str]]] = None,
        surplus_args: Optional[list[tuple[str, str]]] = None,
    ) -> None:
        self.missing_args: list[tuple[str, str]] = missing_args or []
        self.surplus_args: list[tuple[str, str]] = surplus_args or []

    def is_invalid(self) -> bool:
        return len(self.missing_args) > 0

    # Adds two validation states in case two
    def combine(self, other) -> "AssetValidationState":
        return AssetValidationState(
            missing_args=self.missing_args + other.missing_args,
            surplus_args=self.surplus_args + other.surplus_args,
        )
