from typing import Literal

GetBankComplaintProgressSegment = Literal["new", "old"]

GET_BANK_COMPLAINT_PROGRESS_SEGMENT_VALUES: set[GetBankComplaintProgressSegment] = {
    "new",
    "old",
}


def check_get_bank_complaint_progress_segment(
    value: str,
) -> GetBankComplaintProgressSegment:
    if value in GET_BANK_COMPLAINT_PROGRESS_SEGMENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_BANK_COMPLAINT_PROGRESS_SEGMENT_VALUES!r}"
    )
