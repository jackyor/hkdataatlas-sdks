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
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        building_usage_en (None | str | Unset): Publisher field type: esriFieldTypeString
        building_usage_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        lot_number_en (None | str | Unset): Publisher field type: esriFieldTypeString
        lot_number_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        ba14a_ba14b_acknowledge_month_en (None | str | Unset): Publisher field type: esriFieldTypeString
        ba14a_ba14b_acknowledge_month_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        occupation_permit_no_en (None | str | Unset): Publisher field type: esriFieldTypeString
        occupation_permit_no_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        csuid_en (None | str | Unset): Publisher field type: esriFieldTypeString
        csuid_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        last_update (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
    """

    objectid: int | Unset = UNSET
    dataset_en: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    building_usage_en: None | str | Unset = UNSET
    building_usage_tc: None | str | Unset = UNSET
    lot_number_en: None | str | Unset = UNSET
    lot_number_tc: None | str | Unset = UNSET
    ba14a_ba14b_acknowledge_month_en: None | str | Unset = UNSET
    ba14a_ba14b_acknowledge_month_tc: None | str | Unset = UNSET
    occupation_permit_no_en: None | str | Unset = UNSET
    occupation_permit_no_tc: None | str | Unset = UNSET
    csuid_en: None | str | Unset = UNSET
    csuid_tc: None | str | Unset = UNSET
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

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

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

        building_usage_en: None | str | Unset
        if isinstance(self.building_usage_en, Unset):
            building_usage_en = UNSET
        else:
            building_usage_en = self.building_usage_en

        building_usage_tc: None | str | Unset
        if isinstance(self.building_usage_tc, Unset):
            building_usage_tc = UNSET
        else:
            building_usage_tc = self.building_usage_tc

        lot_number_en: None | str | Unset
        if isinstance(self.lot_number_en, Unset):
            lot_number_en = UNSET
        else:
            lot_number_en = self.lot_number_en

        lot_number_tc: None | str | Unset
        if isinstance(self.lot_number_tc, Unset):
            lot_number_tc = UNSET
        else:
            lot_number_tc = self.lot_number_tc

        ba14a_ba14b_acknowledge_month_en: None | str | Unset
        if isinstance(self.ba14a_ba14b_acknowledge_month_en, Unset):
            ba14a_ba14b_acknowledge_month_en = UNSET
        else:
            ba14a_ba14b_acknowledge_month_en = self.ba14a_ba14b_acknowledge_month_en

        ba14a_ba14b_acknowledge_month_tc: None | str | Unset
        if isinstance(self.ba14a_ba14b_acknowledge_month_tc, Unset):
            ba14a_ba14b_acknowledge_month_tc = UNSET
        else:
            ba14a_ba14b_acknowledge_month_tc = self.ba14a_ba14b_acknowledge_month_tc

        occupation_permit_no_en: None | str | Unset
        if isinstance(self.occupation_permit_no_en, Unset):
            occupation_permit_no_en = UNSET
        else:
            occupation_permit_no_en = self.occupation_permit_no_en

        occupation_permit_no_tc: None | str | Unset
        if isinstance(self.occupation_permit_no_tc, Unset):
            occupation_permit_no_tc = UNSET
        else:
            occupation_permit_no_tc = self.occupation_permit_no_tc

        csuid_en: None | str | Unset
        if isinstance(self.csuid_en, Unset):
            csuid_en = UNSET
        else:
            csuid_en = self.csuid_en

        csuid_tc: None | str | Unset
        if isinstance(self.csuid_tc, Unset):
            csuid_tc = UNSET
        else:
            csuid_tc = self.csuid_tc

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
        if name_en is not UNSET:
            field_dict["NameEN"] = name_en
        if address_en is not UNSET:
            field_dict["AddressEN"] = address_en
        if name_tc is not UNSET:
            field_dict["NameTC"] = name_tc
        if address_tc is not UNSET:
            field_dict["AddressTC"] = address_tc
        if district_en is not UNSET:
            field_dict["DistrictEN"] = district_en
        if district_tc is not UNSET:
            field_dict["DistrictTC"] = district_tc
        if building_usage_en is not UNSET:
            field_dict["Building_UsageEN"] = building_usage_en
        if building_usage_tc is not UNSET:
            field_dict["Building_UsageTC"] = building_usage_tc
        if lot_number_en is not UNSET:
            field_dict["Lot_NumberEN"] = lot_number_en
        if lot_number_tc is not UNSET:
            field_dict["Lot_NumberTC"] = lot_number_tc
        if ba14a_ba14b_acknowledge_month_en is not UNSET:
            field_dict["BA14A_BA14B_acknowledge_MonthEN"] = (
                ba14a_ba14b_acknowledge_month_en
            )
        if ba14a_ba14b_acknowledge_month_tc is not UNSET:
            field_dict["BA14A_BA14B_acknowledge_MonthTC"] = (
                ba14a_ba14b_acknowledge_month_tc
            )
        if occupation_permit_no_en is not UNSET:
            field_dict["Occupation_Permit_NoEN"] = occupation_permit_no_en
        if occupation_permit_no_tc is not UNSET:
            field_dict["Occupation_Permit_NoTC"] = occupation_permit_no_tc
        if csuid_en is not UNSET:
            field_dict["CSUID_EN"] = csuid_en
        if csuid_tc is not UNSET:
            field_dict["CSUID_TC"] = csuid_tc
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

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("NameEN", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("AddressEN", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("NameTC", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("AddressTC", UNSET))

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

        def _parse_building_usage_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_usage_en = _parse_building_usage_en(d.pop("Building_UsageEN", UNSET))

        def _parse_building_usage_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_usage_tc = _parse_building_usage_tc(d.pop("Building_UsageTC", UNSET))

        def _parse_lot_number_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lot_number_en = _parse_lot_number_en(d.pop("Lot_NumberEN", UNSET))

        def _parse_lot_number_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lot_number_tc = _parse_lot_number_tc(d.pop("Lot_NumberTC", UNSET))

        def _parse_ba14a_ba14b_acknowledge_month_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba14a_ba14b_acknowledge_month_en = _parse_ba14a_ba14b_acknowledge_month_en(
            d.pop("BA14A_BA14B_acknowledge_MonthEN", UNSET)
        )

        def _parse_ba14a_ba14b_acknowledge_month_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba14a_ba14b_acknowledge_month_tc = _parse_ba14a_ba14b_acknowledge_month_tc(
            d.pop("BA14A_BA14B_acknowledge_MonthTC", UNSET)
        )

        def _parse_occupation_permit_no_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        occupation_permit_no_en = _parse_occupation_permit_no_en(
            d.pop("Occupation_Permit_NoEN", UNSET)
        )

        def _parse_occupation_permit_no_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        occupation_permit_no_tc = _parse_occupation_permit_no_tc(
            d.pop("Occupation_Permit_NoTC", UNSET)
        )

        def _parse_csuid_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        csuid_en = _parse_csuid_en(d.pop("CSUID_EN", UNSET))

        def _parse_csuid_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        csuid_tc = _parse_csuid_tc(d.pop("CSUID_TC", UNSET))

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
            name_en=name_en,
            address_en=address_en,
            name_tc=name_tc,
            address_tc=address_tc,
            district_en=district_en,
            district_tc=district_tc,
            building_usage_en=building_usage_en,
            building_usage_tc=building_usage_tc,
            lot_number_en=lot_number_en,
            lot_number_tc=lot_number_tc,
            ba14a_ba14b_acknowledge_month_en=ba14a_ba14b_acknowledge_month_en,
            ba14a_ba14b_acknowledge_month_tc=ba14a_ba14b_acknowledge_month_tc,
            occupation_permit_no_en=occupation_permit_no_en,
            occupation_permit_no_tc=occupation_permit_no_tc,
            csuid_en=csuid_en,
            csuid_tc=csuid_tc,
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
