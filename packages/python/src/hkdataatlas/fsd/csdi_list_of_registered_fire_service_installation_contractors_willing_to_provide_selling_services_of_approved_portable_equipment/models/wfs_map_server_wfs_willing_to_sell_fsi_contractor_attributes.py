from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsWillingToSellFSIContractorAttributes")


@_attrs_define
class WfsMapServerWfsWillingToSellFSIContractorAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        address_eng (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        registration_c1 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        registration_c2 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        registration_c3 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        northing (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        easting (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    objectid: int | Unset = UNSET
    address_eng: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    registration_c1: None | str | Unset = UNSET
    registration_c2: None | str | Unset = UNSET
    registration_c3: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    easting: float | None | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        address_eng: None | str | Unset
        if isinstance(self.address_eng, Unset):
            address_eng = UNSET
        else:
            address_eng = self.address_eng

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        address_sc: None | str | Unset
        if isinstance(self.address_sc, Unset):
            address_sc = UNSET
        else:
            address_sc = self.address_sc

        registration_c1: None | str | Unset
        if isinstance(self.registration_c1, Unset):
            registration_c1 = UNSET
        else:
            registration_c1 = self.registration_c1

        registration_c2: None | str | Unset
        if isinstance(self.registration_c2, Unset):
            registration_c2 = UNSET
        else:
            registration_c2 = self.registration_c2

        registration_c3: None | str | Unset
        if isinstance(self.registration_c3, Unset):
            registration_c3 = UNSET
        else:
            registration_c3 = self.registration_c3

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if address_eng is not UNSET:
            field_dict["Address_ENG"] = address_eng
        if address_tc is not UNSET:
            field_dict["Address_TC"] = address_tc
        if address_sc is not UNSET:
            field_dict["Address_SC"] = address_sc
        if registration_c1 is not UNSET:
            field_dict["Registration_C1"] = registration_c1
        if registration_c2 is not UNSET:
            field_dict["Registration_C2"] = registration_c2
        if registration_c3 is not UNSET:
            field_dict["Registration_C3"] = registration_c3
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if shape is not UNSET:
            field_dict["Shape"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_address_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_eng = _parse_address_eng(d.pop("Address_ENG", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("Address_TC", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("Address_SC", UNSET))

        def _parse_registration_c1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_c1 = _parse_registration_c1(d.pop("Registration_C1", UNSET))

        def _parse_registration_c2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_c2 = _parse_registration_c2(d.pop("Registration_C2", UNSET))

        def _parse_registration_c3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_c3 = _parse_registration_c3(d.pop("Registration_C3", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("Easting", UNSET))

        shape = d.pop("Shape", UNSET)

        wfs_map_server_wfs_willing_to_sell_fsi_contractor_attributes = cls(
            objectid=objectid,
            address_eng=address_eng,
            address_tc=address_tc,
            address_sc=address_sc,
            registration_c1=registration_c1,
            registration_c2=registration_c2,
            registration_c3=registration_c3,
            northing=northing,
            easting=easting,
            shape=shape,
        )

        wfs_map_server_wfs_willing_to_sell_fsi_contractor_attributes.additional_properties = d
        return wfs_map_server_wfs_willing_to_sell_fsi_contractor_attributes

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
