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
        permit_type_eng (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        permit_type_chin (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        permit_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        issue_on (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        validity (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        permittee_name_eng (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        permittee_name_chin (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        site_address_eng (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        site_address_chin (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        district_eng (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_chin (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        url (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        lat (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        long (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    permit_type_eng: None | str | Unset = UNSET
    permit_type_chin: None | str | Unset = UNSET
    permit_no: None | str | Unset = UNSET
    issue_on: None | str | Unset = UNSET
    validity: None | str | Unset = UNSET
    permittee_name_eng: None | str | Unset = UNSET
    permittee_name_chin: None | str | Unset = UNSET
    site_address_eng: None | str | Unset = UNSET
    site_address_chin: None | str | Unset = UNSET
    district_eng: None | str | Unset = UNSET
    district_chin: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    lat: None | str | Unset = UNSET
    long: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        permit_type_eng: None | str | Unset
        if isinstance(self.permit_type_eng, Unset):
            permit_type_eng = UNSET
        else:
            permit_type_eng = self.permit_type_eng

        permit_type_chin: None | str | Unset
        if isinstance(self.permit_type_chin, Unset):
            permit_type_chin = UNSET
        else:
            permit_type_chin = self.permit_type_chin

        permit_no: None | str | Unset
        if isinstance(self.permit_no, Unset):
            permit_no = UNSET
        else:
            permit_no = self.permit_no

        issue_on: None | str | Unset
        if isinstance(self.issue_on, Unset):
            issue_on = UNSET
        else:
            issue_on = self.issue_on

        validity: None | str | Unset
        if isinstance(self.validity, Unset):
            validity = UNSET
        else:
            validity = self.validity

        permittee_name_eng: None | str | Unset
        if isinstance(self.permittee_name_eng, Unset):
            permittee_name_eng = UNSET
        else:
            permittee_name_eng = self.permittee_name_eng

        permittee_name_chin: None | str | Unset
        if isinstance(self.permittee_name_chin, Unset):
            permittee_name_chin = UNSET
        else:
            permittee_name_chin = self.permittee_name_chin

        site_address_eng: None | str | Unset
        if isinstance(self.site_address_eng, Unset):
            site_address_eng = UNSET
        else:
            site_address_eng = self.site_address_eng

        site_address_chin: None | str | Unset
        if isinstance(self.site_address_chin, Unset):
            site_address_chin = UNSET
        else:
            site_address_chin = self.site_address_chin

        district_eng: None | str | Unset
        if isinstance(self.district_eng, Unset):
            district_eng = UNSET
        else:
            district_eng = self.district_eng

        district_chin: None | str | Unset
        if isinstance(self.district_chin, Unset):
            district_chin = UNSET
        else:
            district_chin = self.district_chin

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        lat: None | str | Unset
        if isinstance(self.lat, Unset):
            lat = UNSET
        else:
            lat = self.lat

        long: None | str | Unset
        if isinstance(self.long, Unset):
            long = UNSET
        else:
            long = self.long

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permit_type_eng is not UNSET:
            field_dict["PERMIT_TYPE_ENG"] = permit_type_eng
        if permit_type_chin is not UNSET:
            field_dict["PERMIT_TYPE_CHIN"] = permit_type_chin
        if permit_no is not UNSET:
            field_dict["PERMIT_NO"] = permit_no
        if issue_on is not UNSET:
            field_dict["ISSUE_ON"] = issue_on
        if validity is not UNSET:
            field_dict["VALIDITY"] = validity
        if permittee_name_eng is not UNSET:
            field_dict["PERMITTEE_NAME_ENG"] = permittee_name_eng
        if permittee_name_chin is not UNSET:
            field_dict["PERMITTEE_NAME_CHIN"] = permittee_name_chin
        if site_address_eng is not UNSET:
            field_dict["SITE_ADDRESS_ENG"] = site_address_eng
        if site_address_chin is not UNSET:
            field_dict["SITE_ADDRESS_CHIN"] = site_address_chin
        if district_eng is not UNSET:
            field_dict["DISTRICT_ENG"] = district_eng
        if district_chin is not UNSET:
            field_dict["DISTRICT_CHIN"] = district_chin
        if url is not UNSET:
            field_dict["URL"] = url
        if lat is not UNSET:
            field_dict["LAT"] = lat
        if long is not UNSET:
            field_dict["LONG"] = long
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_permit_type_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        permit_type_eng = _parse_permit_type_eng(d.pop("PERMIT_TYPE_ENG", UNSET))

        def _parse_permit_type_chin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        permit_type_chin = _parse_permit_type_chin(d.pop("PERMIT_TYPE_CHIN", UNSET))

        def _parse_permit_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        permit_no = _parse_permit_no(d.pop("PERMIT_NO", UNSET))

        def _parse_issue_on(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issue_on = _parse_issue_on(d.pop("ISSUE_ON", UNSET))

        def _parse_validity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        validity = _parse_validity(d.pop("VALIDITY", UNSET))

        def _parse_permittee_name_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        permittee_name_eng = _parse_permittee_name_eng(
            d.pop("PERMITTEE_NAME_ENG", UNSET)
        )

        def _parse_permittee_name_chin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        permittee_name_chin = _parse_permittee_name_chin(
            d.pop("PERMITTEE_NAME_CHIN", UNSET)
        )

        def _parse_site_address_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_address_eng = _parse_site_address_eng(d.pop("SITE_ADDRESS_ENG", UNSET))

        def _parse_site_address_chin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_address_chin = _parse_site_address_chin(d.pop("SITE_ADDRESS_CHIN", UNSET))

        def _parse_district_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_eng = _parse_district_eng(d.pop("DISTRICT_ENG", UNSET))

        def _parse_district_chin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_chin = _parse_district_chin(d.pop("DISTRICT_CHIN", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("URL", UNSET))

        def _parse_lat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lat = _parse_lat(d.pop("LAT", UNSET))

        def _parse_long(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        long = _parse_long(d.pop("LONG", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            permit_type_eng=permit_type_eng,
            permit_type_chin=permit_type_chin,
            permit_no=permit_no,
            issue_on=issue_on,
            validity=validity,
            permittee_name_eng=permittee_name_eng,
            permittee_name_chin=permittee_name_chin,
            site_address_eng=site_address_eng,
            site_address_chin=site_address_chin,
            district_eng=district_eng,
            district_chin=district_chin,
            url=url,
            lat=lat,
            long=long,
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
