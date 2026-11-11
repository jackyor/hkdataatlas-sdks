from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsIncidentAttributes")


@_attrs_define
class WfsMapServerWfsIncidentAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        incid (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        ogdincid (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        callfrom (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        calldate (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML occurrence
            into all JSON queries.
        faildate (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML occurrence
            into all JSON queries.
        easting (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        northing (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        location (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        slopenum (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        feattype (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        scale (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        facaff (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        consec (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        consec_deathno (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        consec_injuryno (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        consec_evacuated (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        consec_roadclosed (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    incid: None | str | Unset = UNSET
    ogdincid: None | str | Unset = UNSET
    callfrom: None | str | Unset = UNSET
    calldate: None | str | Unset = UNSET
    faildate: None | str | Unset = UNSET
    easting: int | None | Unset = UNSET
    northing: int | None | Unset = UNSET
    location: None | str | Unset = UNSET
    slopenum: None | str | Unset = UNSET
    feattype: None | str | Unset = UNSET
    scale: None | str | Unset = UNSET
    facaff: None | str | Unset = UNSET
    consec: None | str | Unset = UNSET
    consec_deathno: None | str | Unset = UNSET
    consec_injuryno: None | str | Unset = UNSET
    consec_evacuated: None | str | Unset = UNSET
    consec_roadclosed: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        incid: None | str | Unset
        if isinstance(self.incid, Unset):
            incid = UNSET
        else:
            incid = self.incid

        ogdincid: None | str | Unset
        if isinstance(self.ogdincid, Unset):
            ogdincid = UNSET
        else:
            ogdincid = self.ogdincid

        callfrom: None | str | Unset
        if isinstance(self.callfrom, Unset):
            callfrom = UNSET
        else:
            callfrom = self.callfrom

        calldate: None | str | Unset
        if isinstance(self.calldate, Unset):
            calldate = UNSET
        else:
            calldate = self.calldate

        faildate: None | str | Unset
        if isinstance(self.faildate, Unset):
            faildate = UNSET
        else:
            faildate = self.faildate

        easting: int | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        northing: int | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        slopenum: None | str | Unset
        if isinstance(self.slopenum, Unset):
            slopenum = UNSET
        else:
            slopenum = self.slopenum

        feattype: None | str | Unset
        if isinstance(self.feattype, Unset):
            feattype = UNSET
        else:
            feattype = self.feattype

        scale: None | str | Unset
        if isinstance(self.scale, Unset):
            scale = UNSET
        else:
            scale = self.scale

        facaff: None | str | Unset
        if isinstance(self.facaff, Unset):
            facaff = UNSET
        else:
            facaff = self.facaff

        consec: None | str | Unset
        if isinstance(self.consec, Unset):
            consec = UNSET
        else:
            consec = self.consec

        consec_deathno: None | str | Unset
        if isinstance(self.consec_deathno, Unset):
            consec_deathno = UNSET
        else:
            consec_deathno = self.consec_deathno

        consec_injuryno: None | str | Unset
        if isinstance(self.consec_injuryno, Unset):
            consec_injuryno = UNSET
        else:
            consec_injuryno = self.consec_injuryno

        consec_evacuated: None | str | Unset
        if isinstance(self.consec_evacuated, Unset):
            consec_evacuated = UNSET
        else:
            consec_evacuated = self.consec_evacuated

        consec_roadclosed: None | str | Unset
        if isinstance(self.consec_roadclosed, Unset):
            consec_roadclosed = UNSET
        else:
            consec_roadclosed = self.consec_roadclosed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if incid is not UNSET:
            field_dict["INCID"] = incid
        if ogdincid is not UNSET:
            field_dict["OGDINCID"] = ogdincid
        if callfrom is not UNSET:
            field_dict["CALLFROM"] = callfrom
        if calldate is not UNSET:
            field_dict["CALLDATE"] = calldate
        if faildate is not UNSET:
            field_dict["FAILDATE"] = faildate
        if easting is not UNSET:
            field_dict["EASTING"] = easting
        if northing is not UNSET:
            field_dict["NORTHING"] = northing
        if location is not UNSET:
            field_dict["LOCATION"] = location
        if slopenum is not UNSET:
            field_dict["SLOPENUM"] = slopenum
        if feattype is not UNSET:
            field_dict["FEATTYPE"] = feattype
        if scale is not UNSET:
            field_dict["SCALE"] = scale
        if facaff is not UNSET:
            field_dict["FACAFF"] = facaff
        if consec is not UNSET:
            field_dict["CONSEC"] = consec
        if consec_deathno is not UNSET:
            field_dict["CONSEC_DEATHNO"] = consec_deathno
        if consec_injuryno is not UNSET:
            field_dict["CONSEC_INJURYNO"] = consec_injuryno
        if consec_evacuated is not UNSET:
            field_dict["CONSEC_EVACUATED"] = consec_evacuated
        if consec_roadclosed is not UNSET:
            field_dict["CONSEC_ROADCLOSED"] = consec_roadclosed

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("Shape", UNSET)

        def _parse_incid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        incid = _parse_incid(d.pop("INCID", UNSET))

        def _parse_ogdincid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ogdincid = _parse_ogdincid(d.pop("OGDINCID", UNSET))

        def _parse_callfrom(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        callfrom = _parse_callfrom(d.pop("CALLFROM", UNSET))

        def _parse_calldate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        calldate = _parse_calldate(d.pop("CALLDATE", UNSET))

        def _parse_faildate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        faildate = _parse_faildate(d.pop("FAILDATE", UNSET))

        def _parse_easting(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        easting = _parse_easting(d.pop("EASTING", UNSET))

        def _parse_northing(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        northing = _parse_northing(d.pop("NORTHING", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("LOCATION", UNSET))

        def _parse_slopenum(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slopenum = _parse_slopenum(d.pop("SLOPENUM", UNSET))

        def _parse_feattype(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feattype = _parse_feattype(d.pop("FEATTYPE", UNSET))

        def _parse_scale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scale = _parse_scale(d.pop("SCALE", UNSET))

        def _parse_facaff(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facaff = _parse_facaff(d.pop("FACAFF", UNSET))

        def _parse_consec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        consec = _parse_consec(d.pop("CONSEC", UNSET))

        def _parse_consec_deathno(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        consec_deathno = _parse_consec_deathno(d.pop("CONSEC_DEATHNO", UNSET))

        def _parse_consec_injuryno(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        consec_injuryno = _parse_consec_injuryno(d.pop("CONSEC_INJURYNO", UNSET))

        def _parse_consec_evacuated(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        consec_evacuated = _parse_consec_evacuated(d.pop("CONSEC_EVACUATED", UNSET))

        def _parse_consec_roadclosed(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        consec_roadclosed = _parse_consec_roadclosed(d.pop("CONSEC_ROADCLOSED", UNSET))

        wfs_map_server_wfs_incident_attributes = cls(
            objectid=objectid,
            shape=shape,
            incid=incid,
            ogdincid=ogdincid,
            callfrom=callfrom,
            calldate=calldate,
            faildate=faildate,
            easting=easting,
            northing=northing,
            location=location,
            slopenum=slopenum,
            feattype=feattype,
            scale=scale,
            facaff=facaff,
            consec=consec,
            consec_deathno=consec_deathno,
            consec_injuryno=consec_injuryno,
            consec_evacuated=consec_evacuated,
            consec_roadclosed=consec_roadclosed,
        )

        wfs_map_server_wfs_incident_attributes.additional_properties = d
        return wfs_map_server_wfs_incident_attributes

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
