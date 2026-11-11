from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsLAOLSRAttributes")


@_attrs_define
class WfsMapServerWfsLAOLSRAttributes:
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
        financial_year_of_land_sale_result_announced (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        賣地結果公布的財政年度 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        disposal_type (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        賣地方式 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        sale_tender_award_date (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        賣地_招標成交日期 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        user (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        用途 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        area_in_square_metres (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        面積_平方米 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        premium_million (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        地價_百萬元 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        no_of_tender_bids (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        投標者總數目 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        highest_tenderer_parent_company (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        最高的投標者_母公司 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        name_of_unsuccessful_tenderers_parent_company_listed_in_alphabetical_order (None | str | Unset): Native XSD type
            . Requiredness is not projected from XML occurrence into all JSON queries.
        落選投標者的名稱_母公司_按英文字母順序臚列 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        tender_amounts_submitted_by_the_unsuccessful_tenderers (None | str | Unset): Native XSD type . Requiredness is
            not projected from XML occurrence into all JSON queries.
        落選投標者的投標金額_以不具名方式_依次由高至低公布 (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        remarks (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        備註 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
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
    financial_year_of_land_sale_result_announced: None | str | Unset = UNSET
    賣地結果公布的財政年度: None | str | Unset = UNSET
    disposal_type: None | str | Unset = UNSET
    賣地方式: None | str | Unset = UNSET
    sale_tender_award_date: None | str | Unset = UNSET
    賣地_招標成交日期: None | str | Unset = UNSET
    user: None | str | Unset = UNSET
    用途: None | str | Unset = UNSET
    area_in_square_metres: None | str | Unset = UNSET
    面積_平方米: None | str | Unset = UNSET
    premium_million: None | str | Unset = UNSET
    地價_百萬元: None | str | Unset = UNSET
    no_of_tender_bids: None | str | Unset = UNSET
    投標者總數目: None | str | Unset = UNSET
    highest_tenderer_parent_company: None | str | Unset = UNSET
    最高的投標者_母公司: None | str | Unset = UNSET
    name_of_unsuccessful_tenderers_parent_company_listed_in_alphabetical_order: (
        None | str | Unset
    ) = UNSET
    落選投標者的名稱_母公司_按英文字母順序臚列: None | str | Unset = UNSET
    tender_amounts_submitted_by_the_unsuccessful_tenderers: None | str | Unset = UNSET
    落選投標者的投標金額_以不具名方式_依次由高至低公布: None | str | Unset = UNSET
    remarks: None | str | Unset = UNSET
    備註: None | str | Unset = UNSET
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

        financial_year_of_land_sale_result_announced: None | str | Unset
        if isinstance(self.financial_year_of_land_sale_result_announced, Unset):
            financial_year_of_land_sale_result_announced = UNSET
        else:
            financial_year_of_land_sale_result_announced = (
                self.financial_year_of_land_sale_result_announced
            )

        賣地結果公布的財政年度: None | str | Unset
        if isinstance(self.賣地結果公布的財政年度, Unset):
            賣地結果公布的財政年度 = UNSET
        else:
            賣地結果公布的財政年度 = self.賣地結果公布的財政年度

        disposal_type: None | str | Unset
        if isinstance(self.disposal_type, Unset):
            disposal_type = UNSET
        else:
            disposal_type = self.disposal_type

        賣地方式: None | str | Unset
        if isinstance(self.賣地方式, Unset):
            賣地方式 = UNSET
        else:
            賣地方式 = self.賣地方式

        sale_tender_award_date: None | str | Unset
        if isinstance(self.sale_tender_award_date, Unset):
            sale_tender_award_date = UNSET
        else:
            sale_tender_award_date = self.sale_tender_award_date

        賣地_招標成交日期: None | str | Unset
        if isinstance(self.賣地_招標成交日期, Unset):
            賣地_招標成交日期 = UNSET
        else:
            賣地_招標成交日期 = self.賣地_招標成交日期

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

        area_in_square_metres: None | str | Unset
        if isinstance(self.area_in_square_metres, Unset):
            area_in_square_metres = UNSET
        else:
            area_in_square_metres = self.area_in_square_metres

        面積_平方米: None | str | Unset
        if isinstance(self.面積_平方米, Unset):
            面積_平方米 = UNSET
        else:
            面積_平方米 = self.面積_平方米

        premium_million: None | str | Unset
        if isinstance(self.premium_million, Unset):
            premium_million = UNSET
        else:
            premium_million = self.premium_million

        地價_百萬元: None | str | Unset
        if isinstance(self.地價_百萬元, Unset):
            地價_百萬元 = UNSET
        else:
            地價_百萬元 = self.地價_百萬元

        no_of_tender_bids: None | str | Unset
        if isinstance(self.no_of_tender_bids, Unset):
            no_of_tender_bids = UNSET
        else:
            no_of_tender_bids = self.no_of_tender_bids

        投標者總數目: None | str | Unset
        if isinstance(self.投標者總數目, Unset):
            投標者總數目 = UNSET
        else:
            投標者總數目 = self.投標者總數目

        highest_tenderer_parent_company: None | str | Unset
        if isinstance(self.highest_tenderer_parent_company, Unset):
            highest_tenderer_parent_company = UNSET
        else:
            highest_tenderer_parent_company = self.highest_tenderer_parent_company

        最高的投標者_母公司: None | str | Unset
        if isinstance(self.最高的投標者_母公司, Unset):
            最高的投標者_母公司 = UNSET
        else:
            最高的投標者_母公司 = self.最高的投標者_母公司

        name_of_unsuccessful_tenderers_parent_company_listed_in_alphabetical_order: (
            None | str | Unset
        )
        if isinstance(
            self.name_of_unsuccessful_tenderers_parent_company_listed_in_alphabetical_order,
            Unset,
        ):
            name_of_unsuccessful_tenderers_parent_company_listed_in_alphabetical_order = UNSET
        else:
            name_of_unsuccessful_tenderers_parent_company_listed_in_alphabetical_order = self.name_of_unsuccessful_tenderers_parent_company_listed_in_alphabetical_order

        落選投標者的名稱_母公司_按英文字母順序臚列: None | str | Unset
        if isinstance(self.落選投標者的名稱_母公司_按英文字母順序臚列, Unset):
            落選投標者的名稱_母公司_按英文字母順序臚列 = UNSET
        else:
            落選投標者的名稱_母公司_按英文字母順序臚列 = (
                self.落選投標者的名稱_母公司_按英文字母順序臚列
            )

        tender_amounts_submitted_by_the_unsuccessful_tenderers: None | str | Unset
        if isinstance(
            self.tender_amounts_submitted_by_the_unsuccessful_tenderers, Unset
        ):
            tender_amounts_submitted_by_the_unsuccessful_tenderers = UNSET
        else:
            tender_amounts_submitted_by_the_unsuccessful_tenderers = (
                self.tender_amounts_submitted_by_the_unsuccessful_tenderers
            )

        落選投標者的投標金額_以不具名方式_依次由高至低公布: None | str | Unset
        if isinstance(self.落選投標者的投標金額_以不具名方式_依次由高至低公布, Unset):
            落選投標者的投標金額_以不具名方式_依次由高至低公布 = UNSET
        else:
            落選投標者的投標金額_以不具名方式_依次由高至低公布 = (
                self.落選投標者的投標金額_以不具名方式_依次由高至低公布
            )

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
        if financial_year_of_land_sale_result_announced is not UNSET:
            field_dict["Financial_Year_of_Land_Sale_Result_Announced"] = (
                financial_year_of_land_sale_result_announced
            )
        if 賣地結果公布的財政年度 is not UNSET:
            field_dict["賣地結果公布的財政年度"] = 賣地結果公布的財政年度
        if disposal_type is not UNSET:
            field_dict["Disposal_Type"] = disposal_type
        if 賣地方式 is not UNSET:
            field_dict["賣地方式"] = 賣地方式
        if sale_tender_award_date is not UNSET:
            field_dict["Sale_Tender_Award_Date"] = sale_tender_award_date
        if 賣地_招標成交日期 is not UNSET:
            field_dict["賣地_招標成交日期"] = 賣地_招標成交日期
        if user is not UNSET:
            field_dict["User"] = user
        if 用途 is not UNSET:
            field_dict["用途"] = 用途
        if area_in_square_metres is not UNSET:
            field_dict["Area_in_Square_Metres"] = area_in_square_metres
        if 面積_平方米 is not UNSET:
            field_dict["面積_平方米_"] = 面積_平方米
        if premium_million is not UNSET:
            field_dict["Premium____Million_"] = premium_million
        if 地價_百萬元 is not UNSET:
            field_dict["地價_百萬元_"] = 地價_百萬元
        if no_of_tender_bids is not UNSET:
            field_dict["No._of_Tender_Bids"] = no_of_tender_bids
        if 投標者總數目 is not UNSET:
            field_dict["投標者總數目"] = 投標者總數目
        if highest_tenderer_parent_company is not UNSET:
            field_dict["Highest_tenderer__parent_company_"] = (
                highest_tenderer_parent_company
            )
        if 最高的投標者_母公司 is not UNSET:
            field_dict["最高的投標者__母公司_"] = 最高的投標者_母公司
        if (
            name_of_unsuccessful_tenderers_parent_company_listed_in_alphabetical_order
            is not UNSET
        ):
            field_dict[
                "Name_of_unsuccessful_tenderers__parent_company__Listed_in_alphabetical_order_"
            ] = name_of_unsuccessful_tenderers_parent_company_listed_in_alphabetical_order
        if 落選投標者的名稱_母公司_按英文字母順序臚列 is not UNSET:
            field_dict["落選投標者的名稱__母公司___按英文字母順序臚列_"] = (
                落選投標者的名稱_母公司_按英文字母順序臚列
            )
        if tender_amounts_submitted_by_the_unsuccessful_tenderers is not UNSET:
            field_dict["Tender_amounts_submitted_by_the_unsuccessful_tenderers"] = (
                tender_amounts_submitted_by_the_unsuccessful_tenderers
            )
        if 落選投標者的投標金額_以不具名方式_依次由高至低公布 is not UNSET:
            field_dict["落選投標者的投標金額__以不具名方式_依次由高至低公布_"] = (
                落選投標者的投標金額_以不具名方式_依次由高至低公布
            )
        if remarks is not UNSET:
            field_dict["Remarks"] = remarks
        if 備註 is not UNSET:
            field_dict["備註"] = 備註
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

        def _parse_financial_year_of_land_sale_result_announced(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        financial_year_of_land_sale_result_announced = (
            _parse_financial_year_of_land_sale_result_announced(
                d.pop("Financial_Year_of_Land_Sale_Result_Announced", UNSET)
            )
        )

        def _parse_賣地結果公布的財政年度(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        賣地結果公布的財政年度 = _parse_賣地結果公布的財政年度(
            d.pop("賣地結果公布的財政年度", UNSET)
        )

        def _parse_disposal_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disposal_type = _parse_disposal_type(d.pop("Disposal_Type", UNSET))

        def _parse_賣地方式(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        賣地方式 = _parse_賣地方式(d.pop("賣地方式", UNSET))

        def _parse_sale_tender_award_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sale_tender_award_date = _parse_sale_tender_award_date(
            d.pop("Sale_Tender_Award_Date", UNSET)
        )

        def _parse_賣地_招標成交日期(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        賣地_招標成交日期 = _parse_賣地_招標成交日期(d.pop("賣地_招標成交日期", UNSET))

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

        def _parse_area_in_square_metres(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_in_square_metres = _parse_area_in_square_metres(
            d.pop("Area_in_Square_Metres", UNSET)
        )

        def _parse_面積_平方米(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        面積_平方米 = _parse_面積_平方米(d.pop("面積_平方米_", UNSET))

        def _parse_premium_million(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        premium_million = _parse_premium_million(d.pop("Premium____Million_", UNSET))

        def _parse_地價_百萬元(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        地價_百萬元 = _parse_地價_百萬元(d.pop("地價_百萬元_", UNSET))

        def _parse_no_of_tender_bids(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_tender_bids = _parse_no_of_tender_bids(d.pop("No._of_Tender_Bids", UNSET))

        def _parse_投標者總數目(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        投標者總數目 = _parse_投標者總數目(d.pop("投標者總數目", UNSET))

        def _parse_highest_tenderer_parent_company(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        highest_tenderer_parent_company = _parse_highest_tenderer_parent_company(
            d.pop("Highest_tenderer__parent_company_", UNSET)
        )

        def _parse_最高的投標者_母公司(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        最高的投標者_母公司 = _parse_最高的投標者_母公司(
            d.pop("最高的投標者__母公司_", UNSET)
        )

        def _parse_name_of_unsuccessful_tenderers_parent_company_listed_in_alphabetical_order(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_unsuccessful_tenderers_parent_company_listed_in_alphabetical_order = _parse_name_of_unsuccessful_tenderers_parent_company_listed_in_alphabetical_order(
            d.pop(
                "Name_of_unsuccessful_tenderers__parent_company__Listed_in_alphabetical_order_",
                UNSET,
            )
        )

        def _parse_落選投標者的名稱_母公司_按英文字母順序臚列(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        落選投標者的名稱_母公司_按英文字母順序臚列 = (
            _parse_落選投標者的名稱_母公司_按英文字母順序臚列(
                d.pop("落選投標者的名稱__母公司___按英文字母順序臚列_", UNSET)
            )
        )

        def _parse_tender_amounts_submitted_by_the_unsuccessful_tenderers(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tender_amounts_submitted_by_the_unsuccessful_tenderers = (
            _parse_tender_amounts_submitted_by_the_unsuccessful_tenderers(
                d.pop("Tender_amounts_submitted_by_the_unsuccessful_tenderers", UNSET)
            )
        )

        def _parse_落選投標者的投標金額_以不具名方式_依次由高至低公布(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        落選投標者的投標金額_以不具名方式_依次由高至低公布 = (
            _parse_落選投標者的投標金額_以不具名方式_依次由高至低公布(
                d.pop("落選投標者的投標金額__以不具名方式_依次由高至低公布_", UNSET)
            )
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

        wfs_map_server_wfs_laolsr_attributes = cls(
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
            financial_year_of_land_sale_result_announced=financial_year_of_land_sale_result_announced,
            賣地結果公布的財政年度=賣地結果公布的財政年度,
            disposal_type=disposal_type,
            賣地方式=賣地方式,
            sale_tender_award_date=sale_tender_award_date,
            賣地_招標成交日期=賣地_招標成交日期,
            user=user,
            用途=用途,
            area_in_square_metres=area_in_square_metres,
            面積_平方米=面積_平方米,
            premium_million=premium_million,
            地價_百萬元=地價_百萬元,
            no_of_tender_bids=no_of_tender_bids,
            投標者總數目=投標者總數目,
            highest_tenderer_parent_company=highest_tenderer_parent_company,
            最高的投標者_母公司=最高的投標者_母公司,
            name_of_unsuccessful_tenderers_parent_company_listed_in_alphabetical_order=name_of_unsuccessful_tenderers_parent_company_listed_in_alphabetical_order,
            落選投標者的名稱_母公司_按英文字母順序臚列=落選投標者的名稱_母公司_按英文字母順序臚列,
            tender_amounts_submitted_by_the_unsuccessful_tenderers=tender_amounts_submitted_by_the_unsuccessful_tenderers,
            落選投標者的投標金額_以不具名方式_依次由高至低公布=落選投標者的投標金額_以不具名方式_依次由高至低公布,
            remarks=remarks,
            備註=備註,
            northing_坐標北=northing_坐標北,
            easting_坐標東=easting_坐標東,
            latitude_緯度=latitude_緯度,
            longitude_經度=longitude_經度,
            last_updated_date_最後更新日期=last_updated_date_最後更新日期,
        )

        wfs_map_server_wfs_laolsr_attributes.additional_properties = d
        return wfs_map_server_wfs_laolsr_attributes

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
