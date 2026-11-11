from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsLGTGAttributes")


@_attrs_define
class WfsMapServerWfsLGTGAttributes:
    """
    Attributes:
        daily_total_cloud_to_ground_lightning_count_all_year_url (None | str | Unset): Native XSD type . Requiredness is
            not projected from XML occurrence into all JSON queries.
        daily_total_cloud_to_ground_lightning_count_current_year_url (None | str | Unset): Native XSD type .
            Requiredness is not projected from XML occurrence into all JSON queries.
        region_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        region_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        region_uc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiCurvePropertyType; JSON geometry is not inferred from its
            XML type.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    daily_total_cloud_to_ground_lightning_count_all_year_url: None | str | Unset = UNSET
    daily_total_cloud_to_ground_lightning_count_current_year_url: None | str | Unset = (
        UNSET
    )
    region_en: None | str | Unset = UNSET
    region_sc: None | str | Unset = UNSET
    region_uc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        daily_total_cloud_to_ground_lightning_count_all_year_url: None | str | Unset
        if isinstance(
            self.daily_total_cloud_to_ground_lightning_count_all_year_url, Unset
        ):
            daily_total_cloud_to_ground_lightning_count_all_year_url = UNSET
        else:
            daily_total_cloud_to_ground_lightning_count_all_year_url = (
                self.daily_total_cloud_to_ground_lightning_count_all_year_url
            )

        daily_total_cloud_to_ground_lightning_count_current_year_url: None | str | Unset
        if isinstance(
            self.daily_total_cloud_to_ground_lightning_count_current_year_url, Unset
        ):
            daily_total_cloud_to_ground_lightning_count_current_year_url = UNSET
        else:
            daily_total_cloud_to_ground_lightning_count_current_year_url = (
                self.daily_total_cloud_to_ground_lightning_count_current_year_url
            )

        region_en: None | str | Unset
        if isinstance(self.region_en, Unset):
            region_en = UNSET
        else:
            region_en = self.region_en

        region_sc: None | str | Unset
        if isinstance(self.region_sc, Unset):
            region_sc = UNSET
        else:
            region_sc = self.region_sc

        region_uc: None | str | Unset
        if isinstance(self.region_uc, Unset):
            region_uc = UNSET
        else:
            region_uc = self.region_uc

        objectid = self.objectid

        shape = self.shape

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if daily_total_cloud_to_ground_lightning_count_all_year_url is not UNSET:
            field_dict["DailyTotalCloudToGroundLightningCount_AllYear_url"] = (
                daily_total_cloud_to_ground_lightning_count_all_year_url
            )
        if daily_total_cloud_to_ground_lightning_count_current_year_url is not UNSET:
            field_dict["DailyTotalCloudToGroundLightningCount_CurrentYear_url"] = (
                daily_total_cloud_to_ground_lightning_count_current_year_url
            )
        if region_en is not UNSET:
            field_dict["Region_en"] = region_en
        if region_sc is not UNSET:
            field_dict["Region_sc"] = region_sc
        if region_uc is not UNSET:
            field_dict["Region_uc"] = region_uc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if shape_length is not UNSET:
            field_dict["SHAPE_Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_daily_total_cloud_to_ground_lightning_count_all_year_url(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        daily_total_cloud_to_ground_lightning_count_all_year_url = (
            _parse_daily_total_cloud_to_ground_lightning_count_all_year_url(
                d.pop("DailyTotalCloudToGroundLightningCount_AllYear_url", UNSET)
            )
        )

        def _parse_daily_total_cloud_to_ground_lightning_count_current_year_url(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        daily_total_cloud_to_ground_lightning_count_current_year_url = (
            _parse_daily_total_cloud_to_ground_lightning_count_current_year_url(
                d.pop("DailyTotalCloudToGroundLightningCount_CurrentYear_url", UNSET)
            )
        )

        def _parse_region_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_en = _parse_region_en(d.pop("Region_en", UNSET))

        def _parse_region_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_sc = _parse_region_sc(d.pop("Region_sc", UNSET))

        def _parse_region_uc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_uc = _parse_region_uc(d.pop("Region_uc", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("SHAPE_Length", UNSET))

        wfs_map_server_wfs_lgtg_attributes = cls(
            daily_total_cloud_to_ground_lightning_count_all_year_url=daily_total_cloud_to_ground_lightning_count_all_year_url,
            daily_total_cloud_to_ground_lightning_count_current_year_url=daily_total_cloud_to_ground_lightning_count_current_year_url,
            region_en=region_en,
            region_sc=region_sc,
            region_uc=region_uc,
            objectid=objectid,
            shape=shape,
            shape_length=shape_length,
        )

        wfs_map_server_wfs_lgtg_attributes.additional_properties = d
        return wfs_map_server_wfs_lgtg_attributes

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
