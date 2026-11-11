from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTable211Attributes")


@_attrs_define
class WfsMapServerWfsTable211Attributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        area_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        industrial_building_sq_m (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        industrial_building_sq_ft (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        industrial_office_building_sq_m (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        industrial_office_building_sq_ft (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        office_building_total_sq_m (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        office_building_total_sq_ft (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from
            XML occurrence into all JSON queries.
        office_building_a_sq_m (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        office_building_a_sq_ft (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        office_building_b_c_sq_m (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        office_building_b_c_sq_ft (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        new_wholesale_conversion_building_sq_m (int | None | Unset): Native XSD type xsd:int. Requiredness is not
            projected from XML occurrence into all JSON queries.
        new_wholesale_conversion_building_sq_ft (int | None | Unset): Native XSD type xsd:int. Requiredness is not
            projected from XML occurrence into all JSON queries.
    """

    objectid: int | Unset = UNSET
    area_en: None | str | Unset = UNSET
    industrial_building_sq_m: int | None | Unset = UNSET
    industrial_building_sq_ft: int | None | Unset = UNSET
    industrial_office_building_sq_m: int | None | Unset = UNSET
    industrial_office_building_sq_ft: int | None | Unset = UNSET
    office_building_total_sq_m: int | None | Unset = UNSET
    office_building_total_sq_ft: int | None | Unset = UNSET
    office_building_a_sq_m: int | None | Unset = UNSET
    office_building_a_sq_ft: int | None | Unset = UNSET
    office_building_b_c_sq_m: None | str | Unset = UNSET
    office_building_b_c_sq_ft: None | str | Unset = UNSET
    new_wholesale_conversion_building_sq_m: int | None | Unset = UNSET
    new_wholesale_conversion_building_sq_ft: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        area_en: None | str | Unset
        if isinstance(self.area_en, Unset):
            area_en = UNSET
        else:
            area_en = self.area_en

        industrial_building_sq_m: int | None | Unset
        if isinstance(self.industrial_building_sq_m, Unset):
            industrial_building_sq_m = UNSET
        else:
            industrial_building_sq_m = self.industrial_building_sq_m

        industrial_building_sq_ft: int | None | Unset
        if isinstance(self.industrial_building_sq_ft, Unset):
            industrial_building_sq_ft = UNSET
        else:
            industrial_building_sq_ft = self.industrial_building_sq_ft

        industrial_office_building_sq_m: int | None | Unset
        if isinstance(self.industrial_office_building_sq_m, Unset):
            industrial_office_building_sq_m = UNSET
        else:
            industrial_office_building_sq_m = self.industrial_office_building_sq_m

        industrial_office_building_sq_ft: int | None | Unset
        if isinstance(self.industrial_office_building_sq_ft, Unset):
            industrial_office_building_sq_ft = UNSET
        else:
            industrial_office_building_sq_ft = self.industrial_office_building_sq_ft

        office_building_total_sq_m: int | None | Unset
        if isinstance(self.office_building_total_sq_m, Unset):
            office_building_total_sq_m = UNSET
        else:
            office_building_total_sq_m = self.office_building_total_sq_m

        office_building_total_sq_ft: int | None | Unset
        if isinstance(self.office_building_total_sq_ft, Unset):
            office_building_total_sq_ft = UNSET
        else:
            office_building_total_sq_ft = self.office_building_total_sq_ft

        office_building_a_sq_m: int | None | Unset
        if isinstance(self.office_building_a_sq_m, Unset):
            office_building_a_sq_m = UNSET
        else:
            office_building_a_sq_m = self.office_building_a_sq_m

        office_building_a_sq_ft: int | None | Unset
        if isinstance(self.office_building_a_sq_ft, Unset):
            office_building_a_sq_ft = UNSET
        else:
            office_building_a_sq_ft = self.office_building_a_sq_ft

        office_building_b_c_sq_m: None | str | Unset
        if isinstance(self.office_building_b_c_sq_m, Unset):
            office_building_b_c_sq_m = UNSET
        else:
            office_building_b_c_sq_m = self.office_building_b_c_sq_m

        office_building_b_c_sq_ft: None | str | Unset
        if isinstance(self.office_building_b_c_sq_ft, Unset):
            office_building_b_c_sq_ft = UNSET
        else:
            office_building_b_c_sq_ft = self.office_building_b_c_sq_ft

        new_wholesale_conversion_building_sq_m: int | None | Unset
        if isinstance(self.new_wholesale_conversion_building_sq_m, Unset):
            new_wholesale_conversion_building_sq_m = UNSET
        else:
            new_wholesale_conversion_building_sq_m = (
                self.new_wholesale_conversion_building_sq_m
            )

        new_wholesale_conversion_building_sq_ft: int | None | Unset
        if isinstance(self.new_wholesale_conversion_building_sq_ft, Unset):
            new_wholesale_conversion_building_sq_ft = UNSET
        else:
            new_wholesale_conversion_building_sq_ft = (
                self.new_wholesale_conversion_building_sq_ft
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if area_en is not UNSET:
            field_dict["Area_En"] = area_en
        if industrial_building_sq_m is not UNSET:
            field_dict["Industrial_building_sq_m"] = industrial_building_sq_m
        if industrial_building_sq_ft is not UNSET:
            field_dict["Industrial_building_sq_ft"] = industrial_building_sq_ft
        if industrial_office_building_sq_m is not UNSET:
            field_dict["Industrial_office_building_sq_m"] = (
                industrial_office_building_sq_m
            )
        if industrial_office_building_sq_ft is not UNSET:
            field_dict["Industrial_office_building_sq_ft"] = (
                industrial_office_building_sq_ft
            )
        if office_building_total_sq_m is not UNSET:
            field_dict["Office_building_Total_sq_m"] = office_building_total_sq_m
        if office_building_total_sq_ft is not UNSET:
            field_dict["Office_building_Total_sq_ft"] = office_building_total_sq_ft
        if office_building_a_sq_m is not UNSET:
            field_dict["Office_building_A_sq_m"] = office_building_a_sq_m
        if office_building_a_sq_ft is not UNSET:
            field_dict["Office_building_A_sq_ft"] = office_building_a_sq_ft
        if office_building_b_c_sq_m is not UNSET:
            field_dict["Office_building_B_C_sq_m"] = office_building_b_c_sq_m
        if office_building_b_c_sq_ft is not UNSET:
            field_dict["Office_building_B_C_sq_ft"] = office_building_b_c_sq_ft
        if new_wholesale_conversion_building_sq_m is not UNSET:
            field_dict["New_wholesale_conversion_building_sq_m"] = (
                new_wholesale_conversion_building_sq_m
            )
        if new_wholesale_conversion_building_sq_ft is not UNSET:
            field_dict["New_wholesale_conversion_building_sq_ft"] = (
                new_wholesale_conversion_building_sq_ft
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_area_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_en = _parse_area_en(d.pop("Area_En", UNSET))

        def _parse_industrial_building_sq_m(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        industrial_building_sq_m = _parse_industrial_building_sq_m(
            d.pop("Industrial_building_sq_m", UNSET)
        )

        def _parse_industrial_building_sq_ft(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        industrial_building_sq_ft = _parse_industrial_building_sq_ft(
            d.pop("Industrial_building_sq_ft", UNSET)
        )

        def _parse_industrial_office_building_sq_m(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        industrial_office_building_sq_m = _parse_industrial_office_building_sq_m(
            d.pop("Industrial_office_building_sq_m", UNSET)
        )

        def _parse_industrial_office_building_sq_ft(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        industrial_office_building_sq_ft = _parse_industrial_office_building_sq_ft(
            d.pop("Industrial_office_building_sq_ft", UNSET)
        )

        def _parse_office_building_total_sq_m(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        office_building_total_sq_m = _parse_office_building_total_sq_m(
            d.pop("Office_building_Total_sq_m", UNSET)
        )

        def _parse_office_building_total_sq_ft(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        office_building_total_sq_ft = _parse_office_building_total_sq_ft(
            d.pop("Office_building_Total_sq_ft", UNSET)
        )

        def _parse_office_building_a_sq_m(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        office_building_a_sq_m = _parse_office_building_a_sq_m(
            d.pop("Office_building_A_sq_m", UNSET)
        )

        def _parse_office_building_a_sq_ft(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        office_building_a_sq_ft = _parse_office_building_a_sq_ft(
            d.pop("Office_building_A_sq_ft", UNSET)
        )

        def _parse_office_building_b_c_sq_m(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_building_b_c_sq_m = _parse_office_building_b_c_sq_m(
            d.pop("Office_building_B_C_sq_m", UNSET)
        )

        def _parse_office_building_b_c_sq_ft(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_building_b_c_sq_ft = _parse_office_building_b_c_sq_ft(
            d.pop("Office_building_B_C_sq_ft", UNSET)
        )

        def _parse_new_wholesale_conversion_building_sq_m(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        new_wholesale_conversion_building_sq_m = (
            _parse_new_wholesale_conversion_building_sq_m(
                d.pop("New_wholesale_conversion_building_sq_m", UNSET)
            )
        )

        def _parse_new_wholesale_conversion_building_sq_ft(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        new_wholesale_conversion_building_sq_ft = (
            _parse_new_wholesale_conversion_building_sq_ft(
                d.pop("New_wholesale_conversion_building_sq_ft", UNSET)
            )
        )

        wfs_map_server_wfs_table_211_attributes = cls(
            objectid=objectid,
            area_en=area_en,
            industrial_building_sq_m=industrial_building_sq_m,
            industrial_building_sq_ft=industrial_building_sq_ft,
            industrial_office_building_sq_m=industrial_office_building_sq_m,
            industrial_office_building_sq_ft=industrial_office_building_sq_ft,
            office_building_total_sq_m=office_building_total_sq_m,
            office_building_total_sq_ft=office_building_total_sq_ft,
            office_building_a_sq_m=office_building_a_sq_m,
            office_building_a_sq_ft=office_building_a_sq_ft,
            office_building_b_c_sq_m=office_building_b_c_sq_m,
            office_building_b_c_sq_ft=office_building_b_c_sq_ft,
            new_wholesale_conversion_building_sq_m=new_wholesale_conversion_building_sq_m,
            new_wholesale_conversion_building_sq_ft=new_wholesale_conversion_building_sq_ft,
        )

        wfs_map_server_wfs_table_211_attributes.additional_properties = d
        return wfs_map_server_wfs_table_211_attributes

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
