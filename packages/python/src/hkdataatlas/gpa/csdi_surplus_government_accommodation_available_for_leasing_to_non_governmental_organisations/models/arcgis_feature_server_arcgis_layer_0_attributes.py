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
        en_name (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_name (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_name (None | str | Unset): Publisher field type: esriFieldTypeString
        en_address (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_address (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_address (None | str | Unset): Publisher field type: esriFieldTypeString
        en_district (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_district (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_district (None | str | Unset): Publisher field type: esriFieldTypeString
        en_photo (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_photo (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_photo (None | str | Unset): Publisher field type: esriFieldTypeString
        en_ava_area_remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_ava_area_remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_ava_area_remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        en_declared_monument_grading_historic_building (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_declared_monument_grading_historic_building (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_declared_monument_grading_historic_building (None | str | Unset): Publisher field type: esriFieldTypeString
        en_lift (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_lift (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_lift (None | str | Unset): Publisher field type: esriFieldTypeString
        en_managing_dept (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_managing_dept (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_managing_dept (None | str | Unset): Publisher field type: esriFieldTypeString
        contact_number (None | str | Unset): Publisher field type: esriFieldTypeString
        en_ava_area (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_ava_area (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_ava_area (None | str | Unset): Publisher field type: esriFieldTypeString
        en_remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    en_name: None | str | Unset = UNSET
    tc_name: None | str | Unset = UNSET
    sc_name: None | str | Unset = UNSET
    en_address: None | str | Unset = UNSET
    tc_address: None | str | Unset = UNSET
    sc_address: None | str | Unset = UNSET
    en_district: None | str | Unset = UNSET
    tc_district: None | str | Unset = UNSET
    sc_district: None | str | Unset = UNSET
    en_photo: None | str | Unset = UNSET
    tc_photo: None | str | Unset = UNSET
    sc_photo: None | str | Unset = UNSET
    en_ava_area_remarks: None | str | Unset = UNSET
    tc_ava_area_remarks: None | str | Unset = UNSET
    sc_ava_area_remarks: None | str | Unset = UNSET
    en_declared_monument_grading_historic_building: None | str | Unset = UNSET
    tc_declared_monument_grading_historic_building: None | str | Unset = UNSET
    sc_declared_monument_grading_historic_building: None | str | Unset = UNSET
    en_lift: None | str | Unset = UNSET
    tc_lift: None | str | Unset = UNSET
    sc_lift: None | str | Unset = UNSET
    en_managing_dept: None | str | Unset = UNSET
    tc_managing_dept: None | str | Unset = UNSET
    sc_managing_dept: None | str | Unset = UNSET
    contact_number: None | str | Unset = UNSET
    en_ava_area: None | str | Unset = UNSET
    tc_ava_area: None | str | Unset = UNSET
    sc_ava_area: None | str | Unset = UNSET
    en_remarks: None | str | Unset = UNSET
    tc_remarks: None | str | Unset = UNSET
    sc_remarks: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        en_name: None | str | Unset
        if isinstance(self.en_name, Unset):
            en_name = UNSET
        else:
            en_name = self.en_name

        tc_name: None | str | Unset
        if isinstance(self.tc_name, Unset):
            tc_name = UNSET
        else:
            tc_name = self.tc_name

        sc_name: None | str | Unset
        if isinstance(self.sc_name, Unset):
            sc_name = UNSET
        else:
            sc_name = self.sc_name

        en_address: None | str | Unset
        if isinstance(self.en_address, Unset):
            en_address = UNSET
        else:
            en_address = self.en_address

        tc_address: None | str | Unset
        if isinstance(self.tc_address, Unset):
            tc_address = UNSET
        else:
            tc_address = self.tc_address

        sc_address: None | str | Unset
        if isinstance(self.sc_address, Unset):
            sc_address = UNSET
        else:
            sc_address = self.sc_address

        en_district: None | str | Unset
        if isinstance(self.en_district, Unset):
            en_district = UNSET
        else:
            en_district = self.en_district

        tc_district: None | str | Unset
        if isinstance(self.tc_district, Unset):
            tc_district = UNSET
        else:
            tc_district = self.tc_district

        sc_district: None | str | Unset
        if isinstance(self.sc_district, Unset):
            sc_district = UNSET
        else:
            sc_district = self.sc_district

        en_photo: None | str | Unset
        if isinstance(self.en_photo, Unset):
            en_photo = UNSET
        else:
            en_photo = self.en_photo

        tc_photo: None | str | Unset
        if isinstance(self.tc_photo, Unset):
            tc_photo = UNSET
        else:
            tc_photo = self.tc_photo

        sc_photo: None | str | Unset
        if isinstance(self.sc_photo, Unset):
            sc_photo = UNSET
        else:
            sc_photo = self.sc_photo

        en_ava_area_remarks: None | str | Unset
        if isinstance(self.en_ava_area_remarks, Unset):
            en_ava_area_remarks = UNSET
        else:
            en_ava_area_remarks = self.en_ava_area_remarks

        tc_ava_area_remarks: None | str | Unset
        if isinstance(self.tc_ava_area_remarks, Unset):
            tc_ava_area_remarks = UNSET
        else:
            tc_ava_area_remarks = self.tc_ava_area_remarks

        sc_ava_area_remarks: None | str | Unset
        if isinstance(self.sc_ava_area_remarks, Unset):
            sc_ava_area_remarks = UNSET
        else:
            sc_ava_area_remarks = self.sc_ava_area_remarks

        en_declared_monument_grading_historic_building: None | str | Unset
        if isinstance(self.en_declared_monument_grading_historic_building, Unset):
            en_declared_monument_grading_historic_building = UNSET
        else:
            en_declared_monument_grading_historic_building = (
                self.en_declared_monument_grading_historic_building
            )

        tc_declared_monument_grading_historic_building: None | str | Unset
        if isinstance(self.tc_declared_monument_grading_historic_building, Unset):
            tc_declared_monument_grading_historic_building = UNSET
        else:
            tc_declared_monument_grading_historic_building = (
                self.tc_declared_monument_grading_historic_building
            )

        sc_declared_monument_grading_historic_building: None | str | Unset
        if isinstance(self.sc_declared_monument_grading_historic_building, Unset):
            sc_declared_monument_grading_historic_building = UNSET
        else:
            sc_declared_monument_grading_historic_building = (
                self.sc_declared_monument_grading_historic_building
            )

        en_lift: None | str | Unset
        if isinstance(self.en_lift, Unset):
            en_lift = UNSET
        else:
            en_lift = self.en_lift

        tc_lift: None | str | Unset
        if isinstance(self.tc_lift, Unset):
            tc_lift = UNSET
        else:
            tc_lift = self.tc_lift

        sc_lift: None | str | Unset
        if isinstance(self.sc_lift, Unset):
            sc_lift = UNSET
        else:
            sc_lift = self.sc_lift

        en_managing_dept: None | str | Unset
        if isinstance(self.en_managing_dept, Unset):
            en_managing_dept = UNSET
        else:
            en_managing_dept = self.en_managing_dept

        tc_managing_dept: None | str | Unset
        if isinstance(self.tc_managing_dept, Unset):
            tc_managing_dept = UNSET
        else:
            tc_managing_dept = self.tc_managing_dept

        sc_managing_dept: None | str | Unset
        if isinstance(self.sc_managing_dept, Unset):
            sc_managing_dept = UNSET
        else:
            sc_managing_dept = self.sc_managing_dept

        contact_number: None | str | Unset
        if isinstance(self.contact_number, Unset):
            contact_number = UNSET
        else:
            contact_number = self.contact_number

        en_ava_area: None | str | Unset
        if isinstance(self.en_ava_area, Unset):
            en_ava_area = UNSET
        else:
            en_ava_area = self.en_ava_area

        tc_ava_area: None | str | Unset
        if isinstance(self.tc_ava_area, Unset):
            tc_ava_area = UNSET
        else:
            tc_ava_area = self.tc_ava_area

        sc_ava_area: None | str | Unset
        if isinstance(self.sc_ava_area, Unset):
            sc_ava_area = UNSET
        else:
            sc_ava_area = self.sc_ava_area

        en_remarks: None | str | Unset
        if isinstance(self.en_remarks, Unset):
            en_remarks = UNSET
        else:
            en_remarks = self.en_remarks

        tc_remarks: None | str | Unset
        if isinstance(self.tc_remarks, Unset):
            tc_remarks = UNSET
        else:
            tc_remarks = self.tc_remarks

        sc_remarks: None | str | Unset
        if isinstance(self.sc_remarks, Unset):
            sc_remarks = UNSET
        else:
            sc_remarks = self.sc_remarks

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if en_name is not UNSET:
            field_dict["en_name"] = en_name
        if tc_name is not UNSET:
            field_dict["tc_name"] = tc_name
        if sc_name is not UNSET:
            field_dict["sc_name"] = sc_name
        if en_address is not UNSET:
            field_dict["en_address"] = en_address
        if tc_address is not UNSET:
            field_dict["tc_address"] = tc_address
        if sc_address is not UNSET:
            field_dict["sc_address"] = sc_address
        if en_district is not UNSET:
            field_dict["en_district"] = en_district
        if tc_district is not UNSET:
            field_dict["tc_district"] = tc_district
        if sc_district is not UNSET:
            field_dict["sc_district"] = sc_district
        if en_photo is not UNSET:
            field_dict["en_photo"] = en_photo
        if tc_photo is not UNSET:
            field_dict["tc_photo"] = tc_photo
        if sc_photo is not UNSET:
            field_dict["sc_photo"] = sc_photo
        if en_ava_area_remarks is not UNSET:
            field_dict["en_ava_area_remarks"] = en_ava_area_remarks
        if tc_ava_area_remarks is not UNSET:
            field_dict["tc_ava_area_remarks"] = tc_ava_area_remarks
        if sc_ava_area_remarks is not UNSET:
            field_dict["sc_ava_area_remarks"] = sc_ava_area_remarks
        if en_declared_monument_grading_historic_building is not UNSET:
            field_dict["en_declared_monument_grading_historic_building"] = (
                en_declared_monument_grading_historic_building
            )
        if tc_declared_monument_grading_historic_building is not UNSET:
            field_dict["tc_declared_monument_grading_historic_building"] = (
                tc_declared_monument_grading_historic_building
            )
        if sc_declared_monument_grading_historic_building is not UNSET:
            field_dict["sc_declared_monument_grading_historic_building"] = (
                sc_declared_monument_grading_historic_building
            )
        if en_lift is not UNSET:
            field_dict["en_lift"] = en_lift
        if tc_lift is not UNSET:
            field_dict["tc_lift"] = tc_lift
        if sc_lift is not UNSET:
            field_dict["sc_lift"] = sc_lift
        if en_managing_dept is not UNSET:
            field_dict["en_managing_dept"] = en_managing_dept
        if tc_managing_dept is not UNSET:
            field_dict["tc_managing_dept"] = tc_managing_dept
        if sc_managing_dept is not UNSET:
            field_dict["sc_managing_dept"] = sc_managing_dept
        if contact_number is not UNSET:
            field_dict["contact_number"] = contact_number
        if en_ava_area is not UNSET:
            field_dict["en_ava_area"] = en_ava_area
        if tc_ava_area is not UNSET:
            field_dict["tc_ava_area"] = tc_ava_area
        if sc_ava_area is not UNSET:
            field_dict["sc_ava_area"] = sc_ava_area
        if en_remarks is not UNSET:
            field_dict["en_remarks"] = en_remarks
        if tc_remarks is not UNSET:
            field_dict["tc_remarks"] = tc_remarks
        if sc_remarks is not UNSET:
            field_dict["sc_remarks"] = sc_remarks
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_en_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_name = _parse_en_name(d.pop("en_name", UNSET))

        def _parse_tc_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_name = _parse_tc_name(d.pop("tc_name", UNSET))

        def _parse_sc_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_name = _parse_sc_name(d.pop("sc_name", UNSET))

        def _parse_en_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_address = _parse_en_address(d.pop("en_address", UNSET))

        def _parse_tc_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_address = _parse_tc_address(d.pop("tc_address", UNSET))

        def _parse_sc_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_address = _parse_sc_address(d.pop("sc_address", UNSET))

        def _parse_en_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_district = _parse_en_district(d.pop("en_district", UNSET))

        def _parse_tc_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_district = _parse_tc_district(d.pop("tc_district", UNSET))

        def _parse_sc_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_district = _parse_sc_district(d.pop("sc_district", UNSET))

        def _parse_en_photo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_photo = _parse_en_photo(d.pop("en_photo", UNSET))

        def _parse_tc_photo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_photo = _parse_tc_photo(d.pop("tc_photo", UNSET))

        def _parse_sc_photo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_photo = _parse_sc_photo(d.pop("sc_photo", UNSET))

        def _parse_en_ava_area_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_ava_area_remarks = _parse_en_ava_area_remarks(
            d.pop("en_ava_area_remarks", UNSET)
        )

        def _parse_tc_ava_area_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_ava_area_remarks = _parse_tc_ava_area_remarks(
            d.pop("tc_ava_area_remarks", UNSET)
        )

        def _parse_sc_ava_area_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_ava_area_remarks = _parse_sc_ava_area_remarks(
            d.pop("sc_ava_area_remarks", UNSET)
        )

        def _parse_en_declared_monument_grading_historic_building(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_declared_monument_grading_historic_building = (
            _parse_en_declared_monument_grading_historic_building(
                d.pop("en_declared_monument_grading_historic_building", UNSET)
            )
        )

        def _parse_tc_declared_monument_grading_historic_building(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_declared_monument_grading_historic_building = (
            _parse_tc_declared_monument_grading_historic_building(
                d.pop("tc_declared_monument_grading_historic_building", UNSET)
            )
        )

        def _parse_sc_declared_monument_grading_historic_building(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_declared_monument_grading_historic_building = (
            _parse_sc_declared_monument_grading_historic_building(
                d.pop("sc_declared_monument_grading_historic_building", UNSET)
            )
        )

        def _parse_en_lift(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_lift = _parse_en_lift(d.pop("en_lift", UNSET))

        def _parse_tc_lift(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_lift = _parse_tc_lift(d.pop("tc_lift", UNSET))

        def _parse_sc_lift(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_lift = _parse_sc_lift(d.pop("sc_lift", UNSET))

        def _parse_en_managing_dept(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_managing_dept = _parse_en_managing_dept(d.pop("en_managing_dept", UNSET))

        def _parse_tc_managing_dept(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_managing_dept = _parse_tc_managing_dept(d.pop("tc_managing_dept", UNSET))

        def _parse_sc_managing_dept(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_managing_dept = _parse_sc_managing_dept(d.pop("sc_managing_dept", UNSET))

        def _parse_contact_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_number = _parse_contact_number(d.pop("contact_number", UNSET))

        def _parse_en_ava_area(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_ava_area = _parse_en_ava_area(d.pop("en_ava_area", UNSET))

        def _parse_tc_ava_area(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_ava_area = _parse_tc_ava_area(d.pop("tc_ava_area", UNSET))

        def _parse_sc_ava_area(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_ava_area = _parse_sc_ava_area(d.pop("sc_ava_area", UNSET))

        def _parse_en_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_remarks = _parse_en_remarks(d.pop("en_remarks", UNSET))

        def _parse_tc_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_remarks = _parse_tc_remarks(d.pop("tc_remarks", UNSET))

        def _parse_sc_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_remarks = _parse_sc_remarks(d.pop("sc_remarks", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            en_name=en_name,
            tc_name=tc_name,
            sc_name=sc_name,
            en_address=en_address,
            tc_address=tc_address,
            sc_address=sc_address,
            en_district=en_district,
            tc_district=tc_district,
            sc_district=sc_district,
            en_photo=en_photo,
            tc_photo=tc_photo,
            sc_photo=sc_photo,
            en_ava_area_remarks=en_ava_area_remarks,
            tc_ava_area_remarks=tc_ava_area_remarks,
            sc_ava_area_remarks=sc_ava_area_remarks,
            en_declared_monument_grading_historic_building=en_declared_monument_grading_historic_building,
            tc_declared_monument_grading_historic_building=tc_declared_monument_grading_historic_building,
            sc_declared_monument_grading_historic_building=sc_declared_monument_grading_historic_building,
            en_lift=en_lift,
            tc_lift=tc_lift,
            sc_lift=sc_lift,
            en_managing_dept=en_managing_dept,
            tc_managing_dept=tc_managing_dept,
            sc_managing_dept=sc_managing_dept,
            contact_number=contact_number,
            en_ava_area=en_ava_area,
            tc_ava_area=tc_ava_area,
            sc_ava_area=sc_ava_area,
            en_remarks=en_remarks,
            tc_remarks=tc_remarks,
            sc_remarks=sc_remarks,
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
