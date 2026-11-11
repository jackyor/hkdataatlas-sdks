from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsHYDRPOLYAttributes")


@_attrs_define
class WfsMapServerWfsHYDRPOLYAttributes:
    """
    Attributes:
        easting (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        northing (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        class_ (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        graphicdataset (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        graphicid (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lastupdatedate (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
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
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    easting: float | None | Unset = UNSET
    northing: float | None | Unset = UNSET
    class_: None | str | Unset = UNSET
    graphicdataset: None | str | Unset = UNSET
    graphicid: float | None | Unset = UNSET
    lastupdatedate: float | None | Unset = UNSET
    physicalstatus: int | None | Unset = UNSET
    priority: int | None | Unset = UNSET
    source: int | None | Unset = UNSET
    subcat: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        class_: None | str | Unset
        if isinstance(self.class_, Unset):
            class_ = UNSET
        else:
            class_ = self.class_

        graphicdataset: None | str | Unset
        if isinstance(self.graphicdataset, Unset):
            graphicdataset = UNSET
        else:
            graphicdataset = self.graphicdataset

        graphicid: float | None | Unset
        if isinstance(self.graphicid, Unset):
            graphicid = UNSET
        else:
            graphicid = self.graphicid

        lastupdatedate: float | None | Unset
        if isinstance(self.lastupdatedate, Unset):
            lastupdatedate = UNSET
        else:
            lastupdatedate = self.lastupdatedate

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

        shape = self.shape

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        shape_area: float | None | Unset
        if isinstance(self.shape_area, Unset):
            shape_area = UNSET
        else:
            shape_area = self.shape_area

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if easting is not UNSET:
            field_dict["EASTING"] = easting
        if northing is not UNSET:
            field_dict["NORTHING"] = northing
        if class_ is not UNSET:
            field_dict["CLASS"] = class_
        if graphicdataset is not UNSET:
            field_dict["GRAPHICDATASET"] = graphicdataset
        if graphicid is not UNSET:
            field_dict["GRAPHICID"] = graphicid
        if lastupdatedate is not UNSET:
            field_dict["LASTUPDATEDATE"] = lastupdatedate
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
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if shape_length is not UNSET:
            field_dict["SHAPE_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["SHAPE_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("EASTING", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("NORTHING", UNSET))

        def _parse_class_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_ = _parse_class_(d.pop("CLASS", UNSET))

        def _parse_graphicdataset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        graphicdataset = _parse_graphicdataset(d.pop("GRAPHICDATASET", UNSET))

        def _parse_graphicid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        graphicid = _parse_graphicid(d.pop("GRAPHICID", UNSET))

        def _parse_lastupdatedate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lastupdatedate = _parse_lastupdatedate(d.pop("LASTUPDATEDATE", UNSET))

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

        shape = d.pop("SHAPE", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("SHAPE_Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("SHAPE_Area", UNSET))

        wfs_map_server_wfs_hydrpoly_attributes = cls(
            easting=easting,
            northing=northing,
            class_=class_,
            graphicdataset=graphicdataset,
            graphicid=graphicid,
            lastupdatedate=lastupdatedate,
            physicalstatus=physicalstatus,
            priority=priority,
            source=source,
            subcat=subcat,
            type_=type_,
            objectid=objectid,
            shape=shape,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_hydrpoly_attributes.additional_properties = d
        return wfs_map_server_wfs_hydrpoly_attributes

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
