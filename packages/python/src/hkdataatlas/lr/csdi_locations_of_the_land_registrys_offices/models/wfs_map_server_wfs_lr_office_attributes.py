from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsLROfficeAttributes")


@_attrs_define
class WfsMapServerWfsLROfficeAttributes:
    """
    Attributes:
        address_of_office_in_eng (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        address_of_office_in_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        address_of_office_in_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        lr_office_in_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        lr_office_in_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        lr_office_in_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        office_tel (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    address_of_office_in_eng: None | str | Unset = UNSET
    address_of_office_in_sc: None | str | Unset = UNSET
    address_of_office_in_tc: None | str | Unset = UNSET
    lr_office_in_en: None | str | Unset = UNSET
    lr_office_in_sc: None | str | Unset = UNSET
    lr_office_in_tc: None | str | Unset = UNSET
    office_tel: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_of_office_in_eng: None | str | Unset
        if isinstance(self.address_of_office_in_eng, Unset):
            address_of_office_in_eng = UNSET
        else:
            address_of_office_in_eng = self.address_of_office_in_eng

        address_of_office_in_sc: None | str | Unset
        if isinstance(self.address_of_office_in_sc, Unset):
            address_of_office_in_sc = UNSET
        else:
            address_of_office_in_sc = self.address_of_office_in_sc

        address_of_office_in_tc: None | str | Unset
        if isinstance(self.address_of_office_in_tc, Unset):
            address_of_office_in_tc = UNSET
        else:
            address_of_office_in_tc = self.address_of_office_in_tc

        lr_office_in_en: None | str | Unset
        if isinstance(self.lr_office_in_en, Unset):
            lr_office_in_en = UNSET
        else:
            lr_office_in_en = self.lr_office_in_en

        lr_office_in_sc: None | str | Unset
        if isinstance(self.lr_office_in_sc, Unset):
            lr_office_in_sc = UNSET
        else:
            lr_office_in_sc = self.lr_office_in_sc

        lr_office_in_tc: None | str | Unset
        if isinstance(self.lr_office_in_tc, Unset):
            lr_office_in_tc = UNSET
        else:
            lr_office_in_tc = self.lr_office_in_tc

        office_tel: float | None | Unset
        if isinstance(self.office_tel, Unset):
            office_tel = UNSET
        else:
            office_tel = self.office_tel

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_of_office_in_eng is not UNSET:
            field_dict["ADDRESS_OF_OFFICE_IN_ENG"] = address_of_office_in_eng
        if address_of_office_in_sc is not UNSET:
            field_dict["ADDRESS_OF_OFFICE_IN_SC"] = address_of_office_in_sc
        if address_of_office_in_tc is not UNSET:
            field_dict["ADDRESS_OF_OFFICE_IN_TC"] = address_of_office_in_tc
        if lr_office_in_en is not UNSET:
            field_dict["LR_OFFICE_IN_EN"] = lr_office_in_en
        if lr_office_in_sc is not UNSET:
            field_dict["LR_OFFICE_IN_SC"] = lr_office_in_sc
        if lr_office_in_tc is not UNSET:
            field_dict["LR_OFFICE_IN_TC"] = lr_office_in_tc
        if office_tel is not UNSET:
            field_dict["OFFICE_TEL"] = office_tel
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address_of_office_in_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_of_office_in_eng = _parse_address_of_office_in_eng(
            d.pop("ADDRESS_OF_OFFICE_IN_ENG", UNSET)
        )

        def _parse_address_of_office_in_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_of_office_in_sc = _parse_address_of_office_in_sc(
            d.pop("ADDRESS_OF_OFFICE_IN_SC", UNSET)
        )

        def _parse_address_of_office_in_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_of_office_in_tc = _parse_address_of_office_in_tc(
            d.pop("ADDRESS_OF_OFFICE_IN_TC", UNSET)
        )

        def _parse_lr_office_in_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lr_office_in_en = _parse_lr_office_in_en(d.pop("LR_OFFICE_IN_EN", UNSET))

        def _parse_lr_office_in_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lr_office_in_sc = _parse_lr_office_in_sc(d.pop("LR_OFFICE_IN_SC", UNSET))

        def _parse_lr_office_in_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lr_office_in_tc = _parse_lr_office_in_tc(d.pop("LR_OFFICE_IN_TC", UNSET))

        def _parse_office_tel(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        office_tel = _parse_office_tel(d.pop("OFFICE_TEL", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfs_lr_office_attributes = cls(
            address_of_office_in_eng=address_of_office_in_eng,
            address_of_office_in_sc=address_of_office_in_sc,
            address_of_office_in_tc=address_of_office_in_tc,
            lr_office_in_en=lr_office_in_en,
            lr_office_in_sc=lr_office_in_sc,
            lr_office_in_tc=lr_office_in_tc,
            office_tel=office_tel,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfs_lr_office_attributes.additional_properties = d
        return wfs_map_server_wfs_lr_office_attributes

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
