from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        road_route_id (int | Unset): Publisher field type: esriFieldTypeInteger
        max_axle_weight (None | str | Unset): Publisher field type: esriFieldTypeString
        vr_id (int | Unset): Publisher field type: esriFieldTypeInteger
        max_length (None | str | Unset): Publisher field type: esriFieldTypeString
        max_weight (None | str | Unset): Publisher field type: esriFieldTypeString
        max_height (None | str | Unset): Publisher field type: esriFieldTypeString
        max_width (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        cre_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        last_upd_date_v (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
        bound (int | None | Unset): Publisher field type: esriFieldTypeInteger
    """

    objectid: int | Unset = UNSET
    road_route_id: int | Unset = UNSET
    max_axle_weight: None | str | Unset = UNSET
    vr_id: int | Unset = UNSET
    max_length: None | str | Unset = UNSET
    max_weight: None | str | Unset = UNSET
    max_height: None | str | Unset = UNSET
    max_width: None | str | Unset = UNSET
    remarks: None | str | Unset = UNSET
    cre_date: Any | Unset = UNSET
    last_upd_date_v: Any | Unset = UNSET
    bound: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        road_route_id = self.road_route_id

        max_axle_weight: None | str | Unset
        if isinstance(self.max_axle_weight, Unset):
            max_axle_weight = UNSET
        else:
            max_axle_weight = self.max_axle_weight

        vr_id = self.vr_id

        max_length: None | str | Unset
        if isinstance(self.max_length, Unset):
            max_length = UNSET
        else:
            max_length = self.max_length

        max_weight: None | str | Unset
        if isinstance(self.max_weight, Unset):
            max_weight = UNSET
        else:
            max_weight = self.max_weight

        max_height: None | str | Unset
        if isinstance(self.max_height, Unset):
            max_height = UNSET
        else:
            max_height = self.max_height

        max_width: None | str | Unset
        if isinstance(self.max_width, Unset):
            max_width = UNSET
        else:
            max_width = self.max_width

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        cre_date = self.cre_date

        last_upd_date_v = self.last_upd_date_v

        bound: int | None | Unset
        if isinstance(self.bound, Unset):
            bound = UNSET
        else:
            bound = self.bound

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if road_route_id is not UNSET:
            field_dict["ROAD_ROUTE_ID"] = road_route_id
        if max_axle_weight is not UNSET:
            field_dict["MAX_AXLE_WEIGHT"] = max_axle_weight
        if vr_id is not UNSET:
            field_dict["VR_ID"] = vr_id
        if max_length is not UNSET:
            field_dict["MAX_LENGTH"] = max_length
        if max_weight is not UNSET:
            field_dict["MAX_WEIGHT"] = max_weight
        if max_height is not UNSET:
            field_dict["MAX_HEIGHT"] = max_height
        if max_width is not UNSET:
            field_dict["MAX_WIDTH"] = max_width
        if remarks is not UNSET:
            field_dict["REMARKS"] = remarks
        if cre_date is not UNSET:
            field_dict["CRE_DATE"] = cre_date
        if last_upd_date_v is not UNSET:
            field_dict["LAST_UPD_DATE_V"] = last_upd_date_v
        if bound is not UNSET:
            field_dict["BOUND"] = bound

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        road_route_id = d.pop("ROAD_ROUTE_ID", UNSET)

        def _parse_max_axle_weight(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_axle_weight = _parse_max_axle_weight(d.pop("MAX_AXLE_WEIGHT", UNSET))

        vr_id = d.pop("VR_ID", UNSET)

        def _parse_max_length(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_length = _parse_max_length(d.pop("MAX_LENGTH", UNSET))

        def _parse_max_weight(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_weight = _parse_max_weight(d.pop("MAX_WEIGHT", UNSET))

        def _parse_max_height(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_height = _parse_max_height(d.pop("MAX_HEIGHT", UNSET))

        def _parse_max_width(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_width = _parse_max_width(d.pop("MAX_WIDTH", UNSET))

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("REMARKS", UNSET))

        cre_date = d.pop("CRE_DATE", UNSET)

        last_upd_date_v = d.pop("LAST_UPD_DATE_V", UNSET)

        def _parse_bound(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bound = _parse_bound(d.pop("BOUND", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            road_route_id=road_route_id,
            max_axle_weight=max_axle_weight,
            vr_id=vr_id,
            max_length=max_length,
            max_weight=max_weight,
            max_height=max_height,
            max_width=max_width,
            remarks=remarks,
            cre_date=cre_date,
            last_upd_date_v=last_upd_date_v,
            bound=bound,
        )

        arcgis_feature_server_arcgis_layer_0_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_0_attributes

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
