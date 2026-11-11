from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer36Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer36Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        color (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        featureid (int | Unset): Publisher field type: esriFieldTypeInteger
        completion_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
        gazette_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        last_upd_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        elevation (None | str | Unset): Publisher field type: esriFieldTypeString
        linetype (None | str | Unset): Publisher field type: esriFieldTypeString
        time_zone (int | None | Unset): Publisher field type: esriFieldTypeInteger
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    color: int | None | Unset = UNSET
    featureid: int | Unset = UNSET
    completion_date: Any | Unset = UNSET
    gazette_date: Any | Unset = UNSET
    last_upd_date: Any | Unset = UNSET
    elevation: None | str | Unset = UNSET
    linetype: None | str | Unset = UNSET
    time_zone: int | None | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        color: int | None | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        featureid = self.featureid

        completion_date = self.completion_date

        gazette_date = self.gazette_date

        last_upd_date = self.last_upd_date

        elevation: None | str | Unset
        if isinstance(self.elevation, Unset):
            elevation = UNSET
        else:
            elevation = self.elevation

        linetype: None | str | Unset
        if isinstance(self.linetype, Unset):
            linetype = UNSET
        else:
            linetype = self.linetype

        time_zone: int | None | Unset
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if color is not UNSET:
            field_dict["COLOR"] = color
        if featureid is not UNSET:
            field_dict["FEATUREID"] = featureid
        if completion_date is not UNSET:
            field_dict["COMPLETION_DATE"] = completion_date
        if gazette_date is not UNSET:
            field_dict["GAZETTE_DATE"] = gazette_date
        if last_upd_date is not UNSET:
            field_dict["LAST_UPD_DATE"] = last_upd_date
        if elevation is not UNSET:
            field_dict["ELEVATION"] = elevation
        if linetype is not UNSET:
            field_dict["LINETYPE"] = linetype
        if time_zone is not UNSET:
            field_dict["TIME_ZONE"] = time_zone
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_color(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        color = _parse_color(d.pop("COLOR", UNSET))

        featureid = d.pop("FEATUREID", UNSET)

        completion_date = d.pop("COMPLETION_DATE", UNSET)

        gazette_date = d.pop("GAZETTE_DATE", UNSET)

        last_upd_date = d.pop("LAST_UPD_DATE", UNSET)

        def _parse_elevation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        elevation = _parse_elevation(d.pop("ELEVATION", UNSET))

        def _parse_linetype(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linetype = _parse_linetype(d.pop("LINETYPE", UNSET))

        def _parse_time_zone(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_zone = _parse_time_zone(d.pop("TIME_ZONE", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_36_attributes = cls(
            objectid=objectid,
            color=color,
            featureid=featureid,
            completion_date=completion_date,
            gazette_date=gazette_date,
            last_upd_date=last_upd_date,
            elevation=elevation,
            linetype=linetype,
            time_zone=time_zone,
            shape_length=shape_length,
        )

        arcgis_feature_server_arcgis_layer_36_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_36_attributes

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
