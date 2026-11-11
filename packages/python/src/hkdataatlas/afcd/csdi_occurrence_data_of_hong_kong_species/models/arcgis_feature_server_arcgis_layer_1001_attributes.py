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
        scientific (None | str | Unset): Publisher field type: esriFieldTypeString
        family (None | str | Unset): Publisher field type: esriFieldTypeString
        record_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        gno (int | None | Unset): Publisher field type: esriFieldTypeInteger
    """

    objectid: int | Unset = UNSET
    scientific: None | str | Unset = UNSET
    family: None | str | Unset = UNSET
    record_date: Any | Unset = UNSET
    gno: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        scientific: None | str | Unset
        if isinstance(self.scientific, Unset):
            scientific = UNSET
        else:
            scientific = self.scientific

        family: None | str | Unset
        if isinstance(self.family, Unset):
            family = UNSET
        else:
            family = self.family

        record_date = self.record_date

        gno: int | None | Unset
        if isinstance(self.gno, Unset):
            gno = UNSET
        else:
            gno = self.gno

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if scientific is not UNSET:
            field_dict["scientific"] = scientific
        if family is not UNSET:
            field_dict["family"] = family
        if record_date is not UNSET:
            field_dict["record_date"] = record_date
        if gno is not UNSET:
            field_dict["gno"] = gno

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_scientific(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scientific = _parse_scientific(d.pop("scientific", UNSET))

        def _parse_family(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        family = _parse_family(d.pop("family", UNSET))

        record_date = d.pop("record_date", UNSET)

        def _parse_gno(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        gno = _parse_gno(d.pop("gno", UNSET))

        arcgis_feature_server_arcgis_layer_1001_attributes = cls(
            objectid=objectid,
            scientific=scientific,
            family=family,
            record_date=record_date,
            gno=gno,
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
