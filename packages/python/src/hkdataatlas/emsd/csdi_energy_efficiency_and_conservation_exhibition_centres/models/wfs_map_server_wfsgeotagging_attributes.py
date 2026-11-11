from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsgeotaggingAttributes")


@_attrs_define
class WfsMapServerWfsgeotaggingAttributes:
    """
    Attributes:
        exhibition_centre_en_address (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        exhibition_centre_en_description (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        exhibition_centre_en_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        exhibition_centre_en_url (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        exhibition_centre_sc_address (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        exhibition_centre_sc_description (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        exhibition_centre_sc_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        exhibition_centre_sc_url (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        exhibition_centre_tc_address (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        exhibition_centre_tc_description (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        exhibition_centre_tc_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        exhibition_centre_tc_url (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        org_en_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        org_sc_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        org_tc_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    exhibition_centre_en_address: None | str | Unset = UNSET
    exhibition_centre_en_description: None | str | Unset = UNSET
    exhibition_centre_en_name: None | str | Unset = UNSET
    exhibition_centre_en_url: None | str | Unset = UNSET
    exhibition_centre_sc_address: None | str | Unset = UNSET
    exhibition_centre_sc_description: None | str | Unset = UNSET
    exhibition_centre_sc_name: None | str | Unset = UNSET
    exhibition_centre_sc_url: None | str | Unset = UNSET
    exhibition_centre_tc_address: None | str | Unset = UNSET
    exhibition_centre_tc_description: None | str | Unset = UNSET
    exhibition_centre_tc_name: None | str | Unset = UNSET
    exhibition_centre_tc_url: None | str | Unset = UNSET
    org_en_name: None | str | Unset = UNSET
    org_sc_name: None | str | Unset = UNSET
    org_tc_name: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exhibition_centre_en_address: None | str | Unset
        if isinstance(self.exhibition_centre_en_address, Unset):
            exhibition_centre_en_address = UNSET
        else:
            exhibition_centre_en_address = self.exhibition_centre_en_address

        exhibition_centre_en_description: None | str | Unset
        if isinstance(self.exhibition_centre_en_description, Unset):
            exhibition_centre_en_description = UNSET
        else:
            exhibition_centre_en_description = self.exhibition_centre_en_description

        exhibition_centre_en_name: None | str | Unset
        if isinstance(self.exhibition_centre_en_name, Unset):
            exhibition_centre_en_name = UNSET
        else:
            exhibition_centre_en_name = self.exhibition_centre_en_name

        exhibition_centre_en_url: None | str | Unset
        if isinstance(self.exhibition_centre_en_url, Unset):
            exhibition_centre_en_url = UNSET
        else:
            exhibition_centre_en_url = self.exhibition_centre_en_url

        exhibition_centre_sc_address: None | str | Unset
        if isinstance(self.exhibition_centre_sc_address, Unset):
            exhibition_centre_sc_address = UNSET
        else:
            exhibition_centre_sc_address = self.exhibition_centre_sc_address

        exhibition_centre_sc_description: None | str | Unset
        if isinstance(self.exhibition_centre_sc_description, Unset):
            exhibition_centre_sc_description = UNSET
        else:
            exhibition_centre_sc_description = self.exhibition_centre_sc_description

        exhibition_centre_sc_name: None | str | Unset
        if isinstance(self.exhibition_centre_sc_name, Unset):
            exhibition_centre_sc_name = UNSET
        else:
            exhibition_centre_sc_name = self.exhibition_centre_sc_name

        exhibition_centre_sc_url: None | str | Unset
        if isinstance(self.exhibition_centre_sc_url, Unset):
            exhibition_centre_sc_url = UNSET
        else:
            exhibition_centre_sc_url = self.exhibition_centre_sc_url

        exhibition_centre_tc_address: None | str | Unset
        if isinstance(self.exhibition_centre_tc_address, Unset):
            exhibition_centre_tc_address = UNSET
        else:
            exhibition_centre_tc_address = self.exhibition_centre_tc_address

        exhibition_centre_tc_description: None | str | Unset
        if isinstance(self.exhibition_centre_tc_description, Unset):
            exhibition_centre_tc_description = UNSET
        else:
            exhibition_centre_tc_description = self.exhibition_centre_tc_description

        exhibition_centre_tc_name: None | str | Unset
        if isinstance(self.exhibition_centre_tc_name, Unset):
            exhibition_centre_tc_name = UNSET
        else:
            exhibition_centre_tc_name = self.exhibition_centre_tc_name

        exhibition_centre_tc_url: None | str | Unset
        if isinstance(self.exhibition_centre_tc_url, Unset):
            exhibition_centre_tc_url = UNSET
        else:
            exhibition_centre_tc_url = self.exhibition_centre_tc_url

        org_en_name: None | str | Unset
        if isinstance(self.org_en_name, Unset):
            org_en_name = UNSET
        else:
            org_en_name = self.org_en_name

        org_sc_name: None | str | Unset
        if isinstance(self.org_sc_name, Unset):
            org_sc_name = UNSET
        else:
            org_sc_name = self.org_sc_name

        org_tc_name: None | str | Unset
        if isinstance(self.org_tc_name, Unset):
            org_tc_name = UNSET
        else:
            org_tc_name = self.org_tc_name

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exhibition_centre_en_address is not UNSET:
            field_dict["Exhibition_centre_en_address"] = exhibition_centre_en_address
        if exhibition_centre_en_description is not UNSET:
            field_dict["Exhibition_centre_en_description"] = (
                exhibition_centre_en_description
            )
        if exhibition_centre_en_name is not UNSET:
            field_dict["Exhibition_centre_en_name"] = exhibition_centre_en_name
        if exhibition_centre_en_url is not UNSET:
            field_dict["Exhibition_centre_en_url"] = exhibition_centre_en_url
        if exhibition_centre_sc_address is not UNSET:
            field_dict["Exhibition_centre_sc_address"] = exhibition_centre_sc_address
        if exhibition_centre_sc_description is not UNSET:
            field_dict["Exhibition_centre_sc_description"] = (
                exhibition_centre_sc_description
            )
        if exhibition_centre_sc_name is not UNSET:
            field_dict["Exhibition_centre_sc_name"] = exhibition_centre_sc_name
        if exhibition_centre_sc_url is not UNSET:
            field_dict["Exhibition_centre_sc_url"] = exhibition_centre_sc_url
        if exhibition_centre_tc_address is not UNSET:
            field_dict["Exhibition_centre_tc_address"] = exhibition_centre_tc_address
        if exhibition_centre_tc_description is not UNSET:
            field_dict["Exhibition_centre_tc_description"] = (
                exhibition_centre_tc_description
            )
        if exhibition_centre_tc_name is not UNSET:
            field_dict["Exhibition_centre_tc_name"] = exhibition_centre_tc_name
        if exhibition_centre_tc_url is not UNSET:
            field_dict["Exhibition_centre_tc_url"] = exhibition_centre_tc_url
        if org_en_name is not UNSET:
            field_dict["org_en_name"] = org_en_name
        if org_sc_name is not UNSET:
            field_dict["org_sc_name"] = org_sc_name
        if org_tc_name is not UNSET:
            field_dict["org_tc_name"] = org_tc_name
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_exhibition_centre_en_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exhibition_centre_en_address = _parse_exhibition_centre_en_address(
            d.pop("Exhibition_centre_en_address", UNSET)
        )

        def _parse_exhibition_centre_en_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exhibition_centre_en_description = _parse_exhibition_centre_en_description(
            d.pop("Exhibition_centre_en_description", UNSET)
        )

        def _parse_exhibition_centre_en_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exhibition_centre_en_name = _parse_exhibition_centre_en_name(
            d.pop("Exhibition_centre_en_name", UNSET)
        )

        def _parse_exhibition_centre_en_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exhibition_centre_en_url = _parse_exhibition_centre_en_url(
            d.pop("Exhibition_centre_en_url", UNSET)
        )

        def _parse_exhibition_centre_sc_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exhibition_centre_sc_address = _parse_exhibition_centre_sc_address(
            d.pop("Exhibition_centre_sc_address", UNSET)
        )

        def _parse_exhibition_centre_sc_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exhibition_centre_sc_description = _parse_exhibition_centre_sc_description(
            d.pop("Exhibition_centre_sc_description", UNSET)
        )

        def _parse_exhibition_centre_sc_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exhibition_centre_sc_name = _parse_exhibition_centre_sc_name(
            d.pop("Exhibition_centre_sc_name", UNSET)
        )

        def _parse_exhibition_centre_sc_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exhibition_centre_sc_url = _parse_exhibition_centre_sc_url(
            d.pop("Exhibition_centre_sc_url", UNSET)
        )

        def _parse_exhibition_centre_tc_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exhibition_centre_tc_address = _parse_exhibition_centre_tc_address(
            d.pop("Exhibition_centre_tc_address", UNSET)
        )

        def _parse_exhibition_centre_tc_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exhibition_centre_tc_description = _parse_exhibition_centre_tc_description(
            d.pop("Exhibition_centre_tc_description", UNSET)
        )

        def _parse_exhibition_centre_tc_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exhibition_centre_tc_name = _parse_exhibition_centre_tc_name(
            d.pop("Exhibition_centre_tc_name", UNSET)
        )

        def _parse_exhibition_centre_tc_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exhibition_centre_tc_url = _parse_exhibition_centre_tc_url(
            d.pop("Exhibition_centre_tc_url", UNSET)
        )

        def _parse_org_en_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        org_en_name = _parse_org_en_name(d.pop("org_en_name", UNSET))

        def _parse_org_sc_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        org_sc_name = _parse_org_sc_name(d.pop("org_sc_name", UNSET))

        def _parse_org_tc_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        org_tc_name = _parse_org_tc_name(d.pop("org_tc_name", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            exhibition_centre_en_address=exhibition_centre_en_address,
            exhibition_centre_en_description=exhibition_centre_en_description,
            exhibition_centre_en_name=exhibition_centre_en_name,
            exhibition_centre_en_url=exhibition_centre_en_url,
            exhibition_centre_sc_address=exhibition_centre_sc_address,
            exhibition_centre_sc_description=exhibition_centre_sc_description,
            exhibition_centre_sc_name=exhibition_centre_sc_name,
            exhibition_centre_sc_url=exhibition_centre_sc_url,
            exhibition_centre_tc_address=exhibition_centre_tc_address,
            exhibition_centre_tc_description=exhibition_centre_tc_description,
            exhibition_centre_tc_name=exhibition_centre_tc_name,
            exhibition_centre_tc_url=exhibition_centre_tc_url,
            org_en_name=org_en_name,
            org_sc_name=org_sc_name,
            org_tc_name=org_tc_name,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfsgeotagging_attributes.additional_properties = d
        return wfs_map_server_wfsgeotagging_attributes

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
