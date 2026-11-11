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
        address (None | str | Unset): Publisher field type: esriFieldTypeString
        address_chtnm (None | str | Unset): Publisher field type: esriFieldTypeString
        address_chsnm (None | str | Unset): Publisher field type: esriFieldTypeString
        bldg_engnm (None | str | Unset): Publisher field type: esriFieldTypeString
        bldg_chtnm (None | str | Unset): Publisher field type: esriFieldTypeString
        bldg_chsnm (None | str | Unset): Publisher field type: esriFieldTypeString
        os_type (None | str | Unset): Publisher field type: esriFieldTypeString
        os_type_chtnm (None | str | Unset): Publisher field type: esriFieldTypeString
        os_type_chsnm (None | str | Unset): Publisher field type: esriFieldTypeString
        os_status (None | str | Unset): Publisher field type: esriFieldTypeString
        os_staus_chtnm (None | str | Unset): Publisher field type: esriFieldTypeString
        os_staus_chsnm (None | str | Unset): Publisher field type: esriFieldTypeString
        beach (None | str | Unset): Publisher field type: esriFieldTypeString
        beach_chtnm (None | str | Unset): Publisher field type: esriFieldTypeString
        beach_chsnm (None | str | Unset): Publisher field type: esriFieldTypeString
        amenity_area (None | str | Unset): Publisher field type: esriFieldTypeString
        amenity_area_chtnm (None | str | Unset): Publisher field type: esriFieldTypeString
        amenity_area_chsnm (None | str | Unset): Publisher field type: esriFieldTypeString
        indoor_facilities (None | str | Unset): Publisher field type: esriFieldTypeString
        indoor_facilities_chtnm (None | str | Unset): Publisher field type: esriFieldTypeString
        indoor_facilities_chsnm (None | str | Unset): Publisher field type: esriFieldTypeString
        completion_year (None | str | Unset): Publisher field type: esriFieldTypeString
        completion_year_chtnm (None | str | Unset): Publisher field type: esriFieldTypeString
        completion_year_chsnm (None | str | Unset): Publisher field type: esriFieldTypeString
        os_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
        os_area_chtnm (float | None | Unset): Publisher field type: esriFieldTypeDouble
        os_area_chsnm (float | None | Unset): Publisher field type: esriFieldTypeDouble
        last_update (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
    """

    objectid: int | Unset = UNSET
    address: None | str | Unset = UNSET
    address_chtnm: None | str | Unset = UNSET
    address_chsnm: None | str | Unset = UNSET
    bldg_engnm: None | str | Unset = UNSET
    bldg_chtnm: None | str | Unset = UNSET
    bldg_chsnm: None | str | Unset = UNSET
    os_type: None | str | Unset = UNSET
    os_type_chtnm: None | str | Unset = UNSET
    os_type_chsnm: None | str | Unset = UNSET
    os_status: None | str | Unset = UNSET
    os_staus_chtnm: None | str | Unset = UNSET
    os_staus_chsnm: None | str | Unset = UNSET
    beach: None | str | Unset = UNSET
    beach_chtnm: None | str | Unset = UNSET
    beach_chsnm: None | str | Unset = UNSET
    amenity_area: None | str | Unset = UNSET
    amenity_area_chtnm: None | str | Unset = UNSET
    amenity_area_chsnm: None | str | Unset = UNSET
    indoor_facilities: None | str | Unset = UNSET
    indoor_facilities_chtnm: None | str | Unset = UNSET
    indoor_facilities_chsnm: None | str | Unset = UNSET
    completion_year: None | str | Unset = UNSET
    completion_year_chtnm: None | str | Unset = UNSET
    completion_year_chsnm: None | str | Unset = UNSET
    os_area: float | None | Unset = UNSET
    os_area_chtnm: float | None | Unset = UNSET
    os_area_chsnm: float | None | Unset = UNSET
    last_update: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        address_chtnm: None | str | Unset
        if isinstance(self.address_chtnm, Unset):
            address_chtnm = UNSET
        else:
            address_chtnm = self.address_chtnm

        address_chsnm: None | str | Unset
        if isinstance(self.address_chsnm, Unset):
            address_chsnm = UNSET
        else:
            address_chsnm = self.address_chsnm

        bldg_engnm: None | str | Unset
        if isinstance(self.bldg_engnm, Unset):
            bldg_engnm = UNSET
        else:
            bldg_engnm = self.bldg_engnm

        bldg_chtnm: None | str | Unset
        if isinstance(self.bldg_chtnm, Unset):
            bldg_chtnm = UNSET
        else:
            bldg_chtnm = self.bldg_chtnm

        bldg_chsnm: None | str | Unset
        if isinstance(self.bldg_chsnm, Unset):
            bldg_chsnm = UNSET
        else:
            bldg_chsnm = self.bldg_chsnm

        os_type: None | str | Unset
        if isinstance(self.os_type, Unset):
            os_type = UNSET
        else:
            os_type = self.os_type

        os_type_chtnm: None | str | Unset
        if isinstance(self.os_type_chtnm, Unset):
            os_type_chtnm = UNSET
        else:
            os_type_chtnm = self.os_type_chtnm

        os_type_chsnm: None | str | Unset
        if isinstance(self.os_type_chsnm, Unset):
            os_type_chsnm = UNSET
        else:
            os_type_chsnm = self.os_type_chsnm

        os_status: None | str | Unset
        if isinstance(self.os_status, Unset):
            os_status = UNSET
        else:
            os_status = self.os_status

        os_staus_chtnm: None | str | Unset
        if isinstance(self.os_staus_chtnm, Unset):
            os_staus_chtnm = UNSET
        else:
            os_staus_chtnm = self.os_staus_chtnm

        os_staus_chsnm: None | str | Unset
        if isinstance(self.os_staus_chsnm, Unset):
            os_staus_chsnm = UNSET
        else:
            os_staus_chsnm = self.os_staus_chsnm

        beach: None | str | Unset
        if isinstance(self.beach, Unset):
            beach = UNSET
        else:
            beach = self.beach

        beach_chtnm: None | str | Unset
        if isinstance(self.beach_chtnm, Unset):
            beach_chtnm = UNSET
        else:
            beach_chtnm = self.beach_chtnm

        beach_chsnm: None | str | Unset
        if isinstance(self.beach_chsnm, Unset):
            beach_chsnm = UNSET
        else:
            beach_chsnm = self.beach_chsnm

        amenity_area: None | str | Unset
        if isinstance(self.amenity_area, Unset):
            amenity_area = UNSET
        else:
            amenity_area = self.amenity_area

        amenity_area_chtnm: None | str | Unset
        if isinstance(self.amenity_area_chtnm, Unset):
            amenity_area_chtnm = UNSET
        else:
            amenity_area_chtnm = self.amenity_area_chtnm

        amenity_area_chsnm: None | str | Unset
        if isinstance(self.amenity_area_chsnm, Unset):
            amenity_area_chsnm = UNSET
        else:
            amenity_area_chsnm = self.amenity_area_chsnm

        indoor_facilities: None | str | Unset
        if isinstance(self.indoor_facilities, Unset):
            indoor_facilities = UNSET
        else:
            indoor_facilities = self.indoor_facilities

        indoor_facilities_chtnm: None | str | Unset
        if isinstance(self.indoor_facilities_chtnm, Unset):
            indoor_facilities_chtnm = UNSET
        else:
            indoor_facilities_chtnm = self.indoor_facilities_chtnm

        indoor_facilities_chsnm: None | str | Unset
        if isinstance(self.indoor_facilities_chsnm, Unset):
            indoor_facilities_chsnm = UNSET
        else:
            indoor_facilities_chsnm = self.indoor_facilities_chsnm

        completion_year: None | str | Unset
        if isinstance(self.completion_year, Unset):
            completion_year = UNSET
        else:
            completion_year = self.completion_year

        completion_year_chtnm: None | str | Unset
        if isinstance(self.completion_year_chtnm, Unset):
            completion_year_chtnm = UNSET
        else:
            completion_year_chtnm = self.completion_year_chtnm

        completion_year_chsnm: None | str | Unset
        if isinstance(self.completion_year_chsnm, Unset):
            completion_year_chsnm = UNSET
        else:
            completion_year_chsnm = self.completion_year_chsnm

        os_area: float | None | Unset
        if isinstance(self.os_area, Unset):
            os_area = UNSET
        else:
            os_area = self.os_area

        os_area_chtnm: float | None | Unset
        if isinstance(self.os_area_chtnm, Unset):
            os_area_chtnm = UNSET
        else:
            os_area_chtnm = self.os_area_chtnm

        os_area_chsnm: float | None | Unset
        if isinstance(self.os_area_chsnm, Unset):
            os_area_chsnm = UNSET
        else:
            os_area_chsnm = self.os_area_chsnm

        last_update = self.last_update

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if address is not UNSET:
            field_dict["ADDRESS"] = address
        if address_chtnm is not UNSET:
            field_dict["ADDRESS_CHTNM"] = address_chtnm
        if address_chsnm is not UNSET:
            field_dict["ADDRESS_CHSNM"] = address_chsnm
        if bldg_engnm is not UNSET:
            field_dict["BLDG_ENGNM"] = bldg_engnm
        if bldg_chtnm is not UNSET:
            field_dict["BLDG_CHTNM"] = bldg_chtnm
        if bldg_chsnm is not UNSET:
            field_dict["BLDG_CHSNM"] = bldg_chsnm
        if os_type is not UNSET:
            field_dict["OS_TYPE"] = os_type
        if os_type_chtnm is not UNSET:
            field_dict["OS_TYPE_CHTNM"] = os_type_chtnm
        if os_type_chsnm is not UNSET:
            field_dict["OS_TYPE_CHSNM"] = os_type_chsnm
        if os_status is not UNSET:
            field_dict["OS_STATUS"] = os_status
        if os_staus_chtnm is not UNSET:
            field_dict["OS_STAUS_CHTNM"] = os_staus_chtnm
        if os_staus_chsnm is not UNSET:
            field_dict["OS_STAUS_CHSNM"] = os_staus_chsnm
        if beach is not UNSET:
            field_dict["BEACH"] = beach
        if beach_chtnm is not UNSET:
            field_dict["BEACH_CHTNM"] = beach_chtnm
        if beach_chsnm is not UNSET:
            field_dict["BEACH_CHSNM"] = beach_chsnm
        if amenity_area is not UNSET:
            field_dict["AMENITY_AREA"] = amenity_area
        if amenity_area_chtnm is not UNSET:
            field_dict["AMENITY_AREA_CHTNM"] = amenity_area_chtnm
        if amenity_area_chsnm is not UNSET:
            field_dict["AMENITY_AREA_CHSNM"] = amenity_area_chsnm
        if indoor_facilities is not UNSET:
            field_dict["INDOOR_FACILITIES"] = indoor_facilities
        if indoor_facilities_chtnm is not UNSET:
            field_dict["INDOOR_FACILITIES_CHTNM"] = indoor_facilities_chtnm
        if indoor_facilities_chsnm is not UNSET:
            field_dict["INDOOR_FACILITIES_CHSNM"] = indoor_facilities_chsnm
        if completion_year is not UNSET:
            field_dict["COMPLETION_YEAR"] = completion_year
        if completion_year_chtnm is not UNSET:
            field_dict["COMPLETION_YEAR_CHTNM"] = completion_year_chtnm
        if completion_year_chsnm is not UNSET:
            field_dict["COMPLETION_YEAR_CHSNM"] = completion_year_chsnm
        if os_area is not UNSET:
            field_dict["OS_AREA"] = os_area
        if os_area_chtnm is not UNSET:
            field_dict["OS_AREA_CHTNM"] = os_area_chtnm
        if os_area_chsnm is not UNSET:
            field_dict["OS_AREA_CHSNM"] = os_area_chsnm
        if last_update is not UNSET:
            field_dict["LAST_UPDATE"] = last_update

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("ADDRESS", UNSET))

        def _parse_address_chtnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_chtnm = _parse_address_chtnm(d.pop("ADDRESS_CHTNM", UNSET))

        def _parse_address_chsnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_chsnm = _parse_address_chsnm(d.pop("ADDRESS_CHSNM", UNSET))

        def _parse_bldg_engnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bldg_engnm = _parse_bldg_engnm(d.pop("BLDG_ENGNM", UNSET))

        def _parse_bldg_chtnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bldg_chtnm = _parse_bldg_chtnm(d.pop("BLDG_CHTNM", UNSET))

        def _parse_bldg_chsnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bldg_chsnm = _parse_bldg_chsnm(d.pop("BLDG_CHSNM", UNSET))

        def _parse_os_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        os_type = _parse_os_type(d.pop("OS_TYPE", UNSET))

        def _parse_os_type_chtnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        os_type_chtnm = _parse_os_type_chtnm(d.pop("OS_TYPE_CHTNM", UNSET))

        def _parse_os_type_chsnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        os_type_chsnm = _parse_os_type_chsnm(d.pop("OS_TYPE_CHSNM", UNSET))

        def _parse_os_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        os_status = _parse_os_status(d.pop("OS_STATUS", UNSET))

        def _parse_os_staus_chtnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        os_staus_chtnm = _parse_os_staus_chtnm(d.pop("OS_STAUS_CHTNM", UNSET))

        def _parse_os_staus_chsnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        os_staus_chsnm = _parse_os_staus_chsnm(d.pop("OS_STAUS_CHSNM", UNSET))

        def _parse_beach(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beach = _parse_beach(d.pop("BEACH", UNSET))

        def _parse_beach_chtnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beach_chtnm = _parse_beach_chtnm(d.pop("BEACH_CHTNM", UNSET))

        def _parse_beach_chsnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beach_chsnm = _parse_beach_chsnm(d.pop("BEACH_CHSNM", UNSET))

        def _parse_amenity_area(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amenity_area = _parse_amenity_area(d.pop("AMENITY_AREA", UNSET))

        def _parse_amenity_area_chtnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amenity_area_chtnm = _parse_amenity_area_chtnm(
            d.pop("AMENITY_AREA_CHTNM", UNSET)
        )

        def _parse_amenity_area_chsnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amenity_area_chsnm = _parse_amenity_area_chsnm(
            d.pop("AMENITY_AREA_CHSNM", UNSET)
        )

        def _parse_indoor_facilities(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        indoor_facilities = _parse_indoor_facilities(d.pop("INDOOR_FACILITIES", UNSET))

        def _parse_indoor_facilities_chtnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        indoor_facilities_chtnm = _parse_indoor_facilities_chtnm(
            d.pop("INDOOR_FACILITIES_CHTNM", UNSET)
        )

        def _parse_indoor_facilities_chsnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        indoor_facilities_chsnm = _parse_indoor_facilities_chsnm(
            d.pop("INDOOR_FACILITIES_CHSNM", UNSET)
        )

        def _parse_completion_year(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completion_year = _parse_completion_year(d.pop("COMPLETION_YEAR", UNSET))

        def _parse_completion_year_chtnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completion_year_chtnm = _parse_completion_year_chtnm(
            d.pop("COMPLETION_YEAR_CHTNM", UNSET)
        )

        def _parse_completion_year_chsnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completion_year_chsnm = _parse_completion_year_chsnm(
            d.pop("COMPLETION_YEAR_CHSNM", UNSET)
        )

        def _parse_os_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        os_area = _parse_os_area(d.pop("OS_AREA", UNSET))

        def _parse_os_area_chtnm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        os_area_chtnm = _parse_os_area_chtnm(d.pop("OS_AREA_CHTNM", UNSET))

        def _parse_os_area_chsnm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        os_area_chsnm = _parse_os_area_chsnm(d.pop("OS_AREA_CHSNM", UNSET))

        last_update = d.pop("LAST_UPDATE", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            address=address,
            address_chtnm=address_chtnm,
            address_chsnm=address_chsnm,
            bldg_engnm=bldg_engnm,
            bldg_chtnm=bldg_chtnm,
            bldg_chsnm=bldg_chsnm,
            os_type=os_type,
            os_type_chtnm=os_type_chtnm,
            os_type_chsnm=os_type_chsnm,
            os_status=os_status,
            os_staus_chtnm=os_staus_chtnm,
            os_staus_chsnm=os_staus_chsnm,
            beach=beach,
            beach_chtnm=beach_chtnm,
            beach_chsnm=beach_chsnm,
            amenity_area=amenity_area,
            amenity_area_chtnm=amenity_area_chtnm,
            amenity_area_chsnm=amenity_area_chsnm,
            indoor_facilities=indoor_facilities,
            indoor_facilities_chtnm=indoor_facilities_chtnm,
            indoor_facilities_chsnm=indoor_facilities_chsnm,
            completion_year=completion_year,
            completion_year_chtnm=completion_year_chtnm,
            completion_year_chsnm=completion_year_chsnm,
            os_area=os_area,
            os_area_chtnm=os_area_chtnm,
            os_area_chsnm=os_area_chsnm,
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
