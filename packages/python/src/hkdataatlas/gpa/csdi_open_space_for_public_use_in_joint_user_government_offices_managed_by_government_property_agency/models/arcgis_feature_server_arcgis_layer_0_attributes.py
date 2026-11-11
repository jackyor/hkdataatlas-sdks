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
        objectid (None | str | Unset): Publisher field type: esriFieldTypeString
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        bldg_engnm (None | str | Unset): Publisher field type: esriFieldTypeString
        bldg_chtnm (None | str | Unset): Publisher field type: esriFieldTypeString
        os_type_en (None | str | Unset): Publisher field type: esriFieldTypeString
        os_type_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        os_status_en (None | str | Unset): Publisher field type: esriFieldTypeString
        os_status_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        beach_en (None | str | Unset): Publisher field type: esriFieldTypeString
        beach_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        amenity_area_en (None | str | Unset): Publisher field type: esriFieldTypeString
        amenity_area_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        indoor_facilities_en (None | str | Unset): Publisher field type: esriFieldTypeString
        indoor_facilities_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        completion_year_en (None | str | Unset): Publisher field type: esriFieldTypeString
        completion_year_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        os_area_en_sq_metre (None | str | Unset): Publisher field type: esriFieldTypeString
        os_area_tc_sq_metre (None | str | Unset): Publisher field type: esriFieldTypeString
        last_update (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid_1 (int | Unset): Publisher field type: esriFieldTypeOID
    """

    objectid: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    bldg_engnm: None | str | Unset = UNSET
    bldg_chtnm: None | str | Unset = UNSET
    os_type_en: None | str | Unset = UNSET
    os_type_tc: None | str | Unset = UNSET
    os_status_en: None | str | Unset = UNSET
    os_status_tc: None | str | Unset = UNSET
    beach_en: None | str | Unset = UNSET
    beach_tc: None | str | Unset = UNSET
    amenity_area_en: None | str | Unset = UNSET
    amenity_area_tc: None | str | Unset = UNSET
    indoor_facilities_en: None | str | Unset = UNSET
    indoor_facilities_tc: None | str | Unset = UNSET
    completion_year_en: None | str | Unset = UNSET
    completion_year_tc: None | str | Unset = UNSET
    os_area_en_sq_metre: None | str | Unset = UNSET
    os_area_tc_sq_metre: None | str | Unset = UNSET
    last_update: None | str | Unset = UNSET
    objectid_1: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid: None | str | Unset
        if isinstance(self.objectid, Unset):
            objectid = UNSET
        else:
            objectid = self.objectid

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        bldg_engnm: None | str | Unset
        if isinstance(self.bldg_engnm, Unset):
            bldg_engnm = UNSET
        else:
            bldg_engnm = self.bldg_engnm

        bldg_chtnm: None | str | Unset
        if isinstance(self.bldg_chtnm, Unset):
            bldg_chtnm = UNSET
        else:
            bldg_chtnm = self.bldg_chtnm

        os_type_en: None | str | Unset
        if isinstance(self.os_type_en, Unset):
            os_type_en = UNSET
        else:
            os_type_en = self.os_type_en

        os_type_tc: None | str | Unset
        if isinstance(self.os_type_tc, Unset):
            os_type_tc = UNSET
        else:
            os_type_tc = self.os_type_tc

        os_status_en: None | str | Unset
        if isinstance(self.os_status_en, Unset):
            os_status_en = UNSET
        else:
            os_status_en = self.os_status_en

        os_status_tc: None | str | Unset
        if isinstance(self.os_status_tc, Unset):
            os_status_tc = UNSET
        else:
            os_status_tc = self.os_status_tc

        beach_en: None | str | Unset
        if isinstance(self.beach_en, Unset):
            beach_en = UNSET
        else:
            beach_en = self.beach_en

        beach_tc: None | str | Unset
        if isinstance(self.beach_tc, Unset):
            beach_tc = UNSET
        else:
            beach_tc = self.beach_tc

        amenity_area_en: None | str | Unset
        if isinstance(self.amenity_area_en, Unset):
            amenity_area_en = UNSET
        else:
            amenity_area_en = self.amenity_area_en

        amenity_area_tc: None | str | Unset
        if isinstance(self.amenity_area_tc, Unset):
            amenity_area_tc = UNSET
        else:
            amenity_area_tc = self.amenity_area_tc

        indoor_facilities_en: None | str | Unset
        if isinstance(self.indoor_facilities_en, Unset):
            indoor_facilities_en = UNSET
        else:
            indoor_facilities_en = self.indoor_facilities_en

        indoor_facilities_tc: None | str | Unset
        if isinstance(self.indoor_facilities_tc, Unset):
            indoor_facilities_tc = UNSET
        else:
            indoor_facilities_tc = self.indoor_facilities_tc

        completion_year_en: None | str | Unset
        if isinstance(self.completion_year_en, Unset):
            completion_year_en = UNSET
        else:
            completion_year_en = self.completion_year_en

        completion_year_tc: None | str | Unset
        if isinstance(self.completion_year_tc, Unset):
            completion_year_tc = UNSET
        else:
            completion_year_tc = self.completion_year_tc

        os_area_en_sq_metre: None | str | Unset
        if isinstance(self.os_area_en_sq_metre, Unset):
            os_area_en_sq_metre = UNSET
        else:
            os_area_en_sq_metre = self.os_area_en_sq_metre

        os_area_tc_sq_metre: None | str | Unset
        if isinstance(self.os_area_tc_sq_metre, Unset):
            os_area_tc_sq_metre = UNSET
        else:
            os_area_tc_sq_metre = self.os_area_tc_sq_metre

        last_update: None | str | Unset
        if isinstance(self.last_update, Unset):
            last_update = UNSET
        else:
            last_update = self.last_update

        objectid_1 = self.objectid_1

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if address_en is not UNSET:
            field_dict["ADDRESS_EN"] = address_en
        if address_tc is not UNSET:
            field_dict["ADDRESS_TC"] = address_tc
        if bldg_engnm is not UNSET:
            field_dict["BLDG_ENGNM"] = bldg_engnm
        if bldg_chtnm is not UNSET:
            field_dict["BLDG_CHTNM"] = bldg_chtnm
        if os_type_en is not UNSET:
            field_dict["OS_TYPE_EN"] = os_type_en
        if os_type_tc is not UNSET:
            field_dict["OS_TYPE_TC"] = os_type_tc
        if os_status_en is not UNSET:
            field_dict["OS_STATUS_EN"] = os_status_en
        if os_status_tc is not UNSET:
            field_dict["OS_STATUS_TC"] = os_status_tc
        if beach_en is not UNSET:
            field_dict["BEACH_EN"] = beach_en
        if beach_tc is not UNSET:
            field_dict["BEACH_TC"] = beach_tc
        if amenity_area_en is not UNSET:
            field_dict["AMENITY_AREA_EN"] = amenity_area_en
        if amenity_area_tc is not UNSET:
            field_dict["AMENITY_AREA_TC"] = amenity_area_tc
        if indoor_facilities_en is not UNSET:
            field_dict["INDOOR_FACILITIES_EN"] = indoor_facilities_en
        if indoor_facilities_tc is not UNSET:
            field_dict["INDOOR_FACILITIES_TC"] = indoor_facilities_tc
        if completion_year_en is not UNSET:
            field_dict["COMPLETION_YEAR_EN"] = completion_year_en
        if completion_year_tc is not UNSET:
            field_dict["COMPLETION_YEAR_TC"] = completion_year_tc
        if os_area_en_sq_metre is not UNSET:
            field_dict["OS_AREA_EN__sq_metre_"] = os_area_en_sq_metre
        if os_area_tc_sq_metre is not UNSET:
            field_dict["OS_AREA_TC__sq_metre_"] = os_area_tc_sq_metre
        if last_update is not UNSET:
            field_dict["LAST_UPDATE"] = last_update
        if objectid_1 is not UNSET:
            field_dict["OBJECTID_1"] = objectid_1

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_objectid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        objectid = _parse_objectid(d.pop("OBJECTID", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("ADDRESS_EN", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("ADDRESS_TC", UNSET))

        def _parse_bldg_engnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bldg_engnm = _parse_bldg_engnm(d.pop("BLDG_ENGNM", UNSET))

        def _parse_bldg_chtnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bldg_chtnm = _parse_bldg_chtnm(d.pop("BLDG_CHTNM", UNSET))

        def _parse_os_type_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        os_type_en = _parse_os_type_en(d.pop("OS_TYPE_EN", UNSET))

        def _parse_os_type_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        os_type_tc = _parse_os_type_tc(d.pop("OS_TYPE_TC", UNSET))

        def _parse_os_status_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        os_status_en = _parse_os_status_en(d.pop("OS_STATUS_EN", UNSET))

        def _parse_os_status_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        os_status_tc = _parse_os_status_tc(d.pop("OS_STATUS_TC", UNSET))

        def _parse_beach_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beach_en = _parse_beach_en(d.pop("BEACH_EN", UNSET))

        def _parse_beach_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beach_tc = _parse_beach_tc(d.pop("BEACH_TC", UNSET))

        def _parse_amenity_area_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amenity_area_en = _parse_amenity_area_en(d.pop("AMENITY_AREA_EN", UNSET))

        def _parse_amenity_area_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amenity_area_tc = _parse_amenity_area_tc(d.pop("AMENITY_AREA_TC", UNSET))

        def _parse_indoor_facilities_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        indoor_facilities_en = _parse_indoor_facilities_en(
            d.pop("INDOOR_FACILITIES_EN", UNSET)
        )

        def _parse_indoor_facilities_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        indoor_facilities_tc = _parse_indoor_facilities_tc(
            d.pop("INDOOR_FACILITIES_TC", UNSET)
        )

        def _parse_completion_year_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completion_year_en = _parse_completion_year_en(
            d.pop("COMPLETION_YEAR_EN", UNSET)
        )

        def _parse_completion_year_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completion_year_tc = _parse_completion_year_tc(
            d.pop("COMPLETION_YEAR_TC", UNSET)
        )

        def _parse_os_area_en_sq_metre(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        os_area_en_sq_metre = _parse_os_area_en_sq_metre(
            d.pop("OS_AREA_EN__sq_metre_", UNSET)
        )

        def _parse_os_area_tc_sq_metre(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        os_area_tc_sq_metre = _parse_os_area_tc_sq_metre(
            d.pop("OS_AREA_TC__sq_metre_", UNSET)
        )

        def _parse_last_update(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_update = _parse_last_update(d.pop("LAST_UPDATE", UNSET))

        objectid_1 = d.pop("OBJECTID_1", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            address_en=address_en,
            address_tc=address_tc,
            bldg_engnm=bldg_engnm,
            bldg_chtnm=bldg_chtnm,
            os_type_en=os_type_en,
            os_type_tc=os_type_tc,
            os_status_en=os_status_en,
            os_status_tc=os_status_tc,
            beach_en=beach_en,
            beach_tc=beach_tc,
            amenity_area_en=amenity_area_en,
            amenity_area_tc=amenity_area_tc,
            indoor_facilities_en=indoor_facilities_en,
            indoor_facilities_tc=indoor_facilities_tc,
            completion_year_en=completion_year_en,
            completion_year_tc=completion_year_tc,
            os_area_en_sq_metre=os_area_en_sq_metre,
            os_area_tc_sq_metre=os_area_tc_sq_metre,
            last_update=last_update,
            objectid_1=objectid_1,
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
