class AssetValidationState:
    def __init__(self, missing_args : list[tuple[str, type]] = None, surplus_args : list[tuple[str, type]] = None) -> None:
        self.missing_args = missing_args or []
        self.surplus_args = surplus_args or []

    def is_invalid(self):
        return len(self.missing_args) > 0

    def combine(self, other):
        return AssetValidationState(
            missing_args = self.missing_args + other.missing_args,
            surplus_args = self.surplus_args + other.surplus_args
        )