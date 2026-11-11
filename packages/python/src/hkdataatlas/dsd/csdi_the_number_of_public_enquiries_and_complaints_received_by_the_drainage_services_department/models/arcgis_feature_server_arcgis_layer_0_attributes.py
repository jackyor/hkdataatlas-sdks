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
        period_of_time (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
        no_public_enquiries_requestfor_services (None | str | Unset): Publisher field type: esriFieldTypeString
        no_public_complaints (None | str | Unset): Publisher field type: esriFieldTypeString
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    period_of_time: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    no_public_enquiries_requestfor_services: None | str | Unset = UNSET
    no_public_complaints: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period_of_time: None | str | Unset
        if isinstance(self.period_of_time, Unset):
            period_of_time = UNSET
        else:
            period_of_time = self.period_of_time

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        shape_area: float | None | Unset
        if isinstance(self.shape_area, Unset):
            shape_area = UNSET
        else:
            shape_area = self.shape_area

        no_public_enquiries_requestfor_services: None | str | Unset
        if isinstance(self.no_public_enquiries_requestfor_services, Unset):
            no_public_enquiries_requestfor_services = UNSET
        else:
            no_public_enquiries_requestfor_services = (
                self.no_public_enquiries_requestfor_services
            )

        no_public_complaints: None | str | Unset
        if isinstance(self.no_public_complaints, Unset):
            no_public_complaints = UNSET
        else:
            no_public_complaints = self.no_public_complaints

        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period_of_time is not UNSET:
            field_dict["Period_of_time"] = period_of_time
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area
        if no_public_enquiries_requestfor_services is not UNSET:
            field_dict["No_Public_Enquiries_RequestforServices"] = (
                no_public_enquiries_requestfor_services
            )
        if no_public_complaints is not UNSET:
            field_dict["No_Public_Complaints"] = no_public_complaints
        if district_en is not UNSET:
            field_dict["District_EN"] = district_en
        if district_tc is not UNSET:
            field_dict["District_TC"] = district_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_period_of_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        period_of_time = _parse_period_of_time(d.pop("Period_of_time", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape__Area", UNSET))

        def _parse_no_public_enquiries_requestfor_services(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_public_enquiries_requestfor_services = (
            _parse_no_public_enquiries_requestfor_services(
                d.pop("No_Public_Enquiries_RequestforServices", UNSET)
            )
        )

        def _parse_no_public_complaints(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_public_complaints = _parse_no_public_complaints(
            d.pop("No_Public_Complaints", UNSET)
        )

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("District_EN", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("District_TC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            period_of_time=period_of_time,
            shape_length=shape_length,
            shape_area=shape_area,
            no_public_enquiries_requestfor_services=no_public_enquiries_requestfor_services,
            no_public_complaints=no_public_complaints,
            district_en=district_en,
            district_tc=district_tc,
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
