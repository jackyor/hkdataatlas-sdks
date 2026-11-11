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
        stn_no (None | str | Unset): Publisher field type: esriFieldTypeString
        locality (None | str | Unset): Publisher field type: esriFieldTypeString
        monu_type (None | str | Unset): Publisher field type: esriFieldTypeString
        hkpd_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lat_deg (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lat_min (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lat_sec (float | None | Unset): Publisher field type: esriFieldTypeDouble
        long_deg (float | None | Unset): Publisher field type: esriFieldTypeDouble
        long_min (float | None | Unset): Publisher field type: esriFieldTypeDouble
        long_sec (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wgs_level (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wgs_svy (None | str | Unset): Publisher field type: esriFieldTypeString
        frame (None | str | Unset): Publisher field type: esriFieldTypeString
        by_transfo (None | str | Unset): Publisher field type: esriFieldTypeString
        ori_transf (None | str | Unset): Publisher field type: esriFieldTypeString
        cla_acurcy (None | str | Unset): Publisher field type: esriFieldTypeString
        gps_acurcy (None | str | Unset): Publisher field type: esriFieldTypeString
        lev_acurcy (None | str | Unset): Publisher field type: esriFieldTypeString
        easting_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        northing_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    stn_no: None | str | Unset = UNSET
    locality: None | str | Unset = UNSET
    monu_type: None | str | Unset = UNSET
    hkpd_m: float | None | Unset = UNSET
    lat_deg: float | None | Unset = UNSET
    lat_min: float | None | Unset = UNSET
    lat_sec: float | None | Unset = UNSET
    long_deg: float | None | Unset = UNSET
    long_min: float | None | Unset = UNSET
    long_sec: float | None | Unset = UNSET
    wgs_level: float | None | Unset = UNSET
    wgs_svy: None | str | Unset = UNSET
    frame: None | str | Unset = UNSET
    by_transfo: None | str | Unset = UNSET
    ori_transf: None | str | Unset = UNSET
    cla_acurcy: None | str | Unset = UNSET
    gps_acurcy: None | str | Unset = UNSET
    lev_acurcy: None | str | Unset = UNSET
    easting_m: float | None | Unset = UNSET
    northing_m: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        stn_no: None | str | Unset
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

        lat_deg: float | None | Unset
        if isinstance(self.lat_deg, Unset):
            lat_deg = UNSET
        else:
            lat_deg = self.lat_deg

        lat_min: float | None | Unset
        if isinstance(self.lat_min, Unset):
            lat_min = UNSET
        else:
            lat_min = self.lat_min

        lat_sec: float | None | Unset
        if isinstance(self.lat_sec, Unset):
            lat_sec = UNSET
        else:
            lat_sec = self.lat_sec

        long_deg: float | None | Unset
        if isinstance(self.long_deg, Unset):
            long_deg = UNSET
        else:
            long_deg = self.long_deg

        long_min: float | None | Unset
        if isinstance(self.long_min, Unset):
            long_min = UNSET
        else:
            long_min = self.long_min

        long_sec: float | None | Unset
        if isinstance(self.long_sec, Unset):
            long_sec = UNSET
        else:
            long_sec = self.long_sec

        wgs_level: float | None | Unset
        if isinstance(self.wgs_level, Unset):
            wgs_level = UNSET
        else:
            wgs_level = self.wgs_level

        wgs_svy: None | str | Unset
        if isinstance(self.wgs_svy, Unset):
            wgs_svy = UNSET
        else:
            wgs_svy = self.wgs_svy

        frame: None | str | Unset
        if isinstance(self.frame, Unset):
            frame = UNSET
        else:
            frame = self.frame

        by_transfo: None | str | Unset
        if isinstance(self.by_transfo, Unset):
            by_transfo = UNSET
        else:
            by_transfo = self.by_transfo

        ori_transf: None | str | Unset
        if isinstance(self.ori_transf, Unset):
            ori_transf = UNSET
        else:
            ori_transf = self.ori_transf

        cla_acurcy: None | str | Unset
        if isinstance(self.cla_acurcy, Unset):
            cla_acurcy = UNSET
        else:
            cla_acurcy = self.cla_acurcy

        gps_acurcy: None | str | Unset
        if isinstance(self.gps_acurcy, Unset):
            gps_acurcy = UNSET
        else:
            gps_acurcy = self.gps_acurcy

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
        if lat_deg is not UNSET:
            field_dict["LAT_DEG"] = lat_deg
        if lat_min is not UNSET:
            field_dict["LAT_MIN"] = lat_min
        if lat_sec is not UNSET:
            field_dict["LAT_SEC"] = lat_sec
        if long_deg is not UNSET:
            field_dict["LONG_DEG"] = long_deg
        if long_min is not UNSET:
            field_dict["LONG_MIN"] = long_min
        if long_sec is not UNSET:
            field_dict["LONG_SEC"] = long_sec
        if wgs_level is not UNSET:
            field_dict["WGS_LEVEL"] = wgs_level
        if wgs_svy is not UNSET:
            field_dict["WGS_SVY"] = wgs_svy
        if frame is not UNSET:
            field_dict["FRAME"] = frame
        if by_transfo is not UNSET:
            field_dict["BY_TRANSFO"] = by_transfo
        if ori_transf is not UNSET:
            field_dict["ORI_TRANSF"] = ori_transf
        if cla_acurcy is not UNSET:
            field_dict["CLA_ACURCY"] = cla_acurcy
        if gps_acurcy is not UNSET:
            field_dict["GPS_ACURCY"] = gps_acurcy
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
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_stn_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

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

        def _parse_lat_deg(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lat_deg = _parse_lat_deg(d.pop("LAT_DEG", UNSET))

        def _parse_lat_min(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lat_min = _parse_lat_min(d.pop("LAT_MIN", UNSET))

        def _parse_lat_sec(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lat_sec = _parse_lat_sec(d.pop("LAT_SEC", UNSET))

        def _parse_long_deg(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        long_deg = _parse_long_deg(d.pop("LONG_DEG", UNSET))

        def _parse_long_min(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        long_min = _parse_long_min(d.pop("LONG_MIN", UNSET))

        def _parse_long_sec(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        long_sec = _parse_long_sec(d.pop("LONG_SEC", UNSET))

        def _parse_wgs_level(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wgs_level = _parse_wgs_level(d.pop("WGS_LEVEL", UNSET))

        def _parse_wgs_svy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wgs_svy = _parse_wgs_svy(d.pop("WGS_SVY", UNSET))

        def _parse_frame(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        frame = _parse_frame(d.pop("FRAME", UNSET))

        def _parse_by_transfo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        by_transfo = _parse_by_transfo(d.pop("BY_TRANSFO", UNSET))

        def _parse_ori_transf(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ori_transf = _parse_ori_transf(d.pop("ORI_TRANSF", UNSET))

        def _parse_cla_acurcy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cla_acurcy = _parse_cla_acurcy(d.pop("CLA_ACURCY", UNSET))

        def _parse_gps_acurcy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gps_acurcy = _parse_gps_acurcy(d.pop("GPS_ACURCY", UNSET))

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

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            stn_no=stn_no,
            locality=locality,
            monu_type=monu_type,
            hkpd_m=hkpd_m,
            lat_deg=lat_deg,
            lat_min=lat_min,
            lat_sec=lat_sec,
            long_deg=long_deg,
            long_min=long_min,
            long_sec=long_sec,
            wgs_level=wgs_level,
            wgs_svy=wgs_svy,
            frame=frame,
            by_transfo=by_transfo,
            ori_transf=ori_transf,
            cla_acurcy=cla_acurcy,
            gps_acurcy=gps_acurcy,
            lev_acurcy=lev_acurcy,
            easting_m=easting_m,
            northing_m=northing_m,
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
