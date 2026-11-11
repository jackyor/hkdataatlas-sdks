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
        objectid (None | str | Unset): Publisher field type: esriFieldTypeString
        address_engnm (None | str | Unset): Publisher field type: esriFieldTypeString
        address_chtnm (None | str | Unset): Publisher field type: esriFieldTypeString
        bldg_engnm (None | str | Unset): Publisher field type: esriFieldTypeString
        bldg_chtnm (None | str | Unset): Publisher field type: esriFieldTypeString
        os_status (None | str | Unset): Publisher field type: esriFieldTypeString
        os_status_chtnm (None | str | Unset): Publisher field type: esriFieldTypeString
        os_type (None | str | Unset): Publisher field type: esriFieldTypeString
        os_type_chtnm (None | str | Unset): Publisher field type: esriFieldTypeString
        beach (None | str | Unset): Publisher field type: esriFieldTypeString
        beach_chtnm (None | str | Unset): Publisher field type: esriFieldTypeString
        amenity_area (None | str | Unset): Publisher field type: esriFieldTypeString
        amenity_area_chtnm (None | str | Unset): Publisher field type: esriFieldTypeString
        indoor_facilities (None | str | Unset): Publisher field type: esriFieldTypeString
        indoor_facilities_chtnm (None | str | Unset): Publisher field type: esriFieldTypeString
        os_area (None | str | Unset): Publisher field type: esriFieldTypeString
        os_area_chtnm (None | str | Unset): Publisher field type: esriFieldTypeString
        remark (None | str | Unset): Publisher field type: esriFieldTypeString
        remark_chtnm (None | str | Unset): Publisher field type: esriFieldTypeString
        last_update (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid_1 (int | Unset): Publisher field type: esriFieldTypeOID
    """

    objectid: None | str | Unset = UNSET
    address_engnm: None | str | Unset = UNSET
    address_chtnm: None | str | Unset = UNSET
    bldg_engnm: None | str | Unset = UNSET
    bldg_chtnm: None | str | Unset = UNSET
    os_status: None | str | Unset = UNSET
    os_status_chtnm: None | str | Unset = UNSET
    os_type: None | str | Unset = UNSET
    os_type_chtnm: None | str | Unset = UNSET
    beach: None | str | Unset = UNSET
    beach_chtnm: None | str | Unset = UNSET
    amenity_area: None | str | Unset = UNSET
    amenity_area_chtnm: None | str | Unset = UNSET
    indoor_facilities: None | str | Unset = UNSET
    indoor_facilities_chtnm: None | str | Unset = UNSET
    os_area: None | str | Unset = UNSET
    os_area_chtnm: None | str | Unset = UNSET
    remark: None | str | Unset = UNSET
    remark_chtnm: None | str | Unset = UNSET
    last_update: None | str | Unset = UNSET
    objectid_1: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid: None | str | Unset
        if isinstance(self.objectid, Unset):
            objectid = UNSET
        else:
            objectid = self.objectid

        address_engnm: None | str | Unset
        if isinstance(self.address_engnm, Unset):
            address_engnm = UNSET
        else:
            address_engnm = self.address_engnm

        address_chtnm: None | str | Unset
        if isinstance(self.address_chtnm, Unset):
            address_chtnm = UNSET
        else:
            address_chtnm = self.address_chtnm

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

        os_status: None | str | Unset
        if isinstance(self.os_status, Unset):
            os_status = UNSET
        else:
            os_status = self.os_status

        os_status_chtnm: None | str | Unset
        if isinstance(self.os_status_chtnm, Unset):
            os_status_chtnm = UNSET
        else:
            os_status_chtnm = self.os_status_chtnm

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

        os_area: None | str | Unset
        if isinstance(self.os_area, Unset):
            os_area = UNSET
        else:
            os_area = self.os_area

        os_area_chtnm: None | str | Unset
        if isinstance(self.os_area_chtnm, Unset):
            os_area_chtnm = UNSET
        else:
            os_area_chtnm = self.os_area_chtnm

        remark: None | str | Unset
        if isinstance(self.remark, Unset):
            remark = UNSET
        else:
            remark = self.remark

        remark_chtnm: None | str | Unset
        if isinstance(self.remark_chtnm, Unset):
            remark_chtnm = UNSET
        else:
            remark_chtnm = self.remark_chtnm

        last_update: None | str | Unset
        if isinstance(self.last_update, Unset):
            last_update = UNSET
        else:
            last_update = self.last_update

        objectid_1 = self.objectid_1

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if address_engnm is not UNSET:
            field_dict["ADDRESS_ENGNM"] = address_engnm
        if address_chtnm is not UNSET:
            field_dict["ADDRESS_CHTNM"] = address_chtnm
        if bldg_engnm is not UNSET:
            field_dict["BLDG_ENGNM"] = bldg_engnm
        if bldg_chtnm is not UNSET:
            field_dict["BLDG_CHTNM"] = bldg_chtnm
        if os_status is not UNSET:
            field_dict["OS_STATUS"] = os_status
        if os_status_chtnm is not UNSET:
            field_dict["OS_STATUS_CHTNM"] = os_status_chtnm
        if os_type is not UNSET:
            field_dict["OS_TYPE"] = os_type
        if os_type_chtnm is not UNSET:
            field_dict["OS_TYPE_CHTNM"] = os_type_chtnm
        if beach is not UNSET:
            field_dict["BEACH"] = beach
        if beach_chtnm is not UNSET:
            field_dict["BEACH_CHTNM"] = beach_chtnm
        if amenity_area is not UNSET:
            field_dict["AMENITY_AREA"] = amenity_area
        if amenity_area_chtnm is not UNSET:
            field_dict["AMENITY_AREA_CHTNM"] = amenity_area_chtnm
        if indoor_facilities is not UNSET:
            field_dict["INDOOR_FACILITIES"] = indoor_facilities
        if indoor_facilities_chtnm is not UNSET:
            field_dict["INDOOR_FACILITIES_CHTNM"] = indoor_facilities_chtnm
        if os_area is not UNSET:
            field_dict["OS_AREA"] = os_area
        if os_area_chtnm is not UNSET:
            field_dict["OS_AREA_CHTNM"] = os_area_chtnm
        if remark is not UNSET:
            field_dict["REMARK"] = remark
        if remark_chtnm is not UNSET:
            field_dict["REMARK_CHTNM"] = remark_chtnm
        if last_update is not UNSET:
            field_dict["LAST_UPDATE"] = last_update
        if objectid_1 is not UNSET:
            field_dict["OBJECTID_1"] = objectid_1

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_objectid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        objectid = _parse_objectid(d.pop("OBJECTID", UNSET))

        def _parse_address_engnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_engnm = _parse_address_engnm(d.pop("ADDRESS_ENGNM", UNSET))

        def _parse_address_chtnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_chtnm = _parse_address_chtnm(d.pop("ADDRESS_CHTNM", UNSET))

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

        def _parse_os_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        os_status = _parse_os_status(d.pop("OS_STATUS", UNSET))

        def _parse_os_status_chtnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        os_status_chtnm = _parse_os_status_chtnm(d.pop("OS_STATUS_CHTNM", UNSET))

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

        def _parse_os_area(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        os_area = _parse_os_area(d.pop("OS_AREA", UNSET))

        def _parse_os_area_chtnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        os_area_chtnm = _parse_os_area_chtnm(d.pop("OS_AREA_CHTNM", UNSET))

        def _parse_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark = _parse_remark(d.pop("REMARK", UNSET))

        def _parse_remark_chtnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark_chtnm = _parse_remark_chtnm(d.pop("REMARK_CHTNM", UNSET))

        def _parse_last_update(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_update = _parse_last_update(d.pop("LAST_UPDATE", UNSET))

        objectid_1 = d.pop("OBJECTID_1", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            address_engnm=address_engnm,
            address_chtnm=address_chtnm,
            bldg_engnm=bldg_engnm,
            bldg_chtnm=bldg_chtnm,
            os_status=os_status,
            os_status_chtnm=os_status_chtnm,
            os_type=os_type,
            os_type_chtnm=os_type_chtnm,
            beach=beach,
            beach_chtnm=beach_chtnm,
            amenity_area=amenity_area,
            amenity_area_chtnm=amenity_area_chtnm,
            indoor_facilities=indoor_facilities,
            indoor_facilities_chtnm=indoor_facilities_chtnm,
            os_area=os_area,
            os_area_chtnm=os_area_chtnm,
            remark=remark,
            remark_chtnm=remark_chtnm,
            last_update=last_update,
            objectid_1=objectid_1,
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
