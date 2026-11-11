from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsLAOCCAttributes")


@_attrs_define
class WfsMapServerWfsLAOCCAttributes:
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
        year_of_issuance_of_certificate_of_compliance (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        合約完成證明書簽發年度 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        date_of_certificate_of_compliance (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        合約完成證明書日期 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        no_of_residential_units_involved (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        涉及住宅單位數目 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
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
    year_of_issuance_of_certificate_of_compliance: None | str | Unset = UNSET
    合約完成證明書簽發年度: None | str | Unset = UNSET
    date_of_certificate_of_compliance: None | str | Unset = UNSET
    合約完成證明書日期: None | str | Unset = UNSET
    no_of_residential_units_involved: None | str | Unset = UNSET
    涉及住宅單位數目: None | str | Unset = UNSET
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

        year_of_issuance_of_certificate_of_compliance: None | str | Unset
        if isinstance(self.year_of_issuance_of_certificate_of_compliance, Unset):
            year_of_issuance_of_certificate_of_compliance = UNSET
        else:
            year_of_issuance_of_certificate_of_compliance = (
                self.year_of_issuance_of_certificate_of_compliance
            )

        合約完成證明書簽發年度: None | str | Unset
        if isinstance(self.合約完成證明書簽發年度, Unset):
            合約完成證明書簽發年度 = UNSET
        else:
            合約完成證明書簽發年度 = self.合約完成證明書簽發年度

        date_of_certificate_of_compliance: None | str | Unset
        if isinstance(self.date_of_certificate_of_compliance, Unset):
            date_of_certificate_of_compliance = UNSET
        else:
            date_of_certificate_of_compliance = self.date_of_certificate_of_compliance

        合約完成證明書日期: None | str | Unset
        if isinstance(self.合約完成證明書日期, Unset):
            合約完成證明書日期 = UNSET
        else:
            合約完成證明書日期 = self.合約完成證明書日期

        no_of_residential_units_involved: None | str | Unset
        if isinstance(self.no_of_residential_units_involved, Unset):
            no_of_residential_units_involved = UNSET
        else:
            no_of_residential_units_involved = self.no_of_residential_units_involved

        涉及住宅單位數目: None | str | Unset
        if isinstance(self.涉及住宅單位數目, Unset):
            涉及住宅單位數目 = UNSET
        else:
            涉及住宅單位數目 = self.涉及住宅單位數目

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
        if year_of_issuance_of_certificate_of_compliance is not UNSET:
            field_dict["Year_of_Issuance_of_Certificate_of_Compliance"] = (
                year_of_issuance_of_certificate_of_compliance
            )
        if 合約完成證明書簽發年度 is not UNSET:
            field_dict["合約完成證明書簽發年度"] = 合約完成證明書簽發年度
        if date_of_certificate_of_compliance is not UNSET:
            field_dict["Date_of_Certificate_of_Compliance"] = (
                date_of_certificate_of_compliance
            )
        if 合約完成證明書日期 is not UNSET:
            field_dict["合約完成證明書日期"] = 合約完成證明書日期
        if no_of_residential_units_involved is not UNSET:
            field_dict["No._of_Residential_Units_Involved"] = (
                no_of_residential_units_involved
            )
        if 涉及住宅單位數目 is not UNSET:
            field_dict["涉及住宅單位數目"] = 涉及住宅單位數目
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

        def _parse_year_of_issuance_of_certificate_of_compliance(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year_of_issuance_of_certificate_of_compliance = (
            _parse_year_of_issuance_of_certificate_of_compliance(
                d.pop("Year_of_Issuance_of_Certificate_of_Compliance", UNSET)
            )
        )

        def _parse_合約完成證明書簽發年度(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        合約完成證明書簽發年度 = _parse_合約完成證明書簽發年度(
            d.pop("合約完成證明書簽發年度", UNSET)
        )

        def _parse_date_of_certificate_of_compliance(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_of_certificate_of_compliance = _parse_date_of_certificate_of_compliance(
            d.pop("Date_of_Certificate_of_Compliance", UNSET)
        )

        def _parse_合約完成證明書日期(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        合約完成證明書日期 = _parse_合約完成證明書日期(
            d.pop("合約完成證明書日期", UNSET)
        )

        def _parse_no_of_residential_units_involved(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_residential_units_involved = _parse_no_of_residential_units_involved(
            d.pop("No._of_Residential_Units_Involved", UNSET)
        )

        def _parse_涉及住宅單位數目(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        涉及住宅單位數目 = _parse_涉及住宅單位數目(d.pop("涉及住宅單位數目", UNSET))

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

        wfs_map_server_wfs_laocc_attributes = cls(
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
            year_of_issuance_of_certificate_of_compliance=year_of_issuance_of_certificate_of_compliance,
            合約完成證明書簽發年度=合約完成證明書簽發年度,
            date_of_certificate_of_compliance=date_of_certificate_of_compliance,
            合約完成證明書日期=合約完成證明書日期,
            no_of_residential_units_involved=no_of_residential_units_involved,
            涉及住宅單位數目=涉及住宅單位數目,
            northing_坐標北=northing_坐標北,
            easting_坐標東=easting_坐標東,
            latitude_緯度=latitude_緯度,
            longitude_經度=longitude_經度,
            last_updated_date_最後更新日期=last_updated_date_最後更新日期,
        )

        wfs_map_server_wfs_laocc_attributes.additional_properties = d
        return wfs_map_server_wfs_laocc_attributes

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
