from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTable3BAttributes")


@_attrs_define
class WfsMapServerWfsTable3BAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        aa_code (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        aa_title (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        food_products_and_beverages (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected
            from XML occurrence into all JSON queries.
        printing_factory (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        vehicle_repairing_washing (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        workshop_miscellaneous (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        workshop_without_specified_type (float | None | Unset): Native XSD type xsd:double. Requiredness is not
            projected from XML occurrence into all JSON queries.
    """

    objectid: int | Unset = UNSET
    aa_code: None | str | Unset = UNSET
    aa_title: None | str | Unset = UNSET
    food_products_and_beverages: float | None | Unset = UNSET
    printing_factory: float | None | Unset = UNSET
    vehicle_repairing_washing: float | None | Unset = UNSET
    workshop_miscellaneous: float | None | Unset = UNSET
    workshop_without_specified_type: float | None | Unset = UNSET
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

        food_products_and_beverages: float | None | Unset
        if isinstance(self.food_products_and_beverages, Unset):
            food_products_and_beverages = UNSET
        else:
            food_products_and_beverages = self.food_products_and_beverages

        printing_factory: float | None | Unset
        if isinstance(self.printing_factory, Unset):
            printing_factory = UNSET
        else:
            printing_factory = self.printing_factory

        vehicle_repairing_washing: float | None | Unset
        if isinstance(self.vehicle_repairing_washing, Unset):
            vehicle_repairing_washing = UNSET
        else:
            vehicle_repairing_washing = self.vehicle_repairing_washing

        workshop_miscellaneous: float | None | Unset
        if isinstance(self.workshop_miscellaneous, Unset):
            workshop_miscellaneous = UNSET
        else:
            workshop_miscellaneous = self.workshop_miscellaneous

        workshop_without_specified_type: float | None | Unset
        if isinstance(self.workshop_without_specified_type, Unset):
            workshop_without_specified_type = UNSET
        else:
            workshop_without_specified_type = self.workshop_without_specified_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if aa_code is not UNSET:
            field_dict["AA_Code"] = aa_code
        if aa_title is not UNSET:
            field_dict["AA_Title"] = aa_title
        if food_products_and_beverages is not UNSET:
            field_dict["Food_products_and_beverages"] = food_products_and_beverages
        if printing_factory is not UNSET:
            field_dict["Printing_factory"] = printing_factory
        if vehicle_repairing_washing is not UNSET:
            field_dict["Vehicle_repairing_washing"] = vehicle_repairing_washing
        if workshop_miscellaneous is not UNSET:
            field_dict["Workshop_miscellaneous"] = workshop_miscellaneous
        if workshop_without_specified_type is not UNSET:
            field_dict["Workshop_without_specified_type"] = (
                workshop_without_specified_type
            )

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

        def _parse_food_products_and_beverages(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        food_products_and_beverages = _parse_food_products_and_beverages(
            d.pop("Food_products_and_beverages", UNSET)
        )

        def _parse_printing_factory(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        printing_factory = _parse_printing_factory(d.pop("Printing_factory", UNSET))

        def _parse_vehicle_repairing_washing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        vehicle_repairing_washing = _parse_vehicle_repairing_washing(
            d.pop("Vehicle_repairing_washing", UNSET)
        )

        def _parse_workshop_miscellaneous(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        workshop_miscellaneous = _parse_workshop_miscellaneous(
            d.pop("Workshop_miscellaneous", UNSET)
        )

        def _parse_workshop_without_specified_type(
            data: object,
        ) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        workshop_without_specified_type = _parse_workshop_without_specified_type(
            d.pop("Workshop_without_specified_type", UNSET)
        )

        wfs_map_server_wfs_table_3b_attributes = cls(
            objectid=objectid,
            aa_code=aa_code,
            aa_title=aa_title,
            food_products_and_beverages=food_products_and_beverages,
            printing_factory=printing_factory,
            vehicle_repairing_washing=vehicle_repairing_washing,
            workshop_miscellaneous=workshop_miscellaneous,
            workshop_without_specified_type=workshop_without_specified_type,
        )

        wfs_map_server_wfs_table_3b_attributes.additional_properties = d
        return wfs_map_server_wfs_table_3b_attributes

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
