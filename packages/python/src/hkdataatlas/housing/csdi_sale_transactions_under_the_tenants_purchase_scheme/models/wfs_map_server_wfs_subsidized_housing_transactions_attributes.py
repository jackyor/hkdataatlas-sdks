from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsSubsidizedHousingTransactionsAttributes")


@_attrs_define
class WfsMapServerWfsSubsidizedHousingTransactionsAttributes:
    """
    Attributes:
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        estate_map_latitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        estate_map_longitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        transaction_price (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        discount_rate (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        saleable_floor_area (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        transaction_price_per_sq (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        assignment_date (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        location_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        location_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        estate_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        estate_name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        floor_level_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        floor_level_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        credit_level_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        credit_level_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
    """

    shape: Any | Unset = UNSET
    objectid: int | Unset = UNSET
    estate_map_latitude: float | None | Unset = UNSET
    estate_map_longitude: float | None | Unset = UNSET
    transaction_price: float | None | Unset = UNSET
    discount_rate: float | None | Unset = UNSET
    saleable_floor_area: None | str | Unset = UNSET
    transaction_price_per_sq: None | str | Unset = UNSET
    assignment_date: None | str | Unset = UNSET
    location_en: None | str | Unset = UNSET
    location_tc: None | str | Unset = UNSET
    estate_name_en: None | str | Unset = UNSET
    estate_name_tc: None | str | Unset = UNSET
    floor_level_en: None | str | Unset = UNSET
    floor_level_tc: None | str | Unset = UNSET
    credit_level_en: None | str | Unset = UNSET
    credit_level_tc: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shape = self.shape

        objectid = self.objectid

        estate_map_latitude: float | None | Unset
        if isinstance(self.estate_map_latitude, Unset):
            estate_map_latitude = UNSET
        else:
            estate_map_latitude = self.estate_map_latitude

        estate_map_longitude: float | None | Unset
        if isinstance(self.estate_map_longitude, Unset):
            estate_map_longitude = UNSET
        else:
            estate_map_longitude = self.estate_map_longitude

        transaction_price: float | None | Unset
        if isinstance(self.transaction_price, Unset):
            transaction_price = UNSET
        else:
            transaction_price = self.transaction_price

        discount_rate: float | None | Unset
        if isinstance(self.discount_rate, Unset):
            discount_rate = UNSET
        else:
            discount_rate = self.discount_rate

        saleable_floor_area: None | str | Unset
        if isinstance(self.saleable_floor_area, Unset):
            saleable_floor_area = UNSET
        else:
            saleable_floor_area = self.saleable_floor_area

        transaction_price_per_sq: None | str | Unset
        if isinstance(self.transaction_price_per_sq, Unset):
            transaction_price_per_sq = UNSET
        else:
            transaction_price_per_sq = self.transaction_price_per_sq

        assignment_date: None | str | Unset
        if isinstance(self.assignment_date, Unset):
            assignment_date = UNSET
        else:
            assignment_date = self.assignment_date

        location_en: None | str | Unset
        if isinstance(self.location_en, Unset):
            location_en = UNSET
        else:
            location_en = self.location_en

        location_tc: None | str | Unset
        if isinstance(self.location_tc, Unset):
            location_tc = UNSET
        else:
            location_tc = self.location_tc

        estate_name_en: None | str | Unset
        if isinstance(self.estate_name_en, Unset):
            estate_name_en = UNSET
        else:
            estate_name_en = self.estate_name_en

        estate_name_tc: None | str | Unset
        if isinstance(self.estate_name_tc, Unset):
            estate_name_tc = UNSET
        else:
            estate_name_tc = self.estate_name_tc

        floor_level_en: None | str | Unset
        if isinstance(self.floor_level_en, Unset):
            floor_level_en = UNSET
        else:
            floor_level_en = self.floor_level_en

        floor_level_tc: None | str | Unset
        if isinstance(self.floor_level_tc, Unset):
            floor_level_tc = UNSET
        else:
            floor_level_tc = self.floor_level_tc

        credit_level_en: None | str | Unset
        if isinstance(self.credit_level_en, Unset):
            credit_level_en = UNSET
        else:
            credit_level_en = self.credit_level_en

        credit_level_tc: None | str | Unset
        if isinstance(self.credit_level_tc, Unset):
            credit_level_tc = UNSET
        else:
            credit_level_tc = self.credit_level_tc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if estate_map_latitude is not UNSET:
            field_dict["estate_map_latitude"] = estate_map_latitude
        if estate_map_longitude is not UNSET:
            field_dict["estate_map_longitude"] = estate_map_longitude
        if transaction_price is not UNSET:
            field_dict["transaction_price"] = transaction_price
        if discount_rate is not UNSET:
            field_dict["discount_rate"] = discount_rate
        if saleable_floor_area is not UNSET:
            field_dict["saleable_floor_area"] = saleable_floor_area
        if transaction_price_per_sq is not UNSET:
            field_dict["transaction_price_per_sq"] = transaction_price_per_sq
        if assignment_date is not UNSET:
            field_dict["assignment_date"] = assignment_date
        if location_en is not UNSET:
            field_dict["location_en"] = location_en
        if location_tc is not UNSET:
            field_dict["location_tc"] = location_tc
        if estate_name_en is not UNSET:
            field_dict["estate_name_en"] = estate_name_en
        if estate_name_tc is not UNSET:
            field_dict["estate_name_tc"] = estate_name_tc
        if floor_level_en is not UNSET:
            field_dict["floor_level_en"] = floor_level_en
        if floor_level_tc is not UNSET:
            field_dict["floor_level_tc"] = floor_level_tc
        if credit_level_en is not UNSET:
            field_dict["credit_level_en"] = credit_level_en
        if credit_level_tc is not UNSET:
            field_dict["credit_level_tc"] = credit_level_tc

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        shape = d.pop("SHAPE", UNSET)

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_estate_map_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        estate_map_latitude = _parse_estate_map_latitude(
            d.pop("estate_map_latitude", UNSET)
        )

        def _parse_estate_map_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        estate_map_longitude = _parse_estate_map_longitude(
            d.pop("estate_map_longitude", UNSET)
        )

        def _parse_transaction_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        transaction_price = _parse_transaction_price(d.pop("transaction_price", UNSET))

        def _parse_discount_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        discount_rate = _parse_discount_rate(d.pop("discount_rate", UNSET))

        def _parse_saleable_floor_area(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        saleable_floor_area = _parse_saleable_floor_area(
            d.pop("saleable_floor_area", UNSET)
        )

        def _parse_transaction_price_per_sq(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transaction_price_per_sq = _parse_transaction_price_per_sq(
            d.pop("transaction_price_per_sq", UNSET)
        )

        def _parse_assignment_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assignment_date = _parse_assignment_date(d.pop("assignment_date", UNSET))

        def _parse_location_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_en = _parse_location_en(d.pop("location_en", UNSET))

        def _parse_location_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_tc = _parse_location_tc(d.pop("location_tc", UNSET))

        def _parse_estate_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estate_name_en = _parse_estate_name_en(d.pop("estate_name_en", UNSET))

        def _parse_estate_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estate_name_tc = _parse_estate_name_tc(d.pop("estate_name_tc", UNSET))

        def _parse_floor_level_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        floor_level_en = _parse_floor_level_en(d.pop("floor_level_en", UNSET))

        def _parse_floor_level_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        floor_level_tc = _parse_floor_level_tc(d.pop("floor_level_tc", UNSET))

        def _parse_credit_level_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        credit_level_en = _parse_credit_level_en(d.pop("credit_level_en", UNSET))

        def _parse_credit_level_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        credit_level_tc = _parse_credit_level_tc(d.pop("credit_level_tc", UNSET))

        wfs_map_server_wfs_subsidized_housing_transactions_attributes = cls(
            shape=shape,
            objectid=objectid,
            estate_map_latitude=estate_map_latitude,
            estate_map_longitude=estate_map_longitude,
            transaction_price=transaction_price,
            discount_rate=discount_rate,
            saleable_floor_area=saleable_floor_area,
            transaction_price_per_sq=transaction_price_per_sq,
            assignment_date=assignment_date,
            location_en=location_en,
            location_tc=location_tc,
            estate_name_en=estate_name_en,
            estate_name_tc=estate_name_tc,
            floor_level_en=floor_level_en,
            floor_level_tc=floor_level_tc,
            credit_level_en=credit_level_en,
            credit_level_tc=credit_level_tc,
        )

        wfs_map_server_wfs_subsidized_housing_transactions_attributes.additional_properties = d
        return wfs_map_server_wfs_subsidized_housing_transactions_attributes

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
