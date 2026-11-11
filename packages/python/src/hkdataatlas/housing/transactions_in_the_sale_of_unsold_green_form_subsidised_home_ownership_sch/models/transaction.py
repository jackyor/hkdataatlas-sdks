from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Transaction")


@_attrs_define
class Transaction:
    """A transaction record. The data dictionary describes the fields below; its human-readable labels do not explicitly
    map every label to a JSON wire property. Wire names shown here are those present in the documented JSON example. The
    dictionary declares area and price as numeric, while the JSON example represents them as strings; both
    representations are allowed.

        Attributes:
            asp_sign_date (str | Unset): Date of Agreement for Sale and Purchase (ASP). The dictionary gives the format as
                dd-mm-yyyy; the documented JSON example uses 25/07/2022.
            block_name (str | Unset): Block name of the purchased flat.
            court_estate_name (str | Unset): Court or estate name of the purchased flat.
            flat_num (str | Unset): Flat number of the purchased flat.
            floor_num (str | Unset): Floor number of the purchased flat.
            sale_price (float | str | Unset): Sale price of the purchased flat. The dictionary declares a numeric value with
                pattern precision notation 999999999999999.99, while the documented JSON example represents it as a string;
                either numeric or string representation is permitted.
            saleable_area (float | str | Unset): Saleable area in square metres. The dictionary declares a numeric value
                with pattern precision notation 9999999.999, while the documented JSON example represents it as a string; either
                numeric or string representation is permitted.
            scheme_name (str | Unset): Subsidised home ownership scheme name.
            scheme_type (str | Unset): Subsidised home ownership scheme type. The dictionary lists GSH as a possible value.
            wing (str | Unset): Wing of the purchased flat.
    """

    asp_sign_date: str | Unset = UNSET
    block_name: str | Unset = UNSET
    court_estate_name: str | Unset = UNSET
    flat_num: str | Unset = UNSET
    floor_num: str | Unset = UNSET
    sale_price: float | str | Unset = UNSET
    saleable_area: float | str | Unset = UNSET
    scheme_name: str | Unset = UNSET
    scheme_type: str | Unset = UNSET
    wing: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asp_sign_date = self.asp_sign_date

        block_name = self.block_name

        court_estate_name = self.court_estate_name

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

        wing = self.wing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asp_sign_date is not UNSET:
            field_dict["asp_sign_date"] = asp_sign_date
        if block_name is not UNSET:
            field_dict["block_name"] = block_name
        if court_estate_name is not UNSET:
            field_dict["court_estate_name"] = court_estate_name
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
        if wing is not UNSET:
            field_dict["wing"] = wing

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        asp_sign_date = d.pop("asp_sign_date", UNSET)

        block_name = d.pop("block_name", UNSET)

        court_estate_name = d.pop("court_estate_name", UNSET)

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

        wing = d.pop("wing", UNSET)

        transaction = cls(
            asp_sign_date=asp_sign_date,
            block_name=block_name,
            court_estate_name=court_estate_name,
            flat_num=flat_num,
            floor_num=floor_num,
            sale_price=sale_price,
            saleable_area=saleable_area,
            scheme_name=scheme_name,
            scheme_type=scheme_type,
            wing=wing,
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
