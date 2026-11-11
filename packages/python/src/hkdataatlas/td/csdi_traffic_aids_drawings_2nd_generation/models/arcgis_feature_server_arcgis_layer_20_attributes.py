from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer20Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer20Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        featureid (int | Unset): Publisher field type: esriFieldTypeInteger
        completion_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
        gazette_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        last_upd_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        elevation (None | str | Unset): Publisher field type: esriFieldTypeString
        angle1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        angle2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ruleid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        override (Any | Unset): Publisher field type: esriFieldTypeBlob; JSON wire representation remains unknown.
        ruleid_1 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        override_1 (Any | Unset): Publisher field type: esriFieldTypeBlob; JSON wire representation remains unknown.
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
        yellowbox_type (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    featureid: int | Unset = UNSET
    completion_date: Any | Unset = UNSET
    gazette_date: Any | Unset = UNSET
    last_upd_date: Any | Unset = UNSET
    elevation: None | str | Unset = UNSET
    angle1: float | None | Unset = UNSET
    angle2: float | None | Unset = UNSET
    ruleid: int | None | Unset = UNSET
    override: Any | Unset = UNSET
    ruleid_1: int | None | Unset = UNSET
    override_1: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    yellowbox_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        featureid = self.featureid

        completion_date = self.completion_date

        gazette_date = self.gazette_date

        last_upd_date = self.last_upd_date

        elevation: None | str | Unset
        if isinstance(self.elevation, Unset):
            elevation = UNSET
        else:
            elevation = self.elevation

        angle1: float | None | Unset
        if isinstance(self.angle1, Unset):
            angle1 = UNSET
        else:
            angle1 = self.angle1

        angle2: float | None | Unset
        if isinstance(self.angle2, Unset):
            angle2 = UNSET
        else:
            angle2 = self.angle2

        ruleid: int | None | Unset
        if isinstance(self.ruleid, Unset):
            ruleid = UNSET
        else:
            ruleid = self.ruleid

        override = self.override

        ruleid_1: int | None | Unset
        if isinstance(self.ruleid_1, Unset):
            ruleid_1 = UNSET
        else:
            ruleid_1 = self.ruleid_1

        override_1 = self.override_1

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        shape_area: float | None | Unset
        if isinstance(self.shape_area, Unset):
            shape_area = UNSET
        else:
            shape_area = self.shape_area

        yellowbox_type: None | str | Unset
        if isinstance(self.yellowbox_type, Unset):
            yellowbox_type = UNSET
        else:
            yellowbox_type = self.yellowbox_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
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
        if angle1 is not UNSET:
            field_dict["ANGLE1"] = angle1
        if angle2 is not UNSET:
            field_dict["ANGLE2"] = angle2
        if ruleid is not UNSET:
            field_dict["RULEID"] = ruleid
        if override is not UNSET:
            field_dict["OVERRIDE"] = override
        if ruleid_1 is not UNSET:
            field_dict["RULEID_1"] = ruleid_1
        if override_1 is not UNSET:
            field_dict["OVERRIDE_1"] = override_1
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area
        if yellowbox_type is not UNSET:
            field_dict["YELLOWBOX_TYPE"] = yellowbox_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

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

        def _parse_angle1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        angle1 = _parse_angle1(d.pop("ANGLE1", UNSET))

        def _parse_angle2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        angle2 = _parse_angle2(d.pop("ANGLE2", UNSET))

        def _parse_ruleid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ruleid = _parse_ruleid(d.pop("RULEID", UNSET))

        override = d.pop("OVERRIDE", UNSET)

        def _parse_ruleid_1(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ruleid_1 = _parse_ruleid_1(d.pop("RULEID_1", UNSET))

        override_1 = d.pop("OVERRIDE_1", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape__Area", UNSET))

        def _parse_yellowbox_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yellowbox_type = _parse_yellowbox_type(d.pop("YELLOWBOX_TYPE", UNSET))

        arcgis_feature_server_arcgis_layer_20_attributes = cls(
            objectid=objectid,
            featureid=featureid,
            completion_date=completion_date,
            gazette_date=gazette_date,
            last_upd_date=last_upd_date,
            elevation=elevation,
            angle1=angle1,
            angle2=angle2,
            ruleid=ruleid,
            override=override,
            ruleid_1=ruleid_1,
            override_1=override_1,
            shape_length=shape_length,
            shape_area=shape_area,
            yellowbox_type=yellowbox_type,
        )

        arcgis_feature_server_arcgis_layer_20_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_20_attributes

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
