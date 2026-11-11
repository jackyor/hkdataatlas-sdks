from typing import Literal

IsCurrRelIndiv = Literal["0", "1"]

IS_CURR_REL_INDIV_VALUES: set[IsCurrRelIndiv] = {
    "0",
    "1",
}


def check_is_curr_rel_indiv(value: str) -> IsCurrRelIndiv:
    if value in IS_CURR_REL_INDIV_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {IS_CURR_REL_INDIV_VALUES!r}"
    )
