from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1001Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1001Attributes:
    """
    Attributes:
        featureid (int | Unset): Publisher field type: esriFieldTypeOID
        street_name_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        street_name_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        meter_nonmeter (None | str | Unset): Publisher field type: esriFieldTypeString
        capacity (int | None | Unset): Publisher field type: esriFieldTypeInteger
        vehicle_type_description_1 (None | str | Unset): Publisher field type: esriFieldTypeString
        vehicle_type_description_2 (None | str | Unset): Publisher field type: esriFieldTypeString
        park_meter_period_desc (None | str | Unset): Publisher field type: esriFieldTypeString
        operative_hour_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        operative_hour_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        irnp_remarks_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        irnp_remarks_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        ot_oper_hr_desc (None | str | Unset): Publisher field type: esriFieldTypeString
        ot_oper_hr_desc_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        ot_irnp_remarks_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        ot_irnp_remarks_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        x_coor (float | None | Unset): Publisher field type: esriFieldTypeDouble
        y_coor (float | None | Unset): Publisher field type: esriFieldTypeDouble
        last_update_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
    """

    featureid: int | Unset = UNSET
    street_name_eng: None | str | Unset = UNSET
    street_name_chi: None | str | Unset = UNSET
    meter_nonmeter: None | str | Unset = UNSET
    capacity: int | None | Unset = UNSET
    vehicle_type_description_1: None | str | Unset = UNSET
    vehicle_type_description_2: None | str | Unset = UNSET
    park_meter_period_desc: None | str | Unset = UNSET
    operative_hour_eng: None | str | Unset = UNSET
    operative_hour_chi: None | str | Unset = UNSET
    irnp_remarks_eng: None | str | Unset = UNSET
    irnp_remarks_chi: None | str | Unset = UNSET
    ot_oper_hr_desc: None | str | Unset = UNSET
    ot_oper_hr_desc_chi: None | str | Unset = UNSET
    ot_irnp_remarks_eng: None | str | Unset = UNSET
    ot_irnp_remarks_chi: None | str | Unset = UNSET
    x_coor: float | None | Unset = UNSET
    y_coor: float | None | Unset = UNSET
    last_update_date: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        featureid = self.featureid

        street_name_eng: None | str | Unset
        if isinstance(self.street_name_eng, Unset):
            street_name_eng = UNSET
        else:
            street_name_eng = self.street_name_eng

        street_name_chi: None | str | Unset
        if isinstance(self.street_name_chi, Unset):
            street_name_chi = UNSET
        else:
            street_name_chi = self.street_name_chi

        meter_nonmeter: None | str | Unset
        if isinstance(self.meter_nonmeter, Unset):
            meter_nonmeter = UNSET
        else:
            meter_nonmeter = self.meter_nonmeter

        capacity: int | None | Unset
        if isinstance(self.capacity, Unset):
            capacity = UNSET
        else:
            capacity = self.capacity

        vehicle_type_description_1: None | str | Unset
        if isinstance(self.vehicle_type_description_1, Unset):
            vehicle_type_description_1 = UNSET
        else:
            vehicle_type_description_1 = self.vehicle_type_description_1

        vehicle_type_description_2: None | str | Unset
        if isinstance(self.vehicle_type_description_2, Unset):
            vehicle_type_description_2 = UNSET
        else:
            vehicle_type_description_2 = self.vehicle_type_description_2

        park_meter_period_desc: None | str | Unset
        if isinstance(self.park_meter_period_desc, Unset):
            park_meter_period_desc = UNSET
        else:
            park_meter_period_desc = self.park_meter_period_desc

        operative_hour_eng: None | str | Unset
        if isinstance(self.operative_hour_eng, Unset):
            operative_hour_eng = UNSET
        else:
            operative_hour_eng = self.operative_hour_eng

        operative_hour_chi: None | str | Unset
        if isinstance(self.operative_hour_chi, Unset):
            operative_hour_chi = UNSET
        else:
            operative_hour_chi = self.operative_hour_chi

        irnp_remarks_eng: None | str | Unset
        if isinstance(self.irnp_remarks_eng, Unset):
            irnp_remarks_eng = UNSET
        else:
            irnp_remarks_eng = self.irnp_remarks_eng

        irnp_remarks_chi: None | str | Unset
        if isinstance(self.irnp_remarks_chi, Unset):
            irnp_remarks_chi = UNSET
        else:
            irnp_remarks_chi = self.irnp_remarks_chi

        ot_oper_hr_desc: None | str | Unset
        if isinstance(self.ot_oper_hr_desc, Unset):
            ot_oper_hr_desc = UNSET
        else:
            ot_oper_hr_desc = self.ot_oper_hr_desc

        ot_oper_hr_desc_chi: None | str | Unset
        if isinstance(self.ot_oper_hr_desc_chi, Unset):
            ot_oper_hr_desc_chi = UNSET
        else:
            ot_oper_hr_desc_chi = self.ot_oper_hr_desc_chi

        ot_irnp_remarks_eng: None | str | Unset
        if isinstance(self.ot_irnp_remarks_eng, Unset):
            ot_irnp_remarks_eng = UNSET
        else:
            ot_irnp_remarks_eng = self.ot_irnp_remarks_eng

        ot_irnp_remarks_chi: None | str | Unset
        if isinstance(self.ot_irnp_remarks_chi, Unset):
            ot_irnp_remarks_chi = UNSET
        else:
            ot_irnp_remarks_chi = self.ot_irnp_remarks_chi

        x_coor: float | None | Unset
        if isinstance(self.x_coor, Unset):
            x_coor = UNSET
        else:
            x_coor = self.x_coor

        y_coor: float | None | Unset
        if isinstance(self.y_coor, Unset):
            y_coor = UNSET
        else:
            y_coor = self.y_coor

        last_update_date = self.last_update_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if featureid is not UNSET:
            field_dict["FEATUREID"] = featureid
        if street_name_eng is not UNSET:
            field_dict["STREET_NAME_ENG"] = street_name_eng
        if street_name_chi is not UNSET:
            field_dict["STREET_NAME_CHI"] = street_name_chi
        if meter_nonmeter is not UNSET:
            field_dict["METER_NONMETER"] = meter_nonmeter
        if capacity is not UNSET:
            field_dict["CAPACITY"] = capacity
        if vehicle_type_description_1 is not UNSET:
            field_dict["VEHICLE_TYPE_DESCRIPTION_1"] = vehicle_type_description_1
        if vehicle_type_description_2 is not UNSET:
            field_dict["VEHICLE_TYPE_DESCRIPTION_2"] = vehicle_type_description_2
        if park_meter_period_desc is not UNSET:
            field_dict["PARK_METER_PERIOD_DESC"] = park_meter_period_desc
        if operative_hour_eng is not UNSET:
            field_dict["OPERATIVE_HOUR_ENG"] = operative_hour_eng
        if operative_hour_chi is not UNSET:
            field_dict["OPERATIVE_HOUR_CHI"] = operative_hour_chi
        if irnp_remarks_eng is not UNSET:
            field_dict["IRNP_REMARKS_ENG"] = irnp_remarks_eng
        if irnp_remarks_chi is not UNSET:
            field_dict["IRNP_REMARKS_CHI"] = irnp_remarks_chi
        if ot_oper_hr_desc is not UNSET:
            field_dict["OT_OPER_HR_DESC"] = ot_oper_hr_desc
        if ot_oper_hr_desc_chi is not UNSET:
            field_dict["OT_OPER_HR_DESC_CHI"] = ot_oper_hr_desc_chi
        if ot_irnp_remarks_eng is not UNSET:
            field_dict["OT_IRNP_REMARKS_ENG"] = ot_irnp_remarks_eng
        if ot_irnp_remarks_chi is not UNSET:
            field_dict["OT_IRNP_REMARKS_CHI"] = ot_irnp_remarks_chi
        if x_coor is not UNSET:
            field_dict["X_COOR"] = x_coor
        if y_coor is not UNSET:
            field_dict["Y_COOR"] = y_coor
        if last_update_date is not UNSET:
            field_dict["LAST_UPDATE_DATE"] = last_update_date

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        featureid = d.pop("FEATUREID", UNSET)

        def _parse_street_name_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_name_eng = _parse_street_name_eng(d.pop("STREET_NAME_ENG", UNSET))

        def _parse_street_name_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_name_chi = _parse_street_name_chi(d.pop("STREET_NAME_CHI", UNSET))

        def _parse_meter_nonmeter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        meter_nonmeter = _parse_meter_nonmeter(d.pop("METER_NONMETER", UNSET))

        def _parse_capacity(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        capacity = _parse_capacity(d.pop("CAPACITY", UNSET))

        def _parse_vehicle_type_description_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vehicle_type_description_1 = _parse_vehicle_type_description_1(
            d.pop("VEHICLE_TYPE_DESCRIPTION_1", UNSET)
        )

        def _parse_vehicle_type_description_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vehicle_type_description_2 = _parse_vehicle_type_description_2(
            d.pop("VEHICLE_TYPE_DESCRIPTION_2", UNSET)
        )

        def _parse_park_meter_period_desc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        park_meter_period_desc = _parse_park_meter_period_desc(
            d.pop("PARK_METER_PERIOD_DESC", UNSET)
        )

        def _parse_operative_hour_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operative_hour_eng = _parse_operative_hour_eng(
            d.pop("OPERATIVE_HOUR_ENG", UNSET)
        )

        def _parse_operative_hour_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operative_hour_chi = _parse_operative_hour_chi(
            d.pop("OPERATIVE_HOUR_CHI", UNSET)
        )

        def _parse_irnp_remarks_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        irnp_remarks_eng = _parse_irnp_remarks_eng(d.pop("IRNP_REMARKS_ENG", UNSET))

        def _parse_irnp_remarks_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        irnp_remarks_chi = _parse_irnp_remarks_chi(d.pop("IRNP_REMARKS_CHI", UNSET))

        def _parse_ot_oper_hr_desc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ot_oper_hr_desc = _parse_ot_oper_hr_desc(d.pop("OT_OPER_HR_DESC", UNSET))

        def _parse_ot_oper_hr_desc_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ot_oper_hr_desc_chi = _parse_ot_oper_hr_desc_chi(
            d.pop("OT_OPER_HR_DESC_CHI", UNSET)
        )

        def _parse_ot_irnp_remarks_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ot_irnp_remarks_eng = _parse_ot_irnp_remarks_eng(
            d.pop("OT_IRNP_REMARKS_ENG", UNSET)
        )

        def _parse_ot_irnp_remarks_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ot_irnp_remarks_chi = _parse_ot_irnp_remarks_chi(
            d.pop("OT_IRNP_REMARKS_CHI", UNSET)
        )

        def _parse_x_coor(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        x_coor = _parse_x_coor(d.pop("X_COOR", UNSET))

        def _parse_y_coor(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        y_coor = _parse_y_coor(d.pop("Y_COOR", UNSET))

        last_update_date = d.pop("LAST_UPDATE_DATE", UNSET)

        arcgis_feature_server_arcgis_layer_1001_attributes = cls(
            featureid=featureid,
            street_name_eng=street_name_eng,
            street_name_chi=street_name_chi,
            meter_nonmeter=meter_nonmeter,
            capacity=capacity,
            vehicle_type_description_1=vehicle_type_description_1,
            vehicle_type_description_2=vehicle_type_description_2,
            park_meter_period_desc=park_meter_period_desc,
            operative_hour_eng=operative_hour_eng,
            operative_hour_chi=operative_hour_chi,
            irnp_remarks_eng=irnp_remarks_eng,
            irnp_remarks_chi=irnp_remarks_chi,
            ot_oper_hr_desc=ot_oper_hr_desc,
            ot_oper_hr_desc_chi=ot_oper_hr_desc_chi,
            ot_irnp_remarks_eng=ot_irnp_remarks_eng,
            ot_irnp_remarks_chi=ot_irnp_remarks_chi,
            x_coor=x_coor,
            y_coor=y_coor,
            last_update_date=last_update_date,
        )

        arcgis_feature_server_arcgis_layer_1001_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1001_attributes

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
