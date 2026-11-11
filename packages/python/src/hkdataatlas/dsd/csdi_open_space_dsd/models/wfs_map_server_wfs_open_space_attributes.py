from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsOpenSpaceAttributes")


@_attrs_define
class WfsMapServerWfsOpenSpaceAttributes:
    """
    Attributes:
        address (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        address_chtnm (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        amenity_area (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        amenity_area_chtnm (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        beach (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        beach_chtnm (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        bldg_chtnm (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        bldg_engnm (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        completion_year (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        completion_year_nil (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        completion_year_chtnm (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        completion_year_chtnm_nil (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        indoor_facilities (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        indoor_facilities_chtnm (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        last_update (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        objectid (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        os_status (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        os_status_chtnm (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        os_type (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        os_type_chtnm (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        shape_area_chtnm (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        xml_geom_error (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML
            occurrence into all JSON queries.
        objectid_1 (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    address: None | str | Unset = UNSET
    address_chtnm: None | str | Unset = UNSET
    amenity_area: None | str | Unset = UNSET
    amenity_area_chtnm: None | str | Unset = UNSET
    beach: None | str | Unset = UNSET
    beach_chtnm: None | str | Unset = UNSET
    bldg_chtnm: None | str | Unset = UNSET
    bldg_engnm: None | str | Unset = UNSET
    completion_year: float | None | Unset = UNSET
    completion_year_nil: None | str | Unset = UNSET
    completion_year_chtnm: float | None | Unset = UNSET
    completion_year_chtnm_nil: None | str | Unset = UNSET
    indoor_facilities: None | str | Unset = UNSET
    indoor_facilities_chtnm: None | str | Unset = UNSET
    last_update: None | str | Unset = UNSET
    objectid: float | None | Unset = UNSET
    os_status: None | str | Unset = UNSET
    os_status_chtnm: None | str | Unset = UNSET
    os_type: None | str | Unset = UNSET
    os_type_chtnm: None | str | Unset = UNSET
    shape_area_chtnm: float | None | Unset = UNSET
    xml_geom_error: int | None | Unset = UNSET
    objectid_1: int | Unset = UNSET
    shape: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        bldg_chtnm: None | str | Unset
        if isinstance(self.bldg_chtnm, Unset):
            bldg_chtnm = UNSET
        else:
            bldg_chtnm = self.bldg_chtnm

        bldg_engnm: None | str | Unset
        if isinstance(self.bldg_engnm, Unset):
            bldg_engnm = UNSET
        else:
            bldg_engnm = self.bldg_engnm

        completion_year: float | None | Unset
        if isinstance(self.completion_year, Unset):
            completion_year = UNSET
        else:
            completion_year = self.completion_year

        completion_year_nil: None | str | Unset
        if isinstance(self.completion_year_nil, Unset):
            completion_year_nil = UNSET
        else:
            completion_year_nil = self.completion_year_nil

        completion_year_chtnm: float | None | Unset
        if isinstance(self.completion_year_chtnm, Unset):
            completion_year_chtnm = UNSET
        else:
            completion_year_chtnm = self.completion_year_chtnm

        completion_year_chtnm_nil: None | str | Unset
        if isinstance(self.completion_year_chtnm_nil, Unset):
            completion_year_chtnm_nil = UNSET
        else:
            completion_year_chtnm_nil = self.completion_year_chtnm_nil

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

        last_update: None | str | Unset
        if isinstance(self.last_update, Unset):
            last_update = UNSET
        else:
            last_update = self.last_update

        objectid: float | None | Unset
        if isinstance(self.objectid, Unset):
            objectid = UNSET
        else:
            objectid = self.objectid

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

        shape_area_chtnm: float | None | Unset
        if isinstance(self.shape_area_chtnm, Unset):
            shape_area_chtnm = UNSET
        else:
            shape_area_chtnm = self.shape_area_chtnm

        xml_geom_error: int | None | Unset
        if isinstance(self.xml_geom_error, Unset):
            xml_geom_error = UNSET
        else:
            xml_geom_error = self.xml_geom_error

        objectid_1 = self.objectid_1

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
        if address is not UNSET:
            field_dict["ADDRESS"] = address
        if address_chtnm is not UNSET:
            field_dict["ADDRESS_CHTNM"] = address_chtnm
        if amenity_area is not UNSET:
            field_dict["AMENITY_AREA"] = amenity_area
        if amenity_area_chtnm is not UNSET:
            field_dict["AMENITY_AREA_CHTNM"] = amenity_area_chtnm
        if beach is not UNSET:
            field_dict["BEACH"] = beach
        if beach_chtnm is not UNSET:
            field_dict["BEACH_CHTNM"] = beach_chtnm
        if bldg_chtnm is not UNSET:
            field_dict["BLDG_CHTNM"] = bldg_chtnm
        if bldg_engnm is not UNSET:
            field_dict["BLDG_ENGNM"] = bldg_engnm
        if completion_year is not UNSET:
            field_dict["COMPLETION_YEAR"] = completion_year
        if completion_year_nil is not UNSET:
            field_dict["COMPLETION_YEAR_nil"] = completion_year_nil
        if completion_year_chtnm is not UNSET:
            field_dict["COMPLETION_YEAR_CHTNM"] = completion_year_chtnm
        if completion_year_chtnm_nil is not UNSET:
            field_dict["COMPLETION_YEAR_CHTNM_nil"] = completion_year_chtnm_nil
        if indoor_facilities is not UNSET:
            field_dict["INDOOR_FACILITIES"] = indoor_facilities
        if indoor_facilities_chtnm is not UNSET:
            field_dict["INDOOR_FACILITIES_CHTNM"] = indoor_facilities_chtnm
        if last_update is not UNSET:
            field_dict["LAST_UPDATE"] = last_update
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if os_status is not UNSET:
            field_dict["OS_STATUS"] = os_status
        if os_status_chtnm is not UNSET:
            field_dict["OS_STATUS_CHTNM"] = os_status_chtnm
        if os_type is not UNSET:
            field_dict["OS_TYPE"] = os_type
        if os_type_chtnm is not UNSET:
            field_dict["OS_TYPE_CHTNM"] = os_type_chtnm
        if shape_area_chtnm is not UNSET:
            field_dict["SHAPE_AREA_CHTNM"] = shape_area_chtnm
        if xml_geom_error is not UNSET:
            field_dict["xml_geom_error"] = xml_geom_error
        if objectid_1 is not UNSET:
            field_dict["OBJECTID_1"] = objectid_1
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

        def _parse_bldg_chtnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bldg_chtnm = _parse_bldg_chtnm(d.pop("BLDG_CHTNM", UNSET))

        def _parse_bldg_engnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bldg_engnm = _parse_bldg_engnm(d.pop("BLDG_ENGNM", UNSET))

        def _parse_completion_year(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        completion_year = _parse_completion_year(d.pop("COMPLETION_YEAR", UNSET))

        def _parse_completion_year_nil(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completion_year_nil = _parse_completion_year_nil(
            d.pop("COMPLETION_YEAR_nil", UNSET)
        )

        def _parse_completion_year_chtnm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        completion_year_chtnm = _parse_completion_year_chtnm(
            d.pop("COMPLETION_YEAR_CHTNM", UNSET)
        )

        def _parse_completion_year_chtnm_nil(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completion_year_chtnm_nil = _parse_completion_year_chtnm_nil(
            d.pop("COMPLETION_YEAR_CHTNM_nil", UNSET)
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

        def _parse_last_update(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_update = _parse_last_update(d.pop("LAST_UPDATE", UNSET))

        def _parse_objectid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        objectid = _parse_objectid(d.pop("OBJECTID", UNSET))

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

        def _parse_shape_area_chtnm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area_chtnm = _parse_shape_area_chtnm(d.pop("SHAPE_AREA_CHTNM", UNSET))

        def _parse_xml_geom_error(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        xml_geom_error = _parse_xml_geom_error(d.pop("xml_geom_error", UNSET))

        objectid_1 = d.pop("OBJECTID_1", UNSET)

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

        wfs_map_server_wfs_open_space_attributes = cls(
            address=address,
            address_chtnm=address_chtnm,
            amenity_area=amenity_area,
            amenity_area_chtnm=amenity_area_chtnm,
            beach=beach,
            beach_chtnm=beach_chtnm,
            bldg_chtnm=bldg_chtnm,
            bldg_engnm=bldg_engnm,
            completion_year=completion_year,
            completion_year_nil=completion_year_nil,
            completion_year_chtnm=completion_year_chtnm,
            completion_year_chtnm_nil=completion_year_chtnm_nil,
            indoor_facilities=indoor_facilities,
            indoor_facilities_chtnm=indoor_facilities_chtnm,
            last_update=last_update,
            objectid=objectid,
            os_status=os_status,
            os_status_chtnm=os_status_chtnm,
            os_type=os_type,
            os_type_chtnm=os_type_chtnm,
            shape_area_chtnm=shape_area_chtnm,
            xml_geom_error=xml_geom_error,
            objectid_1=objectid_1,
            shape=shape,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_open_space_attributes.additional_properties = d
        return wfs_map_server_wfs_open_space_attributes

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
