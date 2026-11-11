from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTable227Attributes")


@_attrs_define
class WfsMapServerWfsTable227Attributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        area_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        own (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        rent (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        rent_free (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
    """

    objectid: int | Unset = UNSET
    area_en: None | str | Unset = UNSET
    own: int | None | Unset = UNSET
    rent: int | None | Unset = UNSET
    rent_free: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        area_en: None | str | Unset
        if isinstance(self.area_en, Unset):
            area_en = UNSET
        else:
            area_en = self.area_en

        own: int | None | Unset
        if isinstance(self.own, Unset):
            own = UNSET
        else:
            own = self.own

        rent: int | None | Unset
        if isinstance(self.rent, Unset):
            rent = UNSET
        else:
            rent = self.rent

        rent_free: int | None | Unset
        if isinstance(self.rent_free, Unset):
            rent_free = UNSET
        else:
            rent_free = self.rent_free

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if area_en is not UNSET:
            field_dict["Area_En"] = area_en
        if own is not UNSET:
            field_dict["Own"] = own
        if rent is not UNSET:
            field_dict["Rent"] = rent
        if rent_free is not UNSET:
            field_dict["Rent_free"] = rent_free

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

        def _parse_own(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        own = _parse_own(d.pop("Own", UNSET))

        def _parse_rent(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rent = _parse_rent(d.pop("Rent", UNSET))

        def _parse_rent_free(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rent_free = _parse_rent_free(d.pop("Rent_free", UNSET))

        wfs_map_server_wfs_table_227_attributes = cls(
            objectid=objectid,
            area_en=area_en,
            own=own,
            rent=rent,
            rent_free=rent_free,
        )

        wfs_map_server_wfs_table_227_attributes.additional_properties = d
        return wfs_map_server_wfs_table_227_attributes

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
