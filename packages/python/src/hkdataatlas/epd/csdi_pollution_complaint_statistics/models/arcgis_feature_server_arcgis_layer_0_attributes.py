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
        dataset_en (None | str | Unset): Publisher field type: esriFieldTypeString
        dataset_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        year_en (None | str | Unset): Publisher field type: esriFieldTypeString
        year_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        total_en (None | str | Unset): Publisher field type: esriFieldTypeString
        total_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_en (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        air_en (None | str | Unset): Publisher field type: esriFieldTypeString
        air_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        noise_en (None | str | Unset): Publisher field type: esriFieldTypeString
        noise_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        water_en (None | str | Unset): Publisher field type: esriFieldTypeString
        water_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        waste_en (None | str | Unset): Publisher field type: esriFieldTypeString
        waste_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        misc_en (None | str | Unset): Publisher field type: esriFieldTypeString
        misc_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        website_en (None | str | Unset): Publisher field type: esriFieldTypeString
        website_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        last_update (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    dataset_en: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    year_en: None | str | Unset = UNSET
    year_tc: None | str | Unset = UNSET
    total_en: None | str | Unset = UNSET
    total_tc: None | str | Unset = UNSET
    percentage_en: None | str | Unset = UNSET
    percentage_tc: None | str | Unset = UNSET
    air_en: None | str | Unset = UNSET
    air_tc: None | str | Unset = UNSET
    noise_en: None | str | Unset = UNSET
    noise_tc: None | str | Unset = UNSET
    water_en: None | str | Unset = UNSET
    water_tc: None | str | Unset = UNSET
    waste_en: None | str | Unset = UNSET
    waste_tc: None | str | Unset = UNSET
    misc_en: None | str | Unset = UNSET
    misc_tc: None | str | Unset = UNSET
    website_en: None | str | Unset = UNSET
    website_tc: None | str | Unset = UNSET
    last_update: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        dataset_en: None | str | Unset
        if isinstance(self.dataset_en, Unset):
            dataset_en = UNSET
        else:
            dataset_en = self.dataset_en

        dataset_tc: None | str | Unset
        if isinstance(self.dataset_tc, Unset):
            dataset_tc = UNSET
        else:
            dataset_tc = self.dataset_tc

        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        year_en: None | str | Unset
        if isinstance(self.year_en, Unset):
            year_en = UNSET
        else:
            year_en = self.year_en

        year_tc: None | str | Unset
        if isinstance(self.year_tc, Unset):
            year_tc = UNSET
        else:
            year_tc = self.year_tc

        total_en: None | str | Unset
        if isinstance(self.total_en, Unset):
            total_en = UNSET
        else:
            total_en = self.total_en

        total_tc: None | str | Unset
        if isinstance(self.total_tc, Unset):
            total_tc = UNSET
        else:
            total_tc = self.total_tc

        percentage_en: None | str | Unset
        if isinstance(self.percentage_en, Unset):
            percentage_en = UNSET
        else:
            percentage_en = self.percentage_en

        percentage_tc: None | str | Unset
        if isinstance(self.percentage_tc, Unset):
            percentage_tc = UNSET
        else:
            percentage_tc = self.percentage_tc

        air_en: None | str | Unset
        if isinstance(self.air_en, Unset):
            air_en = UNSET
        else:
            air_en = self.air_en

        air_tc: None | str | Unset
        if isinstance(self.air_tc, Unset):
            air_tc = UNSET
        else:
            air_tc = self.air_tc

        noise_en: None | str | Unset
        if isinstance(self.noise_en, Unset):
            noise_en = UNSET
        else:
            noise_en = self.noise_en

        noise_tc: None | str | Unset
        if isinstance(self.noise_tc, Unset):
            noise_tc = UNSET
        else:
            noise_tc = self.noise_tc

        water_en: None | str | Unset
        if isinstance(self.water_en, Unset):
            water_en = UNSET
        else:
            water_en = self.water_en

        water_tc: None | str | Unset
        if isinstance(self.water_tc, Unset):
            water_tc = UNSET
        else:
            water_tc = self.water_tc

        waste_en: None | str | Unset
        if isinstance(self.waste_en, Unset):
            waste_en = UNSET
        else:
            waste_en = self.waste_en

        waste_tc: None | str | Unset
        if isinstance(self.waste_tc, Unset):
            waste_tc = UNSET
        else:
            waste_tc = self.waste_tc

        misc_en: None | str | Unset
        if isinstance(self.misc_en, Unset):
            misc_en = UNSET
        else:
            misc_en = self.misc_en

        misc_tc: None | str | Unset
        if isinstance(self.misc_tc, Unset):
            misc_tc = UNSET
        else:
            misc_tc = self.misc_tc

        website_en: None | str | Unset
        if isinstance(self.website_en, Unset):
            website_en = UNSET
        else:
            website_en = self.website_en

        website_tc: None | str | Unset
        if isinstance(self.website_tc, Unset):
            website_tc = UNSET
        else:
            website_tc = self.website_tc

        last_update = self.last_update

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
        if dataset_en is not UNSET:
            field_dict["DatasetEN"] = dataset_en
        if dataset_tc is not UNSET:
            field_dict["DatasetTC"] = dataset_tc
        if district_en is not UNSET:
            field_dict["DistrictEN"] = district_en
        if district_tc is not UNSET:
            field_dict["DistrictTC"] = district_tc
        if year_en is not UNSET:
            field_dict["YearEN"] = year_en
        if year_tc is not UNSET:
            field_dict["YearTC"] = year_tc
        if total_en is not UNSET:
            field_dict["TotalEN"] = total_en
        if total_tc is not UNSET:
            field_dict["TotalTC"] = total_tc
        if percentage_en is not UNSET:
            field_dict["PercentageEN"] = percentage_en
        if percentage_tc is not UNSET:
            field_dict["PercentageTC"] = percentage_tc
        if air_en is not UNSET:
            field_dict["AirEN"] = air_en
        if air_tc is not UNSET:
            field_dict["AirTC"] = air_tc
        if noise_en is not UNSET:
            field_dict["NoiseEN"] = noise_en
        if noise_tc is not UNSET:
            field_dict["NoiseTC"] = noise_tc
        if water_en is not UNSET:
            field_dict["WaterEN"] = water_en
        if water_tc is not UNSET:
            field_dict["WaterTC"] = water_tc
        if waste_en is not UNSET:
            field_dict["WasteEN"] = waste_en
        if waste_tc is not UNSET:
            field_dict["WasteTC"] = waste_tc
        if misc_en is not UNSET:
            field_dict["MiscEN"] = misc_en
        if misc_tc is not UNSET:
            field_dict["MiscTC"] = misc_tc
        if website_en is not UNSET:
            field_dict["WebsiteEN"] = website_en
        if website_tc is not UNSET:
            field_dict["WebsiteTC"] = website_tc
        if last_update is not UNSET:
            field_dict["LastUpdate"] = last_update
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_dataset_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_en = _parse_dataset_en(d.pop("DatasetEN", UNSET))

        def _parse_dataset_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_tc = _parse_dataset_tc(d.pop("DatasetTC", UNSET))

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("DistrictEN", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("DistrictTC", UNSET))

        def _parse_year_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year_en = _parse_year_en(d.pop("YearEN", UNSET))

        def _parse_year_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year_tc = _parse_year_tc(d.pop("YearTC", UNSET))

        def _parse_total_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_en = _parse_total_en(d.pop("TotalEN", UNSET))

        def _parse_total_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_tc = _parse_total_tc(d.pop("TotalTC", UNSET))

        def _parse_percentage_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_en = _parse_percentage_en(d.pop("PercentageEN", UNSET))

        def _parse_percentage_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_tc = _parse_percentage_tc(d.pop("PercentageTC", UNSET))

        def _parse_air_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        air_en = _parse_air_en(d.pop("AirEN", UNSET))

        def _parse_air_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        air_tc = _parse_air_tc(d.pop("AirTC", UNSET))

        def _parse_noise_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        noise_en = _parse_noise_en(d.pop("NoiseEN", UNSET))

        def _parse_noise_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        noise_tc = _parse_noise_tc(d.pop("NoiseTC", UNSET))

        def _parse_water_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        water_en = _parse_water_en(d.pop("WaterEN", UNSET))

        def _parse_water_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        water_tc = _parse_water_tc(d.pop("WaterTC", UNSET))

        def _parse_waste_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        waste_en = _parse_waste_en(d.pop("WasteEN", UNSET))

        def _parse_waste_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        waste_tc = _parse_waste_tc(d.pop("WasteTC", UNSET))

        def _parse_misc_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        misc_en = _parse_misc_en(d.pop("MiscEN", UNSET))

        def _parse_misc_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        misc_tc = _parse_misc_tc(d.pop("MiscTC", UNSET))

        def _parse_website_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_en = _parse_website_en(d.pop("WebsiteEN", UNSET))

        def _parse_website_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_tc = _parse_website_tc(d.pop("WebsiteTC", UNSET))

        last_update = d.pop("LastUpdate", UNSET)

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
            dataset_en=dataset_en,
            dataset_tc=dataset_tc,
            district_en=district_en,
            district_tc=district_tc,
            year_en=year_en,
            year_tc=year_tc,
            total_en=total_en,
            total_tc=total_tc,
            percentage_en=percentage_en,
            percentage_tc=percentage_tc,
            air_en=air_en,
            air_tc=air_tc,
            noise_en=noise_en,
            noise_tc=noise_tc,
            water_en=water_en,
            water_tc=water_tc,
            waste_en=waste_en,
            waste_tc=waste_tc,
            misc_en=misc_en,
            misc_tc=misc_tc,
            website_en=website_en,
            website_tc=website_tc,
            last_update=last_update,
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
