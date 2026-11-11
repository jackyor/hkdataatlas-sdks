from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTable216Attributes")


@_attrs_define
class WfsMapServerWfsTable216Attributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        area_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        person_1_4 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        person_5_9 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        person_10_19 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        person_20_49 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        person_50_99 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        person_100 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        information_cannot_be_provided (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    objectid: int | Unset = UNSET
    area_en: None | str | Unset = UNSET
    person_1_4: int | None | Unset = UNSET
    person_5_9: int | None | Unset = UNSET
    person_10_19: int | None | Unset = UNSET
    person_20_49: int | None | Unset = UNSET
    person_50_99: int | None | Unset = UNSET
    person_100: int | None | Unset = UNSET
    information_cannot_be_provided: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        area_en: None | str | Unset
        if isinstance(self.area_en, Unset):
            area_en = UNSET
        else:
            area_en = self.area_en

        person_1_4: int | None | Unset
        if isinstance(self.person_1_4, Unset):
            person_1_4 = UNSET
        else:
            person_1_4 = self.person_1_4

        person_5_9: int | None | Unset
        if isinstance(self.person_5_9, Unset):
            person_5_9 = UNSET
        else:
            person_5_9 = self.person_5_9

        person_10_19: int | None | Unset
        if isinstance(self.person_10_19, Unset):
            person_10_19 = UNSET
        else:
            person_10_19 = self.person_10_19

        person_20_49: int | None | Unset
        if isinstance(self.person_20_49, Unset):
            person_20_49 = UNSET
        else:
            person_20_49 = self.person_20_49

        person_50_99: int | None | Unset
        if isinstance(self.person_50_99, Unset):
            person_50_99 = UNSET
        else:
            person_50_99 = self.person_50_99

        person_100: int | None | Unset
        if isinstance(self.person_100, Unset):
            person_100 = UNSET
        else:
            person_100 = self.person_100

        information_cannot_be_provided: None | str | Unset
        if isinstance(self.information_cannot_be_provided, Unset):
            information_cannot_be_provided = UNSET
        else:
            information_cannot_be_provided = self.information_cannot_be_provided

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if area_en is not UNSET:
            field_dict["Area_En"] = area_en
        if person_1_4 is not UNSET:
            field_dict["Person_1_4"] = person_1_4
        if person_5_9 is not UNSET:
            field_dict["Person_5_9"] = person_5_9
        if person_10_19 is not UNSET:
            field_dict["Person_10_19"] = person_10_19
        if person_20_49 is not UNSET:
            field_dict["Person_20_49"] = person_20_49
        if person_50_99 is not UNSET:
            field_dict["Person_50_99"] = person_50_99
        if person_100 is not UNSET:
            field_dict["Person_100"] = person_100
        if information_cannot_be_provided is not UNSET:
            field_dict["Information_cannot_be_provided"] = (
                information_cannot_be_provided
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

        def _parse_person_1_4(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        person_1_4 = _parse_person_1_4(d.pop("Person_1_4", UNSET))

        def _parse_person_5_9(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        person_5_9 = _parse_person_5_9(d.pop("Person_5_9", UNSET))

        def _parse_person_10_19(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        person_10_19 = _parse_person_10_19(d.pop("Person_10_19", UNSET))

        def _parse_person_20_49(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        person_20_49 = _parse_person_20_49(d.pop("Person_20_49", UNSET))

        def _parse_person_50_99(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        person_50_99 = _parse_person_50_99(d.pop("Person_50_99", UNSET))

        def _parse_person_100(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        person_100 = _parse_person_100(d.pop("Person_100", UNSET))

        def _parse_information_cannot_be_provided(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        information_cannot_be_provided = _parse_information_cannot_be_provided(
            d.pop("Information_cannot_be_provided", UNSET)
        )

        wfs_map_server_wfs_table_216_attributes = cls(
            objectid=objectid,
            area_en=area_en,
            person_1_4=person_1_4,
            person_5_9=person_5_9,
            person_10_19=person_10_19,
            person_20_49=person_20_49,
            person_50_99=person_50_99,
            person_100=person_100,
            information_cannot_be_provided=information_cannot_be_provided,
        )

        wfs_map_server_wfs_table_216_attributes.additional_properties = d
        return wfs_map_server_wfs_table_216_attributes

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
