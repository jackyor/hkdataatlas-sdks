from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer2Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer2Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        serv_cluster_en (None | str | Unset): Publisher field type: esriFieldTypeString
        serv_cluster_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        serv_cluster_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        add_en (None | str | Unset): Publisher field type: esriFieldTypeString
        add_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        add_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        tel (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    name_sc: None | str | Unset = UNSET
    serv_cluster_en: None | str | Unset = UNSET
    serv_cluster_tc: None | str | Unset = UNSET
    serv_cluster_sc: None | str | Unset = UNSET
    add_en: None | str | Unset = UNSET
    add_tc: None | str | Unset = UNSET
    add_sc: None | str | Unset = UNSET
    tel: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        name_sc: None | str | Unset
        if isinstance(self.name_sc, Unset):
            name_sc = UNSET
        else:
            name_sc = self.name_sc

        serv_cluster_en: None | str | Unset
        if isinstance(self.serv_cluster_en, Unset):
            serv_cluster_en = UNSET
        else:
            serv_cluster_en = self.serv_cluster_en

        serv_cluster_tc: None | str | Unset
        if isinstance(self.serv_cluster_tc, Unset):
            serv_cluster_tc = UNSET
        else:
            serv_cluster_tc = self.serv_cluster_tc

        serv_cluster_sc: None | str | Unset
        if isinstance(self.serv_cluster_sc, Unset):
            serv_cluster_sc = UNSET
        else:
            serv_cluster_sc = self.serv_cluster_sc

        add_en: None | str | Unset
        if isinstance(self.add_en, Unset):
            add_en = UNSET
        else:
            add_en = self.add_en

        add_tc: None | str | Unset
        if isinstance(self.add_tc, Unset):
            add_tc = UNSET
        else:
            add_tc = self.add_tc

        add_sc: None | str | Unset
        if isinstance(self.add_sc, Unset):
            add_sc = UNSET
        else:
            add_sc = self.add_sc

        tel: None | str | Unset
        if isinstance(self.tel, Unset):
            tel = UNSET
        else:
            tel = self.tel

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if name_en is not UNSET:
            field_dict["name_en"] = name_en
        if name_tc is not UNSET:
            field_dict["name_tc"] = name_tc
        if name_sc is not UNSET:
            field_dict["name_sc"] = name_sc
        if serv_cluster_en is not UNSET:
            field_dict["servCluster_en"] = serv_cluster_en
        if serv_cluster_tc is not UNSET:
            field_dict["servCluster_tc"] = serv_cluster_tc
        if serv_cluster_sc is not UNSET:
            field_dict["servCluster_sc"] = serv_cluster_sc
        if add_en is not UNSET:
            field_dict["add_en"] = add_en
        if add_tc is not UNSET:
            field_dict["add_tc"] = add_tc
        if add_sc is not UNSET:
            field_dict["add_sc"] = add_sc
        if tel is not UNSET:
            field_dict["tel"] = tel

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("name_en", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("name_tc", UNSET))

        def _parse_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_sc = _parse_name_sc(d.pop("name_sc", UNSET))

        def _parse_serv_cluster_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        serv_cluster_en = _parse_serv_cluster_en(d.pop("servCluster_en", UNSET))

        def _parse_serv_cluster_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        serv_cluster_tc = _parse_serv_cluster_tc(d.pop("servCluster_tc", UNSET))

        def _parse_serv_cluster_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        serv_cluster_sc = _parse_serv_cluster_sc(d.pop("servCluster_sc", UNSET))

        def _parse_add_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        add_en = _parse_add_en(d.pop("add_en", UNSET))

        def _parse_add_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        add_tc = _parse_add_tc(d.pop("add_tc", UNSET))

        def _parse_add_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        add_sc = _parse_add_sc(d.pop("add_sc", UNSET))

        def _parse_tel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tel = _parse_tel(d.pop("tel", UNSET))

        arcgis_feature_server_arcgis_layer_2_attributes = cls(
            objectid=objectid,
            name_en=name_en,
            name_tc=name_tc,
            name_sc=name_sc,
            serv_cluster_en=serv_cluster_en,
            serv_cluster_tc=serv_cluster_tc,
            serv_cluster_sc=serv_cluster_sc,
            add_en=add_en,
            add_tc=add_tc,
            add_sc=add_sc,
            tel=tel,
        )

        arcgis_feature_server_arcgis_layer_2_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_2_attributes

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
