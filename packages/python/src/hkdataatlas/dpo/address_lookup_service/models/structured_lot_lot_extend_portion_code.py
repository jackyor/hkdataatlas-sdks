from typing import Literal

StructuredLotLotExtendPortionCode = Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]

STRUCTURED_LOT_LOT_EXTEND_PORTION_CODE_VALUES: set[
    StructuredLotLotExtendPortionCode
] = {
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
}


def check_structured_lot_lot_extend_portion_code(
    value: str,
) -> StructuredLotLotExtendPortionCode:
    if value in STRUCTURED_LOT_LOT_EXTEND_PORTION_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STRUCTURED_LOT_LOT_EXTEND_PORTION_CODE_VALUES!r}"
    )
