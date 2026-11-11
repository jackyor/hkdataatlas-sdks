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
        objnam (None | str | Unset): Publisher field type: esriFieldTypeString
        inform (None | str | Unset): Publisher field type: esriFieldTypeString
        traffic (None | str | Unset): Publisher field type: esriFieldTypeString
        vhfchannel (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    objnam: None | str | Unset = UNSET
    inform: None | str | Unset = UNSET
    traffic: None | str | Unset = UNSET
    vhfchannel: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objnam: None | str | Unset
        if isinstance(self.objnam, Unset):
            objnam = UNSET
        else:
            objnam = self.objnam

        inform: None | str | Unset
        if isinstance(self.inform, Unset):
            inform = UNSET
        else:
            inform = self.inform

        traffic: None | str | Unset
        if isinstance(self.traffic, Unset):
            traffic = UNSET
        else:
            traffic = self.traffic

        vhfchannel: None | str | Unset
        if isinstance(self.vhfchannel, Unset):
            vhfchannel = UNSET
        else:
            vhfchannel = self.vhfchannel

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objnam is not UNSET:
            field_dict["OBJNAM"] = objnam
        if inform is not UNSET:
            field_dict["INFORM"] = inform
        if traffic is not UNSET:
            field_dict["TRAFFIC"] = traffic
        if vhfchannel is not UNSET:
            field_dict["VHFCHANNEL"] = vhfchannel
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_objnam(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        objnam = _parse_objnam(d.pop("OBJNAM", UNSET))

        def _parse_inform(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inform = _parse_inform(d.pop("INFORM", UNSET))

        def _parse_traffic(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        traffic = _parse_traffic(d.pop("TRAFFIC", UNSET))

        def _parse_vhfchannel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vhfchannel = _parse_vhfchannel(d.pop("VHFCHANNEL", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objnam=objnam,
            inform=inform,
            traffic=traffic,
            vhfchannel=vhfchannel,
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
