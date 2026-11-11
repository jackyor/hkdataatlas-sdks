from typing import Literal

ListNotificationsLang = Literal["en", "sc", "tc"]

LIST_NOTIFICATIONS_LANG_VALUES: set[ListNotificationsLang] = {
    "en",
    "sc",
    "tc",
}


def check_list_notifications_lang(value: str) -> ListNotificationsLang:
    if value in LIST_NOTIFICATIONS_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_NOTIFICATIONS_LANG_VALUES!r}"
    )
