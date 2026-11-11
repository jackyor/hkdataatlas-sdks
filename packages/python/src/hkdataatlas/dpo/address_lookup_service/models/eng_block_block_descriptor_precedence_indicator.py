from typing import Literal

EngBlockBlockDescriptorPrecedenceIndicator = Literal["N", "Y"]

ENG_BLOCK_BLOCK_DESCRIPTOR_PRECEDENCE_INDICATOR_VALUES: set[
    EngBlockBlockDescriptorPrecedenceIndicator
] = {
    "N",
    "Y",
}


def check_eng_block_block_descriptor_precedence_indicator(
    value: str,
) -> EngBlockBlockDescriptorPrecedenceIndicator:
    if value in ENG_BLOCK_BLOCK_DESCRIPTOR_PRECEDENCE_INDICATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ENG_BLOCK_BLOCK_DESCRIPTOR_PRECEDENCE_INDICATOR_VALUES!r}"
    )
