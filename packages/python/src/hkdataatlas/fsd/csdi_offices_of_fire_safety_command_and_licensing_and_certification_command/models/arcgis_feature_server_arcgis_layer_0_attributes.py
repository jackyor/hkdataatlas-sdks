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
        command (None | str | Unset): Publisher field type: esriFieldTypeString
        office_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        office_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        office_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        office_address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        office_address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        office_address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone (None | str | Unset): Publisher field type: esriFieldTypeString
        district_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    command: None | str | Unset = UNSET
    office_name_en: None | str | Unset = UNSET
    office_name_tc: None | str | Unset = UNSET
    office_name_sc: None | str | Unset = UNSET
    office_address_en: None | str | Unset = UNSET
    office_address_tc: None | str | Unset = UNSET
    office_address_sc: None | str | Unset = UNSET
    telephone: None | str | Unset = UNSET
    district_eng: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    district_sc: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    easting: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        command: None | str | Unset
        if isinstance(self.command, Unset):
            command = UNSET
        else:
            command = self.command

        office_name_en: None | str | Unset
        if isinstance(self.office_name_en, Unset):
            office_name_en = UNSET
        else:
            office_name_en = self.office_name_en

        office_name_tc: None | str | Unset
        if isinstance(self.office_name_tc, Unset):
            office_name_tc = UNSET
        else:
            office_name_tc = self.office_name_tc

        office_name_sc: None | str | Unset
        if isinstance(self.office_name_sc, Unset):
            office_name_sc = UNSET
        else:
            office_name_sc = self.office_name_sc

        office_address_en: None | str | Unset
        if isinstance(self.office_address_en, Unset):
            office_address_en = UNSET
        else:
            office_address_en = self.office_address_en

        office_address_tc: None | str | Unset
        if isinstance(self.office_address_tc, Unset):
            office_address_tc = UNSET
        else:
            office_address_tc = self.office_address_tc

        office_address_sc: None | str | Unset
        if isinstance(self.office_address_sc, Unset):
            office_address_sc = UNSET
        else:
            office_address_sc = self.office_address_sc

        telephone: None | str | Unset
        if isinstance(self.telephone, Unset):
            telephone = UNSET
        else:
            telephone = self.telephone

        district_eng: None | str | Unset
        if isinstance(self.district_eng, Unset):
            district_eng = UNSET
        else:
            district_eng = self.district_eng

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

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if command is not UNSET:
            field_dict["Command"] = command
        if office_name_en is not UNSET:
            field_dict["Office_Name_EN"] = office_name_en
        if office_name_tc is not UNSET:
            field_dict["Office_Name_TC"] = office_name_tc
        if office_name_sc is not UNSET:
            field_dict["Office_Name_SC"] = office_name_sc
        if office_address_en is not UNSET:
            field_dict["Office_Address_EN"] = office_address_en
        if office_address_tc is not UNSET:
            field_dict["Office_Address_TC"] = office_address_tc
        if office_address_sc is not UNSET:
            field_dict["Office_Address_SC"] = office_address_sc
        if telephone is not UNSET:
            field_dict["Telephone"] = telephone
        if district_eng is not UNSET:
            field_dict["District_ENG"] = district_eng
        if district_tc is not UNSET:
            field_dict["District_TC"] = district_tc
        if district_sc is not UNSET:
            field_dict["District_SC"] = district_sc
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if easting is not UNSET:
            field_dict["Easting"] = easting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_command(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        command = _parse_command(d.pop("Command", UNSET))

        def _parse_office_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_name_en = _parse_office_name_en(d.pop("Office_Name_EN", UNSET))

        def _parse_office_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_name_tc = _parse_office_name_tc(d.pop("Office_Name_TC", UNSET))

        def _parse_office_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_name_sc = _parse_office_name_sc(d.pop("Office_Name_SC", UNSET))

        def _parse_office_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_address_en = _parse_office_address_en(d.pop("Office_Address_EN", UNSET))

        def _parse_office_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_address_tc = _parse_office_address_tc(d.pop("Office_Address_TC", UNSET))

        def _parse_office_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_address_sc = _parse_office_address_sc(d.pop("Office_Address_SC", UNSET))

        def _parse_telephone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone = _parse_telephone(d.pop("Telephone", UNSET))

        def _parse_district_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_eng = _parse_district_eng(d.pop("District_ENG", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("District_TC", UNSET))

        def _parse_district_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_sc = _parse_district_sc(d.pop("District_SC", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("Easting", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            command=command,
            office_name_en=office_name_en,
            office_name_tc=office_name_tc,
            office_name_sc=office_name_sc,
            office_address_en=office_address_en,
            office_address_tc=office_address_tc,
            office_address_sc=office_address_sc,
            telephone=telephone,
            district_eng=district_eng,
            district_tc=district_tc,
            district_sc=district_sc,
            northing=northing,
            easting=easting,
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
