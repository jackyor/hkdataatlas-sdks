from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.weather_radiation_report_additional_property_type_2 import (
        WeatherRadiationReportAdditionalPropertyType2,
    )


T = TypeVar("T", bound="WeatherRadiationReport")


@_attrs_define
class WeatherRadiationReport:
    """Weather and Radiation Level Report (RYES). The report uses type keys formed from a documented station name and
    attribute, optionally followed by other-attribute identifiers. Only available attributes are included for each
    station; unavailable attributes may be omitted or returned as an empty string. Exact values are not uniformly
    specified.

    Publisher RYES dynamic-key dictionaries and availability rule (verbatim retained source; the inline 1 after
    Attribute is the following footnote, not a wire-key suffix):

    Weather and Radiation Level RYES { Report type: data,

    type: data, ... type: data, }

    Format of "type": {Station} + {Attribute}1 {OtherAttribute}

    -----

    {Station} list: CheungChau: Cheung Chau ChekLapKok: Chek Lap Kok PingChau: Ping Chau HKO: Hong Kong Observatory
    HongKongPark: Hong Kong Park WongChukHang: Wong Chuk Hang HappyValley: Happy Valley TseungKwanO: Tseung Kwan O KatO:
    Kat O KowloonCity: Kowloon City KingsPark: Kings Park KwunTong: Kwun Tong LauFauShan: Lau Fau Shan TaiMeiTuk: Tai
    Mei Tuk KaiTakRunwayPark: Kai Tak Runway Park ShekKong: Shek Kong ShaTin: Sha Tin SaiKung: Sai Kung ShauKeiWan: Shau
    Kei Wan ShamShuiPo: Sham Shui Po ShaTauKok: Sha Tau Kok Stanley: Stanley SaiWanHo: Sai Wan Ho TapMun: Tap Mun
    TsimBeiTsui: Tsim Bei Tsui TaKwuLing: Ta Kwu Ling TaiPo: Tai Po TuenMun: Tuen Mun TsuenWanShingMunValley: Tsuen Wan
    Shing Mun Valley TsuenWanHoKoon: Tsuen Wan Ho Koon TsingYi: Tsing Yi WongTaiSin: Wong Tai Sin YuenLongPark: Yuen
    Long Park YuenNgFan: Yuen Ng Fan

    -----

    {Attribute} list: LocationName: Station MaxTemp: Maximum air temperature (Celsius) ReadingsMaxTemp: Maximum air
    temperature (Celsius) ReadingsMaxRH: Maximum relative humidity (%) ReadingsAvgRainfall: Average rainfall (mm)
    ReadingsAccumRainfall: Total rainfall since 1st January (mm) Microsieverts: Average ambient gamma radiation dose
    rate (microsievert/hour) MinTemp: Minimum air temperature (Celsius) ReadingsMaxUVIndex: Maximum UV index
    ReadingsMinGrassTemp: Grass minimum temperature (Celsius) ReadingsMinRH: Minimum relative humidity (%)
    ReadingsRainfall: Rainfall (mm) ReadingsMeanUVIndex: Mean UV index ReadingsSunShine: Duration of sunshine(Hours)
    ReadingsMinTemp: Minimum air temperature (Celsius)

    {OtherAttribute} list: BulletinDate: Bulletin date (YYYYMMDD) BulletinTime: Bulletin time (HHMM) HongKongDesc:
    Description of average ambient gamma radiation dose rate taken outdoors in Hong Kong NoteDesc: Note NoteDesc1: Note1
    NoteDesc2: Note2 NoteDesc3: Note3 ReportTimeInfoDate: Information date (YYYYMMDD)

    1. Only available attributes include in response for each station. Unavailable

    attributes will not be included or empty string will be returned.

        Attributes:
            type_ (list[str] | str | Unset): The illustrative report shows the type value data repeated; type representation
                is not specified consistently.
    """

    type_: list[str] | str | Unset = UNSET
    additional_properties: dict[
        str,
        float | list[Any] | None | str | WeatherRadiationReportAdditionalPropertyType2,
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.weather_radiation_report_additional_property_type_2 import (
            WeatherRadiationReportAdditionalPropertyType2,
        )

        type_: list[str] | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, list):
            type_ = self.type_

        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, WeatherRadiationReportAdditionalPropertyType2):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, list):
                field_dict[prop_name] = prop

            else:
                field_dict[prop_name] = prop

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.weather_radiation_report_additional_property_type_2 import (
            WeatherRadiationReportAdditionalPropertyType2,
        )

        d = dict(src_dict)

        def _parse_type_(data: object) -> list[str] | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                type_type_1 = cast(list[str], data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        weather_radiation_report = cls(
            type_=type_,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> (
                float
                | list[Any]
                | None
                | str
                | WeatherRadiationReportAdditionalPropertyType2
            ):
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_2 = (
                        WeatherRadiationReportAdditionalPropertyType2.from_dict(data)
                    )

                    return additional_property_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, list):
                        raise TypeError()
                    additional_property_type_3 = cast(list[Any], data)

                    return additional_property_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(
                    float
                    | list[Any]
                    | None
                    | str
                    | WeatherRadiationReportAdditionalPropertyType2,
                    data,
                )

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        weather_radiation_report.additional_properties = additional_properties
        return weather_radiation_report

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> float | list[Any] | None | str | WeatherRadiationReportAdditionalPropertyType2:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: float
        | list[Any]
        | None
        | str
        | WeatherRadiationReportAdditionalPropertyType2,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
