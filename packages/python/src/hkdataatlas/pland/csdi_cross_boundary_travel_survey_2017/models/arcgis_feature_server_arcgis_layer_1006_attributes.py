from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1006Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1006Attributes:
    """
    Attributes:
        objectid_1 (int | Unset): Publisher field type: esriFieldTypeOID
        objectid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        cp_en (None | str | Unset): Publisher field type: esriFieldTypeString
        y1999 (None | str | Unset): Publisher field type: esriFieldTypeString
        y2001 (None | str | Unset): Publisher field type: esriFieldTypeString
        y2003 (None | str | Unset): Publisher field type: esriFieldTypeString
        y2006 (None | str | Unset): Publisher field type: esriFieldTypeString
        y2007 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2009 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2011 (None | str | Unset): Publisher field type: esriFieldTypeString
        y2013_14 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2015 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2017 (int | None | Unset): Publisher field type: esriFieldTypeInteger
    """

    objectid_1: int | Unset = UNSET
    objectid: int | None | Unset = UNSET
    cp_en: None | str | Unset = UNSET
    y1999: None | str | Unset = UNSET
    y2001: None | str | Unset = UNSET
    y2003: None | str | Unset = UNSET
    y2006: None | str | Unset = UNSET
    y2007: int | None | Unset = UNSET
    y2009: int | None | Unset = UNSET
    y2011: None | str | Unset = UNSET
    y2013_14: int | None | Unset = UNSET
    y2015: int | None | Unset = UNSET
    y2017: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid_1 = self.objectid_1

        objectid: int | None | Unset
        if isinstance(self.objectid, Unset):
            objectid = UNSET
        else:
            objectid = self.objectid

        cp_en: None | str | Unset
        if isinstance(self.cp_en, Unset):
            cp_en = UNSET
        else:
            cp_en = self.cp_en

        y1999: None | str | Unset
        if isinstance(self.y1999, Unset):
            y1999 = UNSET
        else:
            y1999 = self.y1999

        y2001: None | str | Unset
        if isinstance(self.y2001, Unset):
            y2001 = UNSET
        else:
            y2001 = self.y2001

        y2003: None | str | Unset
        if isinstance(self.y2003, Unset):
            y2003 = UNSET
        else:
            y2003 = self.y2003

        y2006: None | str | Unset
        if isinstance(self.y2006, Unset):
            y2006 = UNSET
        else:
            y2006 = self.y2006

        y2007: int | None | Unset
        if isinstance(self.y2007, Unset):
            y2007 = UNSET
        else:
            y2007 = self.y2007

        y2009: int | None | Unset
        if isinstance(self.y2009, Unset):
            y2009 = UNSET
        else:
            y2009 = self.y2009

        y2011: None | str | Unset
        if isinstance(self.y2011, Unset):
            y2011 = UNSET
        else:
            y2011 = self.y2011

        y2013_14: int | None | Unset
        if isinstance(self.y2013_14, Unset):
            y2013_14 = UNSET
        else:
            y2013_14 = self.y2013_14

        y2015: int | None | Unset
        if isinstance(self.y2015, Unset):
            y2015 = UNSET
        else:
            y2015 = self.y2015

        y2017: int | None | Unset
        if isinstance(self.y2017, Unset):
            y2017 = UNSET
        else:
            y2017 = self.y2017

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid_1 is not UNSET:
            field_dict["OBJECTID_1"] = objectid_1
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if cp_en is not UNSET:
            field_dict["CP_En"] = cp_en
        if y1999 is not UNSET:
            field_dict["Y1999"] = y1999
        if y2001 is not UNSET:
            field_dict["Y2001"] = y2001
        if y2003 is not UNSET:
            field_dict["Y2003"] = y2003
        if y2006 is not UNSET:
            field_dict["Y2006"] = y2006
        if y2007 is not UNSET:
            field_dict["Y2007"] = y2007
        if y2009 is not UNSET:
            field_dict["Y2009"] = y2009
        if y2011 is not UNSET:
            field_dict["Y2011"] = y2011
        if y2013_14 is not UNSET:
            field_dict["Y2013_14"] = y2013_14
        if y2015 is not UNSET:
            field_dict["Y2015"] = y2015
        if y2017 is not UNSET:
            field_dict["Y2017"] = y2017

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid_1 = d.pop("OBJECTID_1", UNSET)

        def _parse_objectid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        objectid = _parse_objectid(d.pop("OBJECTID", UNSET))

        def _parse_cp_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cp_en = _parse_cp_en(d.pop("CP_En", UNSET))

        def _parse_y1999(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y1999 = _parse_y1999(d.pop("Y1999", UNSET))

        def _parse_y2001(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2001 = _parse_y2001(d.pop("Y2001", UNSET))

        def _parse_y2003(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2003 = _parse_y2003(d.pop("Y2003", UNSET))

        def _parse_y2006(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2006 = _parse_y2006(d.pop("Y2006", UNSET))

        def _parse_y2007(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2007 = _parse_y2007(d.pop("Y2007", UNSET))

        def _parse_y2009(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2009 = _parse_y2009(d.pop("Y2009", UNSET))

        def _parse_y2011(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2011 = _parse_y2011(d.pop("Y2011", UNSET))

        def _parse_y2013_14(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2013_14 = _parse_y2013_14(d.pop("Y2013_14", UNSET))

        def _parse_y2015(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2015 = _parse_y2015(d.pop("Y2015", UNSET))

        def _parse_y2017(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2017 = _parse_y2017(d.pop("Y2017", UNSET))

        arcgis_feature_server_arcgis_layer_1006_attributes = cls(
            objectid_1=objectid_1,
            objectid=objectid,
            cp_en=cp_en,
            y1999=y1999,
            y2001=y2001,
            y2003=y2003,
            y2006=y2006,
            y2007=y2007,
            y2009=y2009,
            y2011=y2011,
            y2013_14=y2013_14,
            y2015=y2015,
            y2017=y2017,
        )

        arcgis_feature_server_arcgis_layer_1006_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1006_attributes

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
