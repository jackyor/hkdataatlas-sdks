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
        tmcp_id (None | str | Unset): Publisher field type: esriFieldTypeString
        ovt_no (None | str | Unset): Publisher field type: esriFieldTypeString
        height (float | None | Unset): Publisher field type: esriFieldTypeSingle
        crown (float | None | Unset): Publisher field type: esriFieldTypeSingle
        dbh (float | None | Unset): Publisher field type: esriFieldTypeDouble
        location (None | str | Unset): Publisher field type: esriFieldTypeString
        x (float | None | Unset): Publisher field type: esriFieldTypeDouble
        y (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    tmcp_id: None | str | Unset = UNSET
    ovt_no: None | str | Unset = UNSET
    height: float | None | Unset = UNSET
    crown: float | None | Unset = UNSET
    dbh: float | None | Unset = UNSET
    location: None | str | Unset = UNSET
    x: float | None | Unset = UNSET
    y: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        tmcp_id: None | str | Unset
        if isinstance(self.tmcp_id, Unset):
            tmcp_id = UNSET
        else:
            tmcp_id = self.tmcp_id

        ovt_no: None | str | Unset
        if isinstance(self.ovt_no, Unset):
            ovt_no = UNSET
        else:
            ovt_no = self.ovt_no

        height: float | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        crown: float | None | Unset
        if isinstance(self.crown, Unset):
            crown = UNSET
        else:
            crown = self.crown

        dbh: float | None | Unset
        if isinstance(self.dbh, Unset):
            dbh = UNSET
        else:
            dbh = self.dbh

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        x: float | None | Unset
        if isinstance(self.x, Unset):
            x = UNSET
        else:
            x = self.x

        y: float | None | Unset
        if isinstance(self.y, Unset):
            y = UNSET
        else:
            y = self.y

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if tmcp_id is not UNSET:
            field_dict["TMCP_ID"] = tmcp_id
        if ovt_no is not UNSET:
            field_dict["OVT_NO"] = ovt_no
        if height is not UNSET:
            field_dict["HEIGHT"] = height
        if crown is not UNSET:
            field_dict["CROWN"] = crown
        if dbh is not UNSET:
            field_dict["DBH"] = dbh
        if location is not UNSET:
            field_dict["LOCATION"] = location
        if x is not UNSET:
            field_dict["X"] = x
        if y is not UNSET:
            field_dict["Y"] = y

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_tmcp_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tmcp_id = _parse_tmcp_id(d.pop("TMCP_ID", UNSET))

        def _parse_ovt_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ovt_no = _parse_ovt_no(d.pop("OVT_NO", UNSET))

        def _parse_height(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        height = _parse_height(d.pop("HEIGHT", UNSET))

        def _parse_crown(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        crown = _parse_crown(d.pop("CROWN", UNSET))

        def _parse_dbh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dbh = _parse_dbh(d.pop("DBH", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("LOCATION", UNSET))

        def _parse_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        x = _parse_x(d.pop("X", UNSET))

        def _parse_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        y = _parse_y(d.pop("Y", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            tmcp_id=tmcp_id,
            ovt_no=ovt_no,
            height=height,
            crown=crown,
            dbh=dbh,
            location=location,
            x=x,
            y=y,
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
