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
        apr (float | None | Unset): Publisher field type: esriFieldTypeDouble
        aug (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dec (float | None | Unset): Publisher field type: esriFieldTypeDouble
        feb (None | str | Unset): Publisher field type: esriFieldTypeString
        jan (None | str | Unset): Publisher field type: esriFieldTypeString
        jul (float | None | Unset): Publisher field type: esriFieldTypeDouble
        jun (float | None | Unset): Publisher field type: esriFieldTypeDouble
        location_of_dedicated_lpg_filling_station_chinese (None | str | Unset): Publisher field type:
            esriFieldTypeString
        location_of_dedicated_lpg_filling_station_english (None | str | Unset): Publisher field type:
            esriFieldTypeString
        mar (float | None | Unset): Publisher field type: esriFieldTypeDouble
        may (float | None | Unset): Publisher field type: esriFieldTypeDouble
        nov (float | None | Unset): Publisher field type: esriFieldTypeDouble
        oct_ (float | None | Unset): Publisher field type: esriFieldTypeDouble
        sep (float | None | Unset): Publisher field type: esriFieldTypeDouble
        year (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    apr: float | None | Unset = UNSET
    aug: float | None | Unset = UNSET
    dec: float | None | Unset = UNSET
    feb: None | str | Unset = UNSET
    jan: None | str | Unset = UNSET
    jul: float | None | Unset = UNSET
    jun: float | None | Unset = UNSET
    location_of_dedicated_lpg_filling_station_chinese: None | str | Unset = UNSET
    location_of_dedicated_lpg_filling_station_english: None | str | Unset = UNSET
    mar: float | None | Unset = UNSET
    may: float | None | Unset = UNSET
    nov: float | None | Unset = UNSET
    oct_: float | None | Unset = UNSET
    sep: float | None | Unset = UNSET
    year: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apr: float | None | Unset
        if isinstance(self.apr, Unset):
            apr = UNSET
        else:
            apr = self.apr

        aug: float | None | Unset
        if isinstance(self.aug, Unset):
            aug = UNSET
        else:
            aug = self.aug

        dec: float | None | Unset
        if isinstance(self.dec, Unset):
            dec = UNSET
        else:
            dec = self.dec

        feb: None | str | Unset
        if isinstance(self.feb, Unset):
            feb = UNSET
        else:
            feb = self.feb

        jan: None | str | Unset
        if isinstance(self.jan, Unset):
            jan = UNSET
        else:
            jan = self.jan

        jul: float | None | Unset
        if isinstance(self.jul, Unset):
            jul = UNSET
        else:
            jul = self.jul

        jun: float | None | Unset
        if isinstance(self.jun, Unset):
            jun = UNSET
        else:
            jun = self.jun

        location_of_dedicated_lpg_filling_station_chinese: None | str | Unset
        if isinstance(self.location_of_dedicated_lpg_filling_station_chinese, Unset):
            location_of_dedicated_lpg_filling_station_chinese = UNSET
        else:
            location_of_dedicated_lpg_filling_station_chinese = (
                self.location_of_dedicated_lpg_filling_station_chinese
            )

        location_of_dedicated_lpg_filling_station_english: None | str | Unset
        if isinstance(self.location_of_dedicated_lpg_filling_station_english, Unset):
            location_of_dedicated_lpg_filling_station_english = UNSET
        else:
            location_of_dedicated_lpg_filling_station_english = (
                self.location_of_dedicated_lpg_filling_station_english
            )

        mar: float | None | Unset
        if isinstance(self.mar, Unset):
            mar = UNSET
        else:
            mar = self.mar

        may: float | None | Unset
        if isinstance(self.may, Unset):
            may = UNSET
        else:
            may = self.may

        nov: float | None | Unset
        if isinstance(self.nov, Unset):
            nov = UNSET
        else:
            nov = self.nov

        oct_: float | None | Unset
        if isinstance(self.oct_, Unset):
            oct_ = UNSET
        else:
            oct_ = self.oct_

        sep: float | None | Unset
        if isinstance(self.sep, Unset):
            sep = UNSET
        else:
            sep = self.sep

        year: float | None | Unset
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apr is not UNSET:
            field_dict["Apr"] = apr
        if aug is not UNSET:
            field_dict["Aug"] = aug
        if dec is not UNSET:
            field_dict["Dec"] = dec
        if feb is not UNSET:
            field_dict["Feb"] = feb
        if jan is not UNSET:
            field_dict["Jan"] = jan
        if jul is not UNSET:
            field_dict["Jul"] = jul
        if jun is not UNSET:
            field_dict["Jun"] = jun
        if location_of_dedicated_lpg_filling_station_chinese is not UNSET:
            field_dict["Location_of_Dedicated_LPG_Filling_Station_Chinese"] = (
                location_of_dedicated_lpg_filling_station_chinese
            )
        if location_of_dedicated_lpg_filling_station_english is not UNSET:
            field_dict["Location_of_Dedicated_LPG_Filling_Station_English"] = (
                location_of_dedicated_lpg_filling_station_english
            )
        if mar is not UNSET:
            field_dict["Mar"] = mar
        if may is not UNSET:
            field_dict["May"] = may
        if nov is not UNSET:
            field_dict["Nov"] = nov
        if oct_ is not UNSET:
            field_dict["Oct"] = oct_
        if sep is not UNSET:
            field_dict["Sep"] = sep
        if year is not UNSET:
            field_dict["Year"] = year
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_apr(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        apr = _parse_apr(d.pop("Apr", UNSET))

        def _parse_aug(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        aug = _parse_aug(d.pop("Aug", UNSET))

        def _parse_dec(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dec = _parse_dec(d.pop("Dec", UNSET))

        def _parse_feb(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feb = _parse_feb(d.pop("Feb", UNSET))

        def _parse_jan(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        jan = _parse_jan(d.pop("Jan", UNSET))

        def _parse_jul(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        jul = _parse_jul(d.pop("Jul", UNSET))

        def _parse_jun(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        jun = _parse_jun(d.pop("Jun", UNSET))

        def _parse_location_of_dedicated_lpg_filling_station_chinese(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_of_dedicated_lpg_filling_station_chinese = (
            _parse_location_of_dedicated_lpg_filling_station_chinese(
                d.pop("Location_of_Dedicated_LPG_Filling_Station_Chinese", UNSET)
            )
        )

        def _parse_location_of_dedicated_lpg_filling_station_english(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_of_dedicated_lpg_filling_station_english = (
            _parse_location_of_dedicated_lpg_filling_station_english(
                d.pop("Location_of_Dedicated_LPG_Filling_Station_English", UNSET)
            )
        )

        def _parse_mar(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mar = _parse_mar(d.pop("Mar", UNSET))

        def _parse_may(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        may = _parse_may(d.pop("May", UNSET))

        def _parse_nov(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        nov = _parse_nov(d.pop("Nov", UNSET))

        def _parse_oct_(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        oct_ = _parse_oct_(d.pop("Oct", UNSET))

        def _parse_sep(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sep = _parse_sep(d.pop("Sep", UNSET))

        def _parse_year(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        year = _parse_year(d.pop("Year", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            apr=apr,
            aug=aug,
            dec=dec,
            feb=feb,
            jan=jan,
            jul=jul,
            jun=jun,
            location_of_dedicated_lpg_filling_station_chinese=location_of_dedicated_lpg_filling_station_chinese,
            location_of_dedicated_lpg_filling_station_english=location_of_dedicated_lpg_filling_station_english,
            mar=mar,
            may=may,
            nov=nov,
            oct_=oct_,
            sep=sep,
            year=year,
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
