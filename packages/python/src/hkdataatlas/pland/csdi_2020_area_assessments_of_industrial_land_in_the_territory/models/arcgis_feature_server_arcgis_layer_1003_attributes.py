from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1003Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1003Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        aa_code (None | str | Unset): Publisher field type: esriFieldTypeString
        aa_title (None | str | Unset): Publisher field type: esriFieldTypeString
        general_storage (float | None | Unset): Publisher field type: esriFieldTypeDouble
        logistic_warehouse (float | None | Unset): Publisher field type: esriFieldTypeDouble
        storage_miscellaneous (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    aa_code: None | str | Unset = UNSET
    aa_title: None | str | Unset = UNSET
    general_storage: float | None | Unset = UNSET
    logistic_warehouse: float | None | Unset = UNSET
    storage_miscellaneous: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        aa_code: None | str | Unset
        if isinstance(self.aa_code, Unset):
            aa_code = UNSET
        else:
            aa_code = self.aa_code

        aa_title: None | str | Unset
        if isinstance(self.aa_title, Unset):
            aa_title = UNSET
        else:
            aa_title = self.aa_title

        general_storage: float | None | Unset
        if isinstance(self.general_storage, Unset):
            general_storage = UNSET
        else:
            general_storage = self.general_storage

        logistic_warehouse: float | None | Unset
        if isinstance(self.logistic_warehouse, Unset):
            logistic_warehouse = UNSET
        else:
            logistic_warehouse = self.logistic_warehouse

        storage_miscellaneous: float | None | Unset
        if isinstance(self.storage_miscellaneous, Unset):
            storage_miscellaneous = UNSET
        else:
            storage_miscellaneous = self.storage_miscellaneous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if aa_code is not UNSET:
            field_dict["AA_Code"] = aa_code
        if aa_title is not UNSET:
            field_dict["AA_Title"] = aa_title
        if general_storage is not UNSET:
            field_dict["General_storage"] = general_storage
        if logistic_warehouse is not UNSET:
            field_dict["Logistic_warehouse"] = logistic_warehouse
        if storage_miscellaneous is not UNSET:
            field_dict["Storage_miscellaneous"] = storage_miscellaneous

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_aa_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aa_code = _parse_aa_code(d.pop("AA_Code", UNSET))

        def _parse_aa_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aa_title = _parse_aa_title(d.pop("AA_Title", UNSET))

        def _parse_general_storage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        general_storage = _parse_general_storage(d.pop("General_storage", UNSET))

        def _parse_logistic_warehouse(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        logistic_warehouse = _parse_logistic_warehouse(
            d.pop("Logistic_warehouse", UNSET)
        )

        def _parse_storage_miscellaneous(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        storage_miscellaneous = _parse_storage_miscellaneous(
            d.pop("Storage_miscellaneous", UNSET)
        )

        arcgis_feature_server_arcgis_layer_1003_attributes = cls(
            objectid=objectid,
            aa_code=aa_code,
            aa_title=aa_title,
            general_storage=general_storage,
            logistic_warehouse=logistic_warehouse,
            storage_miscellaneous=storage_miscellaneous,
        )

        arcgis_feature_server_arcgis_layer_1003_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1003_attributes

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
