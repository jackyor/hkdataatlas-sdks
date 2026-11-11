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
        addr_eng (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        addr_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        addr_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dataset_eng (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        dataset_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        dataset_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        latitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        longitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        spot_num (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    addr_eng: None | str | Unset = UNSET
    addr_sc: None | str | Unset = UNSET
    addr_tc: None | str | Unset = UNSET
    dataset_eng: None | str | Unset = UNSET
    dataset_sc: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    spot_num: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        addr_eng: None | str | Unset
        if isinstance(self.addr_eng, Unset):
            addr_eng = UNSET
        else:
            addr_eng = self.addr_eng

        addr_sc: None | str | Unset
        if isinstance(self.addr_sc, Unset):
            addr_sc = UNSET
        else:
            addr_sc = self.addr_sc

        addr_tc: None | str | Unset
        if isinstance(self.addr_tc, Unset):
            addr_tc = UNSET
        else:
            addr_tc = self.addr_tc

        dataset_eng: None | str | Unset
        if isinstance(self.dataset_eng, Unset):
            dataset_eng = UNSET
        else:
            dataset_eng = self.dataset_eng

        dataset_sc: None | str | Unset
        if isinstance(self.dataset_sc, Unset):
            dataset_sc = UNSET
        else:
            dataset_sc = self.dataset_sc

        dataset_tc: None | str | Unset
        if isinstance(self.dataset_tc, Unset):
            dataset_tc = UNSET
        else:
            dataset_tc = self.dataset_tc

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

        spot_num: float | None | Unset
        if isinstance(self.spot_num, Unset):
            spot_num = UNSET
        else:
            spot_num = self.spot_num

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if addr_eng is not UNSET:
            field_dict["addr_eng"] = addr_eng
        if addr_sc is not UNSET:
            field_dict["addr_sc"] = addr_sc
        if addr_tc is not UNSET:
            field_dict["addr_tc"] = addr_tc
        if dataset_eng is not UNSET:
            field_dict["dataset_eng"] = dataset_eng
        if dataset_sc is not UNSET:
            field_dict["dataset_sc"] = dataset_sc
        if dataset_tc is not UNSET:
            field_dict["dataset_tc"] = dataset_tc
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if spot_num is not UNSET:
            field_dict["spot_num"] = spot_num
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_addr_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        addr_eng = _parse_addr_eng(d.pop("addr_eng", UNSET))

        def _parse_addr_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        addr_sc = _parse_addr_sc(d.pop("addr_sc", UNSET))

        def _parse_addr_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        addr_tc = _parse_addr_tc(d.pop("addr_tc", UNSET))

        def _parse_dataset_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_eng = _parse_dataset_eng(d.pop("dataset_eng", UNSET))

        def _parse_dataset_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_sc = _parse_dataset_sc(d.pop("dataset_sc", UNSET))

        def _parse_dataset_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_tc = _parse_dataset_tc(d.pop("dataset_tc", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        def _parse_spot_num(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        spot_num = _parse_spot_num(d.pop("spot_num", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            addr_eng=addr_eng,
            addr_sc=addr_sc,
            addr_tc=addr_tc,
            dataset_eng=dataset_eng,
            dataset_sc=dataset_sc,
            dataset_tc=dataset_tc,
            latitude=latitude,
            longitude=longitude,
            spot_num=spot_num,
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
