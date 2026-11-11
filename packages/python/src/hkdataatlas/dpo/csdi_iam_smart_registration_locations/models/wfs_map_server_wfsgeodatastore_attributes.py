from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsgeodatastoreAttributes")


@_attrs_define
class WfsMapServerWfsgeodatastoreAttributes:
    """
    Attributes:
        address_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        latitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        longitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        region_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        region_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        region_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        related_link_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        related_link_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        related_link_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        service_hrs_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        service_hrs_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        service_hrs_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        type_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        type_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        type_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    address_en: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_sc: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_sc: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    region_en: None | str | Unset = UNSET
    region_sc: None | str | Unset = UNSET
    region_tc: None | str | Unset = UNSET
    related_link_en: None | str | Unset = UNSET
    related_link_sc: None | str | Unset = UNSET
    related_link_tc: None | str | Unset = UNSET
    service_hrs_en: None | str | Unset = UNSET
    service_hrs_sc: None | str | Unset = UNSET
    service_hrs_tc: None | str | Unset = UNSET
    type_en: None | str | Unset = UNSET
    type_sc: None | str | Unset = UNSET
    type_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_sc: None | str | Unset
        if isinstance(self.address_sc, Unset):
            address_sc = UNSET
        else:
            address_sc = self.address_sc

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        district_sc: None | str | Unset
        if isinstance(self.district_sc, Unset):
            district_sc = UNSET
        else:
            district_sc = self.district_sc

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        name_sc: None | str | Unset
        if isinstance(self.name_sc, Unset):
            name_sc = UNSET
        else:
            name_sc = self.name_sc

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        region_en: None | str | Unset
        if isinstance(self.region_en, Unset):
            region_en = UNSET
        else:
            region_en = self.region_en

        region_sc: None | str | Unset
        if isinstance(self.region_sc, Unset):
            region_sc = UNSET
        else:
            region_sc = self.region_sc

        region_tc: None | str | Unset
        if isinstance(self.region_tc, Unset):
            region_tc = UNSET
        else:
            region_tc = self.region_tc

        related_link_en: None | str | Unset
        if isinstance(self.related_link_en, Unset):
            related_link_en = UNSET
        else:
            related_link_en = self.related_link_en

        related_link_sc: None | str | Unset
        if isinstance(self.related_link_sc, Unset):
            related_link_sc = UNSET
        else:
            related_link_sc = self.related_link_sc

        related_link_tc: None | str | Unset
        if isinstance(self.related_link_tc, Unset):
            related_link_tc = UNSET
        else:
            related_link_tc = self.related_link_tc

        service_hrs_en: None | str | Unset
        if isinstance(self.service_hrs_en, Unset):
            service_hrs_en = UNSET
        else:
            service_hrs_en = self.service_hrs_en

        service_hrs_sc: None | str | Unset
        if isinstance(self.service_hrs_sc, Unset):
            service_hrs_sc = UNSET
        else:
            service_hrs_sc = self.service_hrs_sc

        service_hrs_tc: None | str | Unset
        if isinstance(self.service_hrs_tc, Unset):
            service_hrs_tc = UNSET
        else:
            service_hrs_tc = self.service_hrs_tc

        type_en: None | str | Unset
        if isinstance(self.type_en, Unset):
            type_en = UNSET
        else:
            type_en = self.type_en

        type_sc: None | str | Unset
        if isinstance(self.type_sc, Unset):
            type_sc = UNSET
        else:
            type_sc = self.type_sc

        type_tc: None | str | Unset
        if isinstance(self.type_tc, Unset):
            type_tc = UNSET
        else:
            type_tc = self.type_tc

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_en is not UNSET:
            field_dict["addressEN"] = address_en
        if address_sc is not UNSET:
            field_dict["addressSC"] = address_sc
        if address_tc is not UNSET:
            field_dict["addressTC"] = address_tc
        if district_en is not UNSET:
            field_dict["districtEN"] = district_en
        if district_sc is not UNSET:
            field_dict["districtSC"] = district_sc
        if district_tc is not UNSET:
            field_dict["districtTC"] = district_tc
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if name_en is not UNSET:
            field_dict["nameEN"] = name_en
        if name_sc is not UNSET:
            field_dict["nameSC"] = name_sc
        if name_tc is not UNSET:
            field_dict["nameTC"] = name_tc
        if region_en is not UNSET:
            field_dict["regionEN"] = region_en
        if region_sc is not UNSET:
            field_dict["regionSC"] = region_sc
        if region_tc is not UNSET:
            field_dict["regionTC"] = region_tc
        if related_link_en is not UNSET:
            field_dict["relatedLinkEN"] = related_link_en
        if related_link_sc is not UNSET:
            field_dict["relatedLinkSC"] = related_link_sc
        if related_link_tc is not UNSET:
            field_dict["relatedLinkTC"] = related_link_tc
        if service_hrs_en is not UNSET:
            field_dict["serviceHrsEN"] = service_hrs_en
        if service_hrs_sc is not UNSET:
            field_dict["serviceHrsSC"] = service_hrs_sc
        if service_hrs_tc is not UNSET:
            field_dict["serviceHrsTC"] = service_hrs_tc
        if type_en is not UNSET:
            field_dict["typeEN"] = type_en
        if type_sc is not UNSET:
            field_dict["typeSC"] = type_sc
        if type_tc is not UNSET:
            field_dict["typeTC"] = type_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("addressEN", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("addressSC", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("addressTC", UNSET))

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("districtEN", UNSET))

        def _parse_district_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_sc = _parse_district_sc(d.pop("districtSC", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("districtTC", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("nameEN", UNSET))

        def _parse_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_sc = _parse_name_sc(d.pop("nameSC", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("nameTC", UNSET))

        def _parse_region_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_en = _parse_region_en(d.pop("regionEN", UNSET))

        def _parse_region_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_sc = _parse_region_sc(d.pop("regionSC", UNSET))

        def _parse_region_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_tc = _parse_region_tc(d.pop("regionTC", UNSET))

        def _parse_related_link_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        related_link_en = _parse_related_link_en(d.pop("relatedLinkEN", UNSET))

        def _parse_related_link_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        related_link_sc = _parse_related_link_sc(d.pop("relatedLinkSC", UNSET))

        def _parse_related_link_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        related_link_tc = _parse_related_link_tc(d.pop("relatedLinkTC", UNSET))

        def _parse_service_hrs_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_hrs_en = _parse_service_hrs_en(d.pop("serviceHrsEN", UNSET))

        def _parse_service_hrs_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_hrs_sc = _parse_service_hrs_sc(d.pop("serviceHrsSC", UNSET))

        def _parse_service_hrs_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_hrs_tc = _parse_service_hrs_tc(d.pop("serviceHrsTC", UNSET))

        def _parse_type_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_en = _parse_type_en(d.pop("typeEN", UNSET))

        def _parse_type_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_sc = _parse_type_sc(d.pop("typeSC", UNSET))

        def _parse_type_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_tc = _parse_type_tc(d.pop("typeTC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeodatastore_attributes = cls(
            address_en=address_en,
            address_sc=address_sc,
            address_tc=address_tc,
            district_en=district_en,
            district_sc=district_sc,
            district_tc=district_tc,
            latitude=latitude,
            longitude=longitude,
            name_en=name_en,
            name_sc=name_sc,
            name_tc=name_tc,
            region_en=region_en,
            region_sc=region_sc,
            region_tc=region_tc,
            related_link_en=related_link_en,
            related_link_sc=related_link_sc,
            related_link_tc=related_link_tc,
            service_hrs_en=service_hrs_en,
            service_hrs_sc=service_hrs_sc,
            service_hrs_tc=service_hrs_tc,
            type_en=type_en,
            type_sc=type_sc,
            type_tc=type_tc,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfsgeodatastore_attributes.additional_properties = d
        return wfs_map_server_wfsgeodatastore_attributes

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
