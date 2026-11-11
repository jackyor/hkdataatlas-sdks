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
        featureid (int | Unset): Publisher field type: esriFieldTypeInteger
        atc_station_no (int | None | Unset): Publisher field type: esriFieldTypeInteger
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    featureid: int | Unset = UNSET
    atc_station_no: int | None | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        featureid = self.featureid

        atc_station_no: int | None | Unset
        if isinstance(self.atc_station_no, Unset):
            atc_station_no = UNSET
        else:
            atc_station_no = self.atc_station_no

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if featureid is not UNSET:
            field_dict["FEATUREID"] = featureid
        if atc_station_no is not UNSET:
            field_dict["ATC_STATION_NO"] = atc_station_no
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        featureid = d.pop("FEATUREID", UNSET)

        def _parse_atc_station_no(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        atc_station_no = _parse_atc_station_no(d.pop("ATC_STATION_NO", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            featureid=featureid,
            atc_station_no=atc_station_no,
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
