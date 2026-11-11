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
        tunnel_control_area_en (None | str | Unset): Publisher field type: esriFieldTypeString
        tunnel_control_area_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        tunnel_control_area_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        operator_en (None | str | Unset): Publisher field type: esriFieldTypeString
        operator_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        operator_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        tel (None | str | Unset): Publisher field type: esriFieldTypeString
        fax (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    tunnel_control_area_en: None | str | Unset = UNSET
    tunnel_control_area_tc: None | str | Unset = UNSET
    tunnel_control_area_sc: None | str | Unset = UNSET
    operator_en: None | str | Unset = UNSET
    operator_tc: None | str | Unset = UNSET
    operator_sc: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    tel: None | str | Unset = UNSET
    fax: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        tunnel_control_area_en: None | str | Unset
        if isinstance(self.tunnel_control_area_en, Unset):
            tunnel_control_area_en = UNSET
        else:
            tunnel_control_area_en = self.tunnel_control_area_en

        tunnel_control_area_tc: None | str | Unset
        if isinstance(self.tunnel_control_area_tc, Unset):
            tunnel_control_area_tc = UNSET
        else:
            tunnel_control_area_tc = self.tunnel_control_area_tc

        tunnel_control_area_sc: None | str | Unset
        if isinstance(self.tunnel_control_area_sc, Unset):
            tunnel_control_area_sc = UNSET
        else:
            tunnel_control_area_sc = self.tunnel_control_area_sc

        operator_en: None | str | Unset
        if isinstance(self.operator_en, Unset):
            operator_en = UNSET
        else:
            operator_en = self.operator_en

        operator_tc: None | str | Unset
        if isinstance(self.operator_tc, Unset):
            operator_tc = UNSET
        else:
            operator_tc = self.operator_tc

        operator_sc: None | str | Unset
        if isinstance(self.operator_sc, Unset):
            operator_sc = UNSET
        else:
            operator_sc = self.operator_sc

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

        address_sc: None | str | Unset
        if isinstance(self.address_sc, Unset):
            address_sc = UNSET
        else:
            address_sc = self.address_sc

        tel: None | str | Unset
        if isinstance(self.tel, Unset):
            tel = UNSET
        else:
            tel = self.tel

        fax: None | str | Unset
        if isinstance(self.fax, Unset):
            fax = UNSET
        else:
            fax = self.fax

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if tunnel_control_area_en is not UNSET:
            field_dict["TunnelControlArea_en"] = tunnel_control_area_en
        if tunnel_control_area_tc is not UNSET:
            field_dict["TunnelControlArea_tc"] = tunnel_control_area_tc
        if tunnel_control_area_sc is not UNSET:
            field_dict["TunnelControlArea_sc"] = tunnel_control_area_sc
        if operator_en is not UNSET:
            field_dict["Operator_en"] = operator_en
        if operator_tc is not UNSET:
            field_dict["Operator_tc"] = operator_tc
        if operator_sc is not UNSET:
            field_dict["Operator_sc"] = operator_sc
        if address_en is not UNSET:
            field_dict["Address_en"] = address_en
        if address_tc is not UNSET:
            field_dict["Address_tc"] = address_tc
        if address_sc is not UNSET:
            field_dict["Address_sc"] = address_sc
        if tel is not UNSET:
            field_dict["Tel"] = tel
        if fax is not UNSET:
            field_dict["Fax"] = fax

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_tunnel_control_area_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tunnel_control_area_en = _parse_tunnel_control_area_en(
            d.pop("TunnelControlArea_en", UNSET)
        )

        def _parse_tunnel_control_area_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tunnel_control_area_tc = _parse_tunnel_control_area_tc(
            d.pop("TunnelControlArea_tc", UNSET)
        )

        def _parse_tunnel_control_area_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tunnel_control_area_sc = _parse_tunnel_control_area_sc(
            d.pop("TunnelControlArea_sc", UNSET)
        )

        def _parse_operator_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operator_en = _parse_operator_en(d.pop("Operator_en", UNSET))

        def _parse_operator_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operator_tc = _parse_operator_tc(d.pop("Operator_tc", UNSET))

        def _parse_operator_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operator_sc = _parse_operator_sc(d.pop("Operator_sc", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("Address_en", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("Address_tc", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("Address_sc", UNSET))

        def _parse_tel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tel = _parse_tel(d.pop("Tel", UNSET))

        def _parse_fax(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax = _parse_fax(d.pop("Fax", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            tunnel_control_area_en=tunnel_control_area_en,
            tunnel_control_area_tc=tunnel_control_area_tc,
            tunnel_control_area_sc=tunnel_control_area_sc,
            operator_en=operator_en,
            operator_tc=operator_tc,
            operator_sc=operator_sc,
            address_en=address_en,
            address_tc=address_tc,
            address_sc=address_sc,
            tel=tel,
            fax=fax,
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
