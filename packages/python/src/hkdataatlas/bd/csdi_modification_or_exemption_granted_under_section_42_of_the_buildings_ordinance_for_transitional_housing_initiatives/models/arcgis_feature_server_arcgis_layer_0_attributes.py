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
        permit_no_en (None | str | Unset): Publisher field type: esriFieldTypeString
        permit_no_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        issue_date_of_the_permit_en (None | str | Unset): Publisher field type: esriFieldTypeString
        issue_date_of_the_permit_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        bd_ref_no_minor_works_sub_no_en (None | str | Unset): Publisher field type: esriFieldTypeString
        bd_ref_no_minor_works_sub_no_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        permit_undertaking_mgmtplan_en (None | str | Unset): Publisher field type: esriFieldTypeString
        permit_undertaking_mgmtplan_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        annual_inspection_report_en (None | str | Unset): Publisher field type: esriFieldTypeString
        annual_inspection_report_tc (None | str | Unset): Publisher field type: esriFieldTypeString
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
    permit_no_en: None | str | Unset = UNSET
    permit_no_tc: None | str | Unset = UNSET
    issue_date_of_the_permit_en: None | str | Unset = UNSET
    issue_date_of_the_permit_tc: None | str | Unset = UNSET
    bd_ref_no_minor_works_sub_no_en: None | str | Unset = UNSET
    bd_ref_no_minor_works_sub_no_tc: None | str | Unset = UNSET
    permit_undertaking_mgmtplan_en: None | str | Unset = UNSET
    permit_undertaking_mgmtplan_tc: None | str | Unset = UNSET
    annual_inspection_report_en: None | str | Unset = UNSET
    annual_inspection_report_tc: None | str | Unset = UNSET
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

        issue_date_of_the_permit_en: None | str | Unset
        if isinstance(self.issue_date_of_the_permit_en, Unset):
            issue_date_of_the_permit_en = UNSET
        else:
            issue_date_of_the_permit_en = self.issue_date_of_the_permit_en

        issue_date_of_the_permit_tc: None | str | Unset
        if isinstance(self.issue_date_of_the_permit_tc, Unset):
            issue_date_of_the_permit_tc = UNSET
        else:
            issue_date_of_the_permit_tc = self.issue_date_of_the_permit_tc

        bd_ref_no_minor_works_sub_no_en: None | str | Unset
        if isinstance(self.bd_ref_no_minor_works_sub_no_en, Unset):
            bd_ref_no_minor_works_sub_no_en = UNSET
        else:
            bd_ref_no_minor_works_sub_no_en = self.bd_ref_no_minor_works_sub_no_en

        bd_ref_no_minor_works_sub_no_tc: None | str | Unset
        if isinstance(self.bd_ref_no_minor_works_sub_no_tc, Unset):
            bd_ref_no_minor_works_sub_no_tc = UNSET
        else:
            bd_ref_no_minor_works_sub_no_tc = self.bd_ref_no_minor_works_sub_no_tc

        permit_undertaking_mgmtplan_en: None | str | Unset
        if isinstance(self.permit_undertaking_mgmtplan_en, Unset):
            permit_undertaking_mgmtplan_en = UNSET
        else:
            permit_undertaking_mgmtplan_en = self.permit_undertaking_mgmtplan_en

        permit_undertaking_mgmtplan_tc: None | str | Unset
        if isinstance(self.permit_undertaking_mgmtplan_tc, Unset):
            permit_undertaking_mgmtplan_tc = UNSET
        else:
            permit_undertaking_mgmtplan_tc = self.permit_undertaking_mgmtplan_tc

        annual_inspection_report_en: None | str | Unset
        if isinstance(self.annual_inspection_report_en, Unset):
            annual_inspection_report_en = UNSET
        else:
            annual_inspection_report_en = self.annual_inspection_report_en

        annual_inspection_report_tc: None | str | Unset
        if isinstance(self.annual_inspection_report_tc, Unset):
            annual_inspection_report_tc = UNSET
        else:
            annual_inspection_report_tc = self.annual_inspection_report_tc

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
        if permit_no_en is not UNSET:
            field_dict["PermitNo_EN"] = permit_no_en
        if permit_no_tc is not UNSET:
            field_dict["PermitNo_TC"] = permit_no_tc
        if issue_date_of_the_permit_en is not UNSET:
            field_dict["IssueDateOfThePermit_EN"] = issue_date_of_the_permit_en
        if issue_date_of_the_permit_tc is not UNSET:
            field_dict["IssueDateOfThePermit_TC"] = issue_date_of_the_permit_tc
        if bd_ref_no_minor_works_sub_no_en is not UNSET:
            field_dict["BDRefNo_MinorWorksSubNo_EN"] = bd_ref_no_minor_works_sub_no_en
        if bd_ref_no_minor_works_sub_no_tc is not UNSET:
            field_dict["BDRefNo_MinorWorksSubNo_TC"] = bd_ref_no_minor_works_sub_no_tc
        if permit_undertaking_mgmtplan_en is not UNSET:
            field_dict["Permit_undertaking_mgmtplan_EN"] = (
                permit_undertaking_mgmtplan_en
            )
        if permit_undertaking_mgmtplan_tc is not UNSET:
            field_dict["Permit_undertaking_mgmtplan_TC"] = (
                permit_undertaking_mgmtplan_tc
            )
        if annual_inspection_report_en is not UNSET:
            field_dict["Annual_Inspection_Report_EN"] = annual_inspection_report_en
        if annual_inspection_report_tc is not UNSET:
            field_dict["Annual_Inspection_Report_TC"] = annual_inspection_report_tc
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

        def _parse_permit_no_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        permit_no_en = _parse_permit_no_en(d.pop("PermitNo_EN", UNSET))

        def _parse_permit_no_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        permit_no_tc = _parse_permit_no_tc(d.pop("PermitNo_TC", UNSET))

        def _parse_issue_date_of_the_permit_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issue_date_of_the_permit_en = _parse_issue_date_of_the_permit_en(
            d.pop("IssueDateOfThePermit_EN", UNSET)
        )

        def _parse_issue_date_of_the_permit_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issue_date_of_the_permit_tc = _parse_issue_date_of_the_permit_tc(
            d.pop("IssueDateOfThePermit_TC", UNSET)
        )

        def _parse_bd_ref_no_minor_works_sub_no_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bd_ref_no_minor_works_sub_no_en = _parse_bd_ref_no_minor_works_sub_no_en(
            d.pop("BDRefNo_MinorWorksSubNo_EN", UNSET)
        )

        def _parse_bd_ref_no_minor_works_sub_no_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bd_ref_no_minor_works_sub_no_tc = _parse_bd_ref_no_minor_works_sub_no_tc(
            d.pop("BDRefNo_MinorWorksSubNo_TC", UNSET)
        )

        def _parse_permit_undertaking_mgmtplan_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        permit_undertaking_mgmtplan_en = _parse_permit_undertaking_mgmtplan_en(
            d.pop("Permit_undertaking_mgmtplan_EN", UNSET)
        )

        def _parse_permit_undertaking_mgmtplan_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        permit_undertaking_mgmtplan_tc = _parse_permit_undertaking_mgmtplan_tc(
            d.pop("Permit_undertaking_mgmtplan_TC", UNSET)
        )

        def _parse_annual_inspection_report_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        annual_inspection_report_en = _parse_annual_inspection_report_en(
            d.pop("Annual_Inspection_Report_EN", UNSET)
        )

        def _parse_annual_inspection_report_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        annual_inspection_report_tc = _parse_annual_inspection_report_tc(
            d.pop("Annual_Inspection_Report_TC", UNSET)
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
            name_en=name_en,
            address_en=address_en,
            name_tc=name_tc,
            address_tc=address_tc,
            permit_no_en=permit_no_en,
            permit_no_tc=permit_no_tc,
            issue_date_of_the_permit_en=issue_date_of_the_permit_en,
            issue_date_of_the_permit_tc=issue_date_of_the_permit_tc,
            bd_ref_no_minor_works_sub_no_en=bd_ref_no_minor_works_sub_no_en,
            bd_ref_no_minor_works_sub_no_tc=bd_ref_no_minor_works_sub_no_tc,
            permit_undertaking_mgmtplan_en=permit_undertaking_mgmtplan_en,
            permit_undertaking_mgmtplan_tc=permit_undertaking_mgmtplan_tc,
            annual_inspection_report_en=annual_inspection_report_en,
            annual_inspection_report_tc=annual_inspection_report_tc,
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
