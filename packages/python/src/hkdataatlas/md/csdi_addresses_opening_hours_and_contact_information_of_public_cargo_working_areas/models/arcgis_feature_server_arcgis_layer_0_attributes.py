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
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hours (None | str | Unset): Publisher field type: esriFieldTypeString
        closing_hours (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        contact (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    name_en: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    name_sc: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    district_sc: None | str | Unset = UNSET
    opening_hours: None | str | Unset = UNSET
    closing_hours: None | str | Unset = UNSET
    remarks_en: None | str | Unset = UNSET
    remarks_tc: None | str | Unset = UNSET
    remarks_sc: None | str | Unset = UNSET
    contact: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        name_sc: None | str | Unset
        if isinstance(self.name_sc, Unset):
            name_sc = UNSET
        else:
            name_sc = self.name_sc

        address_sc: None | str | Unset
        if isinstance(self.address_sc, Unset):
            address_sc = UNSET
        else:
            address_sc = self.address_sc

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

        opening_hours: None | str | Unset
        if isinstance(self.opening_hours, Unset):
            opening_hours = UNSET
        else:
            opening_hours = self.opening_hours

        closing_hours: None | str | Unset
        if isinstance(self.closing_hours, Unset):
            closing_hours = UNSET
        else:
            closing_hours = self.closing_hours

        remarks_en: None | str | Unset
        if isinstance(self.remarks_en, Unset):
            remarks_en = UNSET
        else:
            remarks_en = self.remarks_en

        remarks_tc: None | str | Unset
        if isinstance(self.remarks_tc, Unset):
            remarks_tc = UNSET
        else:
            remarks_tc = self.remarks_tc

        remarks_sc: None | str | Unset
        if isinstance(self.remarks_sc, Unset):
            remarks_sc = UNSET
        else:
            remarks_sc = self.remarks_sc

        contact: None | str | Unset
        if isinstance(self.contact, Unset):
            contact = UNSET
        else:
            contact = self.contact

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name_en is not UNSET:
            field_dict["NAME_EN"] = name_en
        if address_en is not UNSET:
            field_dict["ADDRESS_EN"] = address_en
        if name_tc is not UNSET:
            field_dict["NAME_TC"] = name_tc
        if address_tc is not UNSET:
            field_dict["ADDRESS_TC"] = address_tc
        if name_sc is not UNSET:
            field_dict["NAME_SC"] = name_sc
        if address_sc is not UNSET:
            field_dict["ADDRESS_SC"] = address_sc
        if district_en is not UNSET:
            field_dict["DISTRICT_EN"] = district_en
        if district_tc is not UNSET:
            field_dict["DISTRICT_TC"] = district_tc
        if district_sc is not UNSET:
            field_dict["DISTRICT_SC"] = district_sc
        if opening_hours is not UNSET:
            field_dict["OPENING_HOURS"] = opening_hours
        if closing_hours is not UNSET:
            field_dict["CLOSING_HOURS"] = closing_hours
        if remarks_en is not UNSET:
            field_dict["REMARKS_EN"] = remarks_en
        if remarks_tc is not UNSET:
            field_dict["REMARKS_TC"] = remarks_tc
        if remarks_sc is not UNSET:
            field_dict["REMARKS_SC"] = remarks_sc
        if contact is not UNSET:
            field_dict["CONTACT"] = contact
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("NAME_EN", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("ADDRESS_EN", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("NAME_TC", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("ADDRESS_TC", UNSET))

        def _parse_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_sc = _parse_name_sc(d.pop("NAME_SC", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("ADDRESS_SC", UNSET))

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

        def _parse_opening_hours(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours = _parse_opening_hours(d.pop("OPENING_HOURS", UNSET))

        def _parse_closing_hours(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        closing_hours = _parse_closing_hours(d.pop("CLOSING_HOURS", UNSET))

        def _parse_remarks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_en = _parse_remarks_en(d.pop("REMARKS_EN", UNSET))

        def _parse_remarks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_tc = _parse_remarks_tc(d.pop("REMARKS_TC", UNSET))

        def _parse_remarks_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_sc = _parse_remarks_sc(d.pop("REMARKS_SC", UNSET))

        def _parse_contact(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact = _parse_contact(d.pop("CONTACT", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            name_en=name_en,
            address_en=address_en,
            name_tc=name_tc,
            address_tc=address_tc,
            name_sc=name_sc,
            address_sc=address_sc,
            district_en=district_en,
            district_tc=district_tc,
            district_sc=district_sc,
            opening_hours=opening_hours,
            closing_hours=closing_hours,
            remarks_en=remarks_en,
            remarks_tc=remarks_tc,
            remarks_sc=remarks_sc,
            contact=contact,
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
