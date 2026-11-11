from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tile import Tile


T = TypeVar("T", bound="TilesResponse")


@_attrs_define
class TilesResponse:
    """Legacy documented response structure. Field casing in the dictionary and example differs; the schema uses the casing
    shown in the example and observed response, without asserting that casing is universal for the current endpoint.

        Attributes:
            grid_list (list[Tile] | Unset): Multiple items may be returned when the coordinate falls into multiple tile
                files. The legacy specification says an empty array is returned when there is an error or criteria are not
                matched.
            msg (str | Unset): Success or failure information. The legacy dictionary labels this field Msg. Documented
                possible messages include "Success", "No available 3D Model for Location Specified(e=834251&n=835501)" and
                "Invalid File Type(Only accept OBJ/OSGB/CESIUM)".
            resp_cd (int | Unset): Response code: 0 = success, 1 = fail.
    """

    grid_list: list[Tile] | Unset = UNSET
    msg: str | Unset = UNSET
    resp_cd: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grid_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.grid_list, Unset):
            grid_list = []
            for grid_list_item_data in self.grid_list:
                grid_list_item = grid_list_item_data.to_dict()
                grid_list.append(grid_list_item)

        msg = self.msg

        resp_cd = self.resp_cd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grid_list is not UNSET:
            field_dict["gridList"] = grid_list
        if msg is not UNSET:
            field_dict["msg"] = msg
        if resp_cd is not UNSET:
            field_dict["respCd"] = resp_cd

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.tile import Tile

        d = dict(src_dict)
        _grid_list = d.pop("gridList", UNSET)
        grid_list: list[Tile] | Unset = UNSET
        if _grid_list is not UNSET:
            grid_list = []
            for grid_list_item_data in _grid_list:
                grid_list_item = Tile.from_dict(grid_list_item_data)

                grid_list.append(grid_list_item)

        msg = d.pop("msg", UNSET)

        resp_cd = d.pop("respCd", UNSET)

        tiles_response = cls(
            grid_list=grid_list,
            msg=msg,
            resp_cd=resp_cd,
        )

        tiles_response.additional_properties = d
        return tiles_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
