from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer11Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer11Attributes:
    """
    Attributes:
        annosymid (float | None | Unset): Publisher field type: esriFieldTypeDouble
        class_ (None | str | Unset): Publisher field type: esriFieldTypeString
        height (int | None | Unset): Publisher field type: esriFieldTypeInteger
        lastupdatedate (float | None | Unset): Publisher field type: esriFieldTypeDouble
        physicalstatus (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        subcat (None | str | Unset): Publisher field type: esriFieldTypeString
        trigname (float | None | Unset): Publisher field type: esriFieldTypeSingle
        type_ (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    annosymid: float | None | Unset = UNSET
    class_: None | str | Unset = UNSET
    height: int | None | Unset = UNSET
    lastupdatedate: float | None | Unset = UNSET
    physicalstatus: int | None | Unset = UNSET
    subcat: None | str | Unset = UNSET
    trigname: float | None | Unset = UNSET
    type_: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annosymid: float | None | Unset
        if isinstance(self.annosymid, Unset):
            annosymid = UNSET
        else:
            annosymid = self.annosymid

        class_: None | str | Unset
        if isinstance(self.class_, Unset):
            class_ = UNSET
        else:
            class_ = self.class_

        height: int | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

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

        trigname: float | None | Unset
        if isinstance(self.trigname, Unset):
            trigname = UNSET
        else:
            trigname = self.trigname

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annosymid is not UNSET:
            field_dict["ANNOSYMID"] = annosymid
        if class_ is not UNSET:
            field_dict["CLASS"] = class_
        if height is not UNSET:
            field_dict["HEIGHT"] = height
        if lastupdatedate is not UNSET:
            field_dict["LASTUPDATEDATE"] = lastupdatedate
        if physicalstatus is not UNSET:
            field_dict["PHYSICALSTATUS"] = physicalstatus
        if subcat is not UNSET:
            field_dict["SUBCAT"] = subcat
        if trigname is not UNSET:
            field_dict["TRIGNAME"] = trigname
        if type_ is not UNSET:
            field_dict["TYPE"] = type_
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_annosymid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        annosymid = _parse_annosymid(d.pop("ANNOSYMID", UNSET))

        def _parse_class_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_ = _parse_class_(d.pop("CLASS", UNSET))

        def _parse_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        height = _parse_height(d.pop("HEIGHT", UNSET))

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

        def _parse_trigname(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        trigname = _parse_trigname(d.pop("TRIGNAME", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("TYPE", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_11_attributes = cls(
            annosymid=annosymid,
            class_=class_,
            height=height,
            lastupdatedate=lastupdatedate,
            physicalstatus=physicalstatus,
            subcat=subcat,
            trigname=trigname,
            type_=type_,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_11_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_11_attributes

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
