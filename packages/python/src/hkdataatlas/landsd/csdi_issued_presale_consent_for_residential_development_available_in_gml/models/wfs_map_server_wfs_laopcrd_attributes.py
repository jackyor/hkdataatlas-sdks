from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsLAOPCRDAttributes")


@_attrs_define
class WfsMapServerWfsLAOPCRDAttributes:
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
        address (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        地段編號 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        地址 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        issue_year (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        同意書年份 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        issue_month (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        同意書月份 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        vendor (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        賣方 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        development_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        發展項目名稱 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        holding_company (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        控權公司 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        solicitors (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        律師 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        authorized_person_and_his_her_company (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        認可人士及其公司 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        building_contractor (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        承建商 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        mortgagee (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        按揭銀行 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        undertaking_bank (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        提交承諾書之銀行 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        financier (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        融資人 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        field_a_issue_date (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        field_a_同意書日期 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        field_b_consent_effective_date (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        field_b_同意書生效日期 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        field_c_estimated_completion_date (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        field_c_預計落成日期 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        no_of_days_before_estimated_completion_date_c_b (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        相距預計落成日期的日數_c_b (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        no_of_residential_units (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        住宅單位數目 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        remarks (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        備註 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        last_update (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        最後更新日期 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
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
    address: None | str | Unset = UNSET
    地段編號: None | str | Unset = UNSET
    地址: None | str | Unset = UNSET
    issue_year: None | str | Unset = UNSET
    同意書年份: None | str | Unset = UNSET
    issue_month: None | str | Unset = UNSET
    同意書月份: None | str | Unset = UNSET
    vendor: None | str | Unset = UNSET
    賣方: None | str | Unset = UNSET
    development_name: None | str | Unset = UNSET
    發展項目名稱: None | str | Unset = UNSET
    holding_company: None | str | Unset = UNSET
    控權公司: None | str | Unset = UNSET
    solicitors: None | str | Unset = UNSET
    律師: None | str | Unset = UNSET
    authorized_person_and_his_her_company: None | str | Unset = UNSET
    認可人士及其公司: None | str | Unset = UNSET
    building_contractor: None | str | Unset = UNSET
    承建商: None | str | Unset = UNSET
    mortgagee: None | str | Unset = UNSET
    按揭銀行: None | str | Unset = UNSET
    undertaking_bank: None | str | Unset = UNSET
    提交承諾書之銀行: None | str | Unset = UNSET
    financier: None | str | Unset = UNSET
    融資人: None | str | Unset = UNSET
    field_a_issue_date: None | str | Unset = UNSET
    field_a_同意書日期: None | str | Unset = UNSET
    field_b_consent_effective_date: None | str | Unset = UNSET
    field_b_同意書生效日期: None | str | Unset = UNSET
    field_c_estimated_completion_date: None | str | Unset = UNSET
    field_c_預計落成日期: None | str | Unset = UNSET
    no_of_days_before_estimated_completion_date_c_b: None | str | Unset = UNSET
    相距預計落成日期的日數_c_b: None | str | Unset = UNSET
    no_of_residential_units: None | str | Unset = UNSET
    住宅單位數目: None | str | Unset = UNSET
    remarks: None | str | Unset = UNSET
    備註: None | str | Unset = UNSET
    last_update: None | str | Unset = UNSET
    最後更新日期: None | str | Unset = UNSET
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

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        地段編號: None | str | Unset
        if isinstance(self.地段編號, Unset):
            地段編號 = UNSET
        else:
            地段編號 = self.地段編號

        地址: None | str | Unset
        if isinstance(self.地址, Unset):
            地址 = UNSET
        else:
            地址 = self.地址

        issue_year: None | str | Unset
        if isinstance(self.issue_year, Unset):
            issue_year = UNSET
        else:
            issue_year = self.issue_year

        同意書年份: None | str | Unset
        if isinstance(self.同意書年份, Unset):
            同意書年份 = UNSET
        else:
            同意書年份 = self.同意書年份

        issue_month: None | str | Unset
        if isinstance(self.issue_month, Unset):
            issue_month = UNSET
        else:
            issue_month = self.issue_month

        同意書月份: None | str | Unset
        if isinstance(self.同意書月份, Unset):
            同意書月份 = UNSET
        else:
            同意書月份 = self.同意書月份

        vendor: None | str | Unset
        if isinstance(self.vendor, Unset):
            vendor = UNSET
        else:
            vendor = self.vendor

        賣方: None | str | Unset
        if isinstance(self.賣方, Unset):
            賣方 = UNSET
        else:
            賣方 = self.賣方

        development_name: None | str | Unset
        if isinstance(self.development_name, Unset):
            development_name = UNSET
        else:
            development_name = self.development_name

        發展項目名稱: None | str | Unset
        if isinstance(self.發展項目名稱, Unset):
            發展項目名稱 = UNSET
        else:
            發展項目名稱 = self.發展項目名稱

        holding_company: None | str | Unset
        if isinstance(self.holding_company, Unset):
            holding_company = UNSET
        else:
            holding_company = self.holding_company

        控權公司: None | str | Unset
        if isinstance(self.控權公司, Unset):
            控權公司 = UNSET
        else:
            控權公司 = self.控權公司

        solicitors: None | str | Unset
        if isinstance(self.solicitors, Unset):
            solicitors = UNSET
        else:
            solicitors = self.solicitors

        律師: None | str | Unset
        if isinstance(self.律師, Unset):
            律師 = UNSET
        else:
            律師 = self.律師

        authorized_person_and_his_her_company: None | str | Unset
        if isinstance(self.authorized_person_and_his_her_company, Unset):
            authorized_person_and_his_her_company = UNSET
        else:
            authorized_person_and_his_her_company = (
                self.authorized_person_and_his_her_company
            )

        認可人士及其公司: None | str | Unset
        if isinstance(self.認可人士及其公司, Unset):
            認可人士及其公司 = UNSET
        else:
            認可人士及其公司 = self.認可人士及其公司

        building_contractor: None | str | Unset
        if isinstance(self.building_contractor, Unset):
            building_contractor = UNSET
        else:
            building_contractor = self.building_contractor

        承建商: None | str | Unset
        if isinstance(self.承建商, Unset):
            承建商 = UNSET
        else:
            承建商 = self.承建商

        mortgagee: None | str | Unset
        if isinstance(self.mortgagee, Unset):
            mortgagee = UNSET
        else:
            mortgagee = self.mortgagee

        按揭銀行: None | str | Unset
        if isinstance(self.按揭銀行, Unset):
            按揭銀行 = UNSET
        else:
            按揭銀行 = self.按揭銀行

        undertaking_bank: None | str | Unset
        if isinstance(self.undertaking_bank, Unset):
            undertaking_bank = UNSET
        else:
            undertaking_bank = self.undertaking_bank

        提交承諾書之銀行: None | str | Unset
        if isinstance(self.提交承諾書之銀行, Unset):
            提交承諾書之銀行 = UNSET
        else:
            提交承諾書之銀行 = self.提交承諾書之銀行

        financier: None | str | Unset
        if isinstance(self.financier, Unset):
            financier = UNSET
        else:
            financier = self.financier

        融資人: None | str | Unset
        if isinstance(self.融資人, Unset):
            融資人 = UNSET
        else:
            融資人 = self.融資人

        field_a_issue_date: None | str | Unset
        if isinstance(self.field_a_issue_date, Unset):
            field_a_issue_date = UNSET
        else:
            field_a_issue_date = self.field_a_issue_date

        field_a_同意書日期: None | str | Unset
        if isinstance(self.field_a_同意書日期, Unset):
            field_a_同意書日期 = UNSET
        else:
            field_a_同意書日期 = self.field_a_同意書日期

        field_b_consent_effective_date: None | str | Unset
        if isinstance(self.field_b_consent_effective_date, Unset):
            field_b_consent_effective_date = UNSET
        else:
            field_b_consent_effective_date = self.field_b_consent_effective_date

        field_b_同意書生效日期: None | str | Unset
        if isinstance(self.field_b_同意書生效日期, Unset):
            field_b_同意書生效日期 = UNSET
        else:
            field_b_同意書生效日期 = self.field_b_同意書生效日期

        field_c_estimated_completion_date: None | str | Unset
        if isinstance(self.field_c_estimated_completion_date, Unset):
            field_c_estimated_completion_date = UNSET
        else:
            field_c_estimated_completion_date = self.field_c_estimated_completion_date

        field_c_預計落成日期: None | str | Unset
        if isinstance(self.field_c_預計落成日期, Unset):
            field_c_預計落成日期 = UNSET
        else:
            field_c_預計落成日期 = self.field_c_預計落成日期

        no_of_days_before_estimated_completion_date_c_b: None | str | Unset
        if isinstance(self.no_of_days_before_estimated_completion_date_c_b, Unset):
            no_of_days_before_estimated_completion_date_c_b = UNSET
        else:
            no_of_days_before_estimated_completion_date_c_b = (
                self.no_of_days_before_estimated_completion_date_c_b
            )

        相距預計落成日期的日數_c_b: None | str | Unset
        if isinstance(self.相距預計落成日期的日數_c_b, Unset):
            相距預計落成日期的日數_c_b = UNSET
        else:
            相距預計落成日期的日數_c_b = self.相距預計落成日期的日數_c_b

        no_of_residential_units: None | str | Unset
        if isinstance(self.no_of_residential_units, Unset):
            no_of_residential_units = UNSET
        else:
            no_of_residential_units = self.no_of_residential_units

        住宅單位數目: None | str | Unset
        if isinstance(self.住宅單位數目, Unset):
            住宅單位數目 = UNSET
        else:
            住宅單位數目 = self.住宅單位數目

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

        last_update: None | str | Unset
        if isinstance(self.last_update, Unset):
            last_update = UNSET
        else:
            last_update = self.last_update

        最後更新日期: None | str | Unset
        if isinstance(self.最後更新日期, Unset):
            最後更新日期 = UNSET
        else:
            最後更新日期 = self.最後更新日期

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
        if address is not UNSET:
            field_dict["Address"] = address
        if 地段編號 is not UNSET:
            field_dict["地段編號"] = 地段編號
        if 地址 is not UNSET:
            field_dict["地址"] = 地址
        if issue_year is not UNSET:
            field_dict["Issue_Year"] = issue_year
        if 同意書年份 is not UNSET:
            field_dict["同意書年份"] = 同意書年份
        if issue_month is not UNSET:
            field_dict["Issue_Month"] = issue_month
        if 同意書月份 is not UNSET:
            field_dict["同意書月份"] = 同意書月份
        if vendor is not UNSET:
            field_dict["Vendor"] = vendor
        if 賣方 is not UNSET:
            field_dict["賣方"] = 賣方
        if development_name is not UNSET:
            field_dict["Development_Name"] = development_name
        if 發展項目名稱 is not UNSET:
            field_dict["發展項目名稱"] = 發展項目名稱
        if holding_company is not UNSET:
            field_dict["Holding_Company"] = holding_company
        if 控權公司 is not UNSET:
            field_dict["控權公司"] = 控權公司
        if solicitors is not UNSET:
            field_dict["Solicitors"] = solicitors
        if 律師 is not UNSET:
            field_dict["律師"] = 律師
        if authorized_person_and_his_her_company is not UNSET:
            field_dict["Authorized_Person_and_his_her_Company"] = (
                authorized_person_and_his_her_company
            )
        if 認可人士及其公司 is not UNSET:
            field_dict["認可人士及其公司"] = 認可人士及其公司
        if building_contractor is not UNSET:
            field_dict["Building_Contractor"] = building_contractor
        if 承建商 is not UNSET:
            field_dict["承建商"] = 承建商
        if mortgagee is not UNSET:
            field_dict["Mortgagee"] = mortgagee
        if 按揭銀行 is not UNSET:
            field_dict["按揭銀行"] = 按揭銀行
        if undertaking_bank is not UNSET:
            field_dict["Undertaking_Bank"] = undertaking_bank
        if 提交承諾書之銀行 is not UNSET:
            field_dict["提交承諾書之銀行"] = 提交承諾書之銀行
        if financier is not UNSET:
            field_dict["Financier"] = financier
        if 融資人 is not UNSET:
            field_dict["融資人"] = 融資人
        if field_a_issue_date is not UNSET:
            field_dict["_a__Issue_Date"] = field_a_issue_date
        if field_a_同意書日期 is not UNSET:
            field_dict["_a__同意書日期"] = field_a_同意書日期
        if field_b_consent_effective_date is not UNSET:
            field_dict["_b__Consent_Effective_Date"] = field_b_consent_effective_date
        if field_b_同意書生效日期 is not UNSET:
            field_dict["_b__同意書生效日期"] = field_b_同意書生效日期
        if field_c_estimated_completion_date is not UNSET:
            field_dict["_c__Estimated_Completion_Date"] = (
                field_c_estimated_completion_date
            )
        if field_c_預計落成日期 is not UNSET:
            field_dict["_c__預計落成日期"] = field_c_預計落成日期
        if no_of_days_before_estimated_completion_date_c_b is not UNSET:
            field_dict["No._of_Days_before_Estimated_Completion_Date__c___-__b_"] = (
                no_of_days_before_estimated_completion_date_c_b
            )
        if 相距預計落成日期的日數_c_b is not UNSET:
            field_dict["相距預計落成日期的日數__c___-__b_"] = 相距預計落成日期的日數_c_b
        if no_of_residential_units is not UNSET:
            field_dict["No._of_Residential_Units"] = no_of_residential_units
        if 住宅單位數目 is not UNSET:
            field_dict["住宅單位數目"] = 住宅單位數目
        if remarks is not UNSET:
            field_dict["Remarks"] = remarks
        if 備註 is not UNSET:
            field_dict["備註"] = 備註
        if last_update is not UNSET:
            field_dict["Last_Update"] = last_update
        if 最後更新日期 is not UNSET:
            field_dict["最後更新日期"] = 最後更新日期
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

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("Address", UNSET))

        def _parse_地段編號(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        地段編號 = _parse_地段編號(d.pop("地段編號", UNSET))

        def _parse_地址(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        地址 = _parse_地址(d.pop("地址", UNSET))

        def _parse_issue_year(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issue_year = _parse_issue_year(d.pop("Issue_Year", UNSET))

        def _parse_同意書年份(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        同意書年份 = _parse_同意書年份(d.pop("同意書年份", UNSET))

        def _parse_issue_month(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issue_month = _parse_issue_month(d.pop("Issue_Month", UNSET))

        def _parse_同意書月份(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        同意書月份 = _parse_同意書月份(d.pop("同意書月份", UNSET))

        def _parse_vendor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vendor = _parse_vendor(d.pop("Vendor", UNSET))

        def _parse_賣方(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        賣方 = _parse_賣方(d.pop("賣方", UNSET))

        def _parse_development_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        development_name = _parse_development_name(d.pop("Development_Name", UNSET))

        def _parse_發展項目名稱(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        發展項目名稱 = _parse_發展項目名稱(d.pop("發展項目名稱", UNSET))

        def _parse_holding_company(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        holding_company = _parse_holding_company(d.pop("Holding_Company", UNSET))

        def _parse_控權公司(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        控權公司 = _parse_控權公司(d.pop("控權公司", UNSET))

        def _parse_solicitors(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        solicitors = _parse_solicitors(d.pop("Solicitors", UNSET))

        def _parse_律師(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        律師 = _parse_律師(d.pop("律師", UNSET))

        def _parse_authorized_person_and_his_her_company(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        authorized_person_and_his_her_company = (
            _parse_authorized_person_and_his_her_company(
                d.pop("Authorized_Person_and_his_her_Company", UNSET)
            )
        )

        def _parse_認可人士及其公司(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        認可人士及其公司 = _parse_認可人士及其公司(d.pop("認可人士及其公司", UNSET))

        def _parse_building_contractor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_contractor = _parse_building_contractor(
            d.pop("Building_Contractor", UNSET)
        )

        def _parse_承建商(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        承建商 = _parse_承建商(d.pop("承建商", UNSET))

        def _parse_mortgagee(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mortgagee = _parse_mortgagee(d.pop("Mortgagee", UNSET))

        def _parse_按揭銀行(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        按揭銀行 = _parse_按揭銀行(d.pop("按揭銀行", UNSET))

        def _parse_undertaking_bank(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        undertaking_bank = _parse_undertaking_bank(d.pop("Undertaking_Bank", UNSET))

        def _parse_提交承諾書之銀行(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        提交承諾書之銀行 = _parse_提交承諾書之銀行(d.pop("提交承諾書之銀行", UNSET))

        def _parse_financier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        financier = _parse_financier(d.pop("Financier", UNSET))

        def _parse_融資人(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        融資人 = _parse_融資人(d.pop("融資人", UNSET))

        def _parse_field_a_issue_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_a_issue_date = _parse_field_a_issue_date(d.pop("_a__Issue_Date", UNSET))

        def _parse_field_a_同意書日期(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_a_同意書日期 = _parse_field_a_同意書日期(d.pop("_a__同意書日期", UNSET))

        def _parse_field_b_consent_effective_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_b_consent_effective_date = _parse_field_b_consent_effective_date(
            d.pop("_b__Consent_Effective_Date", UNSET)
        )

        def _parse_field_b_同意書生效日期(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_b_同意書生效日期 = _parse_field_b_同意書生效日期(
            d.pop("_b__同意書生效日期", UNSET)
        )

        def _parse_field_c_estimated_completion_date(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_c_estimated_completion_date = _parse_field_c_estimated_completion_date(
            d.pop("_c__Estimated_Completion_Date", UNSET)
        )

        def _parse_field_c_預計落成日期(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_c_預計落成日期 = _parse_field_c_預計落成日期(
            d.pop("_c__預計落成日期", UNSET)
        )

        def _parse_no_of_days_before_estimated_completion_date_c_b(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_days_before_estimated_completion_date_c_b = (
            _parse_no_of_days_before_estimated_completion_date_c_b(
                d.pop("No._of_Days_before_Estimated_Completion_Date__c___-__b_", UNSET)
            )
        )

        def _parse_相距預計落成日期的日數_c_b(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        相距預計落成日期的日數_c_b = _parse_相距預計落成日期的日數_c_b(
            d.pop("相距預計落成日期的日數__c___-__b_", UNSET)
        )

        def _parse_no_of_residential_units(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_residential_units = _parse_no_of_residential_units(
            d.pop("No._of_Residential_Units", UNSET)
        )

        def _parse_住宅單位數目(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        住宅單位數目 = _parse_住宅單位數目(d.pop("住宅單位數目", UNSET))

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

        def _parse_last_update(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_update = _parse_last_update(d.pop("Last_Update", UNSET))

        def _parse_最後更新日期(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        最後更新日期 = _parse_最後更新日期(d.pop("最後更新日期", UNSET))

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

        wfs_map_server_wfs_laopcrd_attributes = cls(
            shape=shape,
            objectid=objectid,
            dataset=dataset,
            數據集=數據集,
            lot_number=lot_number,
            address=address,
            地段編號=地段編號,
            地址=地址,
            issue_year=issue_year,
            同意書年份=同意書年份,
            issue_month=issue_month,
            同意書月份=同意書月份,
            vendor=vendor,
            賣方=賣方,
            development_name=development_name,
            發展項目名稱=發展項目名稱,
            holding_company=holding_company,
            控權公司=控權公司,
            solicitors=solicitors,
            律師=律師,
            authorized_person_and_his_her_company=authorized_person_and_his_her_company,
            認可人士及其公司=認可人士及其公司,
            building_contractor=building_contractor,
            承建商=承建商,
            mortgagee=mortgagee,
            按揭銀行=按揭銀行,
            undertaking_bank=undertaking_bank,
            提交承諾書之銀行=提交承諾書之銀行,
            financier=financier,
            融資人=融資人,
            field_a_issue_date=field_a_issue_date,
            field_a_同意書日期=field_a_同意書日期,
            field_b_consent_effective_date=field_b_consent_effective_date,
            field_b_同意書生效日期=field_b_同意書生效日期,
            field_c_estimated_completion_date=field_c_estimated_completion_date,
            field_c_預計落成日期=field_c_預計落成日期,
            no_of_days_before_estimated_completion_date_c_b=no_of_days_before_estimated_completion_date_c_b,
            相距預計落成日期的日數_c_b=相距預計落成日期的日數_c_b,
            no_of_residential_units=no_of_residential_units,
            住宅單位數目=住宅單位數目,
            remarks=remarks,
            備註=備註,
            last_update=last_update,
            最後更新日期=最後更新日期,
            northing_坐標北=northing_坐標北,
            easting_坐標東=easting_坐標東,
            latitude_緯度=latitude_緯度,
            longitude_經度=longitude_經度,
            last_updated_date_最後更新日期=last_updated_date_最後更新日期,
        )

        wfs_map_server_wfs_laopcrd_attributes.additional_properties = d
        return wfs_map_server_wfs_laopcrd_attributes

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
