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
        record_id (None | str | Unset): Publisher field type: esriFieldTypeString
        location_en (None | str | Unset): Publisher field type: esriFieldTypeString
        location_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        location_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        shape (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        flooding_blackspot_scale (None | str | Unset): Publisher field type: esriFieldTypeString
        cause_of_flooding_en (None | str | Unset): Publisher field type: esriFieldTypeString
        cause_of_flooding_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        cause_of_flooding_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        responsible_division_en (None | str | Unset): Publisher field type: esriFieldTypeString
        responsible_division_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        responsible_division_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        year_first_appeared (None | str | Unset): Publisher field type: esriFieldTypeString
        commissioning_date_of_drainage_improvement_works_en (None | str | Unset): Publisher field type:
            esriFieldTypeString
        commissioning_date_of_drainage_improvement_works_tc (None | str | Unset): Publisher field type:
            esriFieldTypeString
        commissioning_date_of_drainage_improvement_works_sc (None | str | Unset): Publisher field type:
            esriFieldTypeString
        short_term_mitigation_measures_en (None | str | Unset): Publisher field type: esriFieldTypeString
        short_term_mitigation_measures_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        short_term_mitigation_measures_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        long_term_mitigation_measures_en (None | str | Unset): Publisher field type: esriFieldTypeString
        long_term_mitigation_measures_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        long_term_mitigation_measures_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        remark_en (None | str | Unset): Publisher field type: esriFieldTypeString
        remark_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        remark_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    record_id: None | str | Unset = UNSET
    location_en: None | str | Unset = UNSET
    location_tc: None | str | Unset = UNSET
    location_sc: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    district_sc: None | str | Unset = UNSET
    shape: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    flooding_blackspot_scale: None | str | Unset = UNSET
    cause_of_flooding_en: None | str | Unset = UNSET
    cause_of_flooding_tc: None | str | Unset = UNSET
    cause_of_flooding_sc: None | str | Unset = UNSET
    responsible_division_en: None | str | Unset = UNSET
    responsible_division_tc: None | str | Unset = UNSET
    responsible_division_sc: None | str | Unset = UNSET
    year_first_appeared: None | str | Unset = UNSET
    commissioning_date_of_drainage_improvement_works_en: None | str | Unset = UNSET
    commissioning_date_of_drainage_improvement_works_tc: None | str | Unset = UNSET
    commissioning_date_of_drainage_improvement_works_sc: None | str | Unset = UNSET
    short_term_mitigation_measures_en: None | str | Unset = UNSET
    short_term_mitigation_measures_tc: None | str | Unset = UNSET
    short_term_mitigation_measures_sc: None | str | Unset = UNSET
    long_term_mitigation_measures_en: None | str | Unset = UNSET
    long_term_mitigation_measures_tc: None | str | Unset = UNSET
    long_term_mitigation_measures_sc: None | str | Unset = UNSET
    remark_en: None | str | Unset = UNSET
    remark_tc: None | str | Unset = UNSET
    remark_sc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
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

        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        district_sc: None | str | Unset
        if isinstance(self.district_sc, Unset):
            district_sc = UNSET
        else:
            district_sc = self.district_sc

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

        flooding_blackspot_scale: None | str | Unset
        if isinstance(self.flooding_blackspot_scale, Unset):
            flooding_blackspot_scale = UNSET
        else:
            flooding_blackspot_scale = self.flooding_blackspot_scale

        cause_of_flooding_en: None | str | Unset
        if isinstance(self.cause_of_flooding_en, Unset):
            cause_of_flooding_en = UNSET
        else:
            cause_of_flooding_en = self.cause_of_flooding_en

        cause_of_flooding_tc: None | str | Unset
        if isinstance(self.cause_of_flooding_tc, Unset):
            cause_of_flooding_tc = UNSET
        else:
            cause_of_flooding_tc = self.cause_of_flooding_tc

        cause_of_flooding_sc: None | str | Unset
        if isinstance(self.cause_of_flooding_sc, Unset):
            cause_of_flooding_sc = UNSET
        else:
            cause_of_flooding_sc = self.cause_of_flooding_sc

        responsible_division_en: None | str | Unset
        if isinstance(self.responsible_division_en, Unset):
            responsible_division_en = UNSET
        else:
            responsible_division_en = self.responsible_division_en

        responsible_division_tc: None | str | Unset
        if isinstance(self.responsible_division_tc, Unset):
            responsible_division_tc = UNSET
        else:
            responsible_division_tc = self.responsible_division_tc

        responsible_division_sc: None | str | Unset
        if isinstance(self.responsible_division_sc, Unset):
            responsible_division_sc = UNSET
        else:
            responsible_division_sc = self.responsible_division_sc

        year_first_appeared: None | str | Unset
        if isinstance(self.year_first_appeared, Unset):
            year_first_appeared = UNSET
        else:
            year_first_appeared = self.year_first_appeared

        commissioning_date_of_drainage_improvement_works_en: None | str | Unset
        if isinstance(self.commissioning_date_of_drainage_improvement_works_en, Unset):
            commissioning_date_of_drainage_improvement_works_en = UNSET
        else:
            commissioning_date_of_drainage_improvement_works_en = (
                self.commissioning_date_of_drainage_improvement_works_en
            )

        commissioning_date_of_drainage_improvement_works_tc: None | str | Unset
        if isinstance(self.commissioning_date_of_drainage_improvement_works_tc, Unset):
            commissioning_date_of_drainage_improvement_works_tc = UNSET
        else:
            commissioning_date_of_drainage_improvement_works_tc = (
                self.commissioning_date_of_drainage_improvement_works_tc
            )

        commissioning_date_of_drainage_improvement_works_sc: None | str | Unset
        if isinstance(self.commissioning_date_of_drainage_improvement_works_sc, Unset):
            commissioning_date_of_drainage_improvement_works_sc = UNSET
        else:
            commissioning_date_of_drainage_improvement_works_sc = (
                self.commissioning_date_of_drainage_improvement_works_sc
            )

        short_term_mitigation_measures_en: None | str | Unset
        if isinstance(self.short_term_mitigation_measures_en, Unset):
            short_term_mitigation_measures_en = UNSET
        else:
            short_term_mitigation_measures_en = self.short_term_mitigation_measures_en

        short_term_mitigation_measures_tc: None | str | Unset
        if isinstance(self.short_term_mitigation_measures_tc, Unset):
            short_term_mitigation_measures_tc = UNSET
        else:
            short_term_mitigation_measures_tc = self.short_term_mitigation_measures_tc

        short_term_mitigation_measures_sc: None | str | Unset
        if isinstance(self.short_term_mitigation_measures_sc, Unset):
            short_term_mitigation_measures_sc = UNSET
        else:
            short_term_mitigation_measures_sc = self.short_term_mitigation_measures_sc

        long_term_mitigation_measures_en: None | str | Unset
        if isinstance(self.long_term_mitigation_measures_en, Unset):
            long_term_mitigation_measures_en = UNSET
        else:
            long_term_mitigation_measures_en = self.long_term_mitigation_measures_en

        long_term_mitigation_measures_tc: None | str | Unset
        if isinstance(self.long_term_mitigation_measures_tc, Unset):
            long_term_mitigation_measures_tc = UNSET
        else:
            long_term_mitigation_measures_tc = self.long_term_mitigation_measures_tc

        long_term_mitigation_measures_sc: None | str | Unset
        if isinstance(self.long_term_mitigation_measures_sc, Unset):
            long_term_mitigation_measures_sc = UNSET
        else:
            long_term_mitigation_measures_sc = self.long_term_mitigation_measures_sc

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
        if district_en is not UNSET:
            field_dict["DISTRICT_EN"] = district_en
        if district_tc is not UNSET:
            field_dict["DISTRICT_TC"] = district_tc
        if district_sc is not UNSET:
            field_dict["DISTRICT_SC"] = district_sc
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if latitude is not UNSET:
            field_dict["LATITUDE"] = latitude
        if longitude is not UNSET:
            field_dict["LONGITUDE"] = longitude
        if flooding_blackspot_scale is not UNSET:
            field_dict["FLOODING_BLACKSPOT_SCALE"] = flooding_blackspot_scale
        if cause_of_flooding_en is not UNSET:
            field_dict["CAUSE_OF_FLOODING_EN"] = cause_of_flooding_en
        if cause_of_flooding_tc is not UNSET:
            field_dict["CAUSE_OF_FLOODING_TC"] = cause_of_flooding_tc
        if cause_of_flooding_sc is not UNSET:
            field_dict["CAUSE_OF_FLOODING_SC"] = cause_of_flooding_sc
        if responsible_division_en is not UNSET:
            field_dict["RESPONSIBLE_DIVISION_EN"] = responsible_division_en
        if responsible_division_tc is not UNSET:
            field_dict["RESPONSIBLE_DIVISION_TC"] = responsible_division_tc
        if responsible_division_sc is not UNSET:
            field_dict["RESPONSIBLE_DIVISION_SC"] = responsible_division_sc
        if year_first_appeared is not UNSET:
            field_dict["YEAR_FIRST_APPEARED"] = year_first_appeared
        if commissioning_date_of_drainage_improvement_works_en is not UNSET:
            field_dict["COMMISSIONING_DATE_OF_DRAINAGE_IMPROVEMENT_WORKS_EN"] = (
                commissioning_date_of_drainage_improvement_works_en
            )
        if commissioning_date_of_drainage_improvement_works_tc is not UNSET:
            field_dict["COMMISSIONING_DATE_OF_DRAINAGE_IMPROVEMENT_WORKS_TC"] = (
                commissioning_date_of_drainage_improvement_works_tc
            )
        if commissioning_date_of_drainage_improvement_works_sc is not UNSET:
            field_dict["COMMISSIONING_DATE_OF_DRAINAGE_IMPROVEMENT_WORKS_SC"] = (
                commissioning_date_of_drainage_improvement_works_sc
            )
        if short_term_mitigation_measures_en is not UNSET:
            field_dict["SHORT_TERM_MITIGATION_MEASURES_EN"] = (
                short_term_mitigation_measures_en
            )
        if short_term_mitigation_measures_tc is not UNSET:
            field_dict["SHORT_TERM_MITIGATION_MEASURES_TC"] = (
                short_term_mitigation_measures_tc
            )
        if short_term_mitigation_measures_sc is not UNSET:
            field_dict["SHORT_TERM_MITIGATION_MEASURES_SC"] = (
                short_term_mitigation_measures_sc
            )
        if long_term_mitigation_measures_en is not UNSET:
            field_dict["LONG_TERM_MITIGATION_MEASURES_EN"] = (
                long_term_mitigation_measures_en
            )
        if long_term_mitigation_measures_tc is not UNSET:
            field_dict["LONG_TERM_MITIGATION_MEASURES_TC"] = (
                long_term_mitigation_measures_tc
            )
        if long_term_mitigation_measures_sc is not UNSET:
            field_dict["LONG_TERM_MITIGATION_MEASURES_SC"] = (
                long_term_mitigation_measures_sc
            )
        if remark_en is not UNSET:
            field_dict["REMARK_EN"] = remark_en
        if remark_tc is not UNSET:
            field_dict["REMARK_TC"] = remark_tc
        if remark_sc is not UNSET:
            field_dict["REMARK_SC"] = remark_sc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

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

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("DISTRICT_EN", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("DISTRICT_TC", UNSET))

        def _parse_district_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_sc = _parse_district_sc(d.pop("DISTRICT_SC", UNSET))

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

        def _parse_flooding_blackspot_scale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flooding_blackspot_scale = _parse_flooding_blackspot_scale(
            d.pop("FLOODING_BLACKSPOT_SCALE", UNSET)
        )

        def _parse_cause_of_flooding_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cause_of_flooding_en = _parse_cause_of_flooding_en(
            d.pop("CAUSE_OF_FLOODING_EN", UNSET)
        )

        def _parse_cause_of_flooding_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cause_of_flooding_tc = _parse_cause_of_flooding_tc(
            d.pop("CAUSE_OF_FLOODING_TC", UNSET)
        )

        def _parse_cause_of_flooding_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cause_of_flooding_sc = _parse_cause_of_flooding_sc(
            d.pop("CAUSE_OF_FLOODING_SC", UNSET)
        )

        def _parse_responsible_division_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        responsible_division_en = _parse_responsible_division_en(
            d.pop("RESPONSIBLE_DIVISION_EN", UNSET)
        )

        def _parse_responsible_division_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        responsible_division_tc = _parse_responsible_division_tc(
            d.pop("RESPONSIBLE_DIVISION_TC", UNSET)
        )

        def _parse_responsible_division_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        responsible_division_sc = _parse_responsible_division_sc(
            d.pop("RESPONSIBLE_DIVISION_SC", UNSET)
        )

        def _parse_year_first_appeared(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year_first_appeared = _parse_year_first_appeared(
            d.pop("YEAR_FIRST_APPEARED", UNSET)
        )

        def _parse_commissioning_date_of_drainage_improvement_works_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commissioning_date_of_drainage_improvement_works_en = (
            _parse_commissioning_date_of_drainage_improvement_works_en(
                d.pop("COMMISSIONING_DATE_OF_DRAINAGE_IMPROVEMENT_WORKS_EN", UNSET)
            )
        )

        def _parse_commissioning_date_of_drainage_improvement_works_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commissioning_date_of_drainage_improvement_works_tc = (
            _parse_commissioning_date_of_drainage_improvement_works_tc(
                d.pop("COMMISSIONING_DATE_OF_DRAINAGE_IMPROVEMENT_WORKS_TC", UNSET)
            )
        )

        def _parse_commissioning_date_of_drainage_improvement_works_sc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commissioning_date_of_drainage_improvement_works_sc = (
            _parse_commissioning_date_of_drainage_improvement_works_sc(
                d.pop("COMMISSIONING_DATE_OF_DRAINAGE_IMPROVEMENT_WORKS_SC", UNSET)
            )
        )

        def _parse_short_term_mitigation_measures_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        short_term_mitigation_measures_en = _parse_short_term_mitigation_measures_en(
            d.pop("SHORT_TERM_MITIGATION_MEASURES_EN", UNSET)
        )

        def _parse_short_term_mitigation_measures_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        short_term_mitigation_measures_tc = _parse_short_term_mitigation_measures_tc(
            d.pop("SHORT_TERM_MITIGATION_MEASURES_TC", UNSET)
        )

        def _parse_short_term_mitigation_measures_sc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        short_term_mitigation_measures_sc = _parse_short_term_mitigation_measures_sc(
            d.pop("SHORT_TERM_MITIGATION_MEASURES_SC", UNSET)
        )

        def _parse_long_term_mitigation_measures_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        long_term_mitigation_measures_en = _parse_long_term_mitigation_measures_en(
            d.pop("LONG_TERM_MITIGATION_MEASURES_EN", UNSET)
        )

        def _parse_long_term_mitigation_measures_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        long_term_mitigation_measures_tc = _parse_long_term_mitigation_measures_tc(
            d.pop("LONG_TERM_MITIGATION_MEASURES_TC", UNSET)
        )

        def _parse_long_term_mitigation_measures_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        long_term_mitigation_measures_sc = _parse_long_term_mitigation_measures_sc(
            d.pop("LONG_TERM_MITIGATION_MEASURES_SC", UNSET)
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

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            record_id=record_id,
            location_en=location_en,
            location_tc=location_tc,
            location_sc=location_sc,
            district_en=district_en,
            district_tc=district_tc,
            district_sc=district_sc,
            shape=shape,
            latitude=latitude,
            longitude=longitude,
            flooding_blackspot_scale=flooding_blackspot_scale,
            cause_of_flooding_en=cause_of_flooding_en,
            cause_of_flooding_tc=cause_of_flooding_tc,
            cause_of_flooding_sc=cause_of_flooding_sc,
            responsible_division_en=responsible_division_en,
            responsible_division_tc=responsible_division_tc,
            responsible_division_sc=responsible_division_sc,
            year_first_appeared=year_first_appeared,
            commissioning_date_of_drainage_improvement_works_en=commissioning_date_of_drainage_improvement_works_en,
            commissioning_date_of_drainage_improvement_works_tc=commissioning_date_of_drainage_improvement_works_tc,
            commissioning_date_of_drainage_improvement_works_sc=commissioning_date_of_drainage_improvement_works_sc,
            short_term_mitigation_measures_en=short_term_mitigation_measures_en,
            short_term_mitigation_measures_tc=short_term_mitigation_measures_tc,
            short_term_mitigation_measures_sc=short_term_mitigation_measures_sc,
            long_term_mitigation_measures_en=long_term_mitigation_measures_en,
            long_term_mitigation_measures_tc=long_term_mitigation_measures_tc,
            long_term_mitigation_measures_sc=long_term_mitigation_measures_sc,
            remark_en=remark_en,
            remark_tc=remark_tc,
            remark_sc=remark_sc,
            objectid=objectid,
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
