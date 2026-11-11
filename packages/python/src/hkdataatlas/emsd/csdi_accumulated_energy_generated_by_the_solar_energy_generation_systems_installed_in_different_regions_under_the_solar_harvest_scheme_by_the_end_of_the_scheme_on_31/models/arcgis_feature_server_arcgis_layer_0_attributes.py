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
        energy_generation_in_k_wh (float | None | Unset): Publisher field type: esriFieldTypeDouble
        equivalent_co2_absorption_by_number_of_trees (float | None | Unset): Publisher field type: esriFieldTypeDouble
        equivalent_carbon_reduction_in_kg (float | None | Unset): Publisher field type: esriFieldTypeDouble
        equivalent_monthly_electricity_consumption_of_a_3_person_family (float | None | Unset): Publisher field type:
            esriFieldTypeDouble
        information_last_updated_date (None | str | Unset): Publisher field type: esriFieldTypeString
        region_english (None | str | Unset): Publisher field type: esriFieldTypeString
        region_simplified_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        region_traditional_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    energy_generation_in_k_wh: float | None | Unset = UNSET
    equivalent_co2_absorption_by_number_of_trees: float | None | Unset = UNSET
    equivalent_carbon_reduction_in_kg: float | None | Unset = UNSET
    equivalent_monthly_electricity_consumption_of_a_3_person_family: (
        float | None | Unset
    ) = UNSET
    information_last_updated_date: None | str | Unset = UNSET
    region_english: None | str | Unset = UNSET
    region_simplified_chinese: None | str | Unset = UNSET
    region_traditional_chinese: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        energy_generation_in_k_wh: float | None | Unset
        if isinstance(self.energy_generation_in_k_wh, Unset):
            energy_generation_in_k_wh = UNSET
        else:
            energy_generation_in_k_wh = self.energy_generation_in_k_wh

        equivalent_co2_absorption_by_number_of_trees: float | None | Unset
        if isinstance(self.equivalent_co2_absorption_by_number_of_trees, Unset):
            equivalent_co2_absorption_by_number_of_trees = UNSET
        else:
            equivalent_co2_absorption_by_number_of_trees = (
                self.equivalent_co2_absorption_by_number_of_trees
            )

        equivalent_carbon_reduction_in_kg: float | None | Unset
        if isinstance(self.equivalent_carbon_reduction_in_kg, Unset):
            equivalent_carbon_reduction_in_kg = UNSET
        else:
            equivalent_carbon_reduction_in_kg = self.equivalent_carbon_reduction_in_kg

        equivalent_monthly_electricity_consumption_of_a_3_person_family: (
            float | None | Unset
        )
        if isinstance(
            self.equivalent_monthly_electricity_consumption_of_a_3_person_family, Unset
        ):
            equivalent_monthly_electricity_consumption_of_a_3_person_family = UNSET
        else:
            equivalent_monthly_electricity_consumption_of_a_3_person_family = (
                self.equivalent_monthly_electricity_consumption_of_a_3_person_family
            )

        information_last_updated_date: None | str | Unset
        if isinstance(self.information_last_updated_date, Unset):
            information_last_updated_date = UNSET
        else:
            information_last_updated_date = self.information_last_updated_date

        region_english: None | str | Unset
        if isinstance(self.region_english, Unset):
            region_english = UNSET
        else:
            region_english = self.region_english

        region_simplified_chinese: None | str | Unset
        if isinstance(self.region_simplified_chinese, Unset):
            region_simplified_chinese = UNSET
        else:
            region_simplified_chinese = self.region_simplified_chinese

        region_traditional_chinese: None | str | Unset
        if isinstance(self.region_traditional_chinese, Unset):
            region_traditional_chinese = UNSET
        else:
            region_traditional_chinese = self.region_traditional_chinese

        objectid = self.objectid

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
        if energy_generation_in_k_wh is not UNSET:
            field_dict["Energy_generation_in_kWh"] = energy_generation_in_k_wh
        if equivalent_co2_absorption_by_number_of_trees is not UNSET:
            field_dict["Equivalent_CO2_absorption_by_number_of_trees"] = (
                equivalent_co2_absorption_by_number_of_trees
            )
        if equivalent_carbon_reduction_in_kg is not UNSET:
            field_dict["Equivalent_carbon_reduction_in_kg"] = (
                equivalent_carbon_reduction_in_kg
            )
        if equivalent_monthly_electricity_consumption_of_a_3_person_family is not UNSET:
            field_dict[
                "Equivalent_monthly_electricity_consumption_of_a_3_person_family"
            ] = equivalent_monthly_electricity_consumption_of_a_3_person_family
        if information_last_updated_date is not UNSET:
            field_dict["Information_Last_Updated_Date"] = information_last_updated_date
        if region_english is not UNSET:
            field_dict["Region_English"] = region_english
        if region_simplified_chinese is not UNSET:
            field_dict["Region_Simplified_Chinese"] = region_simplified_chinese
        if region_traditional_chinese is not UNSET:
            field_dict["Region_Traditional_Chinese"] = region_traditional_chinese
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_energy_generation_in_k_wh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        energy_generation_in_k_wh = _parse_energy_generation_in_k_wh(
            d.pop("Energy_generation_in_kWh", UNSET)
        )

        def _parse_equivalent_co2_absorption_by_number_of_trees(
            data: object,
        ) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        equivalent_co2_absorption_by_number_of_trees = (
            _parse_equivalent_co2_absorption_by_number_of_trees(
                d.pop("Equivalent_CO2_absorption_by_number_of_trees", UNSET)
            )
        )

        def _parse_equivalent_carbon_reduction_in_kg(
            data: object,
        ) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        equivalent_carbon_reduction_in_kg = _parse_equivalent_carbon_reduction_in_kg(
            d.pop("Equivalent_carbon_reduction_in_kg", UNSET)
        )

        def _parse_equivalent_monthly_electricity_consumption_of_a_3_person_family(
            data: object,
        ) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        equivalent_monthly_electricity_consumption_of_a_3_person_family = (
            _parse_equivalent_monthly_electricity_consumption_of_a_3_person_family(
                d.pop(
                    "Equivalent_monthly_electricity_consumption_of_a_3_person_family",
                    UNSET,
                )
            )
        )

        def _parse_information_last_updated_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        information_last_updated_date = _parse_information_last_updated_date(
            d.pop("Information_Last_Updated_Date", UNSET)
        )

        def _parse_region_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_english = _parse_region_english(d.pop("Region_English", UNSET))

        def _parse_region_simplified_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_simplified_chinese = _parse_region_simplified_chinese(
            d.pop("Region_Simplified_Chinese", UNSET)
        )

        def _parse_region_traditional_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_traditional_chinese = _parse_region_traditional_chinese(
            d.pop("Region_Traditional_Chinese", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

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
            energy_generation_in_k_wh=energy_generation_in_k_wh,
            equivalent_co2_absorption_by_number_of_trees=equivalent_co2_absorption_by_number_of_trees,
            equivalent_carbon_reduction_in_kg=equivalent_carbon_reduction_in_kg,
            equivalent_monthly_electricity_consumption_of_a_3_person_family=equivalent_monthly_electricity_consumption_of_a_3_person_family,
            information_last_updated_date=information_last_updated_date,
            region_english=region_english,
            region_simplified_chinese=region_simplified_chinese,
            region_traditional_chinese=region_traditional_chinese,
            objectid=objectid,
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
