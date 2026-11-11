from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Transaction")


@_attrs_define
class Transaction:
    """Sale transaction record. The English data dictionary describes these fields; their wire-property names are taken
    from the documented response example. Numeric fields are declared Numeric in the dictionary but represented as
    strings in that example, so both forms are permitted.

        Attributes:
            asp_sign_date (str | Unset): Date of Agreement for Sale and Purchase (ASP), documented in dd/mm/yyyy form.
            block_name (str | Unset): Block name of the purchased flat.
            court_name (str | Unset): Court name of the purchased flat.
            flat_num (str | Unset): Flat number of the purchased flat.
            floor_num (str | Unset): Floor number of the purchased flat.
            sale_price (float | str | Unset): Sale price of the purchased flat. The data dictionary declares Numeric with
                stated form 999999999999999.99, while the response example represents this value as a string; both
                representations are allowed.
            saleable_area (float | str | Unset): Saleable area of the purchased flat in square meters. The data dictionary
                declares Numeric with stated form 9999999.999, while the response example represents this value as a string;
                both representations are allowed.
            scheme_name (str | Unset): Subsidised home ownership scheme name.
            scheme_type (str | Unset): Subsidised home ownership scheme type. The documented possible value is HOS.
    """

    asp_sign_date: str | Unset = UNSET
    block_name: str | Unset = UNSET
    court_name: str | Unset = UNSET
    flat_num: str | Unset = UNSET
    floor_num: str | Unset = UNSET
    sale_price: float | str | Unset = UNSET
    saleable_area: float | str | Unset = UNSET
    scheme_name: str | Unset = UNSET
    scheme_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asp_sign_date = self.asp_sign_date

        block_name = self.block_name

        court_name = self.court_name

        flat_num = self.flat_num

        floor_num = self.floor_num

        sale_price: float | str | Unset
        if isinstance(self.sale_price, Unset):
            sale_price = UNSET
        else:
            sale_price = self.sale_price

        saleable_area: float | str | Unset
        if isinstance(self.saleable_area, Unset):
            saleable_area = UNSET
        else:
            saleable_area = self.saleable_area

        scheme_name = self.scheme_name

        scheme_type = self.scheme_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asp_sign_date is not UNSET:
            field_dict["asp_sign_date"] = asp_sign_date
        if block_name is not UNSET:
            field_dict["block_name"] = block_name
        if court_name is not UNSET:
            field_dict["court_name"] = court_name
        if flat_num is not UNSET:
            field_dict["flat_num"] = flat_num
        if floor_num is not UNSET:
            field_dict["floor_num"] = floor_num
        if sale_price is not UNSET:
            field_dict["sale_price"] = sale_price
        if saleable_area is not UNSET:
            field_dict["saleable_area"] = saleable_area
        if scheme_name is not UNSET:
            field_dict["scheme_name"] = scheme_name
        if scheme_type is not UNSET:
            field_dict["scheme_type"] = scheme_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        asp_sign_date = d.pop("asp_sign_date", UNSET)

        block_name = d.pop("block_name", UNSET)

        court_name = d.pop("court_name", UNSET)

        flat_num = d.pop("flat_num", UNSET)

        floor_num = d.pop("floor_num", UNSET)

        def _parse_sale_price(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        sale_price = _parse_sale_price(d.pop("sale_price", UNSET))

        def _parse_saleable_area(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        saleable_area = _parse_saleable_area(d.pop("saleable_area", UNSET))

        scheme_name = d.pop("scheme_name", UNSET)

        scheme_type = d.pop("scheme_type", UNSET)

        transaction = cls(
            asp_sign_date=asp_sign_date,
            block_name=block_name,
            court_name=court_name,
            flat_num=flat_num,
            floor_num=floor_num,
            sale_price=sale_price,
            saleable_area=saleable_area,
            scheme_name=scheme_name,
            scheme_type=scheme_type,
        )

        transaction.additional_properties = d
        return transaction

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
