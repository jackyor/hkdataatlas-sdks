from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsPOSAttributes")


@_attrs_define
class WfsMapServerWfsPOSAttributes:
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
        ownership (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        業權 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        area_about_m (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        面積_約_平方米 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        accessibility_location (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        前往方法_所處位置 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        opening_hours (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        開放時間 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        provision_of_sheltered_seating (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        提供有蓋座位 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        provision_of_barrier_free_access_facilities (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        提供無障礙通道設施 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        remarks (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        備註 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        relevant_district_lands_office (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        所屬分區地政處 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
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
    facility_name: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    設施名稱: None | str | Unset = UNSET
    地址: None | str | Unset = UNSET
    relevant_district_council: None | str | Unset = UNSET
    所屬區議會: None | str | Unset = UNSET
    ownership: None | str | Unset = UNSET
    業權: None | str | Unset = UNSET
    area_about_m: None | str | Unset = UNSET
    面積_約_平方米: None | str | Unset = UNSET
    accessibility_location: None | str | Unset = UNSET
    前往方法_所處位置: None | str | Unset = UNSET
    opening_hours: None | str | Unset = UNSET
    開放時間: None | str | Unset = UNSET
    provision_of_sheltered_seating: None | str | Unset = UNSET
    提供有蓋座位: None | str | Unset = UNSET
    provision_of_barrier_free_access_facilities: None | str | Unset = UNSET
    提供無障礙通道設施: None | str | Unset = UNSET
    remarks: None | str | Unset = UNSET
    備註: None | str | Unset = UNSET
    relevant_district_lands_office: None | str | Unset = UNSET
    所屬分區地政處: None | str | Unset = UNSET
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

        ownership: None | str | Unset
        if isinstance(self.ownership, Unset):
            ownership = UNSET
        else:
            ownership = self.ownership

        業權: None | str | Unset
        if isinstance(self.業權, Unset):
            業權 = UNSET
        else:
            業權 = self.業權

        area_about_m: None | str | Unset
        if isinstance(self.area_about_m, Unset):
            area_about_m = UNSET
        else:
            area_about_m = self.area_about_m

        面積_約_平方米: None | str | Unset
        if isinstance(self.面積_約_平方米, Unset):
            面積_約_平方米 = UNSET
        else:
            面積_約_平方米 = self.面積_約_平方米

        accessibility_location: None | str | Unset
        if isinstance(self.accessibility_location, Unset):
            accessibility_location = UNSET
        else:
            accessibility_location = self.accessibility_location

        前往方法_所處位置: None | str | Unset
        if isinstance(self.前往方法_所處位置, Unset):
            前往方法_所處位置 = UNSET
        else:
            前往方法_所處位置 = self.前往方法_所處位置

        opening_hours: None | str | Unset
        if isinstance(self.opening_hours, Unset):
            opening_hours = UNSET
        else:
            opening_hours = self.opening_hours

        開放時間: None | str | Unset
        if isinstance(self.開放時間, Unset):
            開放時間 = UNSET
        else:
            開放時間 = self.開放時間

        provision_of_sheltered_seating: None | str | Unset
        if isinstance(self.provision_of_sheltered_seating, Unset):
            provision_of_sheltered_seating = UNSET
        else:
            provision_of_sheltered_seating = self.provision_of_sheltered_seating

        提供有蓋座位: None | str | Unset
        if isinstance(self.提供有蓋座位, Unset):
            提供有蓋座位 = UNSET
        else:
            提供有蓋座位 = self.提供有蓋座位

        provision_of_barrier_free_access_facilities: None | str | Unset
        if isinstance(self.provision_of_barrier_free_access_facilities, Unset):
            provision_of_barrier_free_access_facilities = UNSET
        else:
            provision_of_barrier_free_access_facilities = (
                self.provision_of_barrier_free_access_facilities
            )

        提供無障礙通道設施: None | str | Unset
        if isinstance(self.提供無障礙通道設施, Unset):
            提供無障礙通道設施 = UNSET
        else:
            提供無障礙通道設施 = self.提供無障礙通道設施

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        備註: None | str | Unset
        if isinstance(self.備註, Unset):
            備註 = UNSET
        else:
            備註 = self.備註

        relevant_district_lands_office: None | str | Unset
        if isinstance(self.relevant_district_lands_office, Unset):
            relevant_district_lands_office = UNSET
        else:
            relevant_district_lands_office = self.relevant_district_lands_office

        所屬分區地政處: None | str | Unset
        if isinstance(self.所屬分區地政處, Unset):
            所屬分區地政處 = UNSET
        else:
            所屬分區地政處 = self.所屬分區地政處

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
        if ownership is not UNSET:
            field_dict["Ownership"] = ownership
        if 業權 is not UNSET:
            field_dict["業權"] = 業權
        if area_about_m is not UNSET:
            field_dict["Area__about___m²_"] = area_about_m
        if 面積_約_平方米 is not UNSET:
            field_dict["面積_約__平方米_"] = 面積_約_平方米
        if accessibility_location is not UNSET:
            field_dict["Accessibility___Location"] = accessibility_location
        if 前往方法_所處位置 is not UNSET:
            field_dict["前往方法___所處位置"] = 前往方法_所處位置
        if opening_hours is not UNSET:
            field_dict["Opening_Hours"] = opening_hours
        if 開放時間 is not UNSET:
            field_dict["開放時間"] = 開放時間
        if provision_of_sheltered_seating is not UNSET:
            field_dict["Provision_of_Sheltered_Seating"] = (
                provision_of_sheltered_seating
            )
        if 提供有蓋座位 is not UNSET:
            field_dict["提供有蓋座位"] = 提供有蓋座位
        if provision_of_barrier_free_access_facilities is not UNSET:
            field_dict["Provision_of_Barrier-free-access_Facilities"] = (
                provision_of_barrier_free_access_facilities
            )
        if 提供無障礙通道設施 is not UNSET:
            field_dict["提供無障礙通道設施"] = 提供無障礙通道設施
        if remarks is not UNSET:
            field_dict["Remarks"] = remarks
        if 備註 is not UNSET:
            field_dict["備註"] = 備註
        if relevant_district_lands_office is not UNSET:
            field_dict["Relevant_District_Lands_Office"] = (
                relevant_district_lands_office
            )
        if 所屬分區地政處 is not UNSET:
            field_dict["所屬分區地政處"] = 所屬分區地政處
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

        def _parse_ownership(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ownership = _parse_ownership(d.pop("Ownership", UNSET))

        def _parse_業權(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        業權 = _parse_業權(d.pop("業權", UNSET))

        def _parse_area_about_m(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_about_m = _parse_area_about_m(d.pop("Area__about___m²_", UNSET))

        def _parse_面積_約_平方米(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        面積_約_平方米 = _parse_面積_約_平方米(d.pop("面積_約__平方米_", UNSET))

        def _parse_accessibility_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accessibility_location = _parse_accessibility_location(
            d.pop("Accessibility___Location", UNSET)
        )

        def _parse_前往方法_所處位置(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        前往方法_所處位置 = _parse_前往方法_所處位置(
            d.pop("前往方法___所處位置", UNSET)
        )

        def _parse_opening_hours(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours = _parse_opening_hours(d.pop("Opening_Hours", UNSET))

        def _parse_開放時間(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        開放時間 = _parse_開放時間(d.pop("開放時間", UNSET))

        def _parse_provision_of_sheltered_seating(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provision_of_sheltered_seating = _parse_provision_of_sheltered_seating(
            d.pop("Provision_of_Sheltered_Seating", UNSET)
        )

        def _parse_提供有蓋座位(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        提供有蓋座位 = _parse_提供有蓋座位(d.pop("提供有蓋座位", UNSET))

        def _parse_provision_of_barrier_free_access_facilities(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provision_of_barrier_free_access_facilities = (
            _parse_provision_of_barrier_free_access_facilities(
                d.pop("Provision_of_Barrier-free-access_Facilities", UNSET)
            )
        )

        def _parse_提供無障礙通道設施(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        提供無障礙通道設施 = _parse_提供無障礙通道設施(
            d.pop("提供無障礙通道設施", UNSET)
        )

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("Remarks", UNSET))

        def _parse_備註(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        備註 = _parse_備註(d.pop("備註", UNSET))

        def _parse_relevant_district_lands_office(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relevant_district_lands_office = _parse_relevant_district_lands_office(
            d.pop("Relevant_District_Lands_Office", UNSET)
        )

        def _parse_所屬分區地政處(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        所屬分區地政處 = _parse_所屬分區地政處(d.pop("所屬分區地政處", UNSET))

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

        wfs_map_server_wfs_pos_attributes = cls(
            shape=shape,
            objectid=objectid,
            dataset=dataset,
            數據集=數據集,
            facility_name=facility_name,
            address=address,
            設施名稱=設施名稱,
            地址=地址,
            relevant_district_council=relevant_district_council,
            所屬區議會=所屬區議會,
            ownership=ownership,
            業權=業權,
            area_about_m=area_about_m,
            面積_約_平方米=面積_約_平方米,
            accessibility_location=accessibility_location,
            前往方法_所處位置=前往方法_所處位置,
            opening_hours=opening_hours,
            開放時間=開放時間,
            provision_of_sheltered_seating=provision_of_sheltered_seating,
            提供有蓋座位=提供有蓋座位,
            provision_of_barrier_free_access_facilities=provision_of_barrier_free_access_facilities,
            提供無障礙通道設施=提供無障礙通道設施,
            remarks=remarks,
            備註=備註,
            relevant_district_lands_office=relevant_district_lands_office,
            所屬分區地政處=所屬分區地政處,
            northing_坐標北=northing_坐標北,
            easting_坐標東=easting_坐標東,
            latitude_緯度=latitude_緯度,
            longitude_經度=longitude_經度,
            last_updated_date_最後更新日期=last_updated_date_最後更新日期,
        )

        wfs_map_server_wfs_pos_attributes.additional_properties = d
        return wfs_map_server_wfs_pos_attributes

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
