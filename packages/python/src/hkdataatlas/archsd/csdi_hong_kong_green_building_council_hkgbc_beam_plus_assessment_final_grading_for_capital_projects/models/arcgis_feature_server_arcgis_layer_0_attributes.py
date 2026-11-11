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
        project_title (None | str | Unset): Publisher field type: esriFieldTypeString
        project_title_cht (None | str | Unset): Publisher field type: esriFieldTypeString
        project_title_chs (None | str | Unset): Publisher field type: esriFieldTypeString
        version (None | str | Unset): Publisher field type: esriFieldTypeString
        district (None | str | Unset): Publisher field type: esriFieldTypeString
        district_cht (None | str | Unset): Publisher field type: esriFieldTypeString
        district_chs (None | str | Unset): Publisher field type: esriFieldTypeString
        rating (None | str | Unset): Publisher field type: esriFieldTypeString
        rating_cht (None | str | Unset): Publisher field type: esriFieldTypeString
        rating_chs (None | str | Unset): Publisher field type: esriFieldTypeString
        certification_year (int | None | Unset): Publisher field type: esriFieldTypeInteger
        overall_score (float | None | Unset): Publisher field type: esriFieldTypeDouble
        hk1980n (float | None | Unset): Publisher field type: esriFieldTypeDouble
        hk1980e (float | None | Unset): Publisher field type: esriFieldTypeDouble
        fid (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    project_title: None | str | Unset = UNSET
    project_title_cht: None | str | Unset = UNSET
    project_title_chs: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    district_cht: None | str | Unset = UNSET
    district_chs: None | str | Unset = UNSET
    rating: None | str | Unset = UNSET
    rating_cht: None | str | Unset = UNSET
    rating_chs: None | str | Unset = UNSET
    certification_year: int | None | Unset = UNSET
    overall_score: float | None | Unset = UNSET
    hk1980n: float | None | Unset = UNSET
    hk1980e: float | None | Unset = UNSET
    fid: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_title: None | str | Unset
        if isinstance(self.project_title, Unset):
            project_title = UNSET
        else:
            project_title = self.project_title

        project_title_cht: None | str | Unset
        if isinstance(self.project_title_cht, Unset):
            project_title_cht = UNSET
        else:
            project_title_cht = self.project_title_cht

        project_title_chs: None | str | Unset
        if isinstance(self.project_title_chs, Unset):
            project_title_chs = UNSET
        else:
            project_title_chs = self.project_title_chs

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        district_cht: None | str | Unset
        if isinstance(self.district_cht, Unset):
            district_cht = UNSET
        else:
            district_cht = self.district_cht

        district_chs: None | str | Unset
        if isinstance(self.district_chs, Unset):
            district_chs = UNSET
        else:
            district_chs = self.district_chs

        rating: None | str | Unset
        if isinstance(self.rating, Unset):
            rating = UNSET
        else:
            rating = self.rating

        rating_cht: None | str | Unset
        if isinstance(self.rating_cht, Unset):
            rating_cht = UNSET
        else:
            rating_cht = self.rating_cht

        rating_chs: None | str | Unset
        if isinstance(self.rating_chs, Unset):
            rating_chs = UNSET
        else:
            rating_chs = self.rating_chs

        certification_year: int | None | Unset
        if isinstance(self.certification_year, Unset):
            certification_year = UNSET
        else:
            certification_year = self.certification_year

        overall_score: float | None | Unset
        if isinstance(self.overall_score, Unset):
            overall_score = UNSET
        else:
            overall_score = self.overall_score

        hk1980n: float | None | Unset
        if isinstance(self.hk1980n, Unset):
            hk1980n = UNSET
        else:
            hk1980n = self.hk1980n

        hk1980e: float | None | Unset
        if isinstance(self.hk1980e, Unset):
            hk1980e = UNSET
        else:
            hk1980e = self.hk1980e

        fid: None | str | Unset
        if isinstance(self.fid, Unset):
            fid = UNSET
        else:
            fid = self.fid

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_title is not UNSET:
            field_dict["projectTitle"] = project_title
        if project_title_cht is not UNSET:
            field_dict["projectTitleCht"] = project_title_cht
        if project_title_chs is not UNSET:
            field_dict["projectTitleChs"] = project_title_chs
        if version is not UNSET:
            field_dict["Version"] = version
        if district is not UNSET:
            field_dict["District"] = district
        if district_cht is not UNSET:
            field_dict["DistrictCht"] = district_cht
        if district_chs is not UNSET:
            field_dict["DistrictChs"] = district_chs
        if rating is not UNSET:
            field_dict["Rating"] = rating
        if rating_cht is not UNSET:
            field_dict["RatingCht"] = rating_cht
        if rating_chs is not UNSET:
            field_dict["RatingChs"] = rating_chs
        if certification_year is not UNSET:
            field_dict["CertificationYear"] = certification_year
        if overall_score is not UNSET:
            field_dict["OverallScore"] = overall_score
        if hk1980n is not UNSET:
            field_dict["HK1980N"] = hk1980n
        if hk1980e is not UNSET:
            field_dict["HK1980E"] = hk1980e
        if fid is not UNSET:
            field_dict["fid"] = fid
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_project_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_title = _parse_project_title(d.pop("projectTitle", UNSET))

        def _parse_project_title_cht(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_title_cht = _parse_project_title_cht(d.pop("projectTitleCht", UNSET))

        def _parse_project_title_chs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_title_chs = _parse_project_title_chs(d.pop("projectTitleChs", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("Version", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("District", UNSET))

        def _parse_district_cht(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_cht = _parse_district_cht(d.pop("DistrictCht", UNSET))

        def _parse_district_chs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_chs = _parse_district_chs(d.pop("DistrictChs", UNSET))

        def _parse_rating(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rating = _parse_rating(d.pop("Rating", UNSET))

        def _parse_rating_cht(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rating_cht = _parse_rating_cht(d.pop("RatingCht", UNSET))

        def _parse_rating_chs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rating_chs = _parse_rating_chs(d.pop("RatingChs", UNSET))

        def _parse_certification_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        certification_year = _parse_certification_year(
            d.pop("CertificationYear", UNSET)
        )

        def _parse_overall_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        overall_score = _parse_overall_score(d.pop("OverallScore", UNSET))

        def _parse_hk1980n(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hk1980n = _parse_hk1980n(d.pop("HK1980N", UNSET))

        def _parse_hk1980e(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hk1980e = _parse_hk1980e(d.pop("HK1980E", UNSET))

        def _parse_fid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fid = _parse_fid(d.pop("fid", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            project_title=project_title,
            project_title_cht=project_title_cht,
            project_title_chs=project_title_chs,
            version=version,
            district=district,
            district_cht=district_cht,
            district_chs=district_chs,
            rating=rating,
            rating_cht=rating_cht,
            rating_chs=rating_chs,
            certification_year=certification_year,
            overall_score=overall_score,
            hk1980n=hk1980n,
            hk1980e=hk1980e,
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
