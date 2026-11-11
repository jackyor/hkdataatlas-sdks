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
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        number (float | None | Unset): Publisher field type: esriFieldTypeDouble
        address (None | str | Unset): Publisher field type: esriFieldTypeString
        company_name (None | str | Unset): Publisher field type: esriFieldTypeString
        company_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        company_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        licence_no (None | str | Unset): Publisher field type: esriFieldTypeString
        tel_no (None | str | Unset): Publisher field type: esriFieldTypeString
        trading_as (None | str | Unset): Publisher field type: esriFieldTypeString
        trading_as_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        trading_as_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        type_ (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    number: float | None | Unset = UNSET
    address: None | str | Unset = UNSET
    company_name: None | str | Unset = UNSET
    company_name_sc: None | str | Unset = UNSET
    company_name_tc: None | str | Unset = UNSET
    licence_no: None | str | Unset = UNSET
    tel_no: None | str | Unset = UNSET
    trading_as: None | str | Unset = UNSET
    trading_as_sc: None | str | Unset = UNSET
    trading_as_tc: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        number: float | None | Unset
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        company_name_sc: None | str | Unset
        if isinstance(self.company_name_sc, Unset):
            company_name_sc = UNSET
        else:
            company_name_sc = self.company_name_sc

        company_name_tc: None | str | Unset
        if isinstance(self.company_name_tc, Unset):
            company_name_tc = UNSET
        else:
            company_name_tc = self.company_name_tc

        licence_no: None | str | Unset
        if isinstance(self.licence_no, Unset):
            licence_no = UNSET
        else:
            licence_no = self.licence_no

        tel_no: None | str | Unset
        if isinstance(self.tel_no, Unset):
            tel_no = UNSET
        else:
            tel_no = self.tel_no

        trading_as: None | str | Unset
        if isinstance(self.trading_as, Unset):
            trading_as = UNSET
        else:
            trading_as = self.trading_as

        trading_as_sc: None | str | Unset
        if isinstance(self.trading_as_sc, Unset):
            trading_as_sc = UNSET
        else:
            trading_as_sc = self.trading_as_sc

        trading_as_tc: None | str | Unset
        if isinstance(self.trading_as_tc, Unset):
            trading_as_tc = UNSET
        else:
            trading_as_tc = self.trading_as_tc

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if number is not UNSET:
            field_dict["Number"] = number
        if address is not UNSET:
            field_dict["address"] = address
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if company_name_sc is not UNSET:
            field_dict["company_name_sc"] = company_name_sc
        if company_name_tc is not UNSET:
            field_dict["company_name_tc"] = company_name_tc
        if licence_no is not UNSET:
            field_dict["licence_no"] = licence_no
        if tel_no is not UNSET:
            field_dict["tel_no"] = tel_no
        if trading_as is not UNSET:
            field_dict["trading_as"] = trading_as
        if trading_as_sc is not UNSET:
            field_dict["trading_as_sc"] = trading_as_sc
        if trading_as_tc is not UNSET:
            field_dict["trading_as_tc"] = trading_as_tc
        if type_ is not UNSET:
            field_dict["type"] = type_
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        def _parse_number(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        number = _parse_number(d.pop("Number", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        def _parse_company_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name_sc = _parse_company_name_sc(d.pop("company_name_sc", UNSET))

        def _parse_company_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name_tc = _parse_company_name_tc(d.pop("company_name_tc", UNSET))

        def _parse_licence_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        licence_no = _parse_licence_no(d.pop("licence_no", UNSET))

        def _parse_tel_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tel_no = _parse_tel_no(d.pop("tel_no", UNSET))

        def _parse_trading_as(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trading_as = _parse_trading_as(d.pop("trading_as", UNSET))

        def _parse_trading_as_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trading_as_sc = _parse_trading_as_sc(d.pop("trading_as_sc", UNSET))

        def _parse_trading_as_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trading_as_tc = _parse_trading_as_tc(d.pop("trading_as_tc", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            latitude=latitude,
            longitude=longitude,
            number=number,
            address=address,
            company_name=company_name,
            company_name_sc=company_name_sc,
            company_name_tc=company_name_tc,
            licence_no=licence_no,
            tel_no=tel_no,
            trading_as=trading_as,
            trading_as_sc=trading_as_sc,
            trading_as_tc=trading_as_tc,
            type_=type_,
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
