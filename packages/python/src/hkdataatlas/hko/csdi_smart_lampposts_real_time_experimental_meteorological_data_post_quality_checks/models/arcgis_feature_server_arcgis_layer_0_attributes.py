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
        data_type_collected_01 (None | str | Unset): Publisher field type: esriFieldTypeString
        data_type_collected_02 (None | str | Unset): Publisher field type: esriFieldTypeString
        data_type_collected_04 (None | str | Unset): Publisher field type: esriFieldTypeString
        device_01_data_url (None | str | Unset): Publisher field type: esriFieldTypeString
        device_02_data_url (None | str | Unset): Publisher field type: esriFieldTypeString
        device_04_data_url (None | str | Unset): Publisher field type: esriFieldTypeString
        device_type_name_01 (None | str | Unset): Publisher field type: esriFieldTypeString
        device_type_name_02 (None | str | Unset): Publisher field type: esriFieldTypeString
        device_type_name_04 (None | str | Unset): Publisher field type: esriFieldTypeString
        lp_east (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lp_latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lp_longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lp_north (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lp_number (None | str | Unset): Publisher field type: esriFieldTypeString
        lp_type (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lp_type_name (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    data_type_collected_01: None | str | Unset = UNSET
    data_type_collected_02: None | str | Unset = UNSET
    data_type_collected_04: None | str | Unset = UNSET
    device_01_data_url: None | str | Unset = UNSET
    device_02_data_url: None | str | Unset = UNSET
    device_04_data_url: None | str | Unset = UNSET
    device_type_name_01: None | str | Unset = UNSET
    device_type_name_02: None | str | Unset = UNSET
    device_type_name_04: None | str | Unset = UNSET
    lp_east: float | None | Unset = UNSET
    lp_latitude: float | None | Unset = UNSET
    lp_longitude: float | None | Unset = UNSET
    lp_north: float | None | Unset = UNSET
    lp_number: None | str | Unset = UNSET
    lp_type: float | None | Unset = UNSET
    lp_type_name: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_type_collected_01: None | str | Unset
        if isinstance(self.data_type_collected_01, Unset):
            data_type_collected_01 = UNSET
        else:
            data_type_collected_01 = self.data_type_collected_01

        data_type_collected_02: None | str | Unset
        if isinstance(self.data_type_collected_02, Unset):
            data_type_collected_02 = UNSET
        else:
            data_type_collected_02 = self.data_type_collected_02

        data_type_collected_04: None | str | Unset
        if isinstance(self.data_type_collected_04, Unset):
            data_type_collected_04 = UNSET
        else:
            data_type_collected_04 = self.data_type_collected_04

        device_01_data_url: None | str | Unset
        if isinstance(self.device_01_data_url, Unset):
            device_01_data_url = UNSET
        else:
            device_01_data_url = self.device_01_data_url

        device_02_data_url: None | str | Unset
        if isinstance(self.device_02_data_url, Unset):
            device_02_data_url = UNSET
        else:
            device_02_data_url = self.device_02_data_url

        device_04_data_url: None | str | Unset
        if isinstance(self.device_04_data_url, Unset):
            device_04_data_url = UNSET
        else:
            device_04_data_url = self.device_04_data_url

        device_type_name_01: None | str | Unset
        if isinstance(self.device_type_name_01, Unset):
            device_type_name_01 = UNSET
        else:
            device_type_name_01 = self.device_type_name_01

        device_type_name_02: None | str | Unset
        if isinstance(self.device_type_name_02, Unset):
            device_type_name_02 = UNSET
        else:
            device_type_name_02 = self.device_type_name_02

        device_type_name_04: None | str | Unset
        if isinstance(self.device_type_name_04, Unset):
            device_type_name_04 = UNSET
        else:
            device_type_name_04 = self.device_type_name_04

        lp_east: float | None | Unset
        if isinstance(self.lp_east, Unset):
            lp_east = UNSET
        else:
            lp_east = self.lp_east

        lp_latitude: float | None | Unset
        if isinstance(self.lp_latitude, Unset):
            lp_latitude = UNSET
        else:
            lp_latitude = self.lp_latitude

        lp_longitude: float | None | Unset
        if isinstance(self.lp_longitude, Unset):
            lp_longitude = UNSET
        else:
            lp_longitude = self.lp_longitude

        lp_north: float | None | Unset
        if isinstance(self.lp_north, Unset):
            lp_north = UNSET
        else:
            lp_north = self.lp_north

        lp_number: None | str | Unset
        if isinstance(self.lp_number, Unset):
            lp_number = UNSET
        else:
            lp_number = self.lp_number

        lp_type: float | None | Unset
        if isinstance(self.lp_type, Unset):
            lp_type = UNSET
        else:
            lp_type = self.lp_type

        lp_type_name: None | str | Unset
        if isinstance(self.lp_type_name, Unset):
            lp_type_name = UNSET
        else:
            lp_type_name = self.lp_type_name

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_type_collected_01 is not UNSET:
            field_dict["DATA_TYPE_COLLECTED_01"] = data_type_collected_01
        if data_type_collected_02 is not UNSET:
            field_dict["DATA_TYPE_COLLECTED_02"] = data_type_collected_02
        if data_type_collected_04 is not UNSET:
            field_dict["DATA_TYPE_COLLECTED_04"] = data_type_collected_04
        if device_01_data_url is not UNSET:
            field_dict["DEVICE_01_DATA_URL"] = device_01_data_url
        if device_02_data_url is not UNSET:
            field_dict["DEVICE_02_DATA_URL"] = device_02_data_url
        if device_04_data_url is not UNSET:
            field_dict["DEVICE_04_DATA_URL"] = device_04_data_url
        if device_type_name_01 is not UNSET:
            field_dict["DEVICE_TYPE_NAME_01"] = device_type_name_01
        if device_type_name_02 is not UNSET:
            field_dict["DEVICE_TYPE_NAME_02"] = device_type_name_02
        if device_type_name_04 is not UNSET:
            field_dict["DEVICE_TYPE_NAME_04"] = device_type_name_04
        if lp_east is not UNSET:
            field_dict["LP_EAST"] = lp_east
        if lp_latitude is not UNSET:
            field_dict["LP_LATITUDE"] = lp_latitude
        if lp_longitude is not UNSET:
            field_dict["LP_LONGITUDE"] = lp_longitude
        if lp_north is not UNSET:
            field_dict["LP_NORTH"] = lp_north
        if lp_number is not UNSET:
            field_dict["LP_NUMBER"] = lp_number
        if lp_type is not UNSET:
            field_dict["LP_TYPE"] = lp_type
        if lp_type_name is not UNSET:
            field_dict["LP_TYPE_NAME"] = lp_type_name
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_data_type_collected_01(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_type_collected_01 = _parse_data_type_collected_01(
            d.pop("DATA_TYPE_COLLECTED_01", UNSET)
        )

        def _parse_data_type_collected_02(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_type_collected_02 = _parse_data_type_collected_02(
            d.pop("DATA_TYPE_COLLECTED_02", UNSET)
        )

        def _parse_data_type_collected_04(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_type_collected_04 = _parse_data_type_collected_04(
            d.pop("DATA_TYPE_COLLECTED_04", UNSET)
        )

        def _parse_device_01_data_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_01_data_url = _parse_device_01_data_url(
            d.pop("DEVICE_01_DATA_URL", UNSET)
        )

        def _parse_device_02_data_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_02_data_url = _parse_device_02_data_url(
            d.pop("DEVICE_02_DATA_URL", UNSET)
        )

        def _parse_device_04_data_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_04_data_url = _parse_device_04_data_url(
            d.pop("DEVICE_04_DATA_URL", UNSET)
        )

        def _parse_device_type_name_01(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_type_name_01 = _parse_device_type_name_01(
            d.pop("DEVICE_TYPE_NAME_01", UNSET)
        )

        def _parse_device_type_name_02(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_type_name_02 = _parse_device_type_name_02(
            d.pop("DEVICE_TYPE_NAME_02", UNSET)
        )

        def _parse_device_type_name_04(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_type_name_04 = _parse_device_type_name_04(
            d.pop("DEVICE_TYPE_NAME_04", UNSET)
        )

        def _parse_lp_east(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lp_east = _parse_lp_east(d.pop("LP_EAST", UNSET))

        def _parse_lp_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lp_latitude = _parse_lp_latitude(d.pop("LP_LATITUDE", UNSET))

        def _parse_lp_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lp_longitude = _parse_lp_longitude(d.pop("LP_LONGITUDE", UNSET))

        def _parse_lp_north(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lp_north = _parse_lp_north(d.pop("LP_NORTH", UNSET))

        def _parse_lp_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lp_number = _parse_lp_number(d.pop("LP_NUMBER", UNSET))

        def _parse_lp_type(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lp_type = _parse_lp_type(d.pop("LP_TYPE", UNSET))

        def _parse_lp_type_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lp_type_name = _parse_lp_type_name(d.pop("LP_TYPE_NAME", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            data_type_collected_01=data_type_collected_01,
            data_type_collected_02=data_type_collected_02,
            data_type_collected_04=data_type_collected_04,
            device_01_data_url=device_01_data_url,
            device_02_data_url=device_02_data_url,
            device_04_data_url=device_04_data_url,
            device_type_name_01=device_type_name_01,
            device_type_name_02=device_type_name_02,
            device_type_name_04=device_type_name_04,
            lp_east=lp_east,
            lp_latitude=lp_latitude,
            lp_longitude=lp_longitude,
            lp_north=lp_north,
            lp_number=lp_number,
            lp_type=lp_type,
            lp_type_name=lp_type_name,
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
