from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer6Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer6Attributes:
    """
    Attributes:
        class_ (None | str | Unset): Publisher field type: esriFieldTypeString
        lastupdatedate (float | None | Unset): Publisher field type: esriFieldTypeDouble
        physicalstatus (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        subcat (None | str | Unset): Publisher field type: esriFieldTypeString
        type_ (None | str | Unset): Publisher field type: esriFieldTypeString
        annosymid (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    class_: None | str | Unset = UNSET
    lastupdatedate: float | None | Unset = UNSET
    physicalstatus: int | None | Unset = UNSET
    subcat: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    annosymid: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        class_: None | str | Unset
        if isinstance(self.class_, Unset):
            class_ = UNSET
        else:
            class_ = self.class_

        lastupdatedate: float | None | Unset
        if isinstance(self.lastupdatedate, Unset):
            lastupdatedate = UNSET
        else:
            lastupdatedate = self.lastupdatedate

        physicalstatus: int | None | Unset
        if isinstance(self.physicalstatus, Unset):
            physicalstatus = UNSET
        else:
            physicalstatus = self.physicalstatus

        subcat: None | str | Unset
        if isinstance(self.subcat, Unset):
            subcat = UNSET
        else:
            subcat = self.subcat

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        annosymid: float | None | Unset
        if isinstance(self.annosymid, Unset):
            annosymid = UNSET
        else:
            annosymid = self.annosymid

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if class_ is not UNSET:
            field_dict["CLASS"] = class_
        if lastupdatedate is not UNSET:
            field_dict["LASTUPDATEDATE"] = lastupdatedate
        if physicalstatus is not UNSET:
            field_dict["PHYSICALSTATUS"] = physicalstatus
        if subcat is not UNSET:
            field_dict["SUBCAT"] = subcat
        if type_ is not UNSET:
            field_dict["TYPE"] = type_
        if annosymid is not UNSET:
            field_dict["ANNOSYMID"] = annosymid
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_class_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_ = _parse_class_(d.pop("CLASS", UNSET))

        def _parse_lastupdatedate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lastupdatedate = _parse_lastupdatedate(d.pop("LASTUPDATEDATE", UNSET))

        def _parse_physicalstatus(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        physicalstatus = _parse_physicalstatus(d.pop("PHYSICALSTATUS", UNSET))

        def _parse_subcat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subcat = _parse_subcat(d.pop("SUBCAT", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("TYPE", UNSET))

        def _parse_annosymid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        annosymid = _parse_annosymid(d.pop("ANNOSYMID", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_6_attributes = cls(
            class_=class_,
            lastupdatedate=lastupdatedate,
            physicalstatus=physicalstatus,
            subcat=subcat,
            type_=type_,
            annosymid=annosymid,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_6_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_6_attributes

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
