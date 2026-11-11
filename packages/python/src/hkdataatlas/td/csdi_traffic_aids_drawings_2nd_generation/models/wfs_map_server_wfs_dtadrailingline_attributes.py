from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsDTADRAILINGLINEAttributes")


@_attrs_define
class WfsMapServerWfsDTADRAILINGLINEAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiCurvePropertyType; JSON geometry is not inferred from its
            XML type.
        color (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML occurrence into
            all JSON queries.
        featureid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        completion_date (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML
            occurrence into all JSON queries.
        gazette_date (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML
            occurrence into all JSON queries.
        last_upd_date (str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML occurrence
            into all JSON queries.
        elevation (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        linetype (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        position_1 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        position_2 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        position_3 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        position_4 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        position_5 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        symbol_size_1 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        symbol_size_2 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        symbol_size_3 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        symbol_size_4 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        symbol_size_5 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        symbol_step_1 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        symbol_step_2 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        symbol_step_3 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        symbol_step_4 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        symbol_step_5 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        line_pattern_1 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        line_pattern_2 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        line_pattern_3 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        line_pattern_4 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        line_pattern_5 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        line_width_1 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        line_width_2 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        line_width_3 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        line_width_4 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        line_width_5 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        line_offset_1 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        line_offset_2 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        line_offset_3 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        line_offset_4 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        line_offset_5 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        ruleid (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        ruleid_1 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    color: int | None | Unset = UNSET
    featureid: int | Unset = UNSET
    completion_date: None | str | Unset = UNSET
    gazette_date: None | str | Unset = UNSET
    last_upd_date: str | Unset = UNSET
    elevation: None | str | Unset = UNSET
    linetype: None | str | Unset = UNSET
    position_1: float | None | Unset = UNSET
    position_2: float | None | Unset = UNSET
    position_3: float | None | Unset = UNSET
    position_4: float | None | Unset = UNSET
    position_5: float | None | Unset = UNSET
    symbol_size_1: float | None | Unset = UNSET
    symbol_size_2: float | None | Unset = UNSET
    symbol_size_3: float | None | Unset = UNSET
    symbol_size_4: float | None | Unset = UNSET
    symbol_size_5: float | None | Unset = UNSET
    symbol_step_1: None | str | Unset = UNSET
    symbol_step_2: None | str | Unset = UNSET
    symbol_step_3: None | str | Unset = UNSET
    symbol_step_4: None | str | Unset = UNSET
    symbol_step_5: None | str | Unset = UNSET
    line_pattern_1: None | str | Unset = UNSET
    line_pattern_2: None | str | Unset = UNSET
    line_pattern_3: None | str | Unset = UNSET
    line_pattern_4: None | str | Unset = UNSET
    line_pattern_5: None | str | Unset = UNSET
    line_width_1: float | None | Unset = UNSET
    line_width_2: float | None | Unset = UNSET
    line_width_3: float | None | Unset = UNSET
    line_width_4: float | None | Unset = UNSET
    line_width_5: float | None | Unset = UNSET
    line_offset_1: float | None | Unset = UNSET
    line_offset_2: float | None | Unset = UNSET
    line_offset_3: float | None | Unset = UNSET
    line_offset_4: float | None | Unset = UNSET
    line_offset_5: float | None | Unset = UNSET
    ruleid: int | None | Unset = UNSET
    ruleid_1: int | None | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        color: int | None | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        featureid = self.featureid

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

        last_upd_date = self.last_upd_date

        elevation: None | str | Unset
        if isinstance(self.elevation, Unset):
            elevation = UNSET
        else:
            elevation = self.elevation

        linetype: None | str | Unset
        if isinstance(self.linetype, Unset):
            linetype = UNSET
        else:
            linetype = self.linetype

        position_1: float | None | Unset
        if isinstance(self.position_1, Unset):
            position_1 = UNSET
        else:
            position_1 = self.position_1

        position_2: float | None | Unset
        if isinstance(self.position_2, Unset):
            position_2 = UNSET
        else:
            position_2 = self.position_2

        position_3: float | None | Unset
        if isinstance(self.position_3, Unset):
            position_3 = UNSET
        else:
            position_3 = self.position_3

        position_4: float | None | Unset
        if isinstance(self.position_4, Unset):
            position_4 = UNSET
        else:
            position_4 = self.position_4

        position_5: float | None | Unset
        if isinstance(self.position_5, Unset):
            position_5 = UNSET
        else:
            position_5 = self.position_5

        symbol_size_1: float | None | Unset
        if isinstance(self.symbol_size_1, Unset):
            symbol_size_1 = UNSET
        else:
            symbol_size_1 = self.symbol_size_1

        symbol_size_2: float | None | Unset
        if isinstance(self.symbol_size_2, Unset):
            symbol_size_2 = UNSET
        else:
            symbol_size_2 = self.symbol_size_2

        symbol_size_3: float | None | Unset
        if isinstance(self.symbol_size_3, Unset):
            symbol_size_3 = UNSET
        else:
            symbol_size_3 = self.symbol_size_3

        symbol_size_4: float | None | Unset
        if isinstance(self.symbol_size_4, Unset):
            symbol_size_4 = UNSET
        else:
            symbol_size_4 = self.symbol_size_4

        symbol_size_5: float | None | Unset
        if isinstance(self.symbol_size_5, Unset):
            symbol_size_5 = UNSET
        else:
            symbol_size_5 = self.symbol_size_5

        symbol_step_1: None | str | Unset
        if isinstance(self.symbol_step_1, Unset):
            symbol_step_1 = UNSET
        else:
            symbol_step_1 = self.symbol_step_1

        symbol_step_2: None | str | Unset
        if isinstance(self.symbol_step_2, Unset):
            symbol_step_2 = UNSET
        else:
            symbol_step_2 = self.symbol_step_2

        symbol_step_3: None | str | Unset
        if isinstance(self.symbol_step_3, Unset):
            symbol_step_3 = UNSET
        else:
            symbol_step_3 = self.symbol_step_3

        symbol_step_4: None | str | Unset
        if isinstance(self.symbol_step_4, Unset):
            symbol_step_4 = UNSET
        else:
            symbol_step_4 = self.symbol_step_4

        symbol_step_5: None | str | Unset
        if isinstance(self.symbol_step_5, Unset):
            symbol_step_5 = UNSET
        else:
            symbol_step_5 = self.symbol_step_5

        line_pattern_1: None | str | Unset
        if isinstance(self.line_pattern_1, Unset):
            line_pattern_1 = UNSET
        else:
            line_pattern_1 = self.line_pattern_1

        line_pattern_2: None | str | Unset
        if isinstance(self.line_pattern_2, Unset):
            line_pattern_2 = UNSET
        else:
            line_pattern_2 = self.line_pattern_2

        line_pattern_3: None | str | Unset
        if isinstance(self.line_pattern_3, Unset):
            line_pattern_3 = UNSET
        else:
            line_pattern_3 = self.line_pattern_3

        line_pattern_4: None | str | Unset
        if isinstance(self.line_pattern_4, Unset):
            line_pattern_4 = UNSET
        else:
            line_pattern_4 = self.line_pattern_4

        line_pattern_5: None | str | Unset
        if isinstance(self.line_pattern_5, Unset):
            line_pattern_5 = UNSET
        else:
            line_pattern_5 = self.line_pattern_5

        line_width_1: float | None | Unset
        if isinstance(self.line_width_1, Unset):
            line_width_1 = UNSET
        else:
            line_width_1 = self.line_width_1

        line_width_2: float | None | Unset
        if isinstance(self.line_width_2, Unset):
            line_width_2 = UNSET
        else:
            line_width_2 = self.line_width_2

        line_width_3: float | None | Unset
        if isinstance(self.line_width_3, Unset):
            line_width_3 = UNSET
        else:
            line_width_3 = self.line_width_3

        line_width_4: float | None | Unset
        if isinstance(self.line_width_4, Unset):
            line_width_4 = UNSET
        else:
            line_width_4 = self.line_width_4

        line_width_5: float | None | Unset
        if isinstance(self.line_width_5, Unset):
            line_width_5 = UNSET
        else:
            line_width_5 = self.line_width_5

        line_offset_1: float | None | Unset
        if isinstance(self.line_offset_1, Unset):
            line_offset_1 = UNSET
        else:
            line_offset_1 = self.line_offset_1

        line_offset_2: float | None | Unset
        if isinstance(self.line_offset_2, Unset):
            line_offset_2 = UNSET
        else:
            line_offset_2 = self.line_offset_2

        line_offset_3: float | None | Unset
        if isinstance(self.line_offset_3, Unset):
            line_offset_3 = UNSET
        else:
            line_offset_3 = self.line_offset_3

        line_offset_4: float | None | Unset
        if isinstance(self.line_offset_4, Unset):
            line_offset_4 = UNSET
        else:
            line_offset_4 = self.line_offset_4

        line_offset_5: float | None | Unset
        if isinstance(self.line_offset_5, Unset):
            line_offset_5 = UNSET
        else:
            line_offset_5 = self.line_offset_5

        ruleid: int | None | Unset
        if isinstance(self.ruleid, Unset):
            ruleid = UNSET
        else:
            ruleid = self.ruleid

        ruleid_1: int | None | Unset
        if isinstance(self.ruleid_1, Unset):
            ruleid_1 = UNSET
        else:
            ruleid_1 = self.ruleid_1

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if color is not UNSET:
            field_dict["COLOR"] = color
        if featureid is not UNSET:
            field_dict["FEATUREID"] = featureid
        if completion_date is not UNSET:
            field_dict["COMPLETION_DATE"] = completion_date
        if gazette_date is not UNSET:
            field_dict["GAZETTE_DATE"] = gazette_date
        if last_upd_date is not UNSET:
            field_dict["LAST_UPD_DATE"] = last_upd_date
        if elevation is not UNSET:
            field_dict["ELEVATION"] = elevation
        if linetype is not UNSET:
            field_dict["LINETYPE"] = linetype
        if position_1 is not UNSET:
            field_dict["POSITION_1"] = position_1
        if position_2 is not UNSET:
            field_dict["POSITION_2"] = position_2
        if position_3 is not UNSET:
            field_dict["POSITION_3"] = position_3
        if position_4 is not UNSET:
            field_dict["POSITION_4"] = position_4
        if position_5 is not UNSET:
            field_dict["POSITION_5"] = position_5
        if symbol_size_1 is not UNSET:
            field_dict["SYMBOL_SIZE_1"] = symbol_size_1
        if symbol_size_2 is not UNSET:
            field_dict["SYMBOL_SIZE_2"] = symbol_size_2
        if symbol_size_3 is not UNSET:
            field_dict["SYMBOL_SIZE_3"] = symbol_size_3
        if symbol_size_4 is not UNSET:
            field_dict["SYMBOL_SIZE_4"] = symbol_size_4
        if symbol_size_5 is not UNSET:
            field_dict["SYMBOL_SIZE_5"] = symbol_size_5
        if symbol_step_1 is not UNSET:
            field_dict["SYMBOL_STEP_1"] = symbol_step_1
        if symbol_step_2 is not UNSET:
            field_dict["SYMBOL_STEP_2"] = symbol_step_2
        if symbol_step_3 is not UNSET:
            field_dict["SYMBOL_STEP_3"] = symbol_step_3
        if symbol_step_4 is not UNSET:
            field_dict["SYMBOL_STEP_4"] = symbol_step_4
        if symbol_step_5 is not UNSET:
            field_dict["SYMBOL_STEP_5"] = symbol_step_5
        if line_pattern_1 is not UNSET:
            field_dict["LINE_PATTERN_1"] = line_pattern_1
        if line_pattern_2 is not UNSET:
            field_dict["LINE_PATTERN_2"] = line_pattern_2
        if line_pattern_3 is not UNSET:
            field_dict["LINE_PATTERN_3"] = line_pattern_3
        if line_pattern_4 is not UNSET:
            field_dict["LINE_PATTERN_4"] = line_pattern_4
        if line_pattern_5 is not UNSET:
            field_dict["LINE_PATTERN_5"] = line_pattern_5
        if line_width_1 is not UNSET:
            field_dict["LINE_WIDTH_1"] = line_width_1
        if line_width_2 is not UNSET:
            field_dict["LINE_WIDTH_2"] = line_width_2
        if line_width_3 is not UNSET:
            field_dict["LINE_WIDTH_3"] = line_width_3
        if line_width_4 is not UNSET:
            field_dict["LINE_WIDTH_4"] = line_width_4
        if line_width_5 is not UNSET:
            field_dict["LINE_WIDTH_5"] = line_width_5
        if line_offset_1 is not UNSET:
            field_dict["LINE_OFFSET_1"] = line_offset_1
        if line_offset_2 is not UNSET:
            field_dict["LINE_OFFSET_2"] = line_offset_2
        if line_offset_3 is not UNSET:
            field_dict["LINE_OFFSET_3"] = line_offset_3
        if line_offset_4 is not UNSET:
            field_dict["LINE_OFFSET_4"] = line_offset_4
        if line_offset_5 is not UNSET:
            field_dict["LINE_OFFSET_5"] = line_offset_5
        if ruleid is not UNSET:
            field_dict["RULEID"] = ruleid
        if ruleid_1 is not UNSET:
            field_dict["RULEID_1"] = ruleid_1
        if shape_length is not UNSET:
            field_dict["SHAPE_Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        def _parse_color(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        color = _parse_color(d.pop("COLOR", UNSET))

        featureid = d.pop("FEATUREID", UNSET)

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

        last_upd_date = d.pop("LAST_UPD_DATE", UNSET)

        def _parse_elevation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        elevation = _parse_elevation(d.pop("ELEVATION", UNSET))

        def _parse_linetype(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linetype = _parse_linetype(d.pop("LINETYPE", UNSET))

        def _parse_position_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        position_1 = _parse_position_1(d.pop("POSITION_1", UNSET))

        def _parse_position_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        position_2 = _parse_position_2(d.pop("POSITION_2", UNSET))

        def _parse_position_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        position_3 = _parse_position_3(d.pop("POSITION_3", UNSET))

        def _parse_position_4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        position_4 = _parse_position_4(d.pop("POSITION_4", UNSET))

        def _parse_position_5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        position_5 = _parse_position_5(d.pop("POSITION_5", UNSET))

        def _parse_symbol_size_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        symbol_size_1 = _parse_symbol_size_1(d.pop("SYMBOL_SIZE_1", UNSET))

        def _parse_symbol_size_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        symbol_size_2 = _parse_symbol_size_2(d.pop("SYMBOL_SIZE_2", UNSET))

        def _parse_symbol_size_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        symbol_size_3 = _parse_symbol_size_3(d.pop("SYMBOL_SIZE_3", UNSET))

        def _parse_symbol_size_4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        symbol_size_4 = _parse_symbol_size_4(d.pop("SYMBOL_SIZE_4", UNSET))

        def _parse_symbol_size_5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        symbol_size_5 = _parse_symbol_size_5(d.pop("SYMBOL_SIZE_5", UNSET))

        def _parse_symbol_step_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol_step_1 = _parse_symbol_step_1(d.pop("SYMBOL_STEP_1", UNSET))

        def _parse_symbol_step_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol_step_2 = _parse_symbol_step_2(d.pop("SYMBOL_STEP_2", UNSET))

        def _parse_symbol_step_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol_step_3 = _parse_symbol_step_3(d.pop("SYMBOL_STEP_3", UNSET))

        def _parse_symbol_step_4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol_step_4 = _parse_symbol_step_4(d.pop("SYMBOL_STEP_4", UNSET))

        def _parse_symbol_step_5(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol_step_5 = _parse_symbol_step_5(d.pop("SYMBOL_STEP_5", UNSET))

        def _parse_line_pattern_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        line_pattern_1 = _parse_line_pattern_1(d.pop("LINE_PATTERN_1", UNSET))

        def _parse_line_pattern_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        line_pattern_2 = _parse_line_pattern_2(d.pop("LINE_PATTERN_2", UNSET))

        def _parse_line_pattern_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        line_pattern_3 = _parse_line_pattern_3(d.pop("LINE_PATTERN_3", UNSET))

        def _parse_line_pattern_4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        line_pattern_4 = _parse_line_pattern_4(d.pop("LINE_PATTERN_4", UNSET))

        def _parse_line_pattern_5(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        line_pattern_5 = _parse_line_pattern_5(d.pop("LINE_PATTERN_5", UNSET))

        def _parse_line_width_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        line_width_1 = _parse_line_width_1(d.pop("LINE_WIDTH_1", UNSET))

        def _parse_line_width_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        line_width_2 = _parse_line_width_2(d.pop("LINE_WIDTH_2", UNSET))

        def _parse_line_width_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        line_width_3 = _parse_line_width_3(d.pop("LINE_WIDTH_3", UNSET))

        def _parse_line_width_4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        line_width_4 = _parse_line_width_4(d.pop("LINE_WIDTH_4", UNSET))

        def _parse_line_width_5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        line_width_5 = _parse_line_width_5(d.pop("LINE_WIDTH_5", UNSET))

        def _parse_line_offset_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        line_offset_1 = _parse_line_offset_1(d.pop("LINE_OFFSET_1", UNSET))

        def _parse_line_offset_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        line_offset_2 = _parse_line_offset_2(d.pop("LINE_OFFSET_2", UNSET))

        def _parse_line_offset_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        line_offset_3 = _parse_line_offset_3(d.pop("LINE_OFFSET_3", UNSET))

        def _parse_line_offset_4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        line_offset_4 = _parse_line_offset_4(d.pop("LINE_OFFSET_4", UNSET))

        def _parse_line_offset_5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        line_offset_5 = _parse_line_offset_5(d.pop("LINE_OFFSET_5", UNSET))

        def _parse_ruleid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ruleid = _parse_ruleid(d.pop("RULEID", UNSET))

        def _parse_ruleid_1(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ruleid_1 = _parse_ruleid_1(d.pop("RULEID_1", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("SHAPE_Length", UNSET))

        wfs_map_server_wfs_dtadrailingline_attributes = cls(
            objectid=objectid,
            shape=shape,
            color=color,
            featureid=featureid,
            completion_date=completion_date,
            gazette_date=gazette_date,
            last_upd_date=last_upd_date,
            elevation=elevation,
            linetype=linetype,
            position_1=position_1,
            position_2=position_2,
            position_3=position_3,
            position_4=position_4,
            position_5=position_5,
            symbol_size_1=symbol_size_1,
            symbol_size_2=symbol_size_2,
            symbol_size_3=symbol_size_3,
            symbol_size_4=symbol_size_4,
            symbol_size_5=symbol_size_5,
            symbol_step_1=symbol_step_1,
            symbol_step_2=symbol_step_2,
            symbol_step_3=symbol_step_3,
            symbol_step_4=symbol_step_4,
            symbol_step_5=symbol_step_5,
            line_pattern_1=line_pattern_1,
            line_pattern_2=line_pattern_2,
            line_pattern_3=line_pattern_3,
            line_pattern_4=line_pattern_4,
            line_pattern_5=line_pattern_5,
            line_width_1=line_width_1,
            line_width_2=line_width_2,
            line_width_3=line_width_3,
            line_width_4=line_width_4,
            line_width_5=line_width_5,
            line_offset_1=line_offset_1,
            line_offset_2=line_offset_2,
            line_offset_3=line_offset_3,
            line_offset_4=line_offset_4,
            line_offset_5=line_offset_5,
            ruleid=ruleid,
            ruleid_1=ruleid_1,
            shape_length=shape_length,
        )

        wfs_map_server_wfs_dtadrailingline_attributes.additional_properties = d
        return wfs_map_server_wfs_dtadrailingline_attributes

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
