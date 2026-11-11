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
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        en_address (None | str | Unset): Publisher field type: esriFieldTypeString
        en_company_name (None | str | Unset): Publisher field type: esriFieldTypeString
        en_licence_no (float | None | Unset): Publisher field type: esriFieldTypeDouble
        en_region (None | str | Unset): Publisher field type: esriFieldTypeString
        en_tel_no (float | None | Unset): Publisher field type: esriFieldTypeDouble
        en_type_of_warehouse (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_address (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_company_name (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_licence_no (float | None | Unset): Publisher field type: esriFieldTypeDouble
        sc_region (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_tel_no (float | None | Unset): Publisher field type: esriFieldTypeDouble
        sc_type_of_warehouse (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_address (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_company_name (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_licence_no (float | None | Unset): Publisher field type: esriFieldTypeDouble
        tc_region (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_tel_no (float | None | Unset): Publisher field type: esriFieldTypeDouble
        tc_type_of_warehouse (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    en_address: None | str | Unset = UNSET
    en_company_name: None | str | Unset = UNSET
    en_licence_no: float | None | Unset = UNSET
    en_region: None | str | Unset = UNSET
    en_tel_no: float | None | Unset = UNSET
    en_type_of_warehouse: None | str | Unset = UNSET
    sc_address: None | str | Unset = UNSET
    sc_company_name: None | str | Unset = UNSET
    sc_licence_no: float | None | Unset = UNSET
    sc_region: None | str | Unset = UNSET
    sc_tel_no: float | None | Unset = UNSET
    sc_type_of_warehouse: None | str | Unset = UNSET
    tc_address: None | str | Unset = UNSET
    tc_company_name: None | str | Unset = UNSET
    tc_licence_no: float | None | Unset = UNSET
    tc_region: None | str | Unset = UNSET
    tc_tel_no: float | None | Unset = UNSET
    tc_type_of_warehouse: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        en_address: None | str | Unset
        if isinstance(self.en_address, Unset):
            en_address = UNSET
        else:
            en_address = self.en_address

        en_company_name: None | str | Unset
        if isinstance(self.en_company_name, Unset):
            en_company_name = UNSET
        else:
            en_company_name = self.en_company_name

        en_licence_no: float | None | Unset
        if isinstance(self.en_licence_no, Unset):
            en_licence_no = UNSET
        else:
            en_licence_no = self.en_licence_no

        en_region: None | str | Unset
        if isinstance(self.en_region, Unset):
            en_region = UNSET
        else:
            en_region = self.en_region

        en_tel_no: float | None | Unset
        if isinstance(self.en_tel_no, Unset):
            en_tel_no = UNSET
        else:
            en_tel_no = self.en_tel_no

        en_type_of_warehouse: None | str | Unset
        if isinstance(self.en_type_of_warehouse, Unset):
            en_type_of_warehouse = UNSET
        else:
            en_type_of_warehouse = self.en_type_of_warehouse

        sc_address: None | str | Unset
        if isinstance(self.sc_address, Unset):
            sc_address = UNSET
        else:
            sc_address = self.sc_address

        sc_company_name: None | str | Unset
        if isinstance(self.sc_company_name, Unset):
            sc_company_name = UNSET
        else:
            sc_company_name = self.sc_company_name

        sc_licence_no: float | None | Unset
        if isinstance(self.sc_licence_no, Unset):
            sc_licence_no = UNSET
        else:
            sc_licence_no = self.sc_licence_no

        sc_region: None | str | Unset
        if isinstance(self.sc_region, Unset):
            sc_region = UNSET
        else:
            sc_region = self.sc_region

        sc_tel_no: float | None | Unset
        if isinstance(self.sc_tel_no, Unset):
            sc_tel_no = UNSET
        else:
            sc_tel_no = self.sc_tel_no

        sc_type_of_warehouse: None | str | Unset
        if isinstance(self.sc_type_of_warehouse, Unset):
            sc_type_of_warehouse = UNSET
        else:
            sc_type_of_warehouse = self.sc_type_of_warehouse

        tc_address: None | str | Unset
        if isinstance(self.tc_address, Unset):
            tc_address = UNSET
        else:
            tc_address = self.tc_address

        tc_company_name: None | str | Unset
        if isinstance(self.tc_company_name, Unset):
            tc_company_name = UNSET
        else:
            tc_company_name = self.tc_company_name

        tc_licence_no: float | None | Unset
        if isinstance(self.tc_licence_no, Unset):
            tc_licence_no = UNSET
        else:
            tc_licence_no = self.tc_licence_no

        tc_region: None | str | Unset
        if isinstance(self.tc_region, Unset):
            tc_region = UNSET
        else:
            tc_region = self.tc_region

        tc_tel_no: float | None | Unset
        if isinstance(self.tc_tel_no, Unset):
            tc_tel_no = UNSET
        else:
            tc_tel_no = self.tc_tel_no

        tc_type_of_warehouse: None | str | Unset
        if isinstance(self.tc_type_of_warehouse, Unset):
            tc_type_of_warehouse = UNSET
        else:
            tc_type_of_warehouse = self.tc_type_of_warehouse

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if en_address is not UNSET:
            field_dict["en_address"] = en_address
        if en_company_name is not UNSET:
            field_dict["en_company_name"] = en_company_name
        if en_licence_no is not UNSET:
            field_dict["en_licence_no_"] = en_licence_no
        if en_region is not UNSET:
            field_dict["en_region"] = en_region
        if en_tel_no is not UNSET:
            field_dict["en_tel_no"] = en_tel_no
        if en_type_of_warehouse is not UNSET:
            field_dict["en_type_of_warehouse"] = en_type_of_warehouse
        if sc_address is not UNSET:
            field_dict["sc_address"] = sc_address
        if sc_company_name is not UNSET:
            field_dict["sc_company_name"] = sc_company_name
        if sc_licence_no is not UNSET:
            field_dict["sc_licence_no_"] = sc_licence_no
        if sc_region is not UNSET:
            field_dict["sc_region"] = sc_region
        if sc_tel_no is not UNSET:
            field_dict["sc_tel_no"] = sc_tel_no
        if sc_type_of_warehouse is not UNSET:
            field_dict["sc_type_of_warehouse"] = sc_type_of_warehouse
        if tc_address is not UNSET:
            field_dict["tc_address"] = tc_address
        if tc_company_name is not UNSET:
            field_dict["tc_company_name"] = tc_company_name
        if tc_licence_no is not UNSET:
            field_dict["tc_licence_no_"] = tc_licence_no
        if tc_region is not UNSET:
            field_dict["tc_region"] = tc_region
        if tc_tel_no is not UNSET:
            field_dict["tc_tel_no"] = tc_tel_no
        if tc_type_of_warehouse is not UNSET:
            field_dict["tc_type_of_warehouse"] = tc_type_of_warehouse
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

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

        def _parse_en_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_address = _parse_en_address(d.pop("en_address", UNSET))

        def _parse_en_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_company_name = _parse_en_company_name(d.pop("en_company_name", UNSET))

        def _parse_en_licence_no(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        en_licence_no = _parse_en_licence_no(d.pop("en_licence_no_", UNSET))

        def _parse_en_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_region = _parse_en_region(d.pop("en_region", UNSET))

        def _parse_en_tel_no(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        en_tel_no = _parse_en_tel_no(d.pop("en_tel_no", UNSET))

        def _parse_en_type_of_warehouse(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_type_of_warehouse = _parse_en_type_of_warehouse(
            d.pop("en_type_of_warehouse", UNSET)
        )

        def _parse_sc_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_address = _parse_sc_address(d.pop("sc_address", UNSET))

        def _parse_sc_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_company_name = _parse_sc_company_name(d.pop("sc_company_name", UNSET))

        def _parse_sc_licence_no(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sc_licence_no = _parse_sc_licence_no(d.pop("sc_licence_no_", UNSET))

        def _parse_sc_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_region = _parse_sc_region(d.pop("sc_region", UNSET))

        def _parse_sc_tel_no(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sc_tel_no = _parse_sc_tel_no(d.pop("sc_tel_no", UNSET))

        def _parse_sc_type_of_warehouse(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_type_of_warehouse = _parse_sc_type_of_warehouse(
            d.pop("sc_type_of_warehouse", UNSET)
        )

        def _parse_tc_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_address = _parse_tc_address(d.pop("tc_address", UNSET))

        def _parse_tc_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_company_name = _parse_tc_company_name(d.pop("tc_company_name", UNSET))

        def _parse_tc_licence_no(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tc_licence_no = _parse_tc_licence_no(d.pop("tc_licence_no_", UNSET))

        def _parse_tc_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_region = _parse_tc_region(d.pop("tc_region", UNSET))

        def _parse_tc_tel_no(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tc_tel_no = _parse_tc_tel_no(d.pop("tc_tel_no", UNSET))

        def _parse_tc_type_of_warehouse(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_type_of_warehouse = _parse_tc_type_of_warehouse(
            d.pop("tc_type_of_warehouse", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            latitude=latitude,
            longitude=longitude,
            en_address=en_address,
            en_company_name=en_company_name,
            en_licence_no=en_licence_no,
            en_region=en_region,
            en_tel_no=en_tel_no,
            en_type_of_warehouse=en_type_of_warehouse,
            sc_address=sc_address,
            sc_company_name=sc_company_name,
            sc_licence_no=sc_licence_no,
            sc_region=sc_region,
            sc_tel_no=sc_tel_no,
            sc_type_of_warehouse=sc_type_of_warehouse,
            tc_address=tc_address,
            tc_company_name=tc_company_name,
            tc_licence_no=tc_licence_no,
            tc_region=tc_region,
            tc_tel_no=tc_tel_no,
            tc_type_of_warehouse=tc_type_of_warehouse,
            objectid=objectid,
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
