from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer2Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer2Attributes:
    """
    Attributes:
        premises_code (float | None | Unset): Publisher field type: esriFieldTypeDouble
        premises_desc_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        premises_desc_chi_nil (None | str | Unset): Publisher field type: esriFieldTypeString
        premises_desc_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        school_name_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        school_name_chi_nil (None | str | Unset): Publisher field type: esriFieldTypeString
        school_name_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        school_number (float | None | Unset): Publisher field type: esriFieldTypeDouble
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    premises_code: float | None | Unset = UNSET
    premises_desc_chi: None | str | Unset = UNSET
    premises_desc_chi_nil: None | str | Unset = UNSET
    premises_desc_eng: None | str | Unset = UNSET
    school_name_chi: None | str | Unset = UNSET
    school_name_chi_nil: None | str | Unset = UNSET
    school_name_eng: None | str | Unset = UNSET
    school_number: float | None | Unset = UNSET
    easting: float | None | Unset = UNSET
    northing: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        premises_code: float | None | Unset
        if isinstance(self.premises_code, Unset):
            premises_code = UNSET
        else:
            premises_code = self.premises_code

        premises_desc_chi: None | str | Unset
        if isinstance(self.premises_desc_chi, Unset):
            premises_desc_chi = UNSET
        else:
            premises_desc_chi = self.premises_desc_chi

        premises_desc_chi_nil: None | str | Unset
        if isinstance(self.premises_desc_chi_nil, Unset):
            premises_desc_chi_nil = UNSET
        else:
            premises_desc_chi_nil = self.premises_desc_chi_nil

        premises_desc_eng: None | str | Unset
        if isinstance(self.premises_desc_eng, Unset):
            premises_desc_eng = UNSET
        else:
            premises_desc_eng = self.premises_desc_eng

        school_name_chi: None | str | Unset
        if isinstance(self.school_name_chi, Unset):
            school_name_chi = UNSET
        else:
            school_name_chi = self.school_name_chi

        school_name_chi_nil: None | str | Unset
        if isinstance(self.school_name_chi_nil, Unset):
            school_name_chi_nil = UNSET
        else:
            school_name_chi_nil = self.school_name_chi_nil

        school_name_eng: None | str | Unset
        if isinstance(self.school_name_eng, Unset):
            school_name_eng = UNSET
        else:
            school_name_eng = self.school_name_eng

        school_number: float | None | Unset
        if isinstance(self.school_number, Unset):
            school_number = UNSET
        else:
            school_number = self.school_number

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if premises_code is not UNSET:
            field_dict["PremisesCode"] = premises_code
        if premises_desc_chi is not UNSET:
            field_dict["PremisesDescChi"] = premises_desc_chi
        if premises_desc_chi_nil is not UNSET:
            field_dict["PremisesDescChi_nil"] = premises_desc_chi_nil
        if premises_desc_eng is not UNSET:
            field_dict["PremisesDescEng"] = premises_desc_eng
        if school_name_chi is not UNSET:
            field_dict["SchoolNameChi"] = school_name_chi
        if school_name_chi_nil is not UNSET:
            field_dict["SchoolNameChi_nil"] = school_name_chi_nil
        if school_name_eng is not UNSET:
            field_dict["SchoolNameEng"] = school_name_eng
        if school_number is not UNSET:
            field_dict["SchoolNumber"] = school_number
        if easting is not UNSET:
            field_dict["easting"] = easting
        if northing is not UNSET:
            field_dict["northing"] = northing
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_premises_code(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        premises_code = _parse_premises_code(d.pop("PremisesCode", UNSET))

        def _parse_premises_desc_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        premises_desc_chi = _parse_premises_desc_chi(d.pop("PremisesDescChi", UNSET))

        def _parse_premises_desc_chi_nil(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        premises_desc_chi_nil = _parse_premises_desc_chi_nil(
            d.pop("PremisesDescChi_nil", UNSET)
        )

        def _parse_premises_desc_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        premises_desc_eng = _parse_premises_desc_eng(d.pop("PremisesDescEng", UNSET))

        def _parse_school_name_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_name_chi = _parse_school_name_chi(d.pop("SchoolNameChi", UNSET))

        def _parse_school_name_chi_nil(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_name_chi_nil = _parse_school_name_chi_nil(
            d.pop("SchoolNameChi_nil", UNSET)
        )

        def _parse_school_name_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_name_eng = _parse_school_name_eng(d.pop("SchoolNameEng", UNSET))

        def _parse_school_number(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        school_number = _parse_school_number(d.pop("SchoolNumber", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("easting", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("northing", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_2_attributes = cls(
            premises_code=premises_code,
            premises_desc_chi=premises_desc_chi,
            premises_desc_chi_nil=premises_desc_chi_nil,
            premises_desc_eng=premises_desc_eng,
            school_name_chi=school_name_chi,
            school_name_chi_nil=school_name_chi_nil,
            school_name_eng=school_name_eng,
            school_number=school_number,
            easting=easting,
            northing=northing,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_2_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_2_attributes

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
