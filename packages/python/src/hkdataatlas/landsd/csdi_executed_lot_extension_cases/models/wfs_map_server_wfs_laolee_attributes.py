from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsLAOLEEAttributes")


@_attrs_define
class WfsMapServerWfsLAOLEEAttributes:
    """
    Attributes:
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        dataset (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        數據集 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        lot_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        location (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        地段編號 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        地點 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        relevant_district_council (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        所屬區議會 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        execution_year (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        簽立年度 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        execution_date (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        簽立日期 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        extension_area_hectare_about (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        增批面積_公頃_約 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        user (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        用途 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        premium (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        地價_港幣 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        date_of_registration (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        註冊日期 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        northing_坐標北 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        easting_坐標東 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        latitude_緯度 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        longitude_經度 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        last_updated_date_最後更新日期 (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from
            XML occurrence into all JSON queries.
    """

    shape: Any | Unset = UNSET
    objectid: int | Unset = UNSET
    dataset: None | str | Unset = UNSET
    數據集: None | str | Unset = UNSET
    lot_number: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    地段編號: None | str | Unset = UNSET
    地點: None | str | Unset = UNSET
    relevant_district_council: None | str | Unset = UNSET
    所屬區議會: None | str | Unset = UNSET
    execution_year: None | str | Unset = UNSET
    簽立年度: None | str | Unset = UNSET
    execution_date: None | str | Unset = UNSET
    簽立日期: None | str | Unset = UNSET
    extension_area_hectare_about: None | str | Unset = UNSET
    增批面積_公頃_約: None | str | Unset = UNSET
    user: None | str | Unset = UNSET
    用途: None | str | Unset = UNSET
    premium: None | str | Unset = UNSET
    地價_港幣: None | str | Unset = UNSET
    date_of_registration: None | str | Unset = UNSET
    註冊日期: None | str | Unset = UNSET
    northing_坐標北: float | None | Unset = UNSET
    easting_坐標東: float | None | Unset = UNSET
    latitude_緯度: float | None | Unset = UNSET
    longitude_經度: float | None | Unset = UNSET
    last_updated_date_最後更新日期: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shape = self.shape

        objectid = self.objectid

        dataset: None | str | Unset
        if isinstance(self.dataset, Unset):
            dataset = UNSET
        else:
            dataset = self.dataset

        數據集: None | str | Unset
        if isinstance(self.數據集, Unset):
            數據集 = UNSET
        else:
            數據集 = self.數據集

        lot_number: None | str | Unset
        if isinstance(self.lot_number, Unset):
            lot_number = UNSET
        else:
            lot_number = self.lot_number

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        地段編號: None | str | Unset
        if isinstance(self.地段編號, Unset):
            地段編號 = UNSET
        else:
            地段編號 = self.地段編號

        地點: None | str | Unset
        if isinstance(self.地點, Unset):
            地點 = UNSET
        else:
            地點 = self.地點

        relevant_district_council: None | str | Unset
        if isinstance(self.relevant_district_council, Unset):
            relevant_district_council = UNSET
        else:
            relevant_district_council = self.relevant_district_council

        所屬區議會: None | str | Unset
        if isinstance(self.所屬區議會, Unset):
            所屬區議會 = UNSET
        else:
            所屬區議會 = self.所屬區議會

        execution_year: None | str | Unset
        if isinstance(self.execution_year, Unset):
            execution_year = UNSET
        else:
            execution_year = self.execution_year

        簽立年度: None | str | Unset
        if isinstance(self.簽立年度, Unset):
            簽立年度 = UNSET
        else:
            簽立年度 = self.簽立年度

        execution_date: None | str | Unset
        if isinstance(self.execution_date, Unset):
            execution_date = UNSET
        else:
            execution_date = self.execution_date

        簽立日期: None | str | Unset
        if isinstance(self.簽立日期, Unset):
            簽立日期 = UNSET
        else:
            簽立日期 = self.簽立日期

        extension_area_hectare_about: None | str | Unset
        if isinstance(self.extension_area_hectare_about, Unset):
            extension_area_hectare_about = UNSET
        else:
            extension_area_hectare_about = self.extension_area_hectare_about

        增批面積_公頃_約: None | str | Unset
        if isinstance(self.增批面積_公頃_約, Unset):
            增批面積_公頃_約 = UNSET
        else:
            增批面積_公頃_約 = self.增批面積_公頃_約

        user: None | str | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        用途: None | str | Unset
        if isinstance(self.用途, Unset):
            用途 = UNSET
        else:
            用途 = self.用途

        premium: None | str | Unset
        if isinstance(self.premium, Unset):
            premium = UNSET
        else:
            premium = self.premium

        地價_港幣: None | str | Unset
        if isinstance(self.地價_港幣, Unset):
            地價_港幣 = UNSET
        else:
            地價_港幣 = self.地價_港幣

        date_of_registration: None | str | Unset
        if isinstance(self.date_of_registration, Unset):
            date_of_registration = UNSET
        else:
            date_of_registration = self.date_of_registration

        註冊日期: None | str | Unset
        if isinstance(self.註冊日期, Unset):
            註冊日期 = UNSET
        else:
            註冊日期 = self.註冊日期

        northing_坐標北: float | None | Unset
        if isinstance(self.northing_坐標北, Unset):
            northing_坐標北 = UNSET
        else:
            northing_坐標北 = self.northing_坐標北

        easting_坐標東: float | None | Unset
        if isinstance(self.easting_坐標東, Unset):
            easting_坐標東 = UNSET
        else:
            easting_坐標東 = self.easting_坐標東

        latitude_緯度: float | None | Unset
        if isinstance(self.latitude_緯度, Unset):
            latitude_緯度 = UNSET
        else:
            latitude_緯度 = self.latitude_緯度

        longitude_經度: float | None | Unset
        if isinstance(self.longitude_經度, Unset):
            longitude_經度 = UNSET
        else:
            longitude_經度 = self.longitude_經度

        last_updated_date_最後更新日期: None | str | Unset
        if isinstance(self.last_updated_date_最後更新日期, Unset):
            last_updated_date_最後更新日期 = UNSET
        else:
            last_updated_date_最後更新日期 = self.last_updated_date_最後更新日期

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shape is not UNSET:
            field_dict["shape"] = shape
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if dataset is not UNSET:
            field_dict["Dataset"] = dataset
        if 數據集 is not UNSET:
            field_dict["數據集"] = 數據集
        if lot_number is not UNSET:
            field_dict["Lot_Number"] = lot_number
        if location is not UNSET:
            field_dict["Location"] = location
        if 地段編號 is not UNSET:
            field_dict["地段編號"] = 地段編號
        if 地點 is not UNSET:
            field_dict["地點"] = 地點
        if relevant_district_council is not UNSET:
            field_dict["Relevant_District_Council"] = relevant_district_council
        if 所屬區議會 is not UNSET:
            field_dict["所屬區議會"] = 所屬區議會
        if execution_year is not UNSET:
            field_dict["Execution_Year"] = execution_year
        if 簽立年度 is not UNSET:
            field_dict["簽立年度"] = 簽立年度
        if execution_date is not UNSET:
            field_dict["Execution_Date"] = execution_date
        if 簽立日期 is not UNSET:
            field_dict["簽立日期"] = 簽立日期
        if extension_area_hectare_about is not UNSET:
            field_dict["Extension_Area__hectare___about_"] = (
                extension_area_hectare_about
            )
        if 增批面積_公頃_約 is not UNSET:
            field_dict["增批面積__公頃__約_"] = 增批面積_公頃_約
        if user is not UNSET:
            field_dict["User"] = user
        if 用途 is not UNSET:
            field_dict["用途"] = 用途
        if premium is not UNSET:
            field_dict["Premium____"] = premium
        if 地價_港幣 is not UNSET:
            field_dict["地價_港幣_"] = 地價_港幣
        if date_of_registration is not UNSET:
            field_dict["Date_of_Registration"] = date_of_registration
        if 註冊日期 is not UNSET:
            field_dict["註冊日期"] = 註冊日期
        if northing_坐標北 is not UNSET:
            field_dict["Northing___坐標北"] = northing_坐標北
        if easting_坐標東 is not UNSET:
            field_dict["Easting___坐標東"] = easting_坐標東
        if latitude_緯度 is not UNSET:
            field_dict["Latitude___緯度"] = latitude_緯度
        if longitude_經度 is not UNSET:
            field_dict["Longitude___經度"] = longitude_經度
        if last_updated_date_最後更新日期 is not UNSET:
            field_dict["Last_Updated_Date___最後更新日期"] = (
                last_updated_date_最後更新日期
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        shape = d.pop("shape", UNSET)

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_dataset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset = _parse_dataset(d.pop("Dataset", UNSET))

        def _parse_數據集(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        數據集 = _parse_數據集(d.pop("數據集", UNSET))

        def _parse_lot_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lot_number = _parse_lot_number(d.pop("Lot_Number", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("Location", UNSET))

        def _parse_地段編號(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        地段編號 = _parse_地段編號(d.pop("地段編號", UNSET))

        def _parse_地點(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        地點 = _parse_地點(d.pop("地點", UNSET))

        def _parse_relevant_district_council(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relevant_district_council = _parse_relevant_district_council(
            d.pop("Relevant_District_Council", UNSET)
        )

        def _parse_所屬區議會(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        所屬區議會 = _parse_所屬區議會(d.pop("所屬區議會", UNSET))

        def _parse_execution_year(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        execution_year = _parse_execution_year(d.pop("Execution_Year", UNSET))

        def _parse_簽立年度(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        簽立年度 = _parse_簽立年度(d.pop("簽立年度", UNSET))

        def _parse_execution_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        execution_date = _parse_execution_date(d.pop("Execution_Date", UNSET))

        def _parse_簽立日期(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        簽立日期 = _parse_簽立日期(d.pop("簽立日期", UNSET))

        def _parse_extension_area_hectare_about(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extension_area_hectare_about = _parse_extension_area_hectare_about(
            d.pop("Extension_Area__hectare___about_", UNSET)
        )

        def _parse_增批面積_公頃_約(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        增批面積_公頃_約 = _parse_增批面積_公頃_約(d.pop("增批面積__公頃__約_", UNSET))

        def _parse_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user = _parse_user(d.pop("User", UNSET))

        def _parse_用途(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        用途 = _parse_用途(d.pop("用途", UNSET))

        def _parse_premium(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        premium = _parse_premium(d.pop("Premium____", UNSET))

        def _parse_地價_港幣(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        地價_港幣 = _parse_地價_港幣(d.pop("地價_港幣_", UNSET))

        def _parse_date_of_registration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_of_registration = _parse_date_of_registration(
            d.pop("Date_of_Registration", UNSET)
        )

        def _parse_註冊日期(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        註冊日期 = _parse_註冊日期(d.pop("註冊日期", UNSET))

        def _parse_northing_坐標北(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing_坐標北 = _parse_northing_坐標北(d.pop("Northing___坐標北", UNSET))

        def _parse_easting_坐標東(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting_坐標東 = _parse_easting_坐標東(d.pop("Easting___坐標東", UNSET))

        def _parse_latitude_緯度(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude_緯度 = _parse_latitude_緯度(d.pop("Latitude___緯度", UNSET))

        def _parse_longitude_經度(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude_經度 = _parse_longitude_經度(d.pop("Longitude___經度", UNSET))

        def _parse_last_updated_date_最後更新日期(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_updated_date_最後更新日期 = _parse_last_updated_date_最後更新日期(
            d.pop("Last_Updated_Date___最後更新日期", UNSET)
        )

        wfs_map_server_wfs_laolee_attributes = cls(
            shape=shape,
            objectid=objectid,
            dataset=dataset,
            數據集=數據集,
            lot_number=lot_number,
            location=location,
            地段編號=地段編號,
            地點=地點,
            relevant_district_council=relevant_district_council,
            所屬區議會=所屬區議會,
            execution_year=execution_year,
            簽立年度=簽立年度,
            execution_date=execution_date,
            簽立日期=簽立日期,
            extension_area_hectare_about=extension_area_hectare_about,
            增批面積_公頃_約=增批面積_公頃_約,
            user=user,
            用途=用途,
            premium=premium,
            地價_港幣=地價_港幣,
            date_of_registration=date_of_registration,
            註冊日期=註冊日期,
            northing_坐標北=northing_坐標北,
            easting_坐標東=easting_坐標東,
            latitude_緯度=latitude_緯度,
            longitude_經度=longitude_經度,
            last_updated_date_最後更新日期=last_updated_date_最後更新日期,
        )

        wfs_map_server_wfs_laolee_attributes.additional_properties = d
        return wfs_map_server_wfs_laolee_attributes

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
