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
        ogr_fid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        location (None | str | Unset): Publisher field type: esriFieldTypeString
        year (None | str | Unset): Publisher field type: esriFieldTypeString
        hm0 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        h1_10 (None | str | Unset): Publisher field type: esriFieldTypeString
        hmax (float | None | Unset): Publisher field type: esriFieldTypeDouble
        peaktp (float | None | Unset): Publisher field type: esriFieldTypeDouble
        meandir (None | str | Unset): Publisher field type: esriFieldTypeString
        lng (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lat (float | None | Unset): Publisher field type: esriFieldTypeDouble
        fid (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    ogr_fid: int | None | Unset = UNSET
    location: None | str | Unset = UNSET
    year: None | str | Unset = UNSET
    hm0: float | None | Unset = UNSET
    h1_10: None | str | Unset = UNSET
    hmax: float | None | Unset = UNSET
    peaktp: float | None | Unset = UNSET
    meandir: None | str | Unset = UNSET
    lng: float | None | Unset = UNSET
    lat: float | None | Unset = UNSET
    fid: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ogr_fid: int | None | Unset
        if isinstance(self.ogr_fid, Unset):
            ogr_fid = UNSET
        else:
            ogr_fid = self.ogr_fid

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        year: None | str | Unset
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        hm0: float | None | Unset
        if isinstance(self.hm0, Unset):
            hm0 = UNSET
        else:
            hm0 = self.hm0

        h1_10: None | str | Unset
        if isinstance(self.h1_10, Unset):
            h1_10 = UNSET
        else:
            h1_10 = self.h1_10

        hmax: float | None | Unset
        if isinstance(self.hmax, Unset):
            hmax = UNSET
        else:
            hmax = self.hmax

        peaktp: float | None | Unset
        if isinstance(self.peaktp, Unset):
            peaktp = UNSET
        else:
            peaktp = self.peaktp

        meandir: None | str | Unset
        if isinstance(self.meandir, Unset):
            meandir = UNSET
        else:
            meandir = self.meandir

        lng: float | None | Unset
        if isinstance(self.lng, Unset):
            lng = UNSET
        else:
            lng = self.lng

        lat: float | None | Unset
        if isinstance(self.lat, Unset):
            lat = UNSET
        else:
            lat = self.lat

        fid: None | str | Unset
        if isinstance(self.fid, Unset):
            fid = UNSET
        else:
            fid = self.fid

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ogr_fid is not UNSET:
            field_dict["OGR_FID"] = ogr_fid
        if location is not UNSET:
            field_dict["LOCATION"] = location
        if year is not UNSET:
            field_dict["YEAR"] = year
        if hm0 is not UNSET:
            field_dict["HM0"] = hm0
        if h1_10 is not UNSET:
            field_dict["H1_10"] = h1_10
        if hmax is not UNSET:
            field_dict["HMAX"] = hmax
        if peaktp is not UNSET:
            field_dict["PEAKTP"] = peaktp
        if meandir is not UNSET:
            field_dict["MEANDIR"] = meandir
        if lng is not UNSET:
            field_dict["LNG"] = lng
        if lat is not UNSET:
            field_dict["LAT"] = lat
        if fid is not UNSET:
            field_dict["fid"] = fid
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_ogr_fid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ogr_fid = _parse_ogr_fid(d.pop("OGR_FID", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("LOCATION", UNSET))

        def _parse_year(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year = _parse_year(d.pop("YEAR", UNSET))

        def _parse_hm0(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hm0 = _parse_hm0(d.pop("HM0", UNSET))

        def _parse_h1_10(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        h1_10 = _parse_h1_10(d.pop("H1_10", UNSET))

        def _parse_hmax(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hmax = _parse_hmax(d.pop("HMAX", UNSET))

        def _parse_peaktp(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        peaktp = _parse_peaktp(d.pop("PEAKTP", UNSET))

        def _parse_meandir(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        meandir = _parse_meandir(d.pop("MEANDIR", UNSET))

        def _parse_lng(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lng = _parse_lng(d.pop("LNG", UNSET))

        def _parse_lat(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lat = _parse_lat(d.pop("LAT", UNSET))

        def _parse_fid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fid = _parse_fid(d.pop("fid", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            ogr_fid=ogr_fid,
            location=location,
            year=year,
            hm0=hm0,
            h1_10=h1_10,
            hmax=hmax,
            peaktp=peaktp,
            meandir=meandir,
            lng=lng,
            lat=lat,
            fid=fid,
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
