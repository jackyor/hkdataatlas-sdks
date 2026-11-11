from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsBMpointAttributes")


@_attrs_define
class WfsMapServerWfsBMpointAttributes:
    """
    Attributes:
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        stn_no (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        locality (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        monu_type (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        hkpd_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        cla_acurcy (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        lev_acurcy (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        easting_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        northing_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    shape: Any | Unset = UNSET
    objectid: int | Unset = UNSET
    stn_no: float | None | Unset = UNSET
    locality: None | str | Unset = UNSET
    monu_type: None | str | Unset = UNSET
    hkpd_m: float | None | Unset = UNSET
    cla_acurcy: None | str | Unset = UNSET
    lev_acurcy: None | str | Unset = UNSET
    easting_m: float | None | Unset = UNSET
    northing_m: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shape = self.shape

        objectid = self.objectid

        stn_no: float | None | Unset
        if isinstance(self.stn_no, Unset):
            stn_no = UNSET
        else:
            stn_no = self.stn_no

        locality: None | str | Unset
        if isinstance(self.locality, Unset):
            locality = UNSET
        else:
            locality = self.locality

        monu_type: None | str | Unset
        if isinstance(self.monu_type, Unset):
            monu_type = UNSET
        else:
            monu_type = self.monu_type

        hkpd_m: float | None | Unset
        if isinstance(self.hkpd_m, Unset):
            hkpd_m = UNSET
        else:
            hkpd_m = self.hkpd_m

        cla_acurcy: None | str | Unset
        if isinstance(self.cla_acurcy, Unset):
            cla_acurcy = UNSET
        else:
            cla_acurcy = self.cla_acurcy

        lev_acurcy: None | str | Unset
        if isinstance(self.lev_acurcy, Unset):
            lev_acurcy = UNSET
        else:
            lev_acurcy = self.lev_acurcy

        easting_m: float | None | Unset
        if isinstance(self.easting_m, Unset):
            easting_m = UNSET
        else:
            easting_m = self.easting_m

        northing_m: float | None | Unset
        if isinstance(self.northing_m, Unset):
            northing_m = UNSET
        else:
            northing_m = self.northing_m

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if stn_no is not UNSET:
            field_dict["STN_NO"] = stn_no
        if locality is not UNSET:
            field_dict["LOCALITY"] = locality
        if monu_type is not UNSET:
            field_dict["MONU_TYPE"] = monu_type
        if hkpd_m is not UNSET:
            field_dict["HKPD_m"] = hkpd_m
        if cla_acurcy is not UNSET:
            field_dict["CLA_ACURCY"] = cla_acurcy
        if lev_acurcy is not UNSET:
            field_dict["LEV_ACURCY"] = lev_acurcy
        if easting_m is not UNSET:
            field_dict["Easting_m"] = easting_m
        if northing_m is not UNSET:
            field_dict["Northing_m"] = northing_m

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        shape = d.pop("SHAPE", UNSET)

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_stn_no(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        stn_no = _parse_stn_no(d.pop("STN_NO", UNSET))

        def _parse_locality(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locality = _parse_locality(d.pop("LOCALITY", UNSET))

        def _parse_monu_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        monu_type = _parse_monu_type(d.pop("MONU_TYPE", UNSET))

        def _parse_hkpd_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hkpd_m = _parse_hkpd_m(d.pop("HKPD_m", UNSET))

        def _parse_cla_acurcy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cla_acurcy = _parse_cla_acurcy(d.pop("CLA_ACURCY", UNSET))

        def _parse_lev_acurcy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lev_acurcy = _parse_lev_acurcy(d.pop("LEV_ACURCY", UNSET))

        def _parse_easting_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting_m = _parse_easting_m(d.pop("Easting_m", UNSET))

        def _parse_northing_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing_m = _parse_northing_m(d.pop("Northing_m", UNSET))

        wfs_map_server_wfs_b_mpoint_attributes = cls(
            shape=shape,
            objectid=objectid,
            stn_no=stn_no,
            locality=locality,
            monu_type=monu_type,
            hkpd_m=hkpd_m,
            cla_acurcy=cla_acurcy,
            lev_acurcy=lev_acurcy,
            easting_m=easting_m,
            northing_m=northing_m,
        )

        wfs_map_server_wfs_b_mpoint_attributes.additional_properties = d
        return wfs_map_server_wfs_b_mpoint_attributes

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
