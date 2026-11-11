from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1002Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1002Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        lp_num (None | str | Unset): Publisher field type: esriFieldTypeString
        nfc_url (None | str | Unset): Publisher field type: esriFieldTypeString
        nfc_geouri (None | str | Unset): Publisher field type: esriFieldTypeString
        nfc_lp (None | str | Unset): Publisher field type: esriFieldTypeString
        nfc_hk80 (None | str | Unset): Publisher field type: esriFieldTypeString
        nfc_uid (None | str | Unset): Publisher field type: esriFieldTypeString
        nfc_loc (None | str | Unset): Publisher field type: esriFieldTypeString
        nfc_time (None | str | Unset): Publisher field type: esriFieldTypeString
        nfc_ver (None | str | Unset): Publisher field type: esriFieldTypeString
        nfc_sha256 (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    lp_num: None | str | Unset = UNSET
    nfc_url: None | str | Unset = UNSET
    nfc_geouri: None | str | Unset = UNSET
    nfc_lp: None | str | Unset = UNSET
    nfc_hk80: None | str | Unset = UNSET
    nfc_uid: None | str | Unset = UNSET
    nfc_loc: None | str | Unset = UNSET
    nfc_time: None | str | Unset = UNSET
    nfc_ver: None | str | Unset = UNSET
    nfc_sha256: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        lp_num: None | str | Unset
        if isinstance(self.lp_num, Unset):
            lp_num = UNSET
        else:
            lp_num = self.lp_num

        nfc_url: None | str | Unset
        if isinstance(self.nfc_url, Unset):
            nfc_url = UNSET
        else:
            nfc_url = self.nfc_url

        nfc_geouri: None | str | Unset
        if isinstance(self.nfc_geouri, Unset):
            nfc_geouri = UNSET
        else:
            nfc_geouri = self.nfc_geouri

        nfc_lp: None | str | Unset
        if isinstance(self.nfc_lp, Unset):
            nfc_lp = UNSET
        else:
            nfc_lp = self.nfc_lp

        nfc_hk80: None | str | Unset
        if isinstance(self.nfc_hk80, Unset):
            nfc_hk80 = UNSET
        else:
            nfc_hk80 = self.nfc_hk80

        nfc_uid: None | str | Unset
        if isinstance(self.nfc_uid, Unset):
            nfc_uid = UNSET
        else:
            nfc_uid = self.nfc_uid

        nfc_loc: None | str | Unset
        if isinstance(self.nfc_loc, Unset):
            nfc_loc = UNSET
        else:
            nfc_loc = self.nfc_loc

        nfc_time: None | str | Unset
        if isinstance(self.nfc_time, Unset):
            nfc_time = UNSET
        else:
            nfc_time = self.nfc_time

        nfc_ver: None | str | Unset
        if isinstance(self.nfc_ver, Unset):
            nfc_ver = UNSET
        else:
            nfc_ver = self.nfc_ver

        nfc_sha256: None | str | Unset
        if isinstance(self.nfc_sha256, Unset):
            nfc_sha256 = UNSET
        else:
            nfc_sha256 = self.nfc_sha256

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if lp_num is not UNSET:
            field_dict["LP_NUM"] = lp_num
        if nfc_url is not UNSET:
            field_dict["NFC_URL"] = nfc_url
        if nfc_geouri is not UNSET:
            field_dict["NFC_GEOURI"] = nfc_geouri
        if nfc_lp is not UNSET:
            field_dict["NFC_LP"] = nfc_lp
        if nfc_hk80 is not UNSET:
            field_dict["NFC_HK80"] = nfc_hk80
        if nfc_uid is not UNSET:
            field_dict["NFC_UID"] = nfc_uid
        if nfc_loc is not UNSET:
            field_dict["NFC_LOC"] = nfc_loc
        if nfc_time is not UNSET:
            field_dict["NFC_TIME"] = nfc_time
        if nfc_ver is not UNSET:
            field_dict["NFC_VER"] = nfc_ver
        if nfc_sha256 is not UNSET:
            field_dict["NFC_SHA256"] = nfc_sha256

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_lp_num(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lp_num = _parse_lp_num(d.pop("LP_NUM", UNSET))

        def _parse_nfc_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nfc_url = _parse_nfc_url(d.pop("NFC_URL", UNSET))

        def _parse_nfc_geouri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nfc_geouri = _parse_nfc_geouri(d.pop("NFC_GEOURI", UNSET))

        def _parse_nfc_lp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nfc_lp = _parse_nfc_lp(d.pop("NFC_LP", UNSET))

        def _parse_nfc_hk80(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nfc_hk80 = _parse_nfc_hk80(d.pop("NFC_HK80", UNSET))

        def _parse_nfc_uid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nfc_uid = _parse_nfc_uid(d.pop("NFC_UID", UNSET))

        def _parse_nfc_loc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nfc_loc = _parse_nfc_loc(d.pop("NFC_LOC", UNSET))

        def _parse_nfc_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nfc_time = _parse_nfc_time(d.pop("NFC_TIME", UNSET))

        def _parse_nfc_ver(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nfc_ver = _parse_nfc_ver(d.pop("NFC_VER", UNSET))

        def _parse_nfc_sha256(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nfc_sha256 = _parse_nfc_sha256(d.pop("NFC_SHA256", UNSET))

        arcgis_feature_server_arcgis_layer_1002_attributes = cls(
            objectid=objectid,
            lp_num=lp_num,
            nfc_url=nfc_url,
            nfc_geouri=nfc_geouri,
            nfc_lp=nfc_lp,
            nfc_hk80=nfc_hk80,
            nfc_uid=nfc_uid,
            nfc_loc=nfc_loc,
            nfc_time=nfc_time,
            nfc_ver=nfc_ver,
            nfc_sha256=nfc_sha256,
        )

        arcgis_feature_server_arcgis_layer_1002_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1002_attributes

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
