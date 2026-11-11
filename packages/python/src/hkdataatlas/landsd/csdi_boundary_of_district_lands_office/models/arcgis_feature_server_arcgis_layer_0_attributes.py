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
        landsdepartmentdistrictid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        englishname (None | str | Unset): Publisher field type: esriFieldTypeString
        chinesename (None | str | Unset): Publisher field type: esriFieldTypeString
        address_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        address_chn (None | str | Unset): Publisher field type: esriFieldTypeString
        tel (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    landsdepartmentdistrictid: int | None | Unset = UNSET
    englishname: None | str | Unset = UNSET
    chinesename: None | str | Unset = UNSET
    address_eng: None | str | Unset = UNSET
    address_chn: None | str | Unset = UNSET
    tel: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        landsdepartmentdistrictid: int | None | Unset
        if isinstance(self.landsdepartmentdistrictid, Unset):
            landsdepartmentdistrictid = UNSET
        else:
            landsdepartmentdistrictid = self.landsdepartmentdistrictid

        englishname: None | str | Unset
        if isinstance(self.englishname, Unset):
            englishname = UNSET
        else:
            englishname = self.englishname

        chinesename: None | str | Unset
        if isinstance(self.chinesename, Unset):
            chinesename = UNSET
        else:
            chinesename = self.chinesename

        address_eng: None | str | Unset
        if isinstance(self.address_eng, Unset):
            address_eng = UNSET
        else:
            address_eng = self.address_eng

        address_chn: None | str | Unset
        if isinstance(self.address_chn, Unset):
            address_chn = UNSET
        else:
            address_chn = self.address_chn

        tel: None | str | Unset
        if isinstance(self.tel, Unset):
            tel = UNSET
        else:
            tel = self.tel

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        shape_area: float | None | Unset
        if isinstance(self.shape_area, Unset):
            shape_area = UNSET
        else:
            shape_area = self.shape_area

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if landsdepartmentdistrictid is not UNSET:
            field_dict["LANDSDEPARTMENTDISTRICTID"] = landsdepartmentdistrictid
        if englishname is not UNSET:
            field_dict["ENGLISHNAME"] = englishname
        if chinesename is not UNSET:
            field_dict["CHINESENAME"] = chinesename
        if address_eng is not UNSET:
            field_dict["ADDRESS_ENG"] = address_eng
        if address_chn is not UNSET:
            field_dict["ADDRESS_CHN"] = address_chn
        if tel is not UNSET:
            field_dict["TEL"] = tel
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_landsdepartmentdistrictid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        landsdepartmentdistrictid = _parse_landsdepartmentdistrictid(
            d.pop("LANDSDEPARTMENTDISTRICTID", UNSET)
        )

        def _parse_englishname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        englishname = _parse_englishname(d.pop("ENGLISHNAME", UNSET))

        def _parse_chinesename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinesename = _parse_chinesename(d.pop("CHINESENAME", UNSET))

        def _parse_address_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_eng = _parse_address_eng(d.pop("ADDRESS_ENG", UNSET))

        def _parse_address_chn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_chn = _parse_address_chn(d.pop("ADDRESS_CHN", UNSET))

        def _parse_tel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tel = _parse_tel(d.pop("TEL", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape__Area", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            landsdepartmentdistrictid=landsdepartmentdistrictid,
            englishname=englishname,
            chinesename=chinesename,
            address_eng=address_eng,
            address_chn=address_chn,
            tel=tel,
            shape_length=shape_length,
            shape_area=shape_area,
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
