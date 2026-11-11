from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsIBEACONAttributes")


@_attrs_define
class WfsMapServerWfsIBEACONAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        lp_num (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        ble_ib_uuid (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        ble_ib_major (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        ble_ib_minor (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        ble_ib_tx (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML occurrence
            into all JSON queries.
        ble_ib_hgt (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
    """

    objectid: int | Unset = UNSET
    lp_num: None | str | Unset = UNSET
    ble_ib_uuid: None | str | Unset = UNSET
    ble_ib_major: int | None | Unset = UNSET
    ble_ib_minor: int | None | Unset = UNSET
    ble_ib_tx: int | None | Unset = UNSET
    ble_ib_hgt: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        lp_num: None | str | Unset
        if isinstance(self.lp_num, Unset):
            lp_num = UNSET
        else:
            lp_num = self.lp_num

        ble_ib_uuid: None | str | Unset
        if isinstance(self.ble_ib_uuid, Unset):
            ble_ib_uuid = UNSET
        else:
            ble_ib_uuid = self.ble_ib_uuid

        ble_ib_major: int | None | Unset
        if isinstance(self.ble_ib_major, Unset):
            ble_ib_major = UNSET
        else:
            ble_ib_major = self.ble_ib_major

        ble_ib_minor: int | None | Unset
        if isinstance(self.ble_ib_minor, Unset):
            ble_ib_minor = UNSET
        else:
            ble_ib_minor = self.ble_ib_minor

        ble_ib_tx: int | None | Unset
        if isinstance(self.ble_ib_tx, Unset):
            ble_ib_tx = UNSET
        else:
            ble_ib_tx = self.ble_ib_tx

        ble_ib_hgt: None | str | Unset
        if isinstance(self.ble_ib_hgt, Unset):
            ble_ib_hgt = UNSET
        else:
            ble_ib_hgt = self.ble_ib_hgt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if lp_num is not UNSET:
            field_dict["LP_NUM"] = lp_num
        if ble_ib_uuid is not UNSET:
            field_dict["BLE_IB_UUID"] = ble_ib_uuid
        if ble_ib_major is not UNSET:
            field_dict["BLE_IB_MAJOR"] = ble_ib_major
        if ble_ib_minor is not UNSET:
            field_dict["BLE_IB_MINOR"] = ble_ib_minor
        if ble_ib_tx is not UNSET:
            field_dict["BLE_IB_TX"] = ble_ib_tx
        if ble_ib_hgt is not UNSET:
            field_dict["BLE_IB_HGT"] = ble_ib_hgt

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_lp_num(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lp_num = _parse_lp_num(d.pop("LP_NUM", UNSET))

        def _parse_ble_ib_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ble_ib_uuid = _parse_ble_ib_uuid(d.pop("BLE_IB_UUID", UNSET))

        def _parse_ble_ib_major(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ble_ib_major = _parse_ble_ib_major(d.pop("BLE_IB_MAJOR", UNSET))

        def _parse_ble_ib_minor(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ble_ib_minor = _parse_ble_ib_minor(d.pop("BLE_IB_MINOR", UNSET))

        def _parse_ble_ib_tx(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ble_ib_tx = _parse_ble_ib_tx(d.pop("BLE_IB_TX", UNSET))

        def _parse_ble_ib_hgt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ble_ib_hgt = _parse_ble_ib_hgt(d.pop("BLE_IB_HGT", UNSET))

        wfs_map_server_wfs_ibeacon_attributes = cls(
            objectid=objectid,
            lp_num=lp_num,
            ble_ib_uuid=ble_ib_uuid,
            ble_ib_major=ble_ib_major,
            ble_ib_minor=ble_ib_minor,
            ble_ib_tx=ble_ib_tx,
            ble_ib_hgt=ble_ib_hgt,
        )

        wfs_map_server_wfs_ibeacon_attributes.additional_properties = d
        return wfs_map_server_wfs_ibeacon_attributes

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
