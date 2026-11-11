from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfspolygonAttributes")


@_attrs_define
class WfsMapServerWfspolygonAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        publication_date (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        project_title (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        type_of_government_notice (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        government_notice (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        related_gazette_plan_note (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        type_ (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        feature_id (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    publication_date: None | str | Unset = UNSET
    project_title: None | str | Unset = UNSET
    type_of_government_notice: None | str | Unset = UNSET
    government_notice: None | str | Unset = UNSET
    related_gazette_plan_note: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    feature_id: int | None | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        publication_date: None | str | Unset
        if isinstance(self.publication_date, Unset):
            publication_date = UNSET
        else:
            publication_date = self.publication_date

        project_title: None | str | Unset
        if isinstance(self.project_title, Unset):
            project_title = UNSET
        else:
            project_title = self.project_title

        type_of_government_notice: None | str | Unset
        if isinstance(self.type_of_government_notice, Unset):
            type_of_government_notice = UNSET
        else:
            type_of_government_notice = self.type_of_government_notice

        government_notice: None | str | Unset
        if isinstance(self.government_notice, Unset):
            government_notice = UNSET
        else:
            government_notice = self.government_notice

        related_gazette_plan_note: None | str | Unset
        if isinstance(self.related_gazette_plan_note, Unset):
            related_gazette_plan_note = UNSET
        else:
            related_gazette_plan_note = self.related_gazette_plan_note

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        feature_id: int | None | Unset
        if isinstance(self.feature_id, Unset):
            feature_id = UNSET
        else:
            feature_id = self.feature_id

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
            field_dict["SHAPE"] = shape
        if publication_date is not UNSET:
            field_dict["Publication_Date"] = publication_date
        if project_title is not UNSET:
            field_dict["Project_Title"] = project_title
        if type_of_government_notice is not UNSET:
            field_dict["Type_of_Government_Notice"] = type_of_government_notice
        if government_notice is not UNSET:
            field_dict["Government_Notice"] = government_notice
        if related_gazette_plan_note is not UNSET:
            field_dict["Related_Gazette_Plan__Note_"] = related_gazette_plan_note
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if feature_id is not UNSET:
            field_dict["FeatureID"] = feature_id
        if shape_length is not UNSET:
            field_dict["SHAPE_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["SHAPE_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        def _parse_publication_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publication_date = _parse_publication_date(d.pop("Publication_Date", UNSET))

        def _parse_project_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_title = _parse_project_title(d.pop("Project_Title", UNSET))

        def _parse_type_of_government_notice(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_government_notice = _parse_type_of_government_notice(
            d.pop("Type_of_Government_Notice", UNSET)
        )

        def _parse_government_notice(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        government_notice = _parse_government_notice(d.pop("Government_Notice", UNSET))

        def _parse_related_gazette_plan_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        related_gazette_plan_note = _parse_related_gazette_plan_note(
            d.pop("Related_Gazette_Plan__Note_", UNSET)
        )

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("Type", UNSET))

        def _parse_feature_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        feature_id = _parse_feature_id(d.pop("FeatureID", UNSET))

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

        wfs_map_server_wfspolygon_attributes = cls(
            objectid=objectid,
            shape=shape,
            publication_date=publication_date,
            project_title=project_title,
            type_of_government_notice=type_of_government_notice,
            government_notice=government_notice,
            related_gazette_plan_note=related_gazette_plan_note,
            type_=type_,
            feature_id=feature_id,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfspolygon_attributes.additional_properties = d
        return wfs_map_server_wfspolygon_attributes

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
