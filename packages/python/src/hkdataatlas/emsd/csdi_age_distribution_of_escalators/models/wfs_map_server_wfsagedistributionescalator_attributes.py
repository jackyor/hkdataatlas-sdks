from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsagedistributionescalatorAttributes")


@_attrs_define
class WfsMapServerWfsagedistributionescalatorAttributes:
    """
    Attributes:
        age_range (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        district_traditional_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        number_of_escalators (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    age_range: None | str | Unset = UNSET
    district_english: None | str | Unset = UNSET
    district_traditional_chinese: None | str | Unset = UNSET
    number_of_escalators: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        age_range: None | str | Unset
        if isinstance(self.age_range, Unset):
            age_range = UNSET
        else:
            age_range = self.age_range

        district_english: None | str | Unset
        if isinstance(self.district_english, Unset):
            district_english = UNSET
        else:
            district_english = self.district_english

        district_traditional_chinese: None | str | Unset
        if isinstance(self.district_traditional_chinese, Unset):
            district_traditional_chinese = UNSET
        else:
            district_traditional_chinese = self.district_traditional_chinese

        number_of_escalators: float | None | Unset
        if isinstance(self.number_of_escalators, Unset):
            number_of_escalators = UNSET
        else:
            number_of_escalators = self.number_of_escalators

        objectid = self.objectid

        shape = self.shape

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
        if age_range is not UNSET:
            field_dict["Age_Range"] = age_range
        if district_english is not UNSET:
            field_dict["District_English"] = district_english
        if district_traditional_chinese is not UNSET:
            field_dict["District_Traditional_Chinese"] = district_traditional_chinese
        if number_of_escalators is not UNSET:
            field_dict["Number_of_Escalators"] = number_of_escalators
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if shape_length is not UNSET:
            field_dict["SHAPE_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["SHAPE_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_age_range(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        age_range = _parse_age_range(d.pop("Age_Range", UNSET))

        def _parse_district_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_english = _parse_district_english(d.pop("District_English", UNSET))

        def _parse_district_traditional_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_traditional_chinese = _parse_district_traditional_chinese(
            d.pop("District_Traditional_Chinese", UNSET)
        )

        def _parse_number_of_escalators(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        number_of_escalators = _parse_number_of_escalators(
            d.pop("Number_of_Escalators", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("SHAPE_Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("SHAPE_Area", UNSET))

        wfs_map_server_wfsagedistributionescalator_attributes = cls(
            age_range=age_range,
            district_english=district_english,
            district_traditional_chinese=district_traditional_chinese,
            number_of_escalators=number_of_escalators,
            objectid=objectid,
            shape=shape,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfsagedistributionescalator_attributes.additional_properties = d
        return wfs_map_server_wfsagedistributionescalator_attributes

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
