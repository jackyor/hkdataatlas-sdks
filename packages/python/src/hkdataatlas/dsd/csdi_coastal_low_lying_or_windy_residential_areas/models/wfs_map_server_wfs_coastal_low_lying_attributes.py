from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsCoastalLowLyingAttributes")


@_attrs_define
class WfsMapServerWfsCoastalLowLyingAttributes:
    """
    Attributes:
        record_id (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        location_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        location_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        location_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        shape (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        latitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        longitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        improvement_measures_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        improvement_measures_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        improvement_measures_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        remark_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        remark_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        remark_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape_1 (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its
            XML type.
    """

    record_id: None | str | Unset = UNSET
    location_en: None | str | Unset = UNSET
    location_tc: None | str | Unset = UNSET
    location_sc: None | str | Unset = UNSET
    shape: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    improvement_measures_en: None | str | Unset = UNSET
    improvement_measures_tc: None | str | Unset = UNSET
    improvement_measures_sc: None | str | Unset = UNSET
    remark_en: None | str | Unset = UNSET
    remark_tc: None | str | Unset = UNSET
    remark_sc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_1: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        record_id: None | str | Unset
        if isinstance(self.record_id, Unset):
            record_id = UNSET
        else:
            record_id = self.record_id

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

        location_sc: None | str | Unset
        if isinstance(self.location_sc, Unset):
            location_sc = UNSET
        else:
            location_sc = self.location_sc

        shape: None | str | Unset
        if isinstance(self.shape, Unset):
            shape = UNSET
        else:
            shape = self.shape

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        improvement_measures_en: None | str | Unset
        if isinstance(self.improvement_measures_en, Unset):
            improvement_measures_en = UNSET
        else:
            improvement_measures_en = self.improvement_measures_en

        improvement_measures_tc: None | str | Unset
        if isinstance(self.improvement_measures_tc, Unset):
            improvement_measures_tc = UNSET
        else:
            improvement_measures_tc = self.improvement_measures_tc

        improvement_measures_sc: None | str | Unset
        if isinstance(self.improvement_measures_sc, Unset):
            improvement_measures_sc = UNSET
        else:
            improvement_measures_sc = self.improvement_measures_sc

        remark_en: None | str | Unset
        if isinstance(self.remark_en, Unset):
            remark_en = UNSET
        else:
            remark_en = self.remark_en

        remark_tc: None | str | Unset
        if isinstance(self.remark_tc, Unset):
            remark_tc = UNSET
        else:
            remark_tc = self.remark_tc

        remark_sc: None | str | Unset
        if isinstance(self.remark_sc, Unset):
            remark_sc = UNSET
        else:
            remark_sc = self.remark_sc

        objectid = self.objectid

        shape_1 = self.shape_1

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if record_id is not UNSET:
            field_dict["RECORD_ID"] = record_id
        if location_en is not UNSET:
            field_dict["LOCATION_EN"] = location_en
        if location_tc is not UNSET:
            field_dict["LOCATION_TC"] = location_tc
        if location_sc is not UNSET:
            field_dict["LOCATION_SC"] = location_sc
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if latitude is not UNSET:
            field_dict["LATITUDE"] = latitude
        if longitude is not UNSET:
            field_dict["LONGITUDE"] = longitude
        if improvement_measures_en is not UNSET:
            field_dict["IMPROVEMENT_MEASURES_EN"] = improvement_measures_en
        if improvement_measures_tc is not UNSET:
            field_dict["IMPROVEMENT_MEASURES_TC"] = improvement_measures_tc
        if improvement_measures_sc is not UNSET:
            field_dict["IMPROVEMENT_MEASURES_SC"] = improvement_measures_sc
        if remark_en is not UNSET:
            field_dict["REMARK_EN"] = remark_en
        if remark_tc is not UNSET:
            field_dict["REMARK_TC"] = remark_tc
        if remark_sc is not UNSET:
            field_dict["REMARK_SC"] = remark_sc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape_1 is not UNSET:
            field_dict["SHAPE_1"] = shape_1

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_record_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        record_id = _parse_record_id(d.pop("RECORD_ID", UNSET))

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

        def _parse_location_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_sc = _parse_location_sc(d.pop("LOCATION_SC", UNSET))

        def _parse_shape(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shape = _parse_shape(d.pop("SHAPE", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("LATITUDE", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("LONGITUDE", UNSET))

        def _parse_improvement_measures_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        improvement_measures_en = _parse_improvement_measures_en(
            d.pop("IMPROVEMENT_MEASURES_EN", UNSET)
        )

        def _parse_improvement_measures_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        improvement_measures_tc = _parse_improvement_measures_tc(
            d.pop("IMPROVEMENT_MEASURES_TC", UNSET)
        )

        def _parse_improvement_measures_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        improvement_measures_sc = _parse_improvement_measures_sc(
            d.pop("IMPROVEMENT_MEASURES_SC", UNSET)
        )

        def _parse_remark_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark_en = _parse_remark_en(d.pop("REMARK_EN", UNSET))

        def _parse_remark_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark_tc = _parse_remark_tc(d.pop("REMARK_TC", UNSET))

        def _parse_remark_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark_sc = _parse_remark_sc(d.pop("REMARK_SC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape_1 = d.pop("SHAPE_1", UNSET)

        wfs_map_server_wfs_coastal_low_lying_attributes = cls(
            record_id=record_id,
            location_en=location_en,
            location_tc=location_tc,
            location_sc=location_sc,
            shape=shape,
            latitude=latitude,
            longitude=longitude,
            improvement_measures_en=improvement_measures_en,
            improvement_measures_tc=improvement_measures_tc,
            improvement_measures_sc=improvement_measures_sc,
            remark_en=remark_en,
            remark_tc=remark_tc,
            remark_sc=remark_sc,
            objectid=objectid,
            shape_1=shape_1,
        )

        wfs_map_server_wfs_coastal_low_lying_attributes.additional_properties = d
        return wfs_map_server_wfs_coastal_low_lying_attributes

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
