from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TpsSaleTransaction")


@_attrs_define
class TpsSaleTransaction:
    """TPS record semantics from the publisher dictionary, with exact JSON wire names/string representation corroborated by
    three saved records. Numeric dictionary quantities are string-encoded in those observations; no closed field set or
    universal requiredness is inferred.

        Attributes:
            assignment_date (str | Unset): Assignment date in dd-mm-yyyy format. Publisher label: Assignment Date; declared
                type: Date. Exact JSON key and string representation observed in three saved records; this observation does not
                establish universal requiredness or exhaustive keys.
            credit_level (str | Unset): Credit level of credit. English values documented: F = Full credit, H = Half credit,
                0 = Zero credit. Traditional Chinese values documented: 全 = full, 半 = half, 0 = zero. Publisher label: Credit
                Level; declared type: Text. Exact JSON key and string representation observed in three saved records; this
                observation does not establish universal requiredness or exhaustive keys.
            discount_rate (str | Unset): Discount rate of the flat, in percent. Publisher label: Discount Rate %; declared
                type: Numeric. Exact JSON key and string representation observed in three saved records; this observation does
                not establish universal requiredness or exhaustive keys.
            estate_map_latitude (str | Unset): Map latitude of the TPS estate. Publisher label: The Estate latitude
                parameter in Google Map; declared type: Numeric. Exact JSON key and string representation observed in three
                saved records; this observation does not establish universal requiredness or exhaustive keys.
            estate_map_longitude (str | Unset): Map longitude of the TPS estate. Publisher label: The Estate longitude
                parameter in Google Map; declared type: Numeric. Exact JSON key and string representation observed in three
                saved records; this observation does not establish universal requiredness or exhaustive keys.
            estate_name (str | Unset): Name of the TPS estate. Publisher label: Estate Name; declared type: Text. Exact JSON
                key and string representation observed in three saved records; this observation does not establish universal
                requiredness or exhaustive keys.
            floor_level (str | Unset): Floor of the flat. English categories: H means 27/F or above; M means 14/F to 26/F; L
                means 13/F or below. The Chinese description contains corresponding labels 高, 中, 低, with its final boundary
                wording as printed. Publisher label: Floor Level; declared type: Text. Exact JSON key and string representation
                observed in three saved records; this observation does not establish universal requiredness or exhaustive keys.
            location (str | Unset): Location of the TPS estate. Publisher label: Location; declared type: Text. Exact JSON
                key and string representation observed in three saved records; this observation does not establish universal
                requiredness or exhaustive keys.
            saleable_floor_area (str | Unset): Saleable area of the flat in square metres or square feet. The source states
                1 sq m = 10.764 sq ft. Publisher label: Saleable Floor Area (sq m/sq ft); declared type: Numeric. Exact JSON key
                and string representation observed in three saved records; this observation does not establish universal
                requiredness or exhaustive keys.
            transaction_price (str | Unset): Transaction price of the flat. Publisher label: Transaction Price (HK$);
                declared type: Numeric. Exact JSON key and string representation observed in three saved records; this
                observation does not establish universal requiredness or exhaustive keys.
            transaction_price_per_sq (str | Unset): Transaction price per square metre or square foot of saleable area.
                Publisher label: Transaction Price Per sq m/sq ft (HK$); declared type: Numeric. Exact JSON key and string
                representation observed in three saved records; this observation does not establish universal requiredness or
                exhaustive keys.
    """

    assignment_date: str | Unset = UNSET
    credit_level: str | Unset = UNSET
    discount_rate: str | Unset = UNSET
    estate_map_latitude: str | Unset = UNSET
    estate_map_longitude: str | Unset = UNSET
    estate_name: str | Unset = UNSET
    floor_level: str | Unset = UNSET
    location: str | Unset = UNSET
    saleable_floor_area: str | Unset = UNSET
    transaction_price: str | Unset = UNSET
    transaction_price_per_sq: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignment_date = self.assignment_date

        credit_level = self.credit_level

        discount_rate = self.discount_rate

        estate_map_latitude = self.estate_map_latitude

        estate_map_longitude = self.estate_map_longitude

        estate_name = self.estate_name

        floor_level = self.floor_level

        location = self.location

        saleable_floor_area = self.saleable_floor_area

        transaction_price = self.transaction_price

        transaction_price_per_sq = self.transaction_price_per_sq

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignment_date is not UNSET:
            field_dict["assignment_date"] = assignment_date
        if credit_level is not UNSET:
            field_dict["credit_level"] = credit_level
        if discount_rate is not UNSET:
            field_dict["discount_rate"] = discount_rate
        if estate_map_latitude is not UNSET:
            field_dict["estate_map_latitude"] = estate_map_latitude
        if estate_map_longitude is not UNSET:
            field_dict["estate_map_longitude"] = estate_map_longitude
        if estate_name is not UNSET:
            field_dict["estate_name"] = estate_name
        if floor_level is not UNSET:
            field_dict["floor_level"] = floor_level
        if location is not UNSET:
            field_dict["location"] = location
        if saleable_floor_area is not UNSET:
            field_dict["saleable_floor_area"] = saleable_floor_area
        if transaction_price is not UNSET:
            field_dict["transaction_price"] = transaction_price
        if transaction_price_per_sq is not UNSET:
            field_dict["transaction_price_per_sq"] = transaction_price_per_sq

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        assignment_date = d.pop("assignment_date", UNSET)

        credit_level = d.pop("credit_level", UNSET)

        discount_rate = d.pop("discount_rate", UNSET)

        estate_map_latitude = d.pop("estate_map_latitude", UNSET)

        estate_map_longitude = d.pop("estate_map_longitude", UNSET)

        estate_name = d.pop("estate_name", UNSET)

        floor_level = d.pop("floor_level", UNSET)

        location = d.pop("location", UNSET)

        saleable_floor_area = d.pop("saleable_floor_area", UNSET)

        transaction_price = d.pop("transaction_price", UNSET)

        transaction_price_per_sq = d.pop("transaction_price_per_sq", UNSET)

        tps_sale_transaction = cls(
            assignment_date=assignment_date,
            credit_level=credit_level,
            discount_rate=discount_rate,
            estate_map_latitude=estate_map_latitude,
            estate_map_longitude=estate_map_longitude,
            estate_name=estate_name,
            floor_level=floor_level,
            location=location,
            saleable_floor_area=saleable_floor_area,
            transaction_price=transaction_price,
            transaction_price_per_sq=transaction_price_per_sq,
        )

        tps_sale_transaction.additional_properties = d
        return tps_sale_transaction

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
