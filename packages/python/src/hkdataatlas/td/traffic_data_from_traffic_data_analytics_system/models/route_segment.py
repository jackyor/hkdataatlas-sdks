from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.route_segment_dir import RouteSegmentDir, check_route_segment_dir
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pedestrian_zone import PedestrianZone


T = TypeVar("T", bound="RouteSegment")


@_attrs_define
class RouteSegment:
    """Route segment information.

    Attributes:
        dir_ (RouteSegmentDir | Unset): Travel direction code: 0 = turn to; 1 = keep / turn left to; 2 = keep / turn
            right to; 3 = keep going to; 4 = turn around to.
        ped (list[PedestrianZone] | Unset): Pedestrian Zone information, if applicable.
        rid (list[int] | Unset): Route_ID(s) of Centreline feature in IRN.
    """

    dir_: RouteSegmentDir | Unset = UNSET
    ped: list[PedestrianZone] | Unset = UNSET
    rid: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dir_: int | Unset = UNSET
        if not isinstance(self.dir_, Unset):
            dir_ = self.dir_

        ped: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ped, Unset):
            ped = []
            for ped_item_data in self.ped:
                ped_item = ped_item_data.to_dict()
                ped.append(ped_item)

        rid: list[int] | Unset = UNSET
        if not isinstance(self.rid, Unset):
            rid = self.rid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dir_ is not UNSET:
            field_dict["dir"] = dir_
        if ped is not UNSET:
            field_dict["ped"] = ped
        if rid is not UNSET:
            field_dict["rid"] = rid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pedestrian_zone import PedestrianZone

        d = dict(src_dict)
        _dir_ = d.pop("dir", UNSET)
        dir_: RouteSegmentDir | Unset
        if isinstance(_dir_, Unset):
            dir_ = UNSET
        else:
            dir_ = check_route_segment_dir(_dir_)

        _ped = d.pop("ped", UNSET)
        ped: list[PedestrianZone] | Unset = UNSET
        if _ped is not UNSET:
            ped = []
            for ped_item_data in _ped:
                ped_item = PedestrianZone.from_dict(ped_item_data)

                ped.append(ped_item)

        rid = cast(list[int], d.pop("rid", UNSET))

        route_segment = cls(
            dir_=dir_,
            ped=ped,
            rid=rid,
        )

        route_segment.additional_properties = d
        return route_segment

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
