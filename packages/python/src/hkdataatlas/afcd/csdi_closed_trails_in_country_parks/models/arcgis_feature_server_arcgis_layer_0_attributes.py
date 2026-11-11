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
        trail_id (None | str | Unset): Publisher field type: esriFieldTypeString
        trail_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        trail_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        location_en (None | str | Unset): Publisher field type: esriFieldTypeString
        location_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        status_en (None | str | Unset): Publisher field type: esriFieldTypeString
        status_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        effective_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        expected_expiry_date (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    trail_id: None | str | Unset = UNSET
    trail_name_en: None | str | Unset = UNSET
    trail_name_tc: None | str | Unset = UNSET
    location_en: None | str | Unset = UNSET
    location_tc: None | str | Unset = UNSET
    status_en: None | str | Unset = UNSET
    status_tc: None | str | Unset = UNSET
    effective_date: Any | Unset = UNSET
    expected_expiry_date: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trail_id: None | str | Unset
        if isinstance(self.trail_id, Unset):
            trail_id = UNSET
        else:
            trail_id = self.trail_id

        trail_name_en: None | str | Unset
        if isinstance(self.trail_name_en, Unset):
            trail_name_en = UNSET
        else:
            trail_name_en = self.trail_name_en

        trail_name_tc: None | str | Unset
        if isinstance(self.trail_name_tc, Unset):
            trail_name_tc = UNSET
        else:
            trail_name_tc = self.trail_name_tc

        location_en: None | str | Unset
        if isinstance(self.location_en, Unset):
            location_en = UNSET
        else:
            location_en = self.location_en

        location_tc: None | str | Unset
        if isinstance(self.location_tc, Unset):
            location_tc = UNSET
        else:
            location_tc = self.location_tc

        status_en: None | str | Unset
        if isinstance(self.status_en, Unset):
            status_en = UNSET
        else:
            status_en = self.status_en

        status_tc: None | str | Unset
        if isinstance(self.status_tc, Unset):
            status_tc = UNSET
        else:
            status_tc = self.status_tc

        effective_date = self.effective_date

        expected_expiry_date: None | str | Unset
        if isinstance(self.expected_expiry_date, Unset):
            expected_expiry_date = UNSET
        else:
            expected_expiry_date = self.expected_expiry_date

        objectid = self.objectid

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trail_id is not UNSET:
            field_dict["TRAIL_ID"] = trail_id
        if trail_name_en is not UNSET:
            field_dict["TRAIL_NAME_EN"] = trail_name_en
        if trail_name_tc is not UNSET:
            field_dict["TRAIL_NAME_TC"] = trail_name_tc
        if location_en is not UNSET:
            field_dict["LOCATION_EN"] = location_en
        if location_tc is not UNSET:
            field_dict["LOCATION_TC"] = location_tc
        if status_en is not UNSET:
            field_dict["STATUS_EN"] = status_en
        if status_tc is not UNSET:
            field_dict["STATUS_TC"] = status_tc
        if effective_date is not UNSET:
            field_dict["EFFECTIVE_DATE"] = effective_date
        if expected_expiry_date is not UNSET:
            field_dict["EXPECTED_EXPIRY_DATE"] = expected_expiry_date
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_trail_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trail_id = _parse_trail_id(d.pop("TRAIL_ID", UNSET))

        def _parse_trail_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trail_name_en = _parse_trail_name_en(d.pop("TRAIL_NAME_EN", UNSET))

        def _parse_trail_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trail_name_tc = _parse_trail_name_tc(d.pop("TRAIL_NAME_TC", UNSET))

        def _parse_location_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_en = _parse_location_en(d.pop("LOCATION_EN", UNSET))

        def _parse_location_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_tc = _parse_location_tc(d.pop("LOCATION_TC", UNSET))

        def _parse_status_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_en = _parse_status_en(d.pop("STATUS_EN", UNSET))

        def _parse_status_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_tc = _parse_status_tc(d.pop("STATUS_TC", UNSET))

        effective_date = d.pop("EFFECTIVE_DATE", UNSET)

        def _parse_expected_expiry_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expected_expiry_date = _parse_expected_expiry_date(
            d.pop("EXPECTED_EXPIRY_DATE", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            trail_id=trail_id,
            trail_name_en=trail_name_en,
            trail_name_tc=trail_name_tc,
            location_en=location_en,
            location_tc=location_tc,
            status_en=status_en,
            status_tc=status_tc,
            effective_date=effective_date,
            expected_expiry_date=expected_expiry_date,
            objectid=objectid,
            shape_length=shape_length,
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
