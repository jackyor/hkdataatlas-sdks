from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsDC21CSDUAttributes")


@_attrs_define
class WfsMapServerWfsDC21CSDUAttributes:
    """
    Attributes:
        dc (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        dc_chi (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dc_class (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dc_eng (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        sdu_dh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        sdu_n (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        sdu_oq (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        sdu_pop (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    dc: float | None | Unset = UNSET
    dc_chi: None | str | Unset = UNSET
    dc_class: None | str | Unset = UNSET
    dc_eng: None | str | Unset = UNSET
    sdu_dh: float | None | Unset = UNSET
    sdu_n: float | None | Unset = UNSET
    sdu_oq: float | None | Unset = UNSET
    sdu_pop: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dc: float | None | Unset
        if isinstance(self.dc, Unset):
            dc = UNSET
        else:
            dc = self.dc

        dc_chi: None | str | Unset
        if isinstance(self.dc_chi, Unset):
            dc_chi = UNSET
        else:
            dc_chi = self.dc_chi

        dc_class: None | str | Unset
        if isinstance(self.dc_class, Unset):
            dc_class = UNSET
        else:
            dc_class = self.dc_class

        dc_eng: None | str | Unset
        if isinstance(self.dc_eng, Unset):
            dc_eng = UNSET
        else:
            dc_eng = self.dc_eng

        sdu_dh: float | None | Unset
        if isinstance(self.sdu_dh, Unset):
            sdu_dh = UNSET
        else:
            sdu_dh = self.sdu_dh

        sdu_n: float | None | Unset
        if isinstance(self.sdu_n, Unset):
            sdu_n = UNSET
        else:
            sdu_n = self.sdu_n

        sdu_oq: float | None | Unset
        if isinstance(self.sdu_oq, Unset):
            sdu_oq = UNSET
        else:
            sdu_oq = self.sdu_oq

        sdu_pop: float | None | Unset
        if isinstance(self.sdu_pop, Unset):
            sdu_pop = UNSET
        else:
            sdu_pop = self.sdu_pop

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
        if dc is not UNSET:
            field_dict["dc"] = dc
        if dc_chi is not UNSET:
            field_dict["dc_chi"] = dc_chi
        if dc_class is not UNSET:
            field_dict["dc_class"] = dc_class
        if dc_eng is not UNSET:
            field_dict["dc_eng"] = dc_eng
        if sdu_dh is not UNSET:
            field_dict["sdu_dh"] = sdu_dh
        if sdu_n is not UNSET:
            field_dict["sdu_n"] = sdu_n
        if sdu_oq is not UNSET:
            field_dict["sdu_oq"] = sdu_oq
        if sdu_pop is not UNSET:
            field_dict["sdu_pop"] = sdu_pop
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

        def _parse_dc(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dc = _parse_dc(d.pop("dc", UNSET))

        def _parse_dc_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dc_chi = _parse_dc_chi(d.pop("dc_chi", UNSET))

        def _parse_dc_class(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dc_class = _parse_dc_class(d.pop("dc_class", UNSET))

        def _parse_dc_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dc_eng = _parse_dc_eng(d.pop("dc_eng", UNSET))

        def _parse_sdu_dh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sdu_dh = _parse_sdu_dh(d.pop("sdu_dh", UNSET))

        def _parse_sdu_n(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sdu_n = _parse_sdu_n(d.pop("sdu_n", UNSET))

        def _parse_sdu_oq(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sdu_oq = _parse_sdu_oq(d.pop("sdu_oq", UNSET))

        def _parse_sdu_pop(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sdu_pop = _parse_sdu_pop(d.pop("sdu_pop", UNSET))

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

        wfs_map_server_wfs_dc21csdu_attributes = cls(
            dc=dc,
            dc_chi=dc_chi,
            dc_class=dc_class,
            dc_eng=dc_eng,
            sdu_dh=sdu_dh,
            sdu_n=sdu_n,
            sdu_oq=sdu_oq,
            sdu_pop=sdu_pop,
            objectid=objectid,
            shape=shape,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_dc21csdu_attributes.additional_properties = d
        return wfs_map_server_wfs_dc21csdu_attributes

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
