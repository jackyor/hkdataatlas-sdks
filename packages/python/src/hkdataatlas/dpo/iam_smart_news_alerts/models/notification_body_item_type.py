from typing import Literal

NotificationBodyItemType = Literal["A", "I", "P"]

NOTIFICATION_BODY_ITEM_TYPE_VALUES: set[NotificationBodyItemType] = {
    "A",
    "I",
    "P",
}


def check_notification_body_item_type(value: str) -> NotificationBodyItemType:
    if value in NOTIFICATION_BODY_ITEM_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NOTIFICATION_BODY_ITEM_TYPE_VALUES!r}"
    )
