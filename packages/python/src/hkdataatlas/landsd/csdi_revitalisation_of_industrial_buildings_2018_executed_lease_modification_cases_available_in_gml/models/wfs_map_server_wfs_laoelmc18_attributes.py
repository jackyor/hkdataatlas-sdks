from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsLAOELMC18Attributes")


@_attrs_define
class WfsMapServerWfsLAOELMC18Attributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        dataset (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        數據集 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        facility_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        設施名稱 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        地址 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        relevant_district_council (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        所屬區議會 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        execution_year (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        簽辦年度 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        execution_date (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        簽辦日期 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        user (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        用途 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        premium_hk (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
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

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    dataset: None | str | Unset = UNSET
    數據集: None | str | Unset = UNSET
    facility_name: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    設施名稱: None | str | Unset = UNSET
    地址: None | str | Unset = UNSET
    relevant_district_council: None | str | Unset = UNSET
    所屬區議會: None | str | Unset = UNSET
    execution_year: None | str | Unset = UNSET
    簽辦年度: None | str | Unset = UNSET
    execution_date: None | str | Unset = UNSET
    簽辦日期: None | str | Unset = UNSET
    user: None | str | Unset = UNSET
    用途: None | str | Unset = UNSET
    premium_hk: None | str | Unset = UNSET
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
        objectid = self.objectid

        shape = self.shape

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

        facility_name: None | str | Unset
        if isinstance(self.facility_name, Unset):
            facility_name = UNSET
        else:
            facility_name = self.facility_name

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        設施名稱: None | str | Unset
        if isinstance(self.設施名稱, Unset):
            設施名稱 = UNSET
        else:
            設施名稱 = self.設施名稱

        地址: None | str | Unset
        if isinstance(self.地址, Unset):
            地址 = UNSET
        else:
            地址 = self.地址

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

        簽辦年度: None | str | Unset
        if isinstance(self.簽辦年度, Unset):
            簽辦年度 = UNSET
        else:
            簽辦年度 = self.簽辦年度

        execution_date: None | str | Unset
        if isinstance(self.execution_date, Unset):
            execution_date = UNSET
        else:
            execution_date = self.execution_date

        簽辦日期: None | str | Unset
        if isinstance(self.簽辦日期, Unset):
            簽辦日期 = UNSET
        else:
            簽辦日期 = self.簽辦日期

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

        premium_hk: None | str | Unset
        if isinstance(self.premium_hk, Unset):
            premium_hk = UNSET
        else:
            premium_hk = self.premium_hk

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
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if dataset is not UNSET:
            field_dict["Dataset"] = dataset
        if 數據集 is not UNSET:
            field_dict["數據集"] = 數據集
        if facility_name is not UNSET:
            field_dict["Facility_Name"] = facility_name
        if address is not UNSET:
            field_dict["Address"] = address
        if 設施名稱 is not UNSET:
            field_dict["設施名稱"] = 設施名稱
        if 地址 is not UNSET:
            field_dict["地址"] = 地址
        if relevant_district_council is not UNSET:
            field_dict["Relevant_District_Council"] = relevant_district_council
        if 所屬區議會 is not UNSET:
            field_dict["所屬區議會"] = 所屬區議會
        if execution_year is not UNSET:
            field_dict["Execution_Year"] = execution_year
        if 簽辦年度 is not UNSET:
            field_dict["簽辦年度"] = 簽辦年度
        if execution_date is not UNSET:
            field_dict["Execution_Date"] = execution_date
        if 簽辦日期 is not UNSET:
            field_dict["簽辦日期"] = 簽辦日期
        if user is not UNSET:
            field_dict["User"] = user
        if 用途 is not UNSET:
            field_dict["用途"] = 用途
        if premium_hk is not UNSET:
            field_dict["Premium__HK__"] = premium_hk
        if 地價_港幣 is not UNSET:
            field_dict["地價__港幣_"] = 地價_港幣
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
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("Shape", UNSET)

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

        def _parse_facility_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_name = _parse_facility_name(d.pop("Facility_Name", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("Address", UNSET))

        def _parse_設施名稱(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        設施名稱 = _parse_設施名稱(d.pop("設施名稱", UNSET))

        def _parse_地址(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        地址 = _parse_地址(d.pop("地址", UNSET))

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

        def _parse_簽辦年度(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        簽辦年度 = _parse_簽辦年度(d.pop("簽辦年度", UNSET))

        def _parse_execution_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        execution_date = _parse_execution_date(d.pop("Execution_Date", UNSET))

        def _parse_簽辦日期(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        簽辦日期 = _parse_簽辦日期(d.pop("簽辦日期", UNSET))

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

        def _parse_premium_hk(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        premium_hk = _parse_premium_hk(d.pop("Premium__HK__", UNSET))

        def _parse_地價_港幣(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        地價_港幣 = _parse_地價_港幣(d.pop("地價__港幣_", UNSET))

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

        wfs_map_server_wfs_laoelmc18_attributes = cls(
            objectid=objectid,
            shape=shape,
            dataset=dataset,
            數據集=數據集,
            facility_name=facility_name,
            address=address,
            設施名稱=設施名稱,
            地址=地址,
            relevant_district_council=relevant_district_council,
            所屬區議會=所屬區議會,
            execution_year=execution_year,
            簽辦年度=簽辦年度,
            execution_date=execution_date,
            簽辦日期=簽辦日期,
            user=user,
            用途=用途,
            premium_hk=premium_hk,
            地價_港幣=地價_港幣,
            date_of_registration=date_of_registration,
            註冊日期=註冊日期,
            northing_坐標北=northing_坐標北,
            easting_坐標東=easting_坐標東,
            latitude_緯度=latitude_緯度,
            longitude_經度=longitude_經度,
            last_updated_date_最後更新日期=last_updated_date_最後更新日期,
        )

        wfs_map_server_wfs_laoelmc18_attributes.additional_properties = d
        return wfs_map_server_wfs_laoelmc18_attributes

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
