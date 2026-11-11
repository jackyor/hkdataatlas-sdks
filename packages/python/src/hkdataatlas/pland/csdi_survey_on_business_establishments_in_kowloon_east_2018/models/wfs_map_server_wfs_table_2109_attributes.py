from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTable2109Attributes")


@_attrs_define
class WfsMapServerWfsTable2109Attributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        area_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        industrial_building (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        office_building (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        industrial_office_building (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shop (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        residential_building (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        uncertain (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
    """

    objectid: int | Unset = UNSET
    area_en: None | str | Unset = UNSET
    industrial_building: int | None | Unset = UNSET
    office_building: int | None | Unset = UNSET
    industrial_office_building: int | None | Unset = UNSET
    shop: int | None | Unset = UNSET
    residential_building: int | None | Unset = UNSET
    uncertain: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        area_en: None | str | Unset
        if isinstance(self.area_en, Unset):
            area_en = UNSET
        else:
            area_en = self.area_en

        industrial_building: int | None | Unset
        if isinstance(self.industrial_building, Unset):
            industrial_building = UNSET
        else:
            industrial_building = self.industrial_building

        office_building: int | None | Unset
        if isinstance(self.office_building, Unset):
            office_building = UNSET
        else:
            office_building = self.office_building

        industrial_office_building: int | None | Unset
        if isinstance(self.industrial_office_building, Unset):
            industrial_office_building = UNSET
        else:
            industrial_office_building = self.industrial_office_building

        shop: int | None | Unset
        if isinstance(self.shop, Unset):
            shop = UNSET
        else:
            shop = self.shop

        residential_building: int | None | Unset
        if isinstance(self.residential_building, Unset):
            residential_building = UNSET
        else:
            residential_building = self.residential_building

        uncertain: int | None | Unset
        if isinstance(self.uncertain, Unset):
            uncertain = UNSET
        else:
            uncertain = self.uncertain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if area_en is not UNSET:
            field_dict["Area_En"] = area_en
        if industrial_building is not UNSET:
            field_dict["Industrial_building"] = industrial_building
        if office_building is not UNSET:
            field_dict["Office_building"] = office_building
        if industrial_office_building is not UNSET:
            field_dict["Industrial_office_building"] = industrial_office_building
        if shop is not UNSET:
            field_dict["Shop"] = shop
        if residential_building is not UNSET:
            field_dict["Residential_building"] = residential_building
        if uncertain is not UNSET:
            field_dict["Uncertain"] = uncertain

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

        def _parse_industrial_building(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        industrial_building = _parse_industrial_building(
            d.pop("Industrial_building", UNSET)
        )

        def _parse_office_building(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        office_building = _parse_office_building(d.pop("Office_building", UNSET))

        def _parse_industrial_office_building(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        industrial_office_building = _parse_industrial_office_building(
            d.pop("Industrial_office_building", UNSET)
        )

        def _parse_shop(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        shop = _parse_shop(d.pop("Shop", UNSET))

        def _parse_residential_building(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        residential_building = _parse_residential_building(
            d.pop("Residential_building", UNSET)
        )

        def _parse_uncertain(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        uncertain = _parse_uncertain(d.pop("Uncertain", UNSET))

        wfs_map_server_wfs_table_2109_attributes = cls(
            objectid=objectid,
            area_en=area_en,
            industrial_building=industrial_building,
            office_building=office_building,
            industrial_office_building=industrial_office_building,
            shop=shop,
            residential_building=residential_building,
            uncertain=uncertain,
        )

        wfs_map_server_wfs_table_2109_attributes.additional_properties = d
        return wfs_map_server_wfs_table_2109_attributes

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
