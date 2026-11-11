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
        bldg_chtnm (None | str | Unset): Publisher field type: esriFieldTypeString
        bldg_engnm (None | str | Unset): Publisher field type: esriFieldTypeString
        email (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    bldg_chtnm: None | str | Unset = UNSET
    bldg_engnm: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    telephone: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bldg_chtnm: None | str | Unset
        if isinstance(self.bldg_chtnm, Unset):
            bldg_chtnm = UNSET
        else:
            bldg_chtnm = self.bldg_chtnm

        bldg_engnm: None | str | Unset
        if isinstance(self.bldg_engnm, Unset):
            bldg_engnm = UNSET
        else:
            bldg_engnm = self.bldg_engnm

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        telephone: None | str | Unset
        if isinstance(self.telephone, Unset):
            telephone = UNSET
        else:
            telephone = self.telephone

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bldg_chtnm is not UNSET:
            field_dict["BLDG_CHTNM"] = bldg_chtnm
        if bldg_engnm is not UNSET:
            field_dict["BLDG_ENGNM"] = bldg_engnm
        if email is not UNSET:
            field_dict["Email"] = email
        if telephone is not UNSET:
            field_dict["Telephone"] = telephone
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_bldg_chtnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bldg_chtnm = _parse_bldg_chtnm(d.pop("BLDG_CHTNM", UNSET))

        def _parse_bldg_engnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bldg_engnm = _parse_bldg_engnm(d.pop("BLDG_ENGNM", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("Email", UNSET))

        def _parse_telephone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone = _parse_telephone(d.pop("Telephone", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            bldg_chtnm=bldg_chtnm,
            bldg_engnm=bldg_engnm,
            email=email,
            telephone=telephone,
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
