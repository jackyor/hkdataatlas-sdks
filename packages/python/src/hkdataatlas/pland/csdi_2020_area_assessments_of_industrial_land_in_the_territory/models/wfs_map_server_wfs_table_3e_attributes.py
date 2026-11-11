from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTable3EAttributes")


@_attrs_define
class WfsMapServerWfsTable3EAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        aa_code (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        aa_title (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        shop_and_services (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        data_centre (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        showroom (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        research_centre (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        eating_place (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        miscellaneous (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    objectid: int | Unset = UNSET
    aa_code: None | str | Unset = UNSET
    aa_title: None | str | Unset = UNSET
    shop_and_services: float | None | Unset = UNSET
    data_centre: float | None | Unset = UNSET
    showroom: float | None | Unset = UNSET
    research_centre: float | None | Unset = UNSET
    eating_place: float | None | Unset = UNSET
    miscellaneous: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        aa_code: None | str | Unset
        if isinstance(self.aa_code, Unset):
            aa_code = UNSET
        else:
            aa_code = self.aa_code

        aa_title: None | str | Unset
        if isinstance(self.aa_title, Unset):
            aa_title = UNSET
        else:
            aa_title = self.aa_title

        shop_and_services: float | None | Unset
        if isinstance(self.shop_and_services, Unset):
            shop_and_services = UNSET
        else:
            shop_and_services = self.shop_and_services

        data_centre: float | None | Unset
        if isinstance(self.data_centre, Unset):
            data_centre = UNSET
        else:
            data_centre = self.data_centre

        showroom: float | None | Unset
        if isinstance(self.showroom, Unset):
            showroom = UNSET
        else:
            showroom = self.showroom

        research_centre: float | None | Unset
        if isinstance(self.research_centre, Unset):
            research_centre = UNSET
        else:
            research_centre = self.research_centre

        eating_place: float | None | Unset
        if isinstance(self.eating_place, Unset):
            eating_place = UNSET
        else:
            eating_place = self.eating_place

        miscellaneous: float | None | Unset
        if isinstance(self.miscellaneous, Unset):
            miscellaneous = UNSET
        else:
            miscellaneous = self.miscellaneous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if aa_code is not UNSET:
            field_dict["AA_Code"] = aa_code
        if aa_title is not UNSET:
            field_dict["AA_Title"] = aa_title
        if shop_and_services is not UNSET:
            field_dict["Shop_and_services"] = shop_and_services
        if data_centre is not UNSET:
            field_dict["Data_centre"] = data_centre
        if showroom is not UNSET:
            field_dict["Showroom"] = showroom
        if research_centre is not UNSET:
            field_dict["Research_centre"] = research_centre
        if eating_place is not UNSET:
            field_dict["Eating_place"] = eating_place
        if miscellaneous is not UNSET:
            field_dict["Miscellaneous"] = miscellaneous

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_aa_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aa_code = _parse_aa_code(d.pop("AA_Code", UNSET))

        def _parse_aa_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aa_title = _parse_aa_title(d.pop("AA_Title", UNSET))

        def _parse_shop_and_services(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shop_and_services = _parse_shop_and_services(d.pop("Shop_and_services", UNSET))

        def _parse_data_centre(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        data_centre = _parse_data_centre(d.pop("Data_centre", UNSET))

        def _parse_showroom(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        showroom = _parse_showroom(d.pop("Showroom", UNSET))

        def _parse_research_centre(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        research_centre = _parse_research_centre(d.pop("Research_centre", UNSET))

        def _parse_eating_place(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        eating_place = _parse_eating_place(d.pop("Eating_place", UNSET))

        def _parse_miscellaneous(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        miscellaneous = _parse_miscellaneous(d.pop("Miscellaneous", UNSET))

        wfs_map_server_wfs_table_3e_attributes = cls(
            objectid=objectid,
            aa_code=aa_code,
            aa_title=aa_title,
            shop_and_services=shop_and_services,
            data_centre=data_centre,
            showroom=showroom,
            research_centre=research_centre,
            eating_place=eating_place,
            miscellaneous=miscellaneous,
        )

        wfs_map_server_wfs_table_3e_attributes.additional_properties = d
        return wfs_map_server_wfs_table_3e_attributes

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
