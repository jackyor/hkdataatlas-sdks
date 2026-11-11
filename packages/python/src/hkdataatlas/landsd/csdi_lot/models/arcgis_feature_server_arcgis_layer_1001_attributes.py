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
        prn (str | Unset): Publisher field type: esriFieldTypeString
        lot_type (str | Unset): Publisher field type: esriFieldTypeString
        lot_number (str | Unset): Publisher field type: esriFieldTypeString
        section_1 (None | str | Unset): Publisher field type: esriFieldTypeString
        sub_section_1 (None | str | Unset): Publisher field type: esriFieldTypeString
        section_2 (None | str | Unset): Publisher field type: esriFieldTypeString
        sub_section_2 (None | str | Unset): Publisher field type: esriFieldTypeString
        section_3 (None | str | Unset): Publisher field type: esriFieldTypeString
        sub_section_3 (None | str | Unset): Publisher field type: esriFieldTypeString
        section_4 (None | str | Unset): Publisher field type: esriFieldTypeString
        extension (None | str | Unset): Publisher field type: esriFieldTypeString
        miscellaneous_item (int | None | Unset): Publisher field type: esriFieldTypeInteger
        eng_lot_description (str | Unset): Publisher field type: esriFieldTypeString
        is_closed (int | Unset): Publisher field type: esriFieldTypeSmallInteger
        date_stamp (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
    """

    objectid: int | Unset = UNSET
    prn: str | Unset = UNSET
    lot_type: str | Unset = UNSET
    lot_number: str | Unset = UNSET
    section_1: None | str | Unset = UNSET
    sub_section_1: None | str | Unset = UNSET
    section_2: None | str | Unset = UNSET
    sub_section_2: None | str | Unset = UNSET
    section_3: None | str | Unset = UNSET
    sub_section_3: None | str | Unset = UNSET
    section_4: None | str | Unset = UNSET
    extension: None | str | Unset = UNSET
    miscellaneous_item: int | None | Unset = UNSET
    eng_lot_description: str | Unset = UNSET
    is_closed: int | Unset = UNSET
    date_stamp: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        prn = self.prn

        lot_type = self.lot_type

        lot_number = self.lot_number

        section_1: None | str | Unset
        if isinstance(self.section_1, Unset):
            section_1 = UNSET
        else:
            section_1 = self.section_1

        sub_section_1: None | str | Unset
        if isinstance(self.sub_section_1, Unset):
            sub_section_1 = UNSET
        else:
            sub_section_1 = self.sub_section_1

        section_2: None | str | Unset
        if isinstance(self.section_2, Unset):
            section_2 = UNSET
        else:
            section_2 = self.section_2

        sub_section_2: None | str | Unset
        if isinstance(self.sub_section_2, Unset):
            sub_section_2 = UNSET
        else:
            sub_section_2 = self.sub_section_2

        section_3: None | str | Unset
        if isinstance(self.section_3, Unset):
            section_3 = UNSET
        else:
            section_3 = self.section_3

        sub_section_3: None | str | Unset
        if isinstance(self.sub_section_3, Unset):
            sub_section_3 = UNSET
        else:
            sub_section_3 = self.sub_section_3

        section_4: None | str | Unset
        if isinstance(self.section_4, Unset):
            section_4 = UNSET
        else:
            section_4 = self.section_4

        extension: None | str | Unset
        if isinstance(self.extension, Unset):
            extension = UNSET
        else:
            extension = self.extension

        miscellaneous_item: int | None | Unset
        if isinstance(self.miscellaneous_item, Unset):
            miscellaneous_item = UNSET
        else:
            miscellaneous_item = self.miscellaneous_item

        eng_lot_description = self.eng_lot_description

        is_closed = self.is_closed

        date_stamp = self.date_stamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if prn is not UNSET:
            field_dict["PRN"] = prn
        if lot_type is not UNSET:
            field_dict["LotType"] = lot_type
        if lot_number is not UNSET:
            field_dict["LotNumber"] = lot_number
        if section_1 is not UNSET:
            field_dict["Section1"] = section_1
        if sub_section_1 is not UNSET:
            field_dict["SubSection1"] = sub_section_1
        if section_2 is not UNSET:
            field_dict["Section2"] = section_2
        if sub_section_2 is not UNSET:
            field_dict["SubSection2"] = sub_section_2
        if section_3 is not UNSET:
            field_dict["Section3"] = section_3
        if sub_section_3 is not UNSET:
            field_dict["SubSection3"] = sub_section_3
        if section_4 is not UNSET:
            field_dict["Section4"] = section_4
        if extension is not UNSET:
            field_dict["Extension"] = extension
        if miscellaneous_item is not UNSET:
            field_dict["MiscellaneousItem"] = miscellaneous_item
        if eng_lot_description is not UNSET:
            field_dict["ENGLotDescription"] = eng_lot_description
        if is_closed is not UNSET:
            field_dict["IsClosed"] = is_closed
        if date_stamp is not UNSET:
            field_dict["DateStamp"] = date_stamp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        prn = d.pop("PRN", UNSET)

        lot_type = d.pop("LotType", UNSET)

        lot_number = d.pop("LotNumber", UNSET)

        def _parse_section_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        section_1 = _parse_section_1(d.pop("Section1", UNSET))

        def _parse_sub_section_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_section_1 = _parse_sub_section_1(d.pop("SubSection1", UNSET))

        def _parse_section_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        section_2 = _parse_section_2(d.pop("Section2", UNSET))

        def _parse_sub_section_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_section_2 = _parse_sub_section_2(d.pop("SubSection2", UNSET))

        def _parse_section_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        section_3 = _parse_section_3(d.pop("Section3", UNSET))

        def _parse_sub_section_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_section_3 = _parse_sub_section_3(d.pop("SubSection3", UNSET))

        def _parse_section_4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        section_4 = _parse_section_4(d.pop("Section4", UNSET))

        def _parse_extension(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extension = _parse_extension(d.pop("Extension", UNSET))

        def _parse_miscellaneous_item(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        miscellaneous_item = _parse_miscellaneous_item(
            d.pop("MiscellaneousItem", UNSET)
        )

        eng_lot_description = d.pop("ENGLotDescription", UNSET)

        is_closed = d.pop("IsClosed", UNSET)

        date_stamp = d.pop("DateStamp", UNSET)

        arcgis_feature_server_arcgis_layer_1001_attributes = cls(
            objectid=objectid,
            prn=prn,
            lot_type=lot_type,
            lot_number=lot_number,
            section_1=section_1,
            sub_section_1=sub_section_1,
            section_2=section_2,
            sub_section_2=sub_section_2,
            section_3=section_3,
            sub_section_3=sub_section_3,
            section_4=section_4,
            extension=extension,
            miscellaneous_item=miscellaneous_item,
            eng_lot_description=eng_lot_description,
            is_closed=is_closed,
            date_stamp=date_stamp,
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
