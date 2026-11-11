from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsstreetCtroutputAttributes")


@_attrs_define
class WfsMapServerWfsstreetCtroutputAttributes:
    """
    Attributes:
        spot_id (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        loc_des_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        loc_des_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        loc_des_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        opening_hr (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        dlo_code (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        northing (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        easting (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiPointPropertyType; JSON geometry is not inferred from its
            XML type.
    """

    spot_id: None | str | Unset = UNSET
    loc_des_en: None | str | Unset = UNSET
    loc_des_tc: None | str | Unset = UNSET
    loc_des_sc: None | str | Unset = UNSET
    opening_hr: None | str | Unset = UNSET
    dlo_code: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    easting: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spot_id: None | str | Unset
        if isinstance(self.spot_id, Unset):
            spot_id = UNSET
        else:
            spot_id = self.spot_id

        loc_des_en: None | str | Unset
        if isinstance(self.loc_des_en, Unset):
            loc_des_en = UNSET
        else:
            loc_des_en = self.loc_des_en

        loc_des_tc: None | str | Unset
        if isinstance(self.loc_des_tc, Unset):
            loc_des_tc = UNSET
        else:
            loc_des_tc = self.loc_des_tc

        loc_des_sc: None | str | Unset
        if isinstance(self.loc_des_sc, Unset):
            loc_des_sc = UNSET
        else:
            loc_des_sc = self.loc_des_sc

        opening_hr: None | str | Unset
        if isinstance(self.opening_hr, Unset):
            opening_hr = UNSET
        else:
            opening_hr = self.opening_hr

        dlo_code: None | str | Unset
        if isinstance(self.dlo_code, Unset):
            dlo_code = UNSET
        else:
            dlo_code = self.dlo_code

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if spot_id is not UNSET:
            field_dict["spot_id"] = spot_id
        if loc_des_en is not UNSET:
            field_dict["loc_des_en"] = loc_des_en
        if loc_des_tc is not UNSET:
            field_dict["loc_des_tc"] = loc_des_tc
        if loc_des_sc is not UNSET:
            field_dict["loc_des_sc"] = loc_des_sc
        if opening_hr is not UNSET:
            field_dict["opening_hr"] = opening_hr
        if dlo_code is not UNSET:
            field_dict["dlo_code"] = dlo_code
        if northing is not UNSET:
            field_dict["northing"] = northing
        if easting is not UNSET:
            field_dict["easting"] = easting
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_spot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        spot_id = _parse_spot_id(d.pop("spot_id", UNSET))

        def _parse_loc_des_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        loc_des_en = _parse_loc_des_en(d.pop("loc_des_en", UNSET))

        def _parse_loc_des_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        loc_des_tc = _parse_loc_des_tc(d.pop("loc_des_tc", UNSET))

        def _parse_loc_des_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        loc_des_sc = _parse_loc_des_sc(d.pop("loc_des_sc", UNSET))

        def _parse_opening_hr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hr = _parse_opening_hr(d.pop("opening_hr", UNSET))

        def _parse_dlo_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dlo_code = _parse_dlo_code(d.pop("dlo_code", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("northing", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("easting", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsstreet_ctroutput_attributes = cls(
            spot_id=spot_id,
            loc_des_en=loc_des_en,
            loc_des_tc=loc_des_tc,
            loc_des_sc=loc_des_sc,
            opening_hr=opening_hr,
            dlo_code=dlo_code,
            northing=northing,
            easting=easting,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfsstreet_ctroutput_attributes.additional_properties = d
        return wfs_map_server_wfsstreet_ctroutput_attributes

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
