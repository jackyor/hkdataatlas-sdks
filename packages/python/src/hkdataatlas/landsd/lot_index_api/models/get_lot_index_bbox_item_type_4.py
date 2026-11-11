from typing import Literal

GetLotIndexBboxItemType4 = Literal["EPSG:2326"]

GET_LOT_INDEX_BBOX_ITEM_TYPE_4_VALUES: set[GetLotIndexBboxItemType4] = {
    "EPSG:2326",
}


def check_get_lot_index_bbox_item_type_4(value: str) -> GetLotIndexBboxItemType4:
    if value in GET_LOT_INDEX_BBOX_ITEM_TYPE_4_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_LOT_INDEX_BBOX_ITEM_TYPE_4_VALUES!r}"
    )
