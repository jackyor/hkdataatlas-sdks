from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsGeoNameAttributes")


@_attrs_define
class WfsMapServerWfsGeoNameAttributes:
    """
    Attributes:
        chinesename (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        class_ (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        easting (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        englishname (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        geonameid (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lastupdatedate (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        northing (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        physicalstatus (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML
            occurrence into all JSON queries.
        priority (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML occurrence into
            all JSON queries.
        source (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML occurrence into
            all JSON queries.
        subcat (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        type_ (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
    """

    chinesename: None | str | Unset = UNSET
    class_: None | str | Unset = UNSET
    easting: float | None | Unset = UNSET
    englishname: None | str | Unset = UNSET
    geonameid: float | None | Unset = UNSET
    lastupdatedate: float | None | Unset = UNSET
    northing: float | None | Unset = UNSET
    physicalstatus: int | None | Unset = UNSET
    priority: int | None | Unset = UNSET
    source: int | None | Unset = UNSET
    subcat: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chinesename: None | str | Unset
        if isinstance(self.chinesename, Unset):
            chinesename = UNSET
        else:
            chinesename = self.chinesename

        class_: None | str | Unset
        if isinstance(self.class_, Unset):
            class_ = UNSET
        else:
            class_ = self.class_

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        englishname: None | str | Unset
        if isinstance(self.englishname, Unset):
            englishname = UNSET
        else:
            englishname = self.englishname

        geonameid: float | None | Unset
        if isinstance(self.geonameid, Unset):
            geonameid = UNSET
        else:
            geonameid = self.geonameid

        lastupdatedate: float | None | Unset
        if isinstance(self.lastupdatedate, Unset):
            lastupdatedate = UNSET
        else:
            lastupdatedate = self.lastupdatedate

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        physicalstatus: int | None | Unset
        if isinstance(self.physicalstatus, Unset):
            physicalstatus = UNSET
        else:
            physicalstatus = self.physicalstatus

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        source: int | None | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        subcat: None | str | Unset
        if isinstance(self.subcat, Unset):
            subcat = UNSET
        else:
            subcat = self.subcat

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chinesename is not UNSET:
            field_dict["CHINESENAME"] = chinesename
        if class_ is not UNSET:
            field_dict["CLASS"] = class_
        if easting is not UNSET:
            field_dict["EASTING"] = easting
        if englishname is not UNSET:
            field_dict["ENGLISHNAME"] = englishname
        if geonameid is not UNSET:
            field_dict["GEONAMEID"] = geonameid
        if lastupdatedate is not UNSET:
            field_dict["LASTUPDATEDATE"] = lastupdatedate
        if northing is not UNSET:
            field_dict["NORTHING"] = northing
        if physicalstatus is not UNSET:
            field_dict["PHYSICALSTATUS"] = physicalstatus
        if priority is not UNSET:
            field_dict["PRIORITY"] = priority
        if source is not UNSET:
            field_dict["SOURCE"] = source
        if subcat is not UNSET:
            field_dict["SUBCAT"] = subcat
        if type_ is not UNSET:
            field_dict["TYPE"] = type_
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_chinesename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinesename = _parse_chinesename(d.pop("CHINESENAME", UNSET))

        def _parse_class_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_ = _parse_class_(d.pop("CLASS", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("EASTING", UNSET))

        def _parse_englishname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        englishname = _parse_englishname(d.pop("ENGLISHNAME", UNSET))

        def _parse_geonameid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        geonameid = _parse_geonameid(d.pop("GEONAMEID", UNSET))

        def _parse_lastupdatedate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lastupdatedate = _parse_lastupdatedate(d.pop("LASTUPDATEDATE", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("NORTHING", UNSET))

        def _parse_physicalstatus(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        physicalstatus = _parse_physicalstatus(d.pop("PHYSICALSTATUS", UNSET))

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("PRIORITY", UNSET))

        def _parse_source(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        source = _parse_source(d.pop("SOURCE", UNSET))

        def _parse_subcat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subcat = _parse_subcat(d.pop("SUBCAT", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("TYPE", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        wfs_map_server_wfs_geo_name_attributes = cls(
            chinesename=chinesename,
            class_=class_,
            easting=easting,
            englishname=englishname,
            geonameid=geonameid,
            lastupdatedate=lastupdatedate,
            northing=northing,
            physicalstatus=physicalstatus,
            priority=priority,
            source=source,
            subcat=subcat,
            type_=type_,
            objectid=objectid,
        )

        wfs_map_server_wfs_geo_name_attributes.additional_properties = d
        return wfs_map_server_wfs_geo_name_attributes

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
