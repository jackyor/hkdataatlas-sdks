from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer13Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer13Attributes:
    """
    Attributes:
        featureid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        cre_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        last_upd_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    featureid: int | None | Unset = UNSET
    cre_date: Any | Unset = UNSET
    last_upd_date: Any | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        featureid: int | None | Unset
        if isinstance(self.featureid, Unset):
            featureid = UNSET
        else:
            featureid = self.featureid

        cre_date = self.cre_date

        last_upd_date = self.last_upd_date

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if featureid is not UNSET:
            field_dict["FEATUREID"] = featureid
        if cre_date is not UNSET:
            field_dict["CRE_DATE"] = cre_date
        if last_upd_date is not UNSET:
            field_dict["LAST_UPD_DATE"] = last_upd_date
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_featureid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        featureid = _parse_featureid(d.pop("FEATUREID", UNSET))

        cre_date = d.pop("CRE_DATE", UNSET)

        last_upd_date = d.pop("LAST_UPD_DATE", UNSET)

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_13_attributes = cls(
            featureid=featureid,
            cre_date=cre_date,
            last_upd_date=last_upd_date,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_13_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_13_attributes

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
