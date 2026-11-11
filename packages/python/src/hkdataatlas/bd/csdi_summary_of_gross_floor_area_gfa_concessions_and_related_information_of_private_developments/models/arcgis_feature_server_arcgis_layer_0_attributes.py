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
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        permit_no_en (None | str | Unset): Publisher field type: esriFieldTypeString
        permit_no_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        date_of_occupation_permit_en (None | str | Unset): Publisher field type: esriFieldTypeString
        date_of_occupation_permit_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        building_type_en (None | str | Unset): Publisher field type: esriFieldTypeString
        building_type_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        use_of_building_en (None | str | Unset): Publisher field type: esriFieldTypeString
        use_of_building_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        summary_of_gfa_concessions_en (None | str | Unset): Publisher field type: esriFieldTypeString
        summary_of_gfa_concessions_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        greenery_area_en (None | str | Unset): Publisher field type: esriFieldTypeString
        greenery_area_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        est_energy_perform_consump_en (None | str | Unset): Publisher field type: esriFieldTypeString
        est_energy_perform_consump_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        beam_plus_assessment_result_en (None | str | Unset): Publisher field type: esriFieldTypeString
        beam_plus_assessment_result_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        rttv_en (None | str | Unset): Publisher field type: esriFieldTypeString
        rttv_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        ottv_resident_recreat_faci_en (None | str | Unset): Publisher field type: esriFieldTypeString
        ottv_resident_recreat_faci_tc (None | str | Unset): Publisher field type: esriFieldTypeString
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
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    permit_no_en: None | str | Unset = UNSET
    permit_no_tc: None | str | Unset = UNSET
    date_of_occupation_permit_en: None | str | Unset = UNSET
    date_of_occupation_permit_tc: None | str | Unset = UNSET
    building_type_en: None | str | Unset = UNSET
    building_type_tc: None | str | Unset = UNSET
    use_of_building_en: None | str | Unset = UNSET
    use_of_building_tc: None | str | Unset = UNSET
    summary_of_gfa_concessions_en: None | str | Unset = UNSET
    summary_of_gfa_concessions_tc: None | str | Unset = UNSET
    greenery_area_en: None | str | Unset = UNSET
    greenery_area_tc: None | str | Unset = UNSET
    est_energy_perform_consump_en: None | str | Unset = UNSET
    est_energy_perform_consump_tc: None | str | Unset = UNSET
    beam_plus_assessment_result_en: None | str | Unset = UNSET
    beam_plus_assessment_result_tc: None | str | Unset = UNSET
    rttv_en: None | str | Unset = UNSET
    rttv_tc: None | str | Unset = UNSET
    ottv_resident_recreat_faci_en: None | str | Unset = UNSET
    ottv_resident_recreat_faci_tc: None | str | Unset = UNSET
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

        permit_no_en: None | str | Unset
        if isinstance(self.permit_no_en, Unset):
            permit_no_en = UNSET
        else:
            permit_no_en = self.permit_no_en

        permit_no_tc: None | str | Unset
        if isinstance(self.permit_no_tc, Unset):
            permit_no_tc = UNSET
        else:
            permit_no_tc = self.permit_no_tc

        date_of_occupation_permit_en: None | str | Unset
        if isinstance(self.date_of_occupation_permit_en, Unset):
            date_of_occupation_permit_en = UNSET
        else:
            date_of_occupation_permit_en = self.date_of_occupation_permit_en

        date_of_occupation_permit_tc: None | str | Unset
        if isinstance(self.date_of_occupation_permit_tc, Unset):
            date_of_occupation_permit_tc = UNSET
        else:
            date_of_occupation_permit_tc = self.date_of_occupation_permit_tc

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

        use_of_building_en: None | str | Unset
        if isinstance(self.use_of_building_en, Unset):
            use_of_building_en = UNSET
        else:
            use_of_building_en = self.use_of_building_en

        use_of_building_tc: None | str | Unset
        if isinstance(self.use_of_building_tc, Unset):
            use_of_building_tc = UNSET
        else:
            use_of_building_tc = self.use_of_building_tc

        summary_of_gfa_concessions_en: None | str | Unset
        if isinstance(self.summary_of_gfa_concessions_en, Unset):
            summary_of_gfa_concessions_en = UNSET
        else:
            summary_of_gfa_concessions_en = self.summary_of_gfa_concessions_en

        summary_of_gfa_concessions_tc: None | str | Unset
        if isinstance(self.summary_of_gfa_concessions_tc, Unset):
            summary_of_gfa_concessions_tc = UNSET
        else:
            summary_of_gfa_concessions_tc = self.summary_of_gfa_concessions_tc

        greenery_area_en: None | str | Unset
        if isinstance(self.greenery_area_en, Unset):
            greenery_area_en = UNSET
        else:
            greenery_area_en = self.greenery_area_en

        greenery_area_tc: None | str | Unset
        if isinstance(self.greenery_area_tc, Unset):
            greenery_area_tc = UNSET
        else:
            greenery_area_tc = self.greenery_area_tc

        est_energy_perform_consump_en: None | str | Unset
        if isinstance(self.est_energy_perform_consump_en, Unset):
            est_energy_perform_consump_en = UNSET
        else:
            est_energy_perform_consump_en = self.est_energy_perform_consump_en

        est_energy_perform_consump_tc: None | str | Unset
        if isinstance(self.est_energy_perform_consump_tc, Unset):
            est_energy_perform_consump_tc = UNSET
        else:
            est_energy_perform_consump_tc = self.est_energy_perform_consump_tc

        beam_plus_assessment_result_en: None | str | Unset
        if isinstance(self.beam_plus_assessment_result_en, Unset):
            beam_plus_assessment_result_en = UNSET
        else:
            beam_plus_assessment_result_en = self.beam_plus_assessment_result_en

        beam_plus_assessment_result_tc: None | str | Unset
        if isinstance(self.beam_plus_assessment_result_tc, Unset):
            beam_plus_assessment_result_tc = UNSET
        else:
            beam_plus_assessment_result_tc = self.beam_plus_assessment_result_tc

        rttv_en: None | str | Unset
        if isinstance(self.rttv_en, Unset):
            rttv_en = UNSET
        else:
            rttv_en = self.rttv_en

        rttv_tc: None | str | Unset
        if isinstance(self.rttv_tc, Unset):
            rttv_tc = UNSET
        else:
            rttv_tc = self.rttv_tc

        ottv_resident_recreat_faci_en: None | str | Unset
        if isinstance(self.ottv_resident_recreat_faci_en, Unset):
            ottv_resident_recreat_faci_en = UNSET
        else:
            ottv_resident_recreat_faci_en = self.ottv_resident_recreat_faci_en

        ottv_resident_recreat_faci_tc: None | str | Unset
        if isinstance(self.ottv_resident_recreat_faci_tc, Unset):
            ottv_resident_recreat_faci_tc = UNSET
        else:
            ottv_resident_recreat_faci_tc = self.ottv_resident_recreat_faci_tc

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
        if district_en is not UNSET:
            field_dict["District_EN"] = district_en
        if district_tc is not UNSET:
            field_dict["District_TC"] = district_tc
        if permit_no_en is not UNSET:
            field_dict["Permit_No_EN"] = permit_no_en
        if permit_no_tc is not UNSET:
            field_dict["Permit_No_TC"] = permit_no_tc
        if date_of_occupation_permit_en is not UNSET:
            field_dict["Date_of_Occupation_Permit_EN"] = date_of_occupation_permit_en
        if date_of_occupation_permit_tc is not UNSET:
            field_dict["Date_of_Occupation_Permit_TC"] = date_of_occupation_permit_tc
        if building_type_en is not UNSET:
            field_dict["Building_Type_EN"] = building_type_en
        if building_type_tc is not UNSET:
            field_dict["Building_Type_TC"] = building_type_tc
        if use_of_building_en is not UNSET:
            field_dict["Use_of_Building_EN"] = use_of_building_en
        if use_of_building_tc is not UNSET:
            field_dict["Use_of_Building_TC"] = use_of_building_tc
        if summary_of_gfa_concessions_en is not UNSET:
            field_dict["Summary_of_GFA_Concessions_EN"] = summary_of_gfa_concessions_en
        if summary_of_gfa_concessions_tc is not UNSET:
            field_dict["Summary_of_GFA_Concessions_TC"] = summary_of_gfa_concessions_tc
        if greenery_area_en is not UNSET:
            field_dict["Greenery_Area_EN"] = greenery_area_en
        if greenery_area_tc is not UNSET:
            field_dict["Greenery_Area_TC"] = greenery_area_tc
        if est_energy_perform_consump_en is not UNSET:
            field_dict["Est_Energy_Perform_consump_EN"] = est_energy_perform_consump_en
        if est_energy_perform_consump_tc is not UNSET:
            field_dict["Est_Energy_Perform_consump_TC"] = est_energy_perform_consump_tc
        if beam_plus_assessment_result_en is not UNSET:
            field_dict["BEAM_Plus_Assessment_Result_EN"] = (
                beam_plus_assessment_result_en
            )
        if beam_plus_assessment_result_tc is not UNSET:
            field_dict["BEAM_Plus_Assessment_Result_TC"] = (
                beam_plus_assessment_result_tc
            )
        if rttv_en is not UNSET:
            field_dict["RTTV_EN"] = rttv_en
        if rttv_tc is not UNSET:
            field_dict["RTTV_TC"] = rttv_tc
        if ottv_resident_recreat_faci_en is not UNSET:
            field_dict["OTTV_Resident_Recreat_Faci_EN"] = ottv_resident_recreat_faci_en
        if ottv_resident_recreat_faci_tc is not UNSET:
            field_dict["OTTV_Resident_Recreat_Faci_TC"] = ottv_resident_recreat_faci_tc
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

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("District_EN", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("District_TC", UNSET))

        def _parse_permit_no_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        permit_no_en = _parse_permit_no_en(d.pop("Permit_No_EN", UNSET))

        def _parse_permit_no_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        permit_no_tc = _parse_permit_no_tc(d.pop("Permit_No_TC", UNSET))

        def _parse_date_of_occupation_permit_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_of_occupation_permit_en = _parse_date_of_occupation_permit_en(
            d.pop("Date_of_Occupation_Permit_EN", UNSET)
        )

        def _parse_date_of_occupation_permit_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_of_occupation_permit_tc = _parse_date_of_occupation_permit_tc(
            d.pop("Date_of_Occupation_Permit_TC", UNSET)
        )

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

        def _parse_use_of_building_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        use_of_building_en = _parse_use_of_building_en(
            d.pop("Use_of_Building_EN", UNSET)
        )

        def _parse_use_of_building_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        use_of_building_tc = _parse_use_of_building_tc(
            d.pop("Use_of_Building_TC", UNSET)
        )

        def _parse_summary_of_gfa_concessions_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary_of_gfa_concessions_en = _parse_summary_of_gfa_concessions_en(
            d.pop("Summary_of_GFA_Concessions_EN", UNSET)
        )

        def _parse_summary_of_gfa_concessions_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary_of_gfa_concessions_tc = _parse_summary_of_gfa_concessions_tc(
            d.pop("Summary_of_GFA_Concessions_TC", UNSET)
        )

        def _parse_greenery_area_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        greenery_area_en = _parse_greenery_area_en(d.pop("Greenery_Area_EN", UNSET))

        def _parse_greenery_area_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        greenery_area_tc = _parse_greenery_area_tc(d.pop("Greenery_Area_TC", UNSET))

        def _parse_est_energy_perform_consump_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_energy_perform_consump_en = _parse_est_energy_perform_consump_en(
            d.pop("Est_Energy_Perform_consump_EN", UNSET)
        )

        def _parse_est_energy_perform_consump_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_energy_perform_consump_tc = _parse_est_energy_perform_consump_tc(
            d.pop("Est_Energy_Perform_consump_TC", UNSET)
        )

        def _parse_beam_plus_assessment_result_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beam_plus_assessment_result_en = _parse_beam_plus_assessment_result_en(
            d.pop("BEAM_Plus_Assessment_Result_EN", UNSET)
        )

        def _parse_beam_plus_assessment_result_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beam_plus_assessment_result_tc = _parse_beam_plus_assessment_result_tc(
            d.pop("BEAM_Plus_Assessment_Result_TC", UNSET)
        )

        def _parse_rttv_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rttv_en = _parse_rttv_en(d.pop("RTTV_EN", UNSET))

        def _parse_rttv_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rttv_tc = _parse_rttv_tc(d.pop("RTTV_TC", UNSET))

        def _parse_ottv_resident_recreat_faci_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ottv_resident_recreat_faci_en = _parse_ottv_resident_recreat_faci_en(
            d.pop("OTTV_Resident_Recreat_Faci_EN", UNSET)
        )

        def _parse_ottv_resident_recreat_faci_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ottv_resident_recreat_faci_tc = _parse_ottv_resident_recreat_faci_tc(
            d.pop("OTTV_Resident_Recreat_Faci_TC", UNSET)
        )

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
            district_en=district_en,
            district_tc=district_tc,
            permit_no_en=permit_no_en,
            permit_no_tc=permit_no_tc,
            date_of_occupation_permit_en=date_of_occupation_permit_en,
            date_of_occupation_permit_tc=date_of_occupation_permit_tc,
            building_type_en=building_type_en,
            building_type_tc=building_type_tc,
            use_of_building_en=use_of_building_en,
            use_of_building_tc=use_of_building_tc,
            summary_of_gfa_concessions_en=summary_of_gfa_concessions_en,
            summary_of_gfa_concessions_tc=summary_of_gfa_concessions_tc,
            greenery_area_en=greenery_area_en,
            greenery_area_tc=greenery_area_tc,
            est_energy_perform_consump_en=est_energy_perform_consump_en,
            est_energy_perform_consump_tc=est_energy_perform_consump_tc,
            beam_plus_assessment_result_en=beam_plus_assessment_result_en,
            beam_plus_assessment_result_tc=beam_plus_assessment_result_tc,
            rttv_en=rttv_en,
            rttv_tc=rttv_tc,
            ottv_resident_recreat_faci_en=ottv_resident_recreat_faci_en,
            ottv_resident_recreat_faci_tc=ottv_resident_recreat_faci_tc,
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
