from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsgeotaggingAttributes")


@_attrs_define
class WfsMapServerWfsgeotaggingAttributes:
    """
    Attributes:
        paragliding_area_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        paragliding_area_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        paragliding_area_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        operating_altitude (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        latitude (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        longitude (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        boundary_1_lat (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        boundary_1_long (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        boundary_1_feature (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        boundary_2_lat (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        boundary_2_long (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        boundary_2_feature (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        boundary_3_lat (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        boundary_3_long (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        boundary_3_feature (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        boundary_4_lat (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        boundary_4_long (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        boundary_4_feature (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        boundary_5_lat (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        boundary_5_long (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        boundary_5_feature (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        boundary_6_lat (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        boundary_6_long (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        boundary_6_feature (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        boundary_7_lat (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        boundary_7_long (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        boundary_7_feature (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        link (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        remarks (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    paragliding_area_en: None | str | Unset = UNSET
    paragliding_area_tc: None | str | Unset = UNSET
    paragliding_area_sc: None | str | Unset = UNSET
    operating_altitude: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    boundary_1_lat: None | str | Unset = UNSET
    boundary_1_long: None | str | Unset = UNSET
    boundary_1_feature: None | str | Unset = UNSET
    boundary_2_lat: None | str | Unset = UNSET
    boundary_2_long: None | str | Unset = UNSET
    boundary_2_feature: None | str | Unset = UNSET
    boundary_3_lat: None | str | Unset = UNSET
    boundary_3_long: None | str | Unset = UNSET
    boundary_3_feature: None | str | Unset = UNSET
    boundary_4_lat: None | str | Unset = UNSET
    boundary_4_long: None | str | Unset = UNSET
    boundary_4_feature: None | str | Unset = UNSET
    boundary_5_lat: None | str | Unset = UNSET
    boundary_5_long: None | str | Unset = UNSET
    boundary_5_feature: None | str | Unset = UNSET
    boundary_6_lat: None | str | Unset = UNSET
    boundary_6_long: None | str | Unset = UNSET
    boundary_6_feature: None | str | Unset = UNSET
    boundary_7_lat: None | str | Unset = UNSET
    boundary_7_long: None | str | Unset = UNSET
    boundary_7_feature: None | str | Unset = UNSET
    link: None | str | Unset = UNSET
    remarks: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        paragliding_area_en: None | str | Unset
        if isinstance(self.paragliding_area_en, Unset):
            paragliding_area_en = UNSET
        else:
            paragliding_area_en = self.paragliding_area_en

        paragliding_area_tc: None | str | Unset
        if isinstance(self.paragliding_area_tc, Unset):
            paragliding_area_tc = UNSET
        else:
            paragliding_area_tc = self.paragliding_area_tc

        paragliding_area_sc: None | str | Unset
        if isinstance(self.paragliding_area_sc, Unset):
            paragliding_area_sc = UNSET
        else:
            paragliding_area_sc = self.paragliding_area_sc

        operating_altitude: None | str | Unset
        if isinstance(self.operating_altitude, Unset):
            operating_altitude = UNSET
        else:
            operating_altitude = self.operating_altitude

        latitude: None | str | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: None | str | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        boundary_1_lat: None | str | Unset
        if isinstance(self.boundary_1_lat, Unset):
            boundary_1_lat = UNSET
        else:
            boundary_1_lat = self.boundary_1_lat

        boundary_1_long: None | str | Unset
        if isinstance(self.boundary_1_long, Unset):
            boundary_1_long = UNSET
        else:
            boundary_1_long = self.boundary_1_long

        boundary_1_feature: None | str | Unset
        if isinstance(self.boundary_1_feature, Unset):
            boundary_1_feature = UNSET
        else:
            boundary_1_feature = self.boundary_1_feature

        boundary_2_lat: None | str | Unset
        if isinstance(self.boundary_2_lat, Unset):
            boundary_2_lat = UNSET
        else:
            boundary_2_lat = self.boundary_2_lat

        boundary_2_long: None | str | Unset
        if isinstance(self.boundary_2_long, Unset):
            boundary_2_long = UNSET
        else:
            boundary_2_long = self.boundary_2_long

        boundary_2_feature: None | str | Unset
        if isinstance(self.boundary_2_feature, Unset):
            boundary_2_feature = UNSET
        else:
            boundary_2_feature = self.boundary_2_feature

        boundary_3_lat: None | str | Unset
        if isinstance(self.boundary_3_lat, Unset):
            boundary_3_lat = UNSET
        else:
            boundary_3_lat = self.boundary_3_lat

        boundary_3_long: None | str | Unset
        if isinstance(self.boundary_3_long, Unset):
            boundary_3_long = UNSET
        else:
            boundary_3_long = self.boundary_3_long

        boundary_3_feature: None | str | Unset
        if isinstance(self.boundary_3_feature, Unset):
            boundary_3_feature = UNSET
        else:
            boundary_3_feature = self.boundary_3_feature

        boundary_4_lat: None | str | Unset
        if isinstance(self.boundary_4_lat, Unset):
            boundary_4_lat = UNSET
        else:
            boundary_4_lat = self.boundary_4_lat

        boundary_4_long: None | str | Unset
        if isinstance(self.boundary_4_long, Unset):
            boundary_4_long = UNSET
        else:
            boundary_4_long = self.boundary_4_long

        boundary_4_feature: None | str | Unset
        if isinstance(self.boundary_4_feature, Unset):
            boundary_4_feature = UNSET
        else:
            boundary_4_feature = self.boundary_4_feature

        boundary_5_lat: None | str | Unset
        if isinstance(self.boundary_5_lat, Unset):
            boundary_5_lat = UNSET
        else:
            boundary_5_lat = self.boundary_5_lat

        boundary_5_long: None | str | Unset
        if isinstance(self.boundary_5_long, Unset):
            boundary_5_long = UNSET
        else:
            boundary_5_long = self.boundary_5_long

        boundary_5_feature: None | str | Unset
        if isinstance(self.boundary_5_feature, Unset):
            boundary_5_feature = UNSET
        else:
            boundary_5_feature = self.boundary_5_feature

        boundary_6_lat: None | str | Unset
        if isinstance(self.boundary_6_lat, Unset):
            boundary_6_lat = UNSET
        else:
            boundary_6_lat = self.boundary_6_lat

        boundary_6_long: None | str | Unset
        if isinstance(self.boundary_6_long, Unset):
            boundary_6_long = UNSET
        else:
            boundary_6_long = self.boundary_6_long

        boundary_6_feature: None | str | Unset
        if isinstance(self.boundary_6_feature, Unset):
            boundary_6_feature = UNSET
        else:
            boundary_6_feature = self.boundary_6_feature

        boundary_7_lat: None | str | Unset
        if isinstance(self.boundary_7_lat, Unset):
            boundary_7_lat = UNSET
        else:
            boundary_7_lat = self.boundary_7_lat

        boundary_7_long: None | str | Unset
        if isinstance(self.boundary_7_long, Unset):
            boundary_7_long = UNSET
        else:
            boundary_7_long = self.boundary_7_long

        boundary_7_feature: None | str | Unset
        if isinstance(self.boundary_7_feature, Unset):
            boundary_7_feature = UNSET
        else:
            boundary_7_feature = self.boundary_7_feature

        link: None | str | Unset
        if isinstance(self.link, Unset):
            link = UNSET
        else:
            link = self.link

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if paragliding_area_en is not UNSET:
            field_dict["Paragliding_Area_EN"] = paragliding_area_en
        if paragliding_area_tc is not UNSET:
            field_dict["Paragliding_Area_TC"] = paragliding_area_tc
        if paragliding_area_sc is not UNSET:
            field_dict["Paragliding_Area_SC"] = paragliding_area_sc
        if operating_altitude is not UNSET:
            field_dict["Operating_Altitude"] = operating_altitude
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if boundary_1_lat is not UNSET:
            field_dict["Boundary_1_Lat"] = boundary_1_lat
        if boundary_1_long is not UNSET:
            field_dict["Boundary_1_Long"] = boundary_1_long
        if boundary_1_feature is not UNSET:
            field_dict["Boundary_1_feature"] = boundary_1_feature
        if boundary_2_lat is not UNSET:
            field_dict["Boundary_2_Lat"] = boundary_2_lat
        if boundary_2_long is not UNSET:
            field_dict["Boundary_2_Long"] = boundary_2_long
        if boundary_2_feature is not UNSET:
            field_dict["Boundary_2_feature"] = boundary_2_feature
        if boundary_3_lat is not UNSET:
            field_dict["Boundary_3_Lat"] = boundary_3_lat
        if boundary_3_long is not UNSET:
            field_dict["Boundary_3_Long"] = boundary_3_long
        if boundary_3_feature is not UNSET:
            field_dict["Boundary_3_feature"] = boundary_3_feature
        if boundary_4_lat is not UNSET:
            field_dict["Boundary_4_Lat"] = boundary_4_lat
        if boundary_4_long is not UNSET:
            field_dict["Boundary_4_Long"] = boundary_4_long
        if boundary_4_feature is not UNSET:
            field_dict["Boundary_4_feature"] = boundary_4_feature
        if boundary_5_lat is not UNSET:
            field_dict["Boundary_5_Lat"] = boundary_5_lat
        if boundary_5_long is not UNSET:
            field_dict["Boundary_5_Long"] = boundary_5_long
        if boundary_5_feature is not UNSET:
            field_dict["Boundary_5_feature"] = boundary_5_feature
        if boundary_6_lat is not UNSET:
            field_dict["Boundary_6_Lat"] = boundary_6_lat
        if boundary_6_long is not UNSET:
            field_dict["Boundary_6_Long"] = boundary_6_long
        if boundary_6_feature is not UNSET:
            field_dict["Boundary_6_feature"] = boundary_6_feature
        if boundary_7_lat is not UNSET:
            field_dict["Boundary_7_Lat"] = boundary_7_lat
        if boundary_7_long is not UNSET:
            field_dict["Boundary_7_Long"] = boundary_7_long
        if boundary_7_feature is not UNSET:
            field_dict["Boundary_7_feature"] = boundary_7_feature
        if link is not UNSET:
            field_dict["Link"] = link
        if remarks is not UNSET:
            field_dict["Remarks"] = remarks
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_paragliding_area_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        paragliding_area_en = _parse_paragliding_area_en(
            d.pop("Paragliding_Area_EN", UNSET)
        )

        def _parse_paragliding_area_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        paragliding_area_tc = _parse_paragliding_area_tc(
            d.pop("Paragliding_Area_TC", UNSET)
        )

        def _parse_paragliding_area_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        paragliding_area_sc = _parse_paragliding_area_sc(
            d.pop("Paragliding_Area_SC", UNSET)
        )

        def _parse_operating_altitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operating_altitude = _parse_operating_altitude(
            d.pop("Operating_Altitude", UNSET)
        )

        def _parse_latitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_longitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        def _parse_boundary_1_lat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_1_lat = _parse_boundary_1_lat(d.pop("Boundary_1_Lat", UNSET))

        def _parse_boundary_1_long(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_1_long = _parse_boundary_1_long(d.pop("Boundary_1_Long", UNSET))

        def _parse_boundary_1_feature(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_1_feature = _parse_boundary_1_feature(
            d.pop("Boundary_1_feature", UNSET)
        )

        def _parse_boundary_2_lat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_2_lat = _parse_boundary_2_lat(d.pop("Boundary_2_Lat", UNSET))

        def _parse_boundary_2_long(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_2_long = _parse_boundary_2_long(d.pop("Boundary_2_Long", UNSET))

        def _parse_boundary_2_feature(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_2_feature = _parse_boundary_2_feature(
            d.pop("Boundary_2_feature", UNSET)
        )

        def _parse_boundary_3_lat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_3_lat = _parse_boundary_3_lat(d.pop("Boundary_3_Lat", UNSET))

        def _parse_boundary_3_long(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_3_long = _parse_boundary_3_long(d.pop("Boundary_3_Long", UNSET))

        def _parse_boundary_3_feature(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_3_feature = _parse_boundary_3_feature(
            d.pop("Boundary_3_feature", UNSET)
        )

        def _parse_boundary_4_lat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_4_lat = _parse_boundary_4_lat(d.pop("Boundary_4_Lat", UNSET))

        def _parse_boundary_4_long(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_4_long = _parse_boundary_4_long(d.pop("Boundary_4_Long", UNSET))

        def _parse_boundary_4_feature(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_4_feature = _parse_boundary_4_feature(
            d.pop("Boundary_4_feature", UNSET)
        )

        def _parse_boundary_5_lat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_5_lat = _parse_boundary_5_lat(d.pop("Boundary_5_Lat", UNSET))

        def _parse_boundary_5_long(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_5_long = _parse_boundary_5_long(d.pop("Boundary_5_Long", UNSET))

        def _parse_boundary_5_feature(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_5_feature = _parse_boundary_5_feature(
            d.pop("Boundary_5_feature", UNSET)
        )

        def _parse_boundary_6_lat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_6_lat = _parse_boundary_6_lat(d.pop("Boundary_6_Lat", UNSET))

        def _parse_boundary_6_long(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_6_long = _parse_boundary_6_long(d.pop("Boundary_6_Long", UNSET))

        def _parse_boundary_6_feature(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_6_feature = _parse_boundary_6_feature(
            d.pop("Boundary_6_feature", UNSET)
        )

        def _parse_boundary_7_lat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_7_lat = _parse_boundary_7_lat(d.pop("Boundary_7_Lat", UNSET))

        def _parse_boundary_7_long(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_7_long = _parse_boundary_7_long(d.pop("Boundary_7_Long", UNSET))

        def _parse_boundary_7_feature(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_7_feature = _parse_boundary_7_feature(
            d.pop("Boundary_7_feature", UNSET)
        )

        def _parse_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        link = _parse_link(d.pop("Link", UNSET))

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("Remarks", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            paragliding_area_en=paragliding_area_en,
            paragliding_area_tc=paragliding_area_tc,
            paragliding_area_sc=paragliding_area_sc,
            operating_altitude=operating_altitude,
            latitude=latitude,
            longitude=longitude,
            boundary_1_lat=boundary_1_lat,
            boundary_1_long=boundary_1_long,
            boundary_1_feature=boundary_1_feature,
            boundary_2_lat=boundary_2_lat,
            boundary_2_long=boundary_2_long,
            boundary_2_feature=boundary_2_feature,
            boundary_3_lat=boundary_3_lat,
            boundary_3_long=boundary_3_long,
            boundary_3_feature=boundary_3_feature,
            boundary_4_lat=boundary_4_lat,
            boundary_4_long=boundary_4_long,
            boundary_4_feature=boundary_4_feature,
            boundary_5_lat=boundary_5_lat,
            boundary_5_long=boundary_5_long,
            boundary_5_feature=boundary_5_feature,
            boundary_6_lat=boundary_6_lat,
            boundary_6_long=boundary_6_long,
            boundary_6_feature=boundary_6_feature,
            boundary_7_lat=boundary_7_lat,
            boundary_7_long=boundary_7_long,
            boundary_7_feature=boundary_7_feature,
            link=link,
            remarks=remarks,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfsgeotagging_attributes.additional_properties = d
        return wfs_map_server_wfsgeotagging_attributes

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
