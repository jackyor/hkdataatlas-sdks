from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsHOS2024Attributes")


@_attrs_define
class WfsMapServerWfsHOS2024Attributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        scheme_type (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        scheme_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        scheme_name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        scheme_name_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        date_of_asp (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML
            occurrence into all JSON queries.
        court_estate_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        court_estate_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        court_estate_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        block_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        block_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        block_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wing (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        floor (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        unit (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        saleable_area_of_flats_sq_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected
            from XML occurrence into all JSON queries.
        transaction_price (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    scheme_type: None | str | Unset = UNSET
    scheme_name_en: None | str | Unset = UNSET
    scheme_name_tc: None | str | Unset = UNSET
    scheme_name_sc: None | str | Unset = UNSET
    date_of_asp: None | str | Unset = UNSET
    court_estate_en: None | str | Unset = UNSET
    court_estate_tc: None | str | Unset = UNSET
    court_estate_sc: None | str | Unset = UNSET
    block_en: None | str | Unset = UNSET
    block_tc: None | str | Unset = UNSET
    block_sc: None | str | Unset = UNSET
    wing: None | str | Unset = UNSET
    floor: None | str | Unset = UNSET
    unit: None | str | Unset = UNSET
    saleable_area_of_flats_sq_m: float | None | Unset = UNSET
    transaction_price: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        scheme_type: None | str | Unset
        if isinstance(self.scheme_type, Unset):
            scheme_type = UNSET
        else:
            scheme_type = self.scheme_type

        scheme_name_en: None | str | Unset
        if isinstance(self.scheme_name_en, Unset):
            scheme_name_en = UNSET
        else:
            scheme_name_en = self.scheme_name_en

        scheme_name_tc: None | str | Unset
        if isinstance(self.scheme_name_tc, Unset):
            scheme_name_tc = UNSET
        else:
            scheme_name_tc = self.scheme_name_tc

        scheme_name_sc: None | str | Unset
        if isinstance(self.scheme_name_sc, Unset):
            scheme_name_sc = UNSET
        else:
            scheme_name_sc = self.scheme_name_sc

        date_of_asp: None | str | Unset
        if isinstance(self.date_of_asp, Unset):
            date_of_asp = UNSET
        else:
            date_of_asp = self.date_of_asp

        court_estate_en: None | str | Unset
        if isinstance(self.court_estate_en, Unset):
            court_estate_en = UNSET
        else:
            court_estate_en = self.court_estate_en

        court_estate_tc: None | str | Unset
        if isinstance(self.court_estate_tc, Unset):
            court_estate_tc = UNSET
        else:
            court_estate_tc = self.court_estate_tc

        court_estate_sc: None | str | Unset
        if isinstance(self.court_estate_sc, Unset):
            court_estate_sc = UNSET
        else:
            court_estate_sc = self.court_estate_sc

        block_en: None | str | Unset
        if isinstance(self.block_en, Unset):
            block_en = UNSET
        else:
            block_en = self.block_en

        block_tc: None | str | Unset
        if isinstance(self.block_tc, Unset):
            block_tc = UNSET
        else:
            block_tc = self.block_tc

        block_sc: None | str | Unset
        if isinstance(self.block_sc, Unset):
            block_sc = UNSET
        else:
            block_sc = self.block_sc

        wing: None | str | Unset
        if isinstance(self.wing, Unset):
            wing = UNSET
        else:
            wing = self.wing

        floor: None | str | Unset
        if isinstance(self.floor, Unset):
            floor = UNSET
        else:
            floor = self.floor

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit

        saleable_area_of_flats_sq_m: float | None | Unset
        if isinstance(self.saleable_area_of_flats_sq_m, Unset):
            saleable_area_of_flats_sq_m = UNSET
        else:
            saleable_area_of_flats_sq_m = self.saleable_area_of_flats_sq_m

        transaction_price: float | None | Unset
        if isinstance(self.transaction_price, Unset):
            transaction_price = UNSET
        else:
            transaction_price = self.transaction_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if scheme_type is not UNSET:
            field_dict["Scheme_Type"] = scheme_type
        if scheme_name_en is not UNSET:
            field_dict["Scheme_Name_EN"] = scheme_name_en
        if scheme_name_tc is not UNSET:
            field_dict["Scheme_Name_TC"] = scheme_name_tc
        if scheme_name_sc is not UNSET:
            field_dict["Scheme_Name_SC"] = scheme_name_sc
        if date_of_asp is not UNSET:
            field_dict["Date_of_ASP"] = date_of_asp
        if court_estate_en is not UNSET:
            field_dict["Court_Estate_EN"] = court_estate_en
        if court_estate_tc is not UNSET:
            field_dict["Court_Estate_TC"] = court_estate_tc
        if court_estate_sc is not UNSET:
            field_dict["Court_Estate_SC"] = court_estate_sc
        if block_en is not UNSET:
            field_dict["Block_EN"] = block_en
        if block_tc is not UNSET:
            field_dict["Block_TC"] = block_tc
        if block_sc is not UNSET:
            field_dict["Block_SC"] = block_sc
        if wing is not UNSET:
            field_dict["Wing"] = wing
        if floor is not UNSET:
            field_dict["Floor"] = floor
        if unit is not UNSET:
            field_dict["Unit"] = unit
        if saleable_area_of_flats_sq_m is not UNSET:
            field_dict["Saleable_Area_of_Flats_sq_m"] = saleable_area_of_flats_sq_m
        if transaction_price is not UNSET:
            field_dict["Transaction_Price"] = transaction_price

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("Shape", UNSET)

        def _parse_scheme_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheme_type = _parse_scheme_type(d.pop("Scheme_Type", UNSET))

        def _parse_scheme_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheme_name_en = _parse_scheme_name_en(d.pop("Scheme_Name_EN", UNSET))

        def _parse_scheme_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheme_name_tc = _parse_scheme_name_tc(d.pop("Scheme_Name_TC", UNSET))

        def _parse_scheme_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheme_name_sc = _parse_scheme_name_sc(d.pop("Scheme_Name_SC", UNSET))

        def _parse_date_of_asp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_of_asp = _parse_date_of_asp(d.pop("Date_of_ASP", UNSET))

        def _parse_court_estate_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        court_estate_en = _parse_court_estate_en(d.pop("Court_Estate_EN", UNSET))

        def _parse_court_estate_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        court_estate_tc = _parse_court_estate_tc(d.pop("Court_Estate_TC", UNSET))

        def _parse_court_estate_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        court_estate_sc = _parse_court_estate_sc(d.pop("Court_Estate_SC", UNSET))

        def _parse_block_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        block_en = _parse_block_en(d.pop("Block_EN", UNSET))

        def _parse_block_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        block_tc = _parse_block_tc(d.pop("Block_TC", UNSET))

        def _parse_block_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        block_sc = _parse_block_sc(d.pop("Block_SC", UNSET))

        def _parse_wing(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wing = _parse_wing(d.pop("Wing", UNSET))

        def _parse_floor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        floor = _parse_floor(d.pop("Floor", UNSET))

        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("Unit", UNSET))

        def _parse_saleable_area_of_flats_sq_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        saleable_area_of_flats_sq_m = _parse_saleable_area_of_flats_sq_m(
            d.pop("Saleable_Area_of_Flats_sq_m", UNSET)
        )

        def _parse_transaction_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        transaction_price = _parse_transaction_price(d.pop("Transaction_Price", UNSET))

        wfs_map_server_wfs_hos2024_attributes = cls(
            objectid=objectid,
            shape=shape,
            scheme_type=scheme_type,
            scheme_name_en=scheme_name_en,
            scheme_name_tc=scheme_name_tc,
            scheme_name_sc=scheme_name_sc,
            date_of_asp=date_of_asp,
            court_estate_en=court_estate_en,
            court_estate_tc=court_estate_tc,
            court_estate_sc=court_estate_sc,
            block_en=block_en,
            block_tc=block_tc,
            block_sc=block_sc,
            wing=wing,
            floor=floor,
            unit=unit,
            saleable_area_of_flats_sq_m=saleable_area_of_flats_sq_m,
            transaction_price=transaction_price,
        )

        wfs_map_server_wfs_hos2024_attributes.additional_properties = d
        return wfs_map_server_wfs_hos2024_attributes

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
