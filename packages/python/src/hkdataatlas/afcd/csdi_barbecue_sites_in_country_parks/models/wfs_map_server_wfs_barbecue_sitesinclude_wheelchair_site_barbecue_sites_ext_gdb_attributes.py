from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="WfsMapServerWfsBarbecueSitesincludeWheelchairSiteBarbecueSitesExtGDBAttributes",
)


@_attrs_define
class WfsMapServerWfsBarbecueSitesincludeWheelchairSiteBarbecueSitesExtGDBAttributes:
    """
    Attributes:
        site_id (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        site_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        site_name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        country_park_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        country_park_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        barbecue_area_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        barbecue_area_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        num_of_bbq_pit_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        num_of_bbq_pit_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    site_id: None | str | Unset = UNSET
    site_name_en: None | str | Unset = UNSET
    site_name_tc: None | str | Unset = UNSET
    country_park_en: None | str | Unset = UNSET
    country_park_tc: None | str | Unset = UNSET
    barbecue_area_en: None | str | Unset = UNSET
    barbecue_area_tc: None | str | Unset = UNSET
    num_of_bbq_pit_en: None | str | Unset = UNSET
    num_of_bbq_pit_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id: None | str | Unset
        if isinstance(self.site_id, Unset):
            site_id = UNSET
        else:
            site_id = self.site_id

        site_name_en: None | str | Unset
        if isinstance(self.site_name_en, Unset):
            site_name_en = UNSET
        else:
            site_name_en = self.site_name_en

        site_name_tc: None | str | Unset
        if isinstance(self.site_name_tc, Unset):
            site_name_tc = UNSET
        else:
            site_name_tc = self.site_name_tc

        country_park_en: None | str | Unset
        if isinstance(self.country_park_en, Unset):
            country_park_en = UNSET
        else:
            country_park_en = self.country_park_en

        country_park_tc: None | str | Unset
        if isinstance(self.country_park_tc, Unset):
            country_park_tc = UNSET
        else:
            country_park_tc = self.country_park_tc

        barbecue_area_en: None | str | Unset
        if isinstance(self.barbecue_area_en, Unset):
            barbecue_area_en = UNSET
        else:
            barbecue_area_en = self.barbecue_area_en

        barbecue_area_tc: None | str | Unset
        if isinstance(self.barbecue_area_tc, Unset):
            barbecue_area_tc = UNSET
        else:
            barbecue_area_tc = self.barbecue_area_tc

        num_of_bbq_pit_en: None | str | Unset
        if isinstance(self.num_of_bbq_pit_en, Unset):
            num_of_bbq_pit_en = UNSET
        else:
            num_of_bbq_pit_en = self.num_of_bbq_pit_en

        num_of_bbq_pit_tc: None | str | Unset
        if isinstance(self.num_of_bbq_pit_tc, Unset):
            num_of_bbq_pit_tc = UNSET
        else:
            num_of_bbq_pit_tc = self.num_of_bbq_pit_tc

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_id is not UNSET:
            field_dict["SITE_ID"] = site_id
        if site_name_en is not UNSET:
            field_dict["SITE_NAME_EN"] = site_name_en
        if site_name_tc is not UNSET:
            field_dict["SITE_NAME_TC"] = site_name_tc
        if country_park_en is not UNSET:
            field_dict["COUNTRY_PARK_EN"] = country_park_en
        if country_park_tc is not UNSET:
            field_dict["COUNTRY_PARK_TC"] = country_park_tc
        if barbecue_area_en is not UNSET:
            field_dict["BARBECUE_AREA_EN"] = barbecue_area_en
        if barbecue_area_tc is not UNSET:
            field_dict["BARBECUE_AREA_TC"] = barbecue_area_tc
        if num_of_bbq_pit_en is not UNSET:
            field_dict["NUM_OF_BBQ_PIT_EN"] = num_of_bbq_pit_en
        if num_of_bbq_pit_tc is not UNSET:
            field_dict["NUM_OF_BBQ_PIT_TC"] = num_of_bbq_pit_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["Shape"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_site_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_id = _parse_site_id(d.pop("SITE_ID", UNSET))

        def _parse_site_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_name_en = _parse_site_name_en(d.pop("SITE_NAME_EN", UNSET))

        def _parse_site_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_name_tc = _parse_site_name_tc(d.pop("SITE_NAME_TC", UNSET))

        def _parse_country_park_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_park_en = _parse_country_park_en(d.pop("COUNTRY_PARK_EN", UNSET))

        def _parse_country_park_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_park_tc = _parse_country_park_tc(d.pop("COUNTRY_PARK_TC", UNSET))

        def _parse_barbecue_area_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barbecue_area_en = _parse_barbecue_area_en(d.pop("BARBECUE_AREA_EN", UNSET))

        def _parse_barbecue_area_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barbecue_area_tc = _parse_barbecue_area_tc(d.pop("BARBECUE_AREA_TC", UNSET))

        def _parse_num_of_bbq_pit_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        num_of_bbq_pit_en = _parse_num_of_bbq_pit_en(d.pop("NUM_OF_BBQ_PIT_EN", UNSET))

        def _parse_num_of_bbq_pit_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        num_of_bbq_pit_tc = _parse_num_of_bbq_pit_tc(d.pop("NUM_OF_BBQ_PIT_TC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("Shape", UNSET)

        wfs_map_server_wfs_barbecue_sitesinclude_wheelchair_site_barbecue_sites_ext_gdb_attributes = cls(
            site_id=site_id,
            site_name_en=site_name_en,
            site_name_tc=site_name_tc,
            country_park_en=country_park_en,
            country_park_tc=country_park_tc,
            barbecue_area_en=barbecue_area_en,
            barbecue_area_tc=barbecue_area_tc,
            num_of_bbq_pit_en=num_of_bbq_pit_en,
            num_of_bbq_pit_tc=num_of_bbq_pit_tc,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfs_barbecue_sitesinclude_wheelchair_site_barbecue_sites_ext_gdb_attributes.additional_properties = d
        return wfs_map_server_wfs_barbecue_sitesinclude_wheelchair_site_barbecue_sites_ext_gdb_attributes

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
