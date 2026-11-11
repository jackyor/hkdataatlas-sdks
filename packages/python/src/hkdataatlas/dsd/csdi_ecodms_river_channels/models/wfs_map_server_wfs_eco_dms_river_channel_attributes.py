from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsEcoDmsRiverChannelAttributes")


@_attrs_define
class WfsMapServerWfsEcoDmsRiverChannelAttributes:
    """
    Attributes:
        record_id (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        channel_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        channel_name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        channel_name_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        location_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        location_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        location_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        shape (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        latitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        longitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        intro_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        intro_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        intro_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        remark_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        remark_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        remark_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        pdf_file (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape_1 (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its
            XML type.
    """

    record_id: None | str | Unset = UNSET
    channel_name_en: None | str | Unset = UNSET
    channel_name_tc: None | str | Unset = UNSET
    channel_name_sc: None | str | Unset = UNSET
    location_en: None | str | Unset = UNSET
    location_tc: None | str | Unset = UNSET
    location_sc: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    district_sc: None | str | Unset = UNSET
    shape: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    intro_en: None | str | Unset = UNSET
    intro_tc: None | str | Unset = UNSET
    intro_sc: None | str | Unset = UNSET
    remark_en: None | str | Unset = UNSET
    remark_tc: None | str | Unset = UNSET
    remark_sc: None | str | Unset = UNSET
    pdf_file: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_1: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        record_id: None | str | Unset
        if isinstance(self.record_id, Unset):
            record_id = UNSET
        else:
            record_id = self.record_id

        channel_name_en: None | str | Unset
        if isinstance(self.channel_name_en, Unset):
            channel_name_en = UNSET
        else:
            channel_name_en = self.channel_name_en

        channel_name_tc: None | str | Unset
        if isinstance(self.channel_name_tc, Unset):
            channel_name_tc = UNSET
        else:
            channel_name_tc = self.channel_name_tc

        channel_name_sc: None | str | Unset
        if isinstance(self.channel_name_sc, Unset):
            channel_name_sc = UNSET
        else:
            channel_name_sc = self.channel_name_sc

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

        intro_en: None | str | Unset
        if isinstance(self.intro_en, Unset):
            intro_en = UNSET
        else:
            intro_en = self.intro_en

        intro_tc: None | str | Unset
        if isinstance(self.intro_tc, Unset):
            intro_tc = UNSET
        else:
            intro_tc = self.intro_tc

        intro_sc: None | str | Unset
        if isinstance(self.intro_sc, Unset):
            intro_sc = UNSET
        else:
            intro_sc = self.intro_sc

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

        pdf_file: None | str | Unset
        if isinstance(self.pdf_file, Unset):
            pdf_file = UNSET
        else:
            pdf_file = self.pdf_file

        objectid = self.objectid

        shape_1 = self.shape_1

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if record_id is not UNSET:
            field_dict["RECORD_ID"] = record_id
        if channel_name_en is not UNSET:
            field_dict["CHANNEL_NAME_EN"] = channel_name_en
        if channel_name_tc is not UNSET:
            field_dict["CHANNEL_NAME_TC"] = channel_name_tc
        if channel_name_sc is not UNSET:
            field_dict["CHANNEL_NAME_SC"] = channel_name_sc
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
        if intro_en is not UNSET:
            field_dict["INTRO_EN"] = intro_en
        if intro_tc is not UNSET:
            field_dict["INTRO_TC"] = intro_tc
        if intro_sc is not UNSET:
            field_dict["INTRO_SC"] = intro_sc
        if remark_en is not UNSET:
            field_dict["REMARK_EN"] = remark_en
        if remark_tc is not UNSET:
            field_dict["REMARK_TC"] = remark_tc
        if remark_sc is not UNSET:
            field_dict["REMARK_SC"] = remark_sc
        if pdf_file is not UNSET:
            field_dict["PDF_FILE"] = pdf_file
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

        def _parse_channel_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_name_en = _parse_channel_name_en(d.pop("CHANNEL_NAME_EN", UNSET))

        def _parse_channel_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_name_tc = _parse_channel_name_tc(d.pop("CHANNEL_NAME_TC", UNSET))

        def _parse_channel_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_name_sc = _parse_channel_name_sc(d.pop("CHANNEL_NAME_SC", UNSET))

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

        def _parse_intro_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        intro_en = _parse_intro_en(d.pop("INTRO_EN", UNSET))

        def _parse_intro_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        intro_tc = _parse_intro_tc(d.pop("INTRO_TC", UNSET))

        def _parse_intro_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        intro_sc = _parse_intro_sc(d.pop("INTRO_SC", UNSET))

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

        def _parse_pdf_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pdf_file = _parse_pdf_file(d.pop("PDF_FILE", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape_1 = d.pop("SHAPE_1", UNSET)

        wfs_map_server_wfs_eco_dms_river_channel_attributes = cls(
            record_id=record_id,
            channel_name_en=channel_name_en,
            channel_name_tc=channel_name_tc,
            channel_name_sc=channel_name_sc,
            location_en=location_en,
            location_tc=location_tc,
            location_sc=location_sc,
            district_en=district_en,
            district_tc=district_tc,
            district_sc=district_sc,
            shape=shape,
            latitude=latitude,
            longitude=longitude,
            intro_en=intro_en,
            intro_tc=intro_tc,
            intro_sc=intro_sc,
            remark_en=remark_en,
            remark_tc=remark_tc,
            remark_sc=remark_sc,
            pdf_file=pdf_file,
            objectid=objectid,
            shape_1=shape_1,
        )

        wfs_map_server_wfs_eco_dms_river_channel_attributes.additional_properties = d
        return wfs_map_server_wfs_eco_dms_river_channel_attributes

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
