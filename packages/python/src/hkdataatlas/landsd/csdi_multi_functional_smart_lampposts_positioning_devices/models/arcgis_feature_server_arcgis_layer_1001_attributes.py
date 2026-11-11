from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1001Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1001Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        lp_num (None | str | Unset): Publisher field type: esriFieldTypeString
        rfid_tid (None | str | Unset): Publisher field type: esriFieldTypeString
        rfid_epc (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    lp_num: None | str | Unset = UNSET
    rfid_tid: None | str | Unset = UNSET
    rfid_epc: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        lp_num: None | str | Unset
        if isinstance(self.lp_num, Unset):
            lp_num = UNSET
        else:
            lp_num = self.lp_num

        rfid_tid: None | str | Unset
        if isinstance(self.rfid_tid, Unset):
            rfid_tid = UNSET
        else:
            rfid_tid = self.rfid_tid

        rfid_epc: None | str | Unset
        if isinstance(self.rfid_epc, Unset):
            rfid_epc = UNSET
        else:
            rfid_epc = self.rfid_epc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if lp_num is not UNSET:
            field_dict["LP_NUM"] = lp_num
        if rfid_tid is not UNSET:
            field_dict["RFID_TID"] = rfid_tid
        if rfid_epc is not UNSET:
            field_dict["RFID_EPC"] = rfid_epc

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

        def _parse_rfid_tid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rfid_tid = _parse_rfid_tid(d.pop("RFID_TID", UNSET))

        def _parse_rfid_epc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rfid_epc = _parse_rfid_epc(d.pop("RFID_EPC", UNSET))

        arcgis_feature_server_arcgis_layer_1001_attributes = cls(
            objectid=objectid,
            lp_num=lp_num,
            rfid_tid=rfid_tid,
            rfid_epc=rfid_epc,
        )

        arcgis_feature_server_arcgis_layer_1001_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1001_attributes

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
