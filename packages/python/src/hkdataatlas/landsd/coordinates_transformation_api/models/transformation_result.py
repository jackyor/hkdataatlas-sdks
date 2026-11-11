from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transformation_result_error_code import (
    TransformationResultErrorCode,
    check_transformation_result_error_code,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TransformationResult")


@_attrs_define
class TransformationResult:
    """Publisher-documented return fields. Height fields marked with an asterisk are omitted when no input height is
    provided. The dictionary does not state that every other field is always present.

        Attributes:
            error_code (TransformationResultErrorCode | Unset): Documented error codes: 1 missing mandatory variable; 2
                unrecognized inSys / outSys value; 3 invalid input value(s); 4 coordinates out of range; 5 identical inSys and
                outSys value; 6 unrecognized northing/easting coordinates of UTM Grid / Grid Reference System; 7 unrecognized
                inUnit / outUnit value.
            hk_e (float | Unset): Easting in HK1980 Grid Coordinates.
            hk_ell_hgt (float | Unset): Ellipsoidal height in HK1980 Geographical Coordinates; omitted if no input height is
                provided.
            hk_lat (float | Unset): Latitude in HK1980 Geographical Coordinates.
            hk_long (float | Unset): Longitude in HK1980 Geographical Coordinates.
            hk_n (float | Unset): Northing in HK1980 Grid Coordinates.
            hkpd (float | Unset): Height above the Hong Kong Principal Datum (HKPD); omitted if no input height is provided.
            utm_grid_e (float | Unset): Easting in UTM Grid System.
            utm_grid_n (float | Unset): Northing in UTM Grid System.
            utm_grid_zone (str | Unset): Zone value in UTM Grid System.
            utm_ref_e (str | Unset): Easting in UTM Grid Reference System.
            utm_ref_n (str | Unset): Northing in UTM Grid Reference System.
            utm_ref_zone (str | Unset): Zone value in UTM Grid Reference System.
            wgs_ell_hgt (float | Unset): Ellipsoidal height in WGS84 Geographical System; omitted if no input height is
                provided.
            wgs_lat (float | Unset): Latitude in WGS84 Geographical Coordinates.
            wgs_long (float | Unset): Longitude in WGS84 Geographical Coordinates.
    """

    error_code: TransformationResultErrorCode | Unset = UNSET
    hk_e: float | Unset = UNSET
    hk_ell_hgt: float | Unset = UNSET
    hk_lat: float | Unset = UNSET
    hk_long: float | Unset = UNSET
    hk_n: float | Unset = UNSET
    hkpd: float | Unset = UNSET
    utm_grid_e: float | Unset = UNSET
    utm_grid_n: float | Unset = UNSET
    utm_grid_zone: str | Unset = UNSET
    utm_ref_e: str | Unset = UNSET
    utm_ref_n: str | Unset = UNSET
    utm_ref_zone: str | Unset = UNSET
    wgs_ell_hgt: float | Unset = UNSET
    wgs_lat: float | Unset = UNSET
    wgs_long: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_code: int | Unset = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code

        hk_e = self.hk_e

        hk_ell_hgt = self.hk_ell_hgt

        hk_lat = self.hk_lat

        hk_long = self.hk_long

        hk_n = self.hk_n

        hkpd = self.hkpd

        utm_grid_e = self.utm_grid_e

        utm_grid_n = self.utm_grid_n

        utm_grid_zone = self.utm_grid_zone

        utm_ref_e = self.utm_ref_e

        utm_ref_n = self.utm_ref_n

        utm_ref_zone = self.utm_ref_zone

        wgs_ell_hgt = self.wgs_ell_hgt

        wgs_lat = self.wgs_lat

        wgs_long = self.wgs_long

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_code is not UNSET:
            field_dict["ErrorCode"] = error_code
        if hk_e is not UNSET:
            field_dict["hkE"] = hk_e
        if hk_ell_hgt is not UNSET:
            field_dict["hkEllHgt"] = hk_ell_hgt
        if hk_lat is not UNSET:
            field_dict["hkLat"] = hk_lat
        if hk_long is not UNSET:
            field_dict["hkLong"] = hk_long
        if hk_n is not UNSET:
            field_dict["hkN"] = hk_n
        if hkpd is not UNSET:
            field_dict["hkpd"] = hkpd
        if utm_grid_e is not UNSET:
            field_dict["utmGridE"] = utm_grid_e
        if utm_grid_n is not UNSET:
            field_dict["utmGridN"] = utm_grid_n
        if utm_grid_zone is not UNSET:
            field_dict["utmGridZone"] = utm_grid_zone
        if utm_ref_e is not UNSET:
            field_dict["utmRefE"] = utm_ref_e
        if utm_ref_n is not UNSET:
            field_dict["utmRefN"] = utm_ref_n
        if utm_ref_zone is not UNSET:
            field_dict["utmRefZone"] = utm_ref_zone
        if wgs_ell_hgt is not UNSET:
            field_dict["wgsEllHgt"] = wgs_ell_hgt
        if wgs_lat is not UNSET:
            field_dict["wgsLat"] = wgs_lat
        if wgs_long is not UNSET:
            field_dict["wgsLong"] = wgs_long

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _error_code = d.pop("ErrorCode", UNSET)
        error_code: TransformationResultErrorCode | Unset
        if isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = check_transformation_result_error_code(_error_code)

        hk_e = d.pop("hkE", UNSET)

        hk_ell_hgt = d.pop("hkEllHgt", UNSET)

        hk_lat = d.pop("hkLat", UNSET)

        hk_long = d.pop("hkLong", UNSET)

        hk_n = d.pop("hkN", UNSET)

        hkpd = d.pop("hkpd", UNSET)

        utm_grid_e = d.pop("utmGridE", UNSET)

        utm_grid_n = d.pop("utmGridN", UNSET)

        utm_grid_zone = d.pop("utmGridZone", UNSET)

        utm_ref_e = d.pop("utmRefE", UNSET)

        utm_ref_n = d.pop("utmRefN", UNSET)

        utm_ref_zone = d.pop("utmRefZone", UNSET)

        wgs_ell_hgt = d.pop("wgsEllHgt", UNSET)

        wgs_lat = d.pop("wgsLat", UNSET)

        wgs_long = d.pop("wgsLong", UNSET)

        transformation_result = cls(
            error_code=error_code,
            hk_e=hk_e,
            hk_ell_hgt=hk_ell_hgt,
            hk_lat=hk_lat,
            hk_long=hk_long,
            hk_n=hk_n,
            hkpd=hkpd,
            utm_grid_e=utm_grid_e,
            utm_grid_n=utm_grid_n,
            utm_grid_zone=utm_grid_zone,
            utm_ref_e=utm_ref_e,
            utm_ref_n=utm_ref_n,
            utm_ref_zone=utm_ref_zone,
            wgs_ell_hgt=wgs_ell_hgt,
            wgs_lat=wgs_lat,
            wgs_long=wgs_long,
        )

        transformation_result.additional_properties = d
        return transformation_result

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
