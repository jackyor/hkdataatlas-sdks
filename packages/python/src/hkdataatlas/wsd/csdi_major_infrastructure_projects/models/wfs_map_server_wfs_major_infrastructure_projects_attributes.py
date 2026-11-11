from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsMajorInfrastructureProjectsAttributes")


@_attrs_define
class WfsMapServerWfsMajorInfrastructureProjectsAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        item (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        project (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        overview (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        overview_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        progress (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    item: int | None | Unset = UNSET
    project: None | str | Unset = UNSET
    overview: None | str | Unset = UNSET
    overview_chinese: None | str | Unset = UNSET
    progress: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        item: int | None | Unset
        if isinstance(self.item, Unset):
            item = UNSET
        else:
            item = self.item

        project: None | str | Unset
        if isinstance(self.project, Unset):
            project = UNSET
        else:
            project = self.project

        overview: None | str | Unset
        if isinstance(self.overview, Unset):
            overview = UNSET
        else:
            overview = self.overview

        overview_chinese: None | str | Unset
        if isinstance(self.overview_chinese, Unset):
            overview_chinese = UNSET
        else:
            overview_chinese = self.overview_chinese

        progress: None | str | Unset
        if isinstance(self.progress, Unset):
            progress = UNSET
        else:
            progress = self.progress

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
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if item is not UNSET:
            field_dict["ITEM"] = item
        if project is not UNSET:
            field_dict["PROJECT"] = project
        if overview is not UNSET:
            field_dict["OVERVIEW"] = overview
        if overview_chinese is not UNSET:
            field_dict["OVERVIEW_CHINESE"] = overview_chinese
        if progress is not UNSET:
            field_dict["PROGRESS"] = progress
        if shape_length is not UNSET:
            field_dict["Shape_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("Shape", UNSET)

        def _parse_item(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        item = _parse_item(d.pop("ITEM", UNSET))

        def _parse_project(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project = _parse_project(d.pop("PROJECT", UNSET))

        def _parse_overview(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overview = _parse_overview(d.pop("OVERVIEW", UNSET))

        def _parse_overview_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overview_chinese = _parse_overview_chinese(d.pop("OVERVIEW_CHINESE", UNSET))

        def _parse_progress(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        progress = _parse_progress(d.pop("PROGRESS", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape_Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape_Area", UNSET))

        wfs_map_server_wfs_major_infrastructure_projects_attributes = cls(
            objectid=objectid,
            shape=shape,
            item=item,
            project=project,
            overview=overview,
            overview_chinese=overview_chinese,
            progress=progress,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_major_infrastructure_projects_attributes.additional_properties = d
        return wfs_map_server_wfs_major_infrastructure_projects_attributes

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
