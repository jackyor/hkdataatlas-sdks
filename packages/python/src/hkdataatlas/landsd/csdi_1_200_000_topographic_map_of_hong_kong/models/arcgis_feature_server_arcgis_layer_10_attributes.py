from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer10Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer10Attributes:
    """
    Attributes:
        annosymid (float | None | Unset): Publisher field type: esriFieldTypeDouble
        angle (float | None | Unset): Publisher field type: esriFieldTypeDouble
        annotation_class_id (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        bold (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        class_ (None | str | Unset): Publisher field type: esriFieldTypeString
        character_spacing (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        character_width (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        flip_angle (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        font_leading (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        font_name (None | str | Unset): Publisher field type: esriFieldTypeString
        font_size (float | None | Unset): Publisher field type: esriFieldTypeDouble
        italic (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        lastupdatedate (float | None | Unset): Publisher field type: esriFieldTypeDouble
        subcat (None | str | Unset): Publisher field type: esriFieldTypeString
        status (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        type_ (None | str | Unset): Publisher field type: esriFieldTypeString
        text_string (int | None | Unset): Publisher field type: esriFieldTypeInteger
        underline (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        word_spacing (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    annosymid: float | None | Unset = UNSET
    angle: float | None | Unset = UNSET
    annotation_class_id: int | None | Unset = UNSET
    bold: int | None | Unset = UNSET
    class_: None | str | Unset = UNSET
    character_spacing: int | None | Unset = UNSET
    character_width: int | None | Unset = UNSET
    flip_angle: int | None | Unset = UNSET
    font_leading: int | None | Unset = UNSET
    font_name: None | str | Unset = UNSET
    font_size: float | None | Unset = UNSET
    italic: int | None | Unset = UNSET
    lastupdatedate: float | None | Unset = UNSET
    subcat: None | str | Unset = UNSET
    status: int | None | Unset = UNSET
    type_: None | str | Unset = UNSET
    text_string: int | None | Unset = UNSET
    underline: int | None | Unset = UNSET
    word_spacing: int | None | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annosymid: float | None | Unset
        if isinstance(self.annosymid, Unset):
            annosymid = UNSET
        else:
            annosymid = self.annosymid

        angle: float | None | Unset
        if isinstance(self.angle, Unset):
            angle = UNSET
        else:
            angle = self.angle

        annotation_class_id: int | None | Unset
        if isinstance(self.annotation_class_id, Unset):
            annotation_class_id = UNSET
        else:
            annotation_class_id = self.annotation_class_id

        bold: int | None | Unset
        if isinstance(self.bold, Unset):
            bold = UNSET
        else:
            bold = self.bold

        class_: None | str | Unset
        if isinstance(self.class_, Unset):
            class_ = UNSET
        else:
            class_ = self.class_

        character_spacing: int | None | Unset
        if isinstance(self.character_spacing, Unset):
            character_spacing = UNSET
        else:
            character_spacing = self.character_spacing

        character_width: int | None | Unset
        if isinstance(self.character_width, Unset):
            character_width = UNSET
        else:
            character_width = self.character_width

        flip_angle: int | None | Unset
        if isinstance(self.flip_angle, Unset):
            flip_angle = UNSET
        else:
            flip_angle = self.flip_angle

        font_leading: int | None | Unset
        if isinstance(self.font_leading, Unset):
            font_leading = UNSET
        else:
            font_leading = self.font_leading

        font_name: None | str | Unset
        if isinstance(self.font_name, Unset):
            font_name = UNSET
        else:
            font_name = self.font_name

        font_size: float | None | Unset
        if isinstance(self.font_size, Unset):
            font_size = UNSET
        else:
            font_size = self.font_size

        italic: int | None | Unset
        if isinstance(self.italic, Unset):
            italic = UNSET
        else:
            italic = self.italic

        lastupdatedate: float | None | Unset
        if isinstance(self.lastupdatedate, Unset):
            lastupdatedate = UNSET
        else:
            lastupdatedate = self.lastupdatedate

        subcat: None | str | Unset
        if isinstance(self.subcat, Unset):
            subcat = UNSET
        else:
            subcat = self.subcat

        status: int | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        text_string: int | None | Unset
        if isinstance(self.text_string, Unset):
            text_string = UNSET
        else:
            text_string = self.text_string

        underline: int | None | Unset
        if isinstance(self.underline, Unset):
            underline = UNSET
        else:
            underline = self.underline

        word_spacing: int | None | Unset
        if isinstance(self.word_spacing, Unset):
            word_spacing = UNSET
        else:
            word_spacing = self.word_spacing

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annosymid is not UNSET:
            field_dict["ANNOSYMID"] = annosymid
        if angle is not UNSET:
            field_dict["Angle"] = angle
        if annotation_class_id is not UNSET:
            field_dict["AnnotationClassID"] = annotation_class_id
        if bold is not UNSET:
            field_dict["Bold"] = bold
        if class_ is not UNSET:
            field_dict["CLASS"] = class_
        if character_spacing is not UNSET:
            field_dict["CharacterSpacing"] = character_spacing
        if character_width is not UNSET:
            field_dict["CharacterWidth"] = character_width
        if flip_angle is not UNSET:
            field_dict["FlipAngle"] = flip_angle
        if font_leading is not UNSET:
            field_dict["FontLeading"] = font_leading
        if font_name is not UNSET:
            field_dict["FontName"] = font_name
        if font_size is not UNSET:
            field_dict["FontSize"] = font_size
        if italic is not UNSET:
            field_dict["Italic"] = italic
        if lastupdatedate is not UNSET:
            field_dict["LASTUPDATEDATE"] = lastupdatedate
        if subcat is not UNSET:
            field_dict["SUBCAT"] = subcat
        if status is not UNSET:
            field_dict["Status"] = status
        if type_ is not UNSET:
            field_dict["TYPE"] = type_
        if text_string is not UNSET:
            field_dict["TextString"] = text_string
        if underline is not UNSET:
            field_dict["Underline"] = underline
        if word_spacing is not UNSET:
            field_dict["WordSpacing"] = word_spacing
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_annosymid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        annosymid = _parse_annosymid(d.pop("ANNOSYMID", UNSET))

        def _parse_angle(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        angle = _parse_angle(d.pop("Angle", UNSET))

        def _parse_annotation_class_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        annotation_class_id = _parse_annotation_class_id(
            d.pop("AnnotationClassID", UNSET)
        )

        def _parse_bold(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bold = _parse_bold(d.pop("Bold", UNSET))

        def _parse_class_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_ = _parse_class_(d.pop("CLASS", UNSET))

        def _parse_character_spacing(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        character_spacing = _parse_character_spacing(d.pop("CharacterSpacing", UNSET))

        def _parse_character_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        character_width = _parse_character_width(d.pop("CharacterWidth", UNSET))

        def _parse_flip_angle(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        flip_angle = _parse_flip_angle(d.pop("FlipAngle", UNSET))

        def _parse_font_leading(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        font_leading = _parse_font_leading(d.pop("FontLeading", UNSET))

        def _parse_font_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        font_name = _parse_font_name(d.pop("FontName", UNSET))

        def _parse_font_size(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        font_size = _parse_font_size(d.pop("FontSize", UNSET))

        def _parse_italic(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        italic = _parse_italic(d.pop("Italic", UNSET))

        def _parse_lastupdatedate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lastupdatedate = _parse_lastupdatedate(d.pop("LASTUPDATEDATE", UNSET))

        def _parse_subcat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subcat = _parse_subcat(d.pop("SUBCAT", UNSET))

        def _parse_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        status = _parse_status(d.pop("Status", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("TYPE", UNSET))

        def _parse_text_string(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        text_string = _parse_text_string(d.pop("TextString", UNSET))

        def _parse_underline(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        underline = _parse_underline(d.pop("Underline", UNSET))

        def _parse_word_spacing(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        word_spacing = _parse_word_spacing(d.pop("WordSpacing", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_10_attributes = cls(
            annosymid=annosymid,
            angle=angle,
            annotation_class_id=annotation_class_id,
            bold=bold,
            class_=class_,
            character_spacing=character_spacing,
            character_width=character_width,
            flip_angle=flip_angle,
            font_leading=font_leading,
            font_name=font_name,
            font_size=font_size,
            italic=italic,
            lastupdatedate=lastupdatedate,
            subcat=subcat,
            status=status,
            type_=type_,
            text_string=text_string,
            underline=underline,
            word_spacing=word_spacing,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_10_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_10_attributes

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
