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
        rec_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        location (None | str | Unset): Publisher field type: esriFieldTypeString
        location_c (None | str | Unset): Publisher field type: esriFieldTypeString
        x_coord (float | None | Unset): Publisher field type: esriFieldTypeDouble
        y_coord (float | None | Unset): Publisher field type: esriFieldTypeDouble
        diameter (float | None | Unset): Publisher field type: esriFieldTypeDouble
        water_type (None | str | Unset): Publisher field type: esriFieldTypeString
        time_receipt (float | None | Unset): Publisher field type: esriFieldTypeDouble
        time_supply (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    rec_date: Any | Unset = UNSET
    location: None | str | Unset = UNSET
    location_c: None | str | Unset = UNSET
    x_coord: float | None | Unset = UNSET
    y_coord: float | None | Unset = UNSET
    diameter: float | None | Unset = UNSET
    water_type: None | str | Unset = UNSET
    time_receipt: float | None | Unset = UNSET
    time_supply: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        rec_date = self.rec_date

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        location_c: None | str | Unset
        if isinstance(self.location_c, Unset):
            location_c = UNSET
        else:
            location_c = self.location_c

        x_coord: float | None | Unset
        if isinstance(self.x_coord, Unset):
            x_coord = UNSET
        else:
            x_coord = self.x_coord

        y_coord: float | None | Unset
        if isinstance(self.y_coord, Unset):
            y_coord = UNSET
        else:
            y_coord = self.y_coord

        diameter: float | None | Unset
        if isinstance(self.diameter, Unset):
            diameter = UNSET
        else:
            diameter = self.diameter

        water_type: None | str | Unset
        if isinstance(self.water_type, Unset):
            water_type = UNSET
        else:
            water_type = self.water_type

        time_receipt: float | None | Unset
        if isinstance(self.time_receipt, Unset):
            time_receipt = UNSET
        else:
            time_receipt = self.time_receipt

        time_supply: None | str | Unset
        if isinstance(self.time_supply, Unset):
            time_supply = UNSET
        else:
            time_supply = self.time_supply

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if rec_date is not UNSET:
            field_dict["REC_DATE"] = rec_date
        if location is not UNSET:
            field_dict["LOCATION"] = location
        if location_c is not UNSET:
            field_dict["LOCATION_C"] = location_c
        if x_coord is not UNSET:
            field_dict["X_COORD"] = x_coord
        if y_coord is not UNSET:
            field_dict["Y_COORD"] = y_coord
        if diameter is not UNSET:
            field_dict["DIAMETER"] = diameter
        if water_type is not UNSET:
            field_dict["WATER_TYPE"] = water_type
        if time_receipt is not UNSET:
            field_dict["TIME_RECEIPT"] = time_receipt
        if time_supply is not UNSET:
            field_dict["TIME_SUPPLY"] = time_supply

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        rec_date = d.pop("REC_DATE", UNSET)

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("LOCATION", UNSET))

        def _parse_location_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_c = _parse_location_c(d.pop("LOCATION_C", UNSET))

        def _parse_x_coord(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        x_coord = _parse_x_coord(d.pop("X_COORD", UNSET))

        def _parse_y_coord(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        y_coord = _parse_y_coord(d.pop("Y_COORD", UNSET))

        def _parse_diameter(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        diameter = _parse_diameter(d.pop("DIAMETER", UNSET))

        def _parse_water_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        water_type = _parse_water_type(d.pop("WATER_TYPE", UNSET))

        def _parse_time_receipt(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        time_receipt = _parse_time_receipt(d.pop("TIME_RECEIPT", UNSET))

        def _parse_time_supply(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_supply = _parse_time_supply(d.pop("TIME_SUPPLY", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            rec_date=rec_date,
            location=location,
            location_c=location_c,
            x_coord=x_coord,
            y_coord=y_coord,
            diameter=diameter,
            water_type=water_type,
            time_receipt=time_receipt,
            time_supply=time_supply,
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
