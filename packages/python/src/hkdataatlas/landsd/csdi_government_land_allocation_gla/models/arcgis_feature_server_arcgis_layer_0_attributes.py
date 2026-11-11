from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
        glaid (int | Unset): Publisher field type: esriFieldTypeInteger
        gla_code (int | Unset): Publisher field type: esriFieldTypeSmallInteger
        gla_number (int | Unset): Publisher field type: esriFieldTypeInteger
        gla_number_alpha (None | str | Unset): Publisher field type: esriFieldTypeString
        section_code (None | str | Unset): Publisher field type: esriFieldTypeString
        gla_display_name (str | Unset): Publisher field type: esriFieldTypeString
        gla_type (str | Unset): Publisher field type: esriFieldTypeString
        lbs_info (str | Unset): Publisher field type: esriFieldTypeString
        user_type (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    glaid: int | Unset = UNSET
    gla_code: int | Unset = UNSET
    gla_number: int | Unset = UNSET
    gla_number_alpha: None | str | Unset = UNSET
    section_code: None | str | Unset = UNSET
    gla_display_name: str | Unset = UNSET
    gla_type: str | Unset = UNSET
    lbs_info: str | Unset = UNSET
    user_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

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

        glaid = self.glaid

        gla_code = self.gla_code

        gla_number = self.gla_number

        gla_number_alpha: None | str | Unset
        if isinstance(self.gla_number_alpha, Unset):
            gla_number_alpha = UNSET
        else:
            gla_number_alpha = self.gla_number_alpha

        section_code: None | str | Unset
        if isinstance(self.section_code, Unset):
            section_code = UNSET
        else:
            section_code = self.section_code

        gla_display_name = self.gla_display_name

        gla_type = self.gla_type

        lbs_info = self.lbs_info

        user_type: None | str | Unset
        if isinstance(self.user_type, Unset):
            user_type = UNSET
        else:
            user_type = self.user_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area
        if glaid is not UNSET:
            field_dict["GLAID"] = glaid
        if gla_code is not UNSET:
            field_dict["GLACode"] = gla_code
        if gla_number is not UNSET:
            field_dict["GLANumber"] = gla_number
        if gla_number_alpha is not UNSET:
            field_dict["GLANumberAlpha"] = gla_number_alpha
        if section_code is not UNSET:
            field_dict["SectionCode"] = section_code
        if gla_display_name is not UNSET:
            field_dict["GLADisplayName"] = gla_display_name
        if gla_type is not UNSET:
            field_dict["GLAType"] = gla_type
        if lbs_info is not UNSET:
            field_dict["LBSInfo"] = lbs_info
        if user_type is not UNSET:
            field_dict["UserType"] = user_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape__Area", UNSET))

        glaid = d.pop("GLAID", UNSET)

        gla_code = d.pop("GLACode", UNSET)

        gla_number = d.pop("GLANumber", UNSET)

        def _parse_gla_number_alpha(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gla_number_alpha = _parse_gla_number_alpha(d.pop("GLANumberAlpha", UNSET))

        def _parse_section_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        section_code = _parse_section_code(d.pop("SectionCode", UNSET))

        gla_display_name = d.pop("GLADisplayName", UNSET)

        gla_type = d.pop("GLAType", UNSET)

        lbs_info = d.pop("LBSInfo", UNSET)

        def _parse_user_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_type = _parse_user_type(d.pop("UserType", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            shape_length=shape_length,
            shape_area=shape_area,
            glaid=glaid,
            gla_code=gla_code,
            gla_number=gla_number,
            gla_number_alpha=gla_number_alpha,
            section_code=section_code,
            gla_display_name=gla_display_name,
            gla_type=gla_type,
            lbs_info=lbs_info,
            user_type=user_type,
        )

        arcgis_feature_server_arcgis_layer_0_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_0_attributes

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
