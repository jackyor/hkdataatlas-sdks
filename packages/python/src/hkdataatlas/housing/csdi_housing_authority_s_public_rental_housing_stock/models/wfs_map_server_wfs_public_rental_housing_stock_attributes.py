from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsPublicRentalHousingStockAttributes")


@_attrs_define
class WfsMapServerWfsPublicRentalHousingStockAttributes:
    """
    Attributes:
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        estate_english_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        estate_chinese_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        district_english_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        district_chinese_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        region_english_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        region_chinese_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        english_name_of_block (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        chinese_name_of_block (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        flat_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        floor_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        internal_floor_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        avail_of_elevator_services (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        estate_map_latitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        estate_map_longitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    shape: Any | Unset = UNSET
    objectid: int | Unset = UNSET
    estate_english_name: None | str | Unset = UNSET
    estate_chinese_name: None | str | Unset = UNSET
    district_english_name: None | str | Unset = UNSET
    district_chinese_name: None | str | Unset = UNSET
    region_english_name: None | str | Unset = UNSET
    region_chinese_name: None | str | Unset = UNSET
    english_name_of_block: None | str | Unset = UNSET
    chinese_name_of_block: None | str | Unset = UNSET
    flat_number: None | str | Unset = UNSET
    floor_number: None | str | Unset = UNSET
    internal_floor_area: float | None | Unset = UNSET
    avail_of_elevator_services: None | str | Unset = UNSET
    estate_map_latitude: float | None | Unset = UNSET
    estate_map_longitude: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shape = self.shape

        objectid = self.objectid

        estate_english_name: None | str | Unset
        if isinstance(self.estate_english_name, Unset):
            estate_english_name = UNSET
        else:
            estate_english_name = self.estate_english_name

        estate_chinese_name: None | str | Unset
        if isinstance(self.estate_chinese_name, Unset):
            estate_chinese_name = UNSET
        else:
            estate_chinese_name = self.estate_chinese_name

        district_english_name: None | str | Unset
        if isinstance(self.district_english_name, Unset):
            district_english_name = UNSET
        else:
            district_english_name = self.district_english_name

        district_chinese_name: None | str | Unset
        if isinstance(self.district_chinese_name, Unset):
            district_chinese_name = UNSET
        else:
            district_chinese_name = self.district_chinese_name

        region_english_name: None | str | Unset
        if isinstance(self.region_english_name, Unset):
            region_english_name = UNSET
        else:
            region_english_name = self.region_english_name

        region_chinese_name: None | str | Unset
        if isinstance(self.region_chinese_name, Unset):
            region_chinese_name = UNSET
        else:
            region_chinese_name = self.region_chinese_name

        english_name_of_block: None | str | Unset
        if isinstance(self.english_name_of_block, Unset):
            english_name_of_block = UNSET
        else:
            english_name_of_block = self.english_name_of_block

        chinese_name_of_block: None | str | Unset
        if isinstance(self.chinese_name_of_block, Unset):
            chinese_name_of_block = UNSET
        else:
            chinese_name_of_block = self.chinese_name_of_block

        flat_number: None | str | Unset
        if isinstance(self.flat_number, Unset):
            flat_number = UNSET
        else:
            flat_number = self.flat_number

        floor_number: None | str | Unset
        if isinstance(self.floor_number, Unset):
            floor_number = UNSET
        else:
            floor_number = self.floor_number

        internal_floor_area: float | None | Unset
        if isinstance(self.internal_floor_area, Unset):
            internal_floor_area = UNSET
        else:
            internal_floor_area = self.internal_floor_area

        avail_of_elevator_services: None | str | Unset
        if isinstance(self.avail_of_elevator_services, Unset):
            avail_of_elevator_services = UNSET
        else:
            avail_of_elevator_services = self.avail_of_elevator_services

        estate_map_latitude: float | None | Unset
        if isinstance(self.estate_map_latitude, Unset):
            estate_map_latitude = UNSET
        else:
            estate_map_latitude = self.estate_map_latitude

        estate_map_longitude: float | None | Unset
        if isinstance(self.estate_map_longitude, Unset):
            estate_map_longitude = UNSET
        else:
            estate_map_longitude = self.estate_map_longitude

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if estate_english_name is not UNSET:
            field_dict["estate_english_name"] = estate_english_name
        if estate_chinese_name is not UNSET:
            field_dict["estate_chinese_name"] = estate_chinese_name
        if district_english_name is not UNSET:
            field_dict["district_english_name"] = district_english_name
        if district_chinese_name is not UNSET:
            field_dict["district_chinese_name"] = district_chinese_name
        if region_english_name is not UNSET:
            field_dict["region_english_name"] = region_english_name
        if region_chinese_name is not UNSET:
            field_dict["region_chinese_name"] = region_chinese_name
        if english_name_of_block is not UNSET:
            field_dict["english_name_of_block"] = english_name_of_block
        if chinese_name_of_block is not UNSET:
            field_dict["chinese_name_of_block"] = chinese_name_of_block
        if flat_number is not UNSET:
            field_dict["flat_number"] = flat_number
        if floor_number is not UNSET:
            field_dict["floor_number"] = floor_number
        if internal_floor_area is not UNSET:
            field_dict["internal_floor_area"] = internal_floor_area
        if avail_of_elevator_services is not UNSET:
            field_dict["avail_of_elevator_services"] = avail_of_elevator_services
        if estate_map_latitude is not UNSET:
            field_dict["estate_map_latitude"] = estate_map_latitude
        if estate_map_longitude is not UNSET:
            field_dict["estate_map_longitude"] = estate_map_longitude

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        shape = d.pop("SHAPE", UNSET)

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_estate_english_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estate_english_name = _parse_estate_english_name(
            d.pop("estate_english_name", UNSET)
        )

        def _parse_estate_chinese_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estate_chinese_name = _parse_estate_chinese_name(
            d.pop("estate_chinese_name", UNSET)
        )

        def _parse_district_english_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_english_name = _parse_district_english_name(
            d.pop("district_english_name", UNSET)
        )

        def _parse_district_chinese_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_chinese_name = _parse_district_chinese_name(
            d.pop("district_chinese_name", UNSET)
        )

        def _parse_region_english_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_english_name = _parse_region_english_name(
            d.pop("region_english_name", UNSET)
        )

        def _parse_region_chinese_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_chinese_name = _parse_region_chinese_name(
            d.pop("region_chinese_name", UNSET)
        )

        def _parse_english_name_of_block(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        english_name_of_block = _parse_english_name_of_block(
            d.pop("english_name_of_block", UNSET)
        )

        def _parse_chinese_name_of_block(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinese_name_of_block = _parse_chinese_name_of_block(
            d.pop("chinese_name_of_block", UNSET)
        )

        def _parse_flat_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flat_number = _parse_flat_number(d.pop("flat_number", UNSET))

        def _parse_floor_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        floor_number = _parse_floor_number(d.pop("floor_number", UNSET))

        def _parse_internal_floor_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        internal_floor_area = _parse_internal_floor_area(
            d.pop("internal_floor_area", UNSET)
        )

        def _parse_avail_of_elevator_services(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avail_of_elevator_services = _parse_avail_of_elevator_services(
            d.pop("avail_of_elevator_services", UNSET)
        )

        def _parse_estate_map_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        estate_map_latitude = _parse_estate_map_latitude(
            d.pop("estate_map_latitude", UNSET)
        )

        def _parse_estate_map_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        estate_map_longitude = _parse_estate_map_longitude(
            d.pop("estate_map_longitude", UNSET)
        )

        wfs_map_server_wfs_public_rental_housing_stock_attributes = cls(
            shape=shape,
            objectid=objectid,
            estate_english_name=estate_english_name,
            estate_chinese_name=estate_chinese_name,
            district_english_name=district_english_name,
            district_chinese_name=district_chinese_name,
            region_english_name=region_english_name,
            region_chinese_name=region_chinese_name,
            english_name_of_block=english_name_of_block,
            chinese_name_of_block=chinese_name_of_block,
            flat_number=flat_number,
            floor_number=floor_number,
            internal_floor_area=internal_floor_area,
            avail_of_elevator_services=avail_of_elevator_services,
            estate_map_latitude=estate_map_latitude,
            estate_map_longitude=estate_map_longitude,
        )

        wfs_map_server_wfs_public_rental_housing_stock_attributes.additional_properties = d
        return wfs_map_server_wfs_public_rental_housing_stock_attributes

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
