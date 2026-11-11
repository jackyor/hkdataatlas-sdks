from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1000Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1000Attributes:
    """
    Attributes:
        geonameid (float | None | Unset): Publisher field type: esriFieldTypeDouble
        annosymid (float | None | Unset): Publisher field type: esriFieldTypeDouble
        graphicdataset (None | str | Unset): Publisher field type: esriFieldTypeString
        graphicid (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    geonameid: float | None | Unset = UNSET
    annosymid: float | None | Unset = UNSET
    graphicdataset: None | str | Unset = UNSET
    graphicid: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        geonameid: float | None | Unset
        if isinstance(self.geonameid, Unset):
            geonameid = UNSET
        else:
            geonameid = self.geonameid

        annosymid: float | None | Unset
        if isinstance(self.annosymid, Unset):
            annosymid = UNSET
        else:
            annosymid = self.annosymid

        graphicdataset: None | str | Unset
        if isinstance(self.graphicdataset, Unset):
            graphicdataset = UNSET
        else:
            graphicdataset = self.graphicdataset

        graphicid: None | str | Unset
        if isinstance(self.graphicid, Unset):
            graphicid = UNSET
        else:
            graphicid = self.graphicid

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if geonameid is not UNSET:
            field_dict["GEONAMEID"] = geonameid
        if annosymid is not UNSET:
            field_dict["ANNOSYMID"] = annosymid
        if graphicdataset is not UNSET:
            field_dict["GRAPHICDATASET"] = graphicdataset
        if graphicid is not UNSET:
            field_dict["GRAPHICID"] = graphicid
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_geonameid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        geonameid = _parse_geonameid(d.pop("GEONAMEID", UNSET))

        def _parse_annosymid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        annosymid = _parse_annosymid(d.pop("ANNOSYMID", UNSET))

        def _parse_graphicdataset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        graphicdataset = _parse_graphicdataset(d.pop("GRAPHICDATASET", UNSET))

        def _parse_graphicid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        graphicid = _parse_graphicid(d.pop("GRAPHICID", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_1000_attributes = cls(
            geonameid=geonameid,
            annosymid=annosymid,
            graphicdataset=graphicdataset,
            graphicid=graphicid,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_1000_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1000_attributes

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
