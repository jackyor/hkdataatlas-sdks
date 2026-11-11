from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1005Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1005Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        building_structure_id (int | Unset): Publisher field type: esriFieldTypeInteger
        ddsd_type (None | str | Unset): Publisher field type: esriFieldTypeString
        ddsd_no (None | str | Unset): Publisher field type: esriFieldTypeString
        lot_type (str | Unset): Publisher field type: esriFieldTypeString
        lot_no (str | Unset): Publisher field type: esriFieldTypeString
        section_1 (None | str | Unset): Publisher field type: esriFieldTypeString
        sub_section_1 (None | str | Unset): Publisher field type: esriFieldTypeString
        section_2 (None | str | Unset): Publisher field type: esriFieldTypeString
        sub_section_2 (None | str | Unset): Publisher field type: esriFieldTypeString
        section_3 (None | str | Unset): Publisher field type: esriFieldTypeString
        sub_section_3 (None | str | Unset): Publisher field type: esriFieldTypeString
        section_4 (None | str | Unset): Publisher field type: esriFieldTypeString
        ext_portion (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        misc_no (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
    """

    objectid: int | Unset = UNSET
    building_structure_id: int | Unset = UNSET
    ddsd_type: None | str | Unset = UNSET
    ddsd_no: None | str | Unset = UNSET
    lot_type: str | Unset = UNSET
    lot_no: str | Unset = UNSET
    section_1: None | str | Unset = UNSET
    sub_section_1: None | str | Unset = UNSET
    section_2: None | str | Unset = UNSET
    sub_section_2: None | str | Unset = UNSET
    section_3: None | str | Unset = UNSET
    sub_section_3: None | str | Unset = UNSET
    section_4: None | str | Unset = UNSET
    ext_portion: int | None | Unset = UNSET
    misc_no: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        building_structure_id = self.building_structure_id

        ddsd_type: None | str | Unset
        if isinstance(self.ddsd_type, Unset):
            ddsd_type = UNSET
        else:
            ddsd_type = self.ddsd_type

        ddsd_no: None | str | Unset
        if isinstance(self.ddsd_no, Unset):
            ddsd_no = UNSET
        else:
            ddsd_no = self.ddsd_no

        lot_type = self.lot_type

        lot_no = self.lot_no

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

        ext_portion: int | None | Unset
        if isinstance(self.ext_portion, Unset):
            ext_portion = UNSET
        else:
            ext_portion = self.ext_portion

        misc_no: int | None | Unset
        if isinstance(self.misc_no, Unset):
            misc_no = UNSET
        else:
            misc_no = self.misc_no

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if building_structure_id is not UNSET:
            field_dict["BuildingStructureID"] = building_structure_id
        if ddsd_type is not UNSET:
            field_dict["DDSDType"] = ddsd_type
        if ddsd_no is not UNSET:
            field_dict["DDSDNo"] = ddsd_no
        if lot_type is not UNSET:
            field_dict["LotType"] = lot_type
        if lot_no is not UNSET:
            field_dict["LotNo"] = lot_no
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
        if ext_portion is not UNSET:
            field_dict["ExtPortion"] = ext_portion
        if misc_no is not UNSET:
            field_dict["MiscNo"] = misc_no

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        building_structure_id = d.pop("BuildingStructureID", UNSET)

        def _parse_ddsd_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ddsd_type = _parse_ddsd_type(d.pop("DDSDType", UNSET))

        def _parse_ddsd_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ddsd_no = _parse_ddsd_no(d.pop("DDSDNo", UNSET))

        lot_type = d.pop("LotType", UNSET)

        lot_no = d.pop("LotNo", UNSET)

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

        def _parse_ext_portion(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ext_portion = _parse_ext_portion(d.pop("ExtPortion", UNSET))

        def _parse_misc_no(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        misc_no = _parse_misc_no(d.pop("MiscNo", UNSET))

        arcgis_feature_server_arcgis_layer_1005_attributes = cls(
            objectid=objectid,
            building_structure_id=building_structure_id,
            ddsd_type=ddsd_type,
            ddsd_no=ddsd_no,
            lot_type=lot_type,
            lot_no=lot_no,
            section_1=section_1,
            sub_section_1=sub_section_1,
            section_2=section_2,
            sub_section_2=sub_section_2,
            section_3=section_3,
            sub_section_3=sub_section_3,
            section_4=section_4,
            ext_portion=ext_portion,
            misc_no=misc_no,
        )

        arcgis_feature_server_arcgis_layer_1005_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1005_attributes

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
