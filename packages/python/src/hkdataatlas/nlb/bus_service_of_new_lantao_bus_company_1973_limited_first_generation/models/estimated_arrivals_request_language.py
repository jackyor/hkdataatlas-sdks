from typing import Literal

EstimatedArrivalsRequestLanguage = Literal["cn", "en", "zh"]

ESTIMATED_ARRIVALS_REQUEST_LANGUAGE_VALUES: set[EstimatedArrivalsRequestLanguage] = {
    "cn",
    "en",
    "zh",
}


def check_estimated_arrivals_request_language(
    value: str,
) -> EstimatedArrivalsRequestLanguage:
    if value in ESTIMATED_ARRIVALS_REQUEST_LANGUAGE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESTIMATED_ARRIVALS_REQUEST_LANGUAGE_VALUES!r}"
    )
