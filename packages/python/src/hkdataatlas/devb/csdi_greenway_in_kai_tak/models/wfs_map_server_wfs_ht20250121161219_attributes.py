from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsHT20250121161219Attributes")


@_attrs_define
class WfsMapServerWfsHT20250121161219Attributes:
    """
    Attributes:
        item_no (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        trail (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        trail_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        address (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        url_image (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiPointPropertyType; JSON geometry is not inferred from its
            XML type.
    """

    item_no: int | None | Unset = UNSET
    trail: None | str | Unset = UNSET
    trail_tc: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    url_image: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_no: int | None | Unset
        if isinstance(self.item_no, Unset):
            item_no = UNSET
        else:
            item_no = self.item_no

        trail: None | str | Unset
        if isinstance(self.trail, Unset):
            trail = UNSET
        else:
            trail = self.trail

        trail_tc: None | str | Unset
        if isinstance(self.trail_tc, Unset):
            trail_tc = UNSET
        else:
            trail_tc = self.trail_tc

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        url_image: None | str | Unset
        if isinstance(self.url_image, Unset):
            url_image = UNSET
        else:
            url_image = self.url_image

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_no is not UNSET:
            field_dict["ITEM_NO"] = item_no
        if trail is not UNSET:
            field_dict["TRAIL"] = trail
        if trail_tc is not UNSET:
            field_dict["TRAIL_TC"] = trail_tc
        if name is not UNSET:
            field_dict["NAME"] = name
        if name_tc is not UNSET:
            field_dict["NAME_TC"] = name_tc
        if address is not UNSET:
            field_dict["ADDRESS"] = address
        if address_tc is not UNSET:
            field_dict["ADDRESS_TC"] = address_tc
        if url_image is not UNSET:
            field_dict["URL_IMAGE"] = url_image
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_item_no(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        item_no = _parse_item_no(d.pop("ITEM_NO", UNSET))

        def _parse_trail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trail = _parse_trail(d.pop("TRAIL", UNSET))

        def _parse_trail_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trail_tc = _parse_trail_tc(d.pop("TRAIL_TC", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("NAME", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("NAME_TC", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("ADDRESS", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("ADDRESS_TC", UNSET))

        def _parse_url_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_image = _parse_url_image(d.pop("URL_IMAGE", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfs_ht20250121161219_attributes = cls(
            item_no=item_no,
            trail=trail,
            trail_tc=trail_tc,
            name=name,
            name_tc=name_tc,
            address=address,
            address_tc=address_tc,
            url_image=url_image,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfs_ht20250121161219_attributes.additional_properties = d
        return wfs_map_server_wfs_ht20250121161219_attributes

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
