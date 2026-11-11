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
        region (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        district (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        addr_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        addr_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        addr_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        lat (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        lng (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        sm_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        sm_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        sm_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        tel (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        sm_addr_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        sm_addr_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        sm_addr_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    region: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    addr_en: None | str | Unset = UNSET
    addr_tc: None | str | Unset = UNSET
    addr_sc: None | str | Unset = UNSET
    lat: None | str | Unset = UNSET
    lng: None | str | Unset = UNSET
    sm_en: None | str | Unset = UNSET
    sm_tc: None | str | Unset = UNSET
    sm_sc: None | str | Unset = UNSET
    tel: None | str | Unset = UNSET
    sm_addr_en: None | str | Unset = UNSET
    sm_addr_tc: None | str | Unset = UNSET
    sm_addr_sc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        addr_en: None | str | Unset
        if isinstance(self.addr_en, Unset):
            addr_en = UNSET
        else:
            addr_en = self.addr_en

        addr_tc: None | str | Unset
        if isinstance(self.addr_tc, Unset):
            addr_tc = UNSET
        else:
            addr_tc = self.addr_tc

        addr_sc: None | str | Unset
        if isinstance(self.addr_sc, Unset):
            addr_sc = UNSET
        else:
            addr_sc = self.addr_sc

        lat: None | str | Unset
        if isinstance(self.lat, Unset):
            lat = UNSET
        else:
            lat = self.lat

        lng: None | str | Unset
        if isinstance(self.lng, Unset):
            lng = UNSET
        else:
            lng = self.lng

        sm_en: None | str | Unset
        if isinstance(self.sm_en, Unset):
            sm_en = UNSET
        else:
            sm_en = self.sm_en

        sm_tc: None | str | Unset
        if isinstance(self.sm_tc, Unset):
            sm_tc = UNSET
        else:
            sm_tc = self.sm_tc

        sm_sc: None | str | Unset
        if isinstance(self.sm_sc, Unset):
            sm_sc = UNSET
        else:
            sm_sc = self.sm_sc

        tel: None | str | Unset
        if isinstance(self.tel, Unset):
            tel = UNSET
        else:
            tel = self.tel

        sm_addr_en: None | str | Unset
        if isinstance(self.sm_addr_en, Unset):
            sm_addr_en = UNSET
        else:
            sm_addr_en = self.sm_addr_en

        sm_addr_tc: None | str | Unset
        if isinstance(self.sm_addr_tc, Unset):
            sm_addr_tc = UNSET
        else:
            sm_addr_tc = self.sm_addr_tc

        sm_addr_sc: None | str | Unset
        if isinstance(self.sm_addr_sc, Unset):
            sm_addr_sc = UNSET
        else:
            sm_addr_sc = self.sm_addr_sc

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region is not UNSET:
            field_dict["Region"] = region
        if district is not UNSET:
            field_dict["District"] = district
        if addr_en is not UNSET:
            field_dict["addr_en"] = addr_en
        if addr_tc is not UNSET:
            field_dict["addr_tc"] = addr_tc
        if addr_sc is not UNSET:
            field_dict["addr_sc"] = addr_sc
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lng is not UNSET:
            field_dict["lng"] = lng
        if sm_en is not UNSET:
            field_dict["sm_en"] = sm_en
        if sm_tc is not UNSET:
            field_dict["sm_tc"] = sm_tc
        if sm_sc is not UNSET:
            field_dict["sm_sc"] = sm_sc
        if tel is not UNSET:
            field_dict["tel"] = tel
        if sm_addr_en is not UNSET:
            field_dict["sm_addr_en"] = sm_addr_en
        if sm_addr_tc is not UNSET:
            field_dict["sm_addr_tc"] = sm_addr_tc
        if sm_addr_sc is not UNSET:
            field_dict["sm_addr_sc"] = sm_addr_sc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("Region", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("District", UNSET))

        def _parse_addr_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        addr_en = _parse_addr_en(d.pop("addr_en", UNSET))

        def _parse_addr_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        addr_tc = _parse_addr_tc(d.pop("addr_tc", UNSET))

        def _parse_addr_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        addr_sc = _parse_addr_sc(d.pop("addr_sc", UNSET))

        def _parse_lat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lat = _parse_lat(d.pop("lat", UNSET))

        def _parse_lng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lng = _parse_lng(d.pop("lng", UNSET))

        def _parse_sm_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sm_en = _parse_sm_en(d.pop("sm_en", UNSET))

        def _parse_sm_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sm_tc = _parse_sm_tc(d.pop("sm_tc", UNSET))

        def _parse_sm_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sm_sc = _parse_sm_sc(d.pop("sm_sc", UNSET))

        def _parse_tel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tel = _parse_tel(d.pop("tel", UNSET))

        def _parse_sm_addr_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sm_addr_en = _parse_sm_addr_en(d.pop("sm_addr_en", UNSET))

        def _parse_sm_addr_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sm_addr_tc = _parse_sm_addr_tc(d.pop("sm_addr_tc", UNSET))

        def _parse_sm_addr_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sm_addr_sc = _parse_sm_addr_sc(d.pop("sm_addr_sc", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            region=region,
            district=district,
            addr_en=addr_en,
            addr_tc=addr_tc,
            addr_sc=addr_sc,
            lat=lat,
            lng=lng,
            sm_en=sm_en,
            sm_tc=sm_tc,
            sm_sc=sm_sc,
            tel=tel,
            sm_addr_en=sm_addr_en,
            sm_addr_tc=sm_addr_tc,
            sm_addr_sc=sm_addr_sc,
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
