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
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        dataset_en (None | str | Unset): Publisher field type: esriFieldTypeString
        dataset_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        dataset_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        spot (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    address_en: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    dataset_en: None | str | Unset = UNSET
    dataset_sc: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_sc: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    spot: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_sc: None | str | Unset
        if isinstance(self.address_sc, Unset):
            address_sc = UNSET
        else:
            address_sc = self.address_sc

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        dataset_en: None | str | Unset
        if isinstance(self.dataset_en, Unset):
            dataset_en = UNSET
        else:
            dataset_en = self.dataset_en

        dataset_sc: None | str | Unset
        if isinstance(self.dataset_sc, Unset):
            dataset_sc = UNSET
        else:
            dataset_sc = self.dataset_sc

        dataset_tc: None | str | Unset
        if isinstance(self.dataset_tc, Unset):
            dataset_tc = UNSET
        else:
            dataset_tc = self.dataset_tc

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        name_sc: None | str | Unset
        if isinstance(self.name_sc, Unset):
            name_sc = UNSET
        else:
            name_sc = self.name_sc

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        spot: float | None | Unset
        if isinstance(self.spot, Unset):
            spot = UNSET
        else:
            spot = self.spot

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_en is not UNSET:
            field_dict["Address_EN"] = address_en
        if address_sc is not UNSET:
            field_dict["Address_SC"] = address_sc
        if address_tc is not UNSET:
            field_dict["Address_TC"] = address_tc
        if dataset_en is not UNSET:
            field_dict["DATASET_EN"] = dataset_en
        if dataset_sc is not UNSET:
            field_dict["DATASET_SC"] = dataset_sc
        if dataset_tc is not UNSET:
            field_dict["DATASET_TC"] = dataset_tc
        if name_en is not UNSET:
            field_dict["Name_EN"] = name_en
        if name_sc is not UNSET:
            field_dict["Name_SC"] = name_sc
        if name_tc is not UNSET:
            field_dict["Name_TC"] = name_tc
        if spot is not UNSET:
            field_dict["SPOT"] = spot
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("Address_EN", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("Address_SC", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("Address_TC", UNSET))

        def _parse_dataset_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_en = _parse_dataset_en(d.pop("DATASET_EN", UNSET))

        def _parse_dataset_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_sc = _parse_dataset_sc(d.pop("DATASET_SC", UNSET))

        def _parse_dataset_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_tc = _parse_dataset_tc(d.pop("DATASET_TC", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("Name_EN", UNSET))

        def _parse_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_sc = _parse_name_sc(d.pop("Name_SC", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("Name_TC", UNSET))

        def _parse_spot(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        spot = _parse_spot(d.pop("SPOT", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            address_en=address_en,
            address_sc=address_sc,
            address_tc=address_tc,
            dataset_en=dataset_en,
            dataset_sc=dataset_sc,
            dataset_tc=dataset_tc,
            name_en=name_en,
            name_sc=name_sc,
            name_tc=name_tc,
            spot=spot,
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
