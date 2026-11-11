from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer5Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer5Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        photo_no (None | str | Unset): Publisher field type: esriFieldTypeString
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        location_english (None | str | Unset): Publisher field type: esriFieldTypeString
        location_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        flying_height (float | None | Unset): Publisher field type: esriFieldTypeDouble
        date_of_flight (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        oblique (None | str | Unset): Publisher field type: esriFieldTypeString
        flight_direction (float | None | Unset): Publisher field type: esriFieldTypeDouble
        photo_scale (float | None | Unset): Publisher field type: esriFieldTypeDouble
        footprint_1_easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        footprint_1_northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        footprint_2_easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        footprint_2_northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        footprint_3_easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        footprint_3_northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        footprint_4_easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        footprint_4_northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        footprint_1_longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        footprint_1_latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        footprint_2_longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        footprint_2_latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        footprint_3_longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        footprint_3_latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        footprint_4_longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        footprint_4_latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    photo_no: None | str | Unset = UNSET
    easting: float | None | Unset = UNSET
    northing: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    location_english: None | str | Unset = UNSET
    location_chinese: None | str | Unset = UNSET
    flying_height: float | None | Unset = UNSET
    date_of_flight: Any | Unset = UNSET
    oblique: None | str | Unset = UNSET
    flight_direction: float | None | Unset = UNSET
    photo_scale: float | None | Unset = UNSET
    footprint_1_easting: float | None | Unset = UNSET
    footprint_1_northing: float | None | Unset = UNSET
    footprint_2_easting: float | None | Unset = UNSET
    footprint_2_northing: float | None | Unset = UNSET
    footprint_3_easting: float | None | Unset = UNSET
    footprint_3_northing: float | None | Unset = UNSET
    footprint_4_easting: float | None | Unset = UNSET
    footprint_4_northing: float | None | Unset = UNSET
    footprint_1_longitude: float | None | Unset = UNSET
    footprint_1_latitude: float | None | Unset = UNSET
    footprint_2_longitude: float | None | Unset = UNSET
    footprint_2_latitude: float | None | Unset = UNSET
    footprint_3_longitude: float | None | Unset = UNSET
    footprint_3_latitude: float | None | Unset = UNSET
    footprint_4_longitude: float | None | Unset = UNSET
    footprint_4_latitude: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        photo_no: None | str | Unset
        if isinstance(self.photo_no, Unset):
            photo_no = UNSET
        else:
            photo_no = self.photo_no

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        location_english: None | str | Unset
        if isinstance(self.location_english, Unset):
            location_english = UNSET
        else:
            location_english = self.location_english

        location_chinese: None | str | Unset
        if isinstance(self.location_chinese, Unset):
            location_chinese = UNSET
        else:
            location_chinese = self.location_chinese

        flying_height: float | None | Unset
        if isinstance(self.flying_height, Unset):
            flying_height = UNSET
        else:
            flying_height = self.flying_height

        date_of_flight = self.date_of_flight

        oblique: None | str | Unset
        if isinstance(self.oblique, Unset):
            oblique = UNSET
        else:
            oblique = self.oblique

        flight_direction: float | None | Unset
        if isinstance(self.flight_direction, Unset):
            flight_direction = UNSET
        else:
            flight_direction = self.flight_direction

        photo_scale: float | None | Unset
        if isinstance(self.photo_scale, Unset):
            photo_scale = UNSET
        else:
            photo_scale = self.photo_scale

        footprint_1_easting: float | None | Unset
        if isinstance(self.footprint_1_easting, Unset):
            footprint_1_easting = UNSET
        else:
            footprint_1_easting = self.footprint_1_easting

        footprint_1_northing: float | None | Unset
        if isinstance(self.footprint_1_northing, Unset):
            footprint_1_northing = UNSET
        else:
            footprint_1_northing = self.footprint_1_northing

        footprint_2_easting: float | None | Unset
        if isinstance(self.footprint_2_easting, Unset):
            footprint_2_easting = UNSET
        else:
            footprint_2_easting = self.footprint_2_easting

        footprint_2_northing: float | None | Unset
        if isinstance(self.footprint_2_northing, Unset):
            footprint_2_northing = UNSET
        else:
            footprint_2_northing = self.footprint_2_northing

        footprint_3_easting: float | None | Unset
        if isinstance(self.footprint_3_easting, Unset):
            footprint_3_easting = UNSET
        else:
            footprint_3_easting = self.footprint_3_easting

        footprint_3_northing: float | None | Unset
        if isinstance(self.footprint_3_northing, Unset):
            footprint_3_northing = UNSET
        else:
            footprint_3_northing = self.footprint_3_northing

        footprint_4_easting: float | None | Unset
        if isinstance(self.footprint_4_easting, Unset):
            footprint_4_easting = UNSET
        else:
            footprint_4_easting = self.footprint_4_easting

        footprint_4_northing: float | None | Unset
        if isinstance(self.footprint_4_northing, Unset):
            footprint_4_northing = UNSET
        else:
            footprint_4_northing = self.footprint_4_northing

        footprint_1_longitude: float | None | Unset
        if isinstance(self.footprint_1_longitude, Unset):
            footprint_1_longitude = UNSET
        else:
            footprint_1_longitude = self.footprint_1_longitude

        footprint_1_latitude: float | None | Unset
        if isinstance(self.footprint_1_latitude, Unset):
            footprint_1_latitude = UNSET
        else:
            footprint_1_latitude = self.footprint_1_latitude

        footprint_2_longitude: float | None | Unset
        if isinstance(self.footprint_2_longitude, Unset):
            footprint_2_longitude = UNSET
        else:
            footprint_2_longitude = self.footprint_2_longitude

        footprint_2_latitude: float | None | Unset
        if isinstance(self.footprint_2_latitude, Unset):
            footprint_2_latitude = UNSET
        else:
            footprint_2_latitude = self.footprint_2_latitude

        footprint_3_longitude: float | None | Unset
        if isinstance(self.footprint_3_longitude, Unset):
            footprint_3_longitude = UNSET
        else:
            footprint_3_longitude = self.footprint_3_longitude

        footprint_3_latitude: float | None | Unset
        if isinstance(self.footprint_3_latitude, Unset):
            footprint_3_latitude = UNSET
        else:
            footprint_3_latitude = self.footprint_3_latitude

        footprint_4_longitude: float | None | Unset
        if isinstance(self.footprint_4_longitude, Unset):
            footprint_4_longitude = UNSET
        else:
            footprint_4_longitude = self.footprint_4_longitude

        footprint_4_latitude: float | None | Unset
        if isinstance(self.footprint_4_latitude, Unset):
            footprint_4_latitude = UNSET
        else:
            footprint_4_latitude = self.footprint_4_latitude

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if photo_no is not UNSET:
            field_dict["PhotoNo"] = photo_no
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if location_english is not UNSET:
            field_dict["LocationEnglish"] = location_english
        if location_chinese is not UNSET:
            field_dict["LocationChinese"] = location_chinese
        if flying_height is not UNSET:
            field_dict["FlyingHeight"] = flying_height
        if date_of_flight is not UNSET:
            field_dict["DateOfFlight"] = date_of_flight
        if oblique is not UNSET:
            field_dict["Oblique"] = oblique
        if flight_direction is not UNSET:
            field_dict["FlightDirection"] = flight_direction
        if photo_scale is not UNSET:
            field_dict["PhotoScale"] = photo_scale
        if footprint_1_easting is not UNSET:
            field_dict["Footprint1_Easting"] = footprint_1_easting
        if footprint_1_northing is not UNSET:
            field_dict["Footprint1_Northing"] = footprint_1_northing
        if footprint_2_easting is not UNSET:
            field_dict["Footprint2_Easting"] = footprint_2_easting
        if footprint_2_northing is not UNSET:
            field_dict["Footprint2_Northing"] = footprint_2_northing
        if footprint_3_easting is not UNSET:
            field_dict["Footprint3_Easting"] = footprint_3_easting
        if footprint_3_northing is not UNSET:
            field_dict["Footprint3_Northing"] = footprint_3_northing
        if footprint_4_easting is not UNSET:
            field_dict["Footprint4_Easting"] = footprint_4_easting
        if footprint_4_northing is not UNSET:
            field_dict["Footprint4_Northing"] = footprint_4_northing
        if footprint_1_longitude is not UNSET:
            field_dict["Footprint1_Longitude"] = footprint_1_longitude
        if footprint_1_latitude is not UNSET:
            field_dict["Footprint1_Latitude"] = footprint_1_latitude
        if footprint_2_longitude is not UNSET:
            field_dict["Footprint2_Longitude"] = footprint_2_longitude
        if footprint_2_latitude is not UNSET:
            field_dict["Footprint2_Latitude"] = footprint_2_latitude
        if footprint_3_longitude is not UNSET:
            field_dict["Footprint3_Longitude"] = footprint_3_longitude
        if footprint_3_latitude is not UNSET:
            field_dict["Footprint3_Latitude"] = footprint_3_latitude
        if footprint_4_longitude is not UNSET:
            field_dict["Footprint4_Longitude"] = footprint_4_longitude
        if footprint_4_latitude is not UNSET:
            field_dict["Footprint4_Latitude"] = footprint_4_latitude

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_photo_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo_no = _parse_photo_no(d.pop("PhotoNo", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("Easting", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_location_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_english = _parse_location_english(d.pop("LocationEnglish", UNSET))

        def _parse_location_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_chinese = _parse_location_chinese(d.pop("LocationChinese", UNSET))

        def _parse_flying_height(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        flying_height = _parse_flying_height(d.pop("FlyingHeight", UNSET))

        date_of_flight = d.pop("DateOfFlight", UNSET)

        def _parse_oblique(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        oblique = _parse_oblique(d.pop("Oblique", UNSET))

        def _parse_flight_direction(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        flight_direction = _parse_flight_direction(d.pop("FlightDirection", UNSET))

        def _parse_photo_scale(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        photo_scale = _parse_photo_scale(d.pop("PhotoScale", UNSET))

        def _parse_footprint_1_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        footprint_1_easting = _parse_footprint_1_easting(
            d.pop("Footprint1_Easting", UNSET)
        )

        def _parse_footprint_1_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        footprint_1_northing = _parse_footprint_1_northing(
            d.pop("Footprint1_Northing", UNSET)
        )

        def _parse_footprint_2_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        footprint_2_easting = _parse_footprint_2_easting(
            d.pop("Footprint2_Easting", UNSET)
        )

        def _parse_footprint_2_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        footprint_2_northing = _parse_footprint_2_northing(
            d.pop("Footprint2_Northing", UNSET)
        )

        def _parse_footprint_3_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        footprint_3_easting = _parse_footprint_3_easting(
            d.pop("Footprint3_Easting", UNSET)
        )

        def _parse_footprint_3_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        footprint_3_northing = _parse_footprint_3_northing(
            d.pop("Footprint3_Northing", UNSET)
        )

        def _parse_footprint_4_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        footprint_4_easting = _parse_footprint_4_easting(
            d.pop("Footprint4_Easting", UNSET)
        )

        def _parse_footprint_4_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        footprint_4_northing = _parse_footprint_4_northing(
            d.pop("Footprint4_Northing", UNSET)
        )

        def _parse_footprint_1_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        footprint_1_longitude = _parse_footprint_1_longitude(
            d.pop("Footprint1_Longitude", UNSET)
        )

        def _parse_footprint_1_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        footprint_1_latitude = _parse_footprint_1_latitude(
            d.pop("Footprint1_Latitude", UNSET)
        )

        def _parse_footprint_2_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        footprint_2_longitude = _parse_footprint_2_longitude(
            d.pop("Footprint2_Longitude", UNSET)
        )

        def _parse_footprint_2_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        footprint_2_latitude = _parse_footprint_2_latitude(
            d.pop("Footprint2_Latitude", UNSET)
        )

        def _parse_footprint_3_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        footprint_3_longitude = _parse_footprint_3_longitude(
            d.pop("Footprint3_Longitude", UNSET)
        )

        def _parse_footprint_3_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        footprint_3_latitude = _parse_footprint_3_latitude(
            d.pop("Footprint3_Latitude", UNSET)
        )

        def _parse_footprint_4_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        footprint_4_longitude = _parse_footprint_4_longitude(
            d.pop("Footprint4_Longitude", UNSET)
        )

        def _parse_footprint_4_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        footprint_4_latitude = _parse_footprint_4_latitude(
            d.pop("Footprint4_Latitude", UNSET)
        )

        arcgis_feature_server_arcgis_layer_5_attributes = cls(
            objectid=objectid,
            photo_no=photo_no,
            easting=easting,
            northing=northing,
            longitude=longitude,
            latitude=latitude,
            location_english=location_english,
            location_chinese=location_chinese,
            flying_height=flying_height,
            date_of_flight=date_of_flight,
            oblique=oblique,
            flight_direction=flight_direction,
            photo_scale=photo_scale,
            footprint_1_easting=footprint_1_easting,
            footprint_1_northing=footprint_1_northing,
            footprint_2_easting=footprint_2_easting,
            footprint_2_northing=footprint_2_northing,
            footprint_3_easting=footprint_3_easting,
            footprint_3_northing=footprint_3_northing,
            footprint_4_easting=footprint_4_easting,
            footprint_4_northing=footprint_4_northing,
            footprint_1_longitude=footprint_1_longitude,
            footprint_1_latitude=footprint_1_latitude,
            footprint_2_longitude=footprint_2_longitude,
            footprint_2_latitude=footprint_2_latitude,
            footprint_3_longitude=footprint_3_longitude,
            footprint_3_latitude=footprint_3_latitude,
            footprint_4_longitude=footprint_4_longitude,
            footprint_4_latitude=footprint_4_latitude,
        )

        arcgis_feature_server_arcgis_layer_5_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_5_attributes

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
