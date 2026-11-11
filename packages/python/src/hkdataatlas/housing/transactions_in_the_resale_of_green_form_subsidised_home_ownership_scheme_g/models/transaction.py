from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Transaction")


@_attrs_define
class Transaction:
    """Transaction record. The data dictionary declares the fields below as text or numeric. However, the JSON example
    represents every value as a string, including the numeric area and price; this discrepancy is preserved by allowing
    either string or number for those numeric fields. The publisher does not specify field requiredness.

        Attributes:
            asp_sign_date (str | Unset): Date of Agreement for Sale and Purchase (ASP). The data dictionary specifies the
                text date format as dd-mm-yyyy, while the JSON example uses 14/06/2023; both representations are preserved here
                without asserting a single wire format.
            block_name (str | Unset): Block name of the purchased flat.
            court_estate_name (str | Unset): Court/Estate name of the purchased flat.
            flat_num (str | Unset): Flat number of the purchased flat.
            floor_num (str | Unset): Floor number of the purchased flat.
            sale_price (float | str | Unset): Sale price of the purchased flat. The data dictionary declares a numeric value
                with a stated shape of 999999999999999.99, while the example encodes it as the string "2188000.0"; either number
                or string is allowed to preserve this discrepancy.
            saleable_area (float | str | Unset): Saleable area of the purchased flat in square metres. The data dictionary
                declares a numeric value with a stated shape of 9999999.999, while the example encodes it as the string "36.9";
                either number or string is allowed to preserve this discrepancy.
            scheme_name (str | Unset): Subsidised home ownership scheme name.
            scheme_type (str | Unset): Subsidised home ownership scheme type. The documented possible value is GSH.
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
