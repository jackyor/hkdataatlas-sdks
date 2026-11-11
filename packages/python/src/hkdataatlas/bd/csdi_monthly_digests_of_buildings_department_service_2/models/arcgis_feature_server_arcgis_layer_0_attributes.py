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
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        year_en (None | str | Unset): Publisher field type: esriFieldTypeString
        year_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        month_en (None | str | Unset): Publisher field type: esriFieldTypeString
        month_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        region_en (None | str | Unset): Publisher field type: esriFieldTypeString
        region_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_blocks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_blocks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        building_type_en (None | str | Unset): Publisher field type: esriFieldTypeString
        building_type_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        domestic_gfa_en (None | str | Unset): Publisher field type: esriFieldTypeString
        domestic_gfa_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        non_domestic_gfa_en (None | str | Unset): Publisher field type: esriFieldTypeString
        non_domestic_gfa_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        authorized_person_en (None | str | Unset): Publisher field type: esriFieldTypeString
        authorized_person_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        reg_structural_engineer_en (None | str | Unset): Publisher field type: esriFieldTypeString
        reg_structural_engineer_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        applicant_en (None | str | Unset): Publisher field type: esriFieldTypeString
        applicant_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        last_update (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
    """

    objectid: int | Unset = UNSET
    dataset_en: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    year_en: None | str | Unset = UNSET
    year_tc: None | str | Unset = UNSET
    month_en: None | str | Unset = UNSET
    month_tc: None | str | Unset = UNSET
    region_en: None | str | Unset = UNSET
    region_tc: None | str | Unset = UNSET
    no_of_blocks_en: None | str | Unset = UNSET
    no_of_blocks_tc: None | str | Unset = UNSET
    building_type_en: None | str | Unset = UNSET
    building_type_tc: None | str | Unset = UNSET
    domestic_gfa_en: None | str | Unset = UNSET
    domestic_gfa_tc: None | str | Unset = UNSET
    non_domestic_gfa_en: None | str | Unset = UNSET
    non_domestic_gfa_tc: None | str | Unset = UNSET
    authorized_person_en: None | str | Unset = UNSET
    authorized_person_tc: None | str | Unset = UNSET
    reg_structural_engineer_en: None | str | Unset = UNSET
    reg_structural_engineer_tc: None | str | Unset = UNSET
    applicant_en: None | str | Unset = UNSET
    applicant_tc: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    easting: float | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    last_update: Any | Unset = UNSET
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

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

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

        month_en: None | str | Unset
        if isinstance(self.month_en, Unset):
            month_en = UNSET
        else:
            month_en = self.month_en

        month_tc: None | str | Unset
        if isinstance(self.month_tc, Unset):
            month_tc = UNSET
        else:
            month_tc = self.month_tc

        region_en: None | str | Unset
        if isinstance(self.region_en, Unset):
            region_en = UNSET
        else:
            region_en = self.region_en

        region_tc: None | str | Unset
        if isinstance(self.region_tc, Unset):
            region_tc = UNSET
        else:
            region_tc = self.region_tc

        no_of_blocks_en: None | str | Unset
        if isinstance(self.no_of_blocks_en, Unset):
            no_of_blocks_en = UNSET
        else:
            no_of_blocks_en = self.no_of_blocks_en

        no_of_blocks_tc: None | str | Unset
        if isinstance(self.no_of_blocks_tc, Unset):
            no_of_blocks_tc = UNSET
        else:
            no_of_blocks_tc = self.no_of_blocks_tc

        building_type_en: None | str | Unset
        if isinstance(self.building_type_en, Unset):
            building_type_en = UNSET
        else:
            building_type_en = self.building_type_en

        building_type_tc: None | str | Unset
        if isinstance(self.building_type_tc, Unset):
            building_type_tc = UNSET
        else:
            building_type_tc = self.building_type_tc

        domestic_gfa_en: None | str | Unset
        if isinstance(self.domestic_gfa_en, Unset):
            domestic_gfa_en = UNSET
        else:
            domestic_gfa_en = self.domestic_gfa_en

        domestic_gfa_tc: None | str | Unset
        if isinstance(self.domestic_gfa_tc, Unset):
            domestic_gfa_tc = UNSET
        else:
            domestic_gfa_tc = self.domestic_gfa_tc

        non_domestic_gfa_en: None | str | Unset
        if isinstance(self.non_domestic_gfa_en, Unset):
            non_domestic_gfa_en = UNSET
        else:
            non_domestic_gfa_en = self.non_domestic_gfa_en

        non_domestic_gfa_tc: None | str | Unset
        if isinstance(self.non_domestic_gfa_tc, Unset):
            non_domestic_gfa_tc = UNSET
        else:
            non_domestic_gfa_tc = self.non_domestic_gfa_tc

        authorized_person_en: None | str | Unset
        if isinstance(self.authorized_person_en, Unset):
            authorized_person_en = UNSET
        else:
            authorized_person_en = self.authorized_person_en

        authorized_person_tc: None | str | Unset
        if isinstance(self.authorized_person_tc, Unset):
            authorized_person_tc = UNSET
        else:
            authorized_person_tc = self.authorized_person_tc

        reg_structural_engineer_en: None | str | Unset
        if isinstance(self.reg_structural_engineer_en, Unset):
            reg_structural_engineer_en = UNSET
        else:
            reg_structural_engineer_en = self.reg_structural_engineer_en

        reg_structural_engineer_tc: None | str | Unset
        if isinstance(self.reg_structural_engineer_tc, Unset):
            reg_structural_engineer_tc = UNSET
        else:
            reg_structural_engineer_tc = self.reg_structural_engineer_tc

        applicant_en: None | str | Unset
        if isinstance(self.applicant_en, Unset):
            applicant_en = UNSET
        else:
            applicant_en = self.applicant_en

        applicant_tc: None | str | Unset
        if isinstance(self.applicant_tc, Unset):
            applicant_tc = UNSET
        else:
            applicant_tc = self.applicant_tc

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        last_update = self.last_update

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if dataset_en is not UNSET:
            field_dict["DatasetEN"] = dataset_en
        if dataset_tc is not UNSET:
            field_dict["DatasetTC"] = dataset_tc
        if address_en is not UNSET:
            field_dict["AddressEN"] = address_en
        if address_tc is not UNSET:
            field_dict["AddressTC"] = address_tc
        if year_en is not UNSET:
            field_dict["Year_EN"] = year_en
        if year_tc is not UNSET:
            field_dict["Year_TC"] = year_tc
        if month_en is not UNSET:
            field_dict["Month_EN"] = month_en
        if month_tc is not UNSET:
            field_dict["Month_TC"] = month_tc
        if region_en is not UNSET:
            field_dict["Region_EN"] = region_en
        if region_tc is not UNSET:
            field_dict["Region_TC"] = region_tc
        if no_of_blocks_en is not UNSET:
            field_dict["No_of_Blocks_EN"] = no_of_blocks_en
        if no_of_blocks_tc is not UNSET:
            field_dict["No_of_Blocks_TC"] = no_of_blocks_tc
        if building_type_en is not UNSET:
            field_dict["Building_Type_EN"] = building_type_en
        if building_type_tc is not UNSET:
            field_dict["Building_Type_TC"] = building_type_tc
        if domestic_gfa_en is not UNSET:
            field_dict["Domestic_GFA_EN"] = domestic_gfa_en
        if domestic_gfa_tc is not UNSET:
            field_dict["Domestic_GFA_TC"] = domestic_gfa_tc
        if non_domestic_gfa_en is not UNSET:
            field_dict["NonDomestic_GFA_EN"] = non_domestic_gfa_en
        if non_domestic_gfa_tc is not UNSET:
            field_dict["NonDomestic_GFA_TC"] = non_domestic_gfa_tc
        if authorized_person_en is not UNSET:
            field_dict["Authorized_Person_EN"] = authorized_person_en
        if authorized_person_tc is not UNSET:
            field_dict["Authorized_Person_TC"] = authorized_person_tc
        if reg_structural_engineer_en is not UNSET:
            field_dict["Reg_Structural_Engineer_EN"] = reg_structural_engineer_en
        if reg_structural_engineer_tc is not UNSET:
            field_dict["Reg_Structural_Engineer_TC"] = reg_structural_engineer_tc
        if applicant_en is not UNSET:
            field_dict["Applicant_EN"] = applicant_en
        if applicant_tc is not UNSET:
            field_dict["Applicant_TC"] = applicant_tc
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if last_update is not UNSET:
            field_dict["LastUpdate"] = last_update

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

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("AddressEN", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("AddressTC", UNSET))

        def _parse_year_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year_en = _parse_year_en(d.pop("Year_EN", UNSET))

        def _parse_year_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year_tc = _parse_year_tc(d.pop("Year_TC", UNSET))

        def _parse_month_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        month_en = _parse_month_en(d.pop("Month_EN", UNSET))

        def _parse_month_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        month_tc = _parse_month_tc(d.pop("Month_TC", UNSET))

        def _parse_region_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_en = _parse_region_en(d.pop("Region_EN", UNSET))

        def _parse_region_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_tc = _parse_region_tc(d.pop("Region_TC", UNSET))

        def _parse_no_of_blocks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_blocks_en = _parse_no_of_blocks_en(d.pop("No_of_Blocks_EN", UNSET))

        def _parse_no_of_blocks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_blocks_tc = _parse_no_of_blocks_tc(d.pop("No_of_Blocks_TC", UNSET))

        def _parse_building_type_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_type_en = _parse_building_type_en(d.pop("Building_Type_EN", UNSET))

        def _parse_building_type_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_type_tc = _parse_building_type_tc(d.pop("Building_Type_TC", UNSET))

        def _parse_domestic_gfa_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domestic_gfa_en = _parse_domestic_gfa_en(d.pop("Domestic_GFA_EN", UNSET))

        def _parse_domestic_gfa_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domestic_gfa_tc = _parse_domestic_gfa_tc(d.pop("Domestic_GFA_TC", UNSET))

        def _parse_non_domestic_gfa_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        non_domestic_gfa_en = _parse_non_domestic_gfa_en(
            d.pop("NonDomestic_GFA_EN", UNSET)
        )

        def _parse_non_domestic_gfa_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        non_domestic_gfa_tc = _parse_non_domestic_gfa_tc(
            d.pop("NonDomestic_GFA_TC", UNSET)
        )

        def _parse_authorized_person_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        authorized_person_en = _parse_authorized_person_en(
            d.pop("Authorized_Person_EN", UNSET)
        )

        def _parse_authorized_person_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        authorized_person_tc = _parse_authorized_person_tc(
            d.pop("Authorized_Person_TC", UNSET)
        )

        def _parse_reg_structural_engineer_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reg_structural_engineer_en = _parse_reg_structural_engineer_en(
            d.pop("Reg_Structural_Engineer_EN", UNSET)
        )

        def _parse_reg_structural_engineer_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reg_structural_engineer_tc = _parse_reg_structural_engineer_tc(
            d.pop("Reg_Structural_Engineer_TC", UNSET)
        )

        def _parse_applicant_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        applicant_en = _parse_applicant_en(d.pop("Applicant_EN", UNSET))

        def _parse_applicant_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        applicant_tc = _parse_applicant_tc(d.pop("Applicant_TC", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("Easting", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        last_update = d.pop("LastUpdate", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            dataset_en=dataset_en,
            dataset_tc=dataset_tc,
            address_en=address_en,
            address_tc=address_tc,
            year_en=year_en,
            year_tc=year_tc,
            month_en=month_en,
            month_tc=month_tc,
            region_en=region_en,
            region_tc=region_tc,
            no_of_blocks_en=no_of_blocks_en,
            no_of_blocks_tc=no_of_blocks_tc,
            building_type_en=building_type_en,
            building_type_tc=building_type_tc,
            domestic_gfa_en=domestic_gfa_en,
            domestic_gfa_tc=domestic_gfa_tc,
            non_domestic_gfa_en=non_domestic_gfa_en,
            non_domestic_gfa_tc=non_domestic_gfa_tc,
            authorized_person_en=authorized_person_en,
            authorized_person_tc=authorized_person_tc,
            reg_structural_engineer_en=reg_structural_engineer_en,
            reg_structural_engineer_tc=reg_structural_engineer_tc,
            applicant_en=applicant_en,
            applicant_tc=applicant_tc,
            northing=northing,
            easting=easting,
            latitude=latitude,
            longitude=longitude,
            last_update=last_update,
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
