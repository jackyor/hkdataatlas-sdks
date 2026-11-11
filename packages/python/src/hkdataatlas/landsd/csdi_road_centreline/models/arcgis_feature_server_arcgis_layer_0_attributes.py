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
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        streetcentrelineid (int | Unset): Publisher field type: esriFieldTypeInteger
        streetcode (int | Unset): Publisher field type: esriFieldTypeInteger
        streettype (str | Unset): Publisher field type: esriFieldTypeString
        englishstreetname (None | str | Unset): Publisher field type: esriFieldTypeString
        chinesestreetname (None | str | Unset): Publisher field type: esriFieldTypeString
        lastupdatedate (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    streetcentrelineid: int | Unset = UNSET
    streetcode: int | Unset = UNSET
    streettype: str | Unset = UNSET
    englishstreetname: None | str | Unset = UNSET
    chinesestreetname: None | str | Unset = UNSET
    lastupdatedate: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        streetcentrelineid = self.streetcentrelineid

        streetcode = self.streetcode

        streettype = self.streettype

        englishstreetname: None | str | Unset
        if isinstance(self.englishstreetname, Unset):
            englishstreetname = UNSET
        else:
            englishstreetname = self.englishstreetname

        chinesestreetname: None | str | Unset
        if isinstance(self.chinesestreetname, Unset):
            chinesestreetname = UNSET
        else:
            chinesestreetname = self.chinesestreetname

        lastupdatedate = self.lastupdatedate

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if streetcentrelineid is not UNSET:
            field_dict["STREETCENTRELINEID"] = streetcentrelineid
        if streetcode is not UNSET:
            field_dict["STREETCODE"] = streetcode
        if streettype is not UNSET:
            field_dict["STREETTYPE"] = streettype
        if englishstreetname is not UNSET:
            field_dict["ENGLISHSTREETNAME"] = englishstreetname
        if chinesestreetname is not UNSET:
            field_dict["CHINESESTREETNAME"] = chinesestreetname
        if lastupdatedate is not UNSET:
            field_dict["LASTUPDATEDATE"] = lastupdatedate
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        streetcentrelineid = d.pop("STREETCENTRELINEID", UNSET)

        streetcode = d.pop("STREETCODE", UNSET)

        streettype = d.pop("STREETTYPE", UNSET)

        def _parse_englishstreetname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        englishstreetname = _parse_englishstreetname(d.pop("ENGLISHSTREETNAME", UNSET))

        def _parse_chinesestreetname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinesestreetname = _parse_chinesestreetname(d.pop("CHINESESTREETNAME", UNSET))

        lastupdatedate = d.pop("LASTUPDATEDATE", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            streetcentrelineid=streetcentrelineid,
            streetcode=streetcode,
            streettype=streettype,
            englishstreetname=englishstreetname,
            chinesestreetname=chinesestreetname,
            lastupdatedate=lastupdatedate,
            shape_length=shape_length,
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
