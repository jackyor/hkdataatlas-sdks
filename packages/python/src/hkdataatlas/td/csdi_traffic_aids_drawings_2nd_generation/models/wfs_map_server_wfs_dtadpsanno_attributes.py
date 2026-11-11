from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsDTADPSANNOAttributes")


@_attrs_define
class WfsMapServerWfsDTADPSANNOAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        feature_id (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        z_order (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        annotation_class_id (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        symbol_id (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        status (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML occurrence into
            all JSON queries.
        text_string (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        font_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        font_size (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        bold (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML occurrence into all
            JSON queries.
        italic (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML occurrence into
            all JSON queries.
        underline (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML occurrence
            into all JSON queries.
        vertical_alignment (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML
            occurrence into all JSON queries.
        horizontal_alignment (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML
            occurrence into all JSON queries.
        x_offset (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        y_offset (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        angle (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        font_leading (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        word_spacing (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        character_width (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        character_spacing (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        flip_angle (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        override (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        refname (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        completion_date (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML
            occurrence into all JSON queries.
        gazette_date (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML
            occurrence into all JSON queries.
        last_upd_date (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML
            occurrence into all JSON queries.
        elevation (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        gg_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    feature_id: int | None | Unset = UNSET
    z_order: int | None | Unset = UNSET
    annotation_class_id: int | None | Unset = UNSET
    symbol_id: int | None | Unset = UNSET
    status: int | None | Unset = UNSET
    text_string: None | str | Unset = UNSET
    font_name: None | str | Unset = UNSET
    font_size: float | None | Unset = UNSET
    bold: int | None | Unset = UNSET
    italic: int | None | Unset = UNSET
    underline: int | None | Unset = UNSET
    vertical_alignment: int | None | Unset = UNSET
    horizontal_alignment: int | None | Unset = UNSET
    x_offset: float | None | Unset = UNSET
    y_offset: float | None | Unset = UNSET
    angle: float | None | Unset = UNSET
    font_leading: float | None | Unset = UNSET
    word_spacing: float | None | Unset = UNSET
    character_width: float | None | Unset = UNSET
    character_spacing: float | None | Unset = UNSET
    flip_angle: float | None | Unset = UNSET
    override: int | None | Unset = UNSET
    refname: None | str | Unset = UNSET
    completion_date: None | str | Unset = UNSET
    gazette_date: None | str | Unset = UNSET
    last_upd_date: None | str | Unset = UNSET
    elevation: None | str | Unset = UNSET
    gg_name: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        feature_id: int | None | Unset
        if isinstance(self.feature_id, Unset):
            feature_id = UNSET
        else:
            feature_id = self.feature_id

        z_order: int | None | Unset
        if isinstance(self.z_order, Unset):
            z_order = UNSET
        else:
            z_order = self.z_order

        annotation_class_id: int | None | Unset
        if isinstance(self.annotation_class_id, Unset):
            annotation_class_id = UNSET
        else:
            annotation_class_id = self.annotation_class_id

        symbol_id: int | None | Unset
        if isinstance(self.symbol_id, Unset):
            symbol_id = UNSET
        else:
            symbol_id = self.symbol_id

        status: int | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        text_string: None | str | Unset
        if isinstance(self.text_string, Unset):
            text_string = UNSET
        else:
            text_string = self.text_string

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

        bold: int | None | Unset
        if isinstance(self.bold, Unset):
            bold = UNSET
        else:
            bold = self.bold

        italic: int | None | Unset
        if isinstance(self.italic, Unset):
            italic = UNSET
        else:
            italic = self.italic

        underline: int | None | Unset
        if isinstance(self.underline, Unset):
            underline = UNSET
        else:
            underline = self.underline

        vertical_alignment: int | None | Unset
        if isinstance(self.vertical_alignment, Unset):
            vertical_alignment = UNSET
        else:
            vertical_alignment = self.vertical_alignment

        horizontal_alignment: int | None | Unset
        if isinstance(self.horizontal_alignment, Unset):
            horizontal_alignment = UNSET
        else:
            horizontal_alignment = self.horizontal_alignment

        x_offset: float | None | Unset
        if isinstance(self.x_offset, Unset):
            x_offset = UNSET
        else:
            x_offset = self.x_offset

        y_offset: float | None | Unset
        if isinstance(self.y_offset, Unset):
            y_offset = UNSET
        else:
            y_offset = self.y_offset

        angle: float | None | Unset
        if isinstance(self.angle, Unset):
            angle = UNSET
        else:
            angle = self.angle

        font_leading: float | None | Unset
        if isinstance(self.font_leading, Unset):
            font_leading = UNSET
        else:
            font_leading = self.font_leading

        word_spacing: float | None | Unset
        if isinstance(self.word_spacing, Unset):
            word_spacing = UNSET
        else:
            word_spacing = self.word_spacing

        character_width: float | None | Unset
        if isinstance(self.character_width, Unset):
            character_width = UNSET
        else:
            character_width = self.character_width

        character_spacing: float | None | Unset
        if isinstance(self.character_spacing, Unset):
            character_spacing = UNSET
        else:
            character_spacing = self.character_spacing

        flip_angle: float | None | Unset
        if isinstance(self.flip_angle, Unset):
            flip_angle = UNSET
        else:
            flip_angle = self.flip_angle

        override: int | None | Unset
        if isinstance(self.override, Unset):
            override = UNSET
        else:
            override = self.override

        refname: None | str | Unset
        if isinstance(self.refname, Unset):
            refname = UNSET
        else:
            refname = self.refname

        completion_date: None | str | Unset
        if isinstance(self.completion_date, Unset):
            completion_date = UNSET
        else:
            completion_date = self.completion_date

        gazette_date: None | str | Unset
        if isinstance(self.gazette_date, Unset):
            gazette_date = UNSET
        else:
            gazette_date = self.gazette_date

        last_upd_date: None | str | Unset
        if isinstance(self.last_upd_date, Unset):
            last_upd_date = UNSET
        else:
            last_upd_date = self.last_upd_date

        elevation: None | str | Unset
        if isinstance(self.elevation, Unset):
            elevation = UNSET
        else:
            elevation = self.elevation

        gg_name: None | str | Unset
        if isinstance(self.gg_name, Unset):
            gg_name = UNSET
        else:
            gg_name = self.gg_name

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
        if feature_id is not UNSET:
            field_dict["FeatureID"] = feature_id
        if z_order is not UNSET:
            field_dict["ZOrder"] = z_order
        if annotation_class_id is not UNSET:
            field_dict["AnnotationClassID"] = annotation_class_id
        if symbol_id is not UNSET:
            field_dict["SymbolID"] = symbol_id
        if status is not UNSET:
            field_dict["Status"] = status
        if text_string is not UNSET:
            field_dict["TextString"] = text_string
        if font_name is not UNSET:
            field_dict["FontName"] = font_name
        if font_size is not UNSET:
            field_dict["FontSize"] = font_size
        if bold is not UNSET:
            field_dict["Bold"] = bold
        if italic is not UNSET:
            field_dict["Italic"] = italic
        if underline is not UNSET:
            field_dict["Underline"] = underline
        if vertical_alignment is not UNSET:
            field_dict["VerticalAlignment"] = vertical_alignment
        if horizontal_alignment is not UNSET:
            field_dict["HorizontalAlignment"] = horizontal_alignment
        if x_offset is not UNSET:
            field_dict["XOffset"] = x_offset
        if y_offset is not UNSET:
            field_dict["YOffset"] = y_offset
        if angle is not UNSET:
            field_dict["Angle"] = angle
        if font_leading is not UNSET:
            field_dict["FontLeading"] = font_leading
        if word_spacing is not UNSET:
            field_dict["WordSpacing"] = word_spacing
        if character_width is not UNSET:
            field_dict["CharacterWidth"] = character_width
        if character_spacing is not UNSET:
            field_dict["CharacterSpacing"] = character_spacing
        if flip_angle is not UNSET:
            field_dict["FlipAngle"] = flip_angle
        if override is not UNSET:
            field_dict["Override"] = override
        if refname is not UNSET:
            field_dict["REFNAME"] = refname
        if completion_date is not UNSET:
            field_dict["COMPLETION_DATE"] = completion_date
        if gazette_date is not UNSET:
            field_dict["GAZETTE_DATE"] = gazette_date
        if last_upd_date is not UNSET:
            field_dict["LAST_UPD_DATE"] = last_upd_date
        if elevation is not UNSET:
            field_dict["ELEVATION"] = elevation
        if gg_name is not UNSET:
            field_dict["GG_NAME"] = gg_name
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

        def _parse_feature_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        feature_id = _parse_feature_id(d.pop("FeatureID", UNSET))

        def _parse_z_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        z_order = _parse_z_order(d.pop("ZOrder", UNSET))

        def _parse_annotation_class_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        annotation_class_id = _parse_annotation_class_id(
            d.pop("AnnotationClassID", UNSET)
        )

        def _parse_symbol_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        symbol_id = _parse_symbol_id(d.pop("SymbolID", UNSET))

        def _parse_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        status = _parse_status(d.pop("Status", UNSET))

        def _parse_text_string(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text_string = _parse_text_string(d.pop("TextString", UNSET))

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

        def _parse_bold(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bold = _parse_bold(d.pop("Bold", UNSET))

        def _parse_italic(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        italic = _parse_italic(d.pop("Italic", UNSET))

        def _parse_underline(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        underline = _parse_underline(d.pop("Underline", UNSET))

        def _parse_vertical_alignment(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vertical_alignment = _parse_vertical_alignment(
            d.pop("VerticalAlignment", UNSET)
        )

        def _parse_horizontal_alignment(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        horizontal_alignment = _parse_horizontal_alignment(
            d.pop("HorizontalAlignment", UNSET)
        )

        def _parse_x_offset(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        x_offset = _parse_x_offset(d.pop("XOffset", UNSET))

        def _parse_y_offset(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        y_offset = _parse_y_offset(d.pop("YOffset", UNSET))

        def _parse_angle(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        angle = _parse_angle(d.pop("Angle", UNSET))

        def _parse_font_leading(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        font_leading = _parse_font_leading(d.pop("FontLeading", UNSET))

        def _parse_word_spacing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        word_spacing = _parse_word_spacing(d.pop("WordSpacing", UNSET))

        def _parse_character_width(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        character_width = _parse_character_width(d.pop("CharacterWidth", UNSET))

        def _parse_character_spacing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        character_spacing = _parse_character_spacing(d.pop("CharacterSpacing", UNSET))

        def _parse_flip_angle(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        flip_angle = _parse_flip_angle(d.pop("FlipAngle", UNSET))

        def _parse_override(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        override = _parse_override(d.pop("Override", UNSET))

        def _parse_refname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refname = _parse_refname(d.pop("REFNAME", UNSET))

        def _parse_completion_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completion_date = _parse_completion_date(d.pop("COMPLETION_DATE", UNSET))

        def _parse_gazette_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gazette_date = _parse_gazette_date(d.pop("GAZETTE_DATE", UNSET))

        def _parse_last_upd_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_upd_date = _parse_last_upd_date(d.pop("LAST_UPD_DATE", UNSET))

        def _parse_elevation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        elevation = _parse_elevation(d.pop("ELEVATION", UNSET))

        def _parse_gg_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gg_name = _parse_gg_name(d.pop("GG_NAME", UNSET))

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

        wfs_map_server_wfs_dtadpsanno_attributes = cls(
            objectid=objectid,
            shape=shape,
            feature_id=feature_id,
            z_order=z_order,
            annotation_class_id=annotation_class_id,
            symbol_id=symbol_id,
            status=status,
            text_string=text_string,
            font_name=font_name,
            font_size=font_size,
            bold=bold,
            italic=italic,
            underline=underline,
            vertical_alignment=vertical_alignment,
            horizontal_alignment=horizontal_alignment,
            x_offset=x_offset,
            y_offset=y_offset,
            angle=angle,
            font_leading=font_leading,
            word_spacing=word_spacing,
            character_width=character_width,
            character_spacing=character_spacing,
            flip_angle=flip_angle,
            override=override,
            refname=refname,
            completion_date=completion_date,
            gazette_date=gazette_date,
            last_upd_date=last_upd_date,
            elevation=elevation,
            gg_name=gg_name,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_dtadpsanno_attributes.additional_properties = d
        return wfs_map_server_wfs_dtadpsanno_attributes

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
