from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsSSUG21CAttributes")


@_attrs_define
class WfsMapServerWfsSSUG21CAttributes:
    """
    Attributes:
        dh (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        oq (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        ssbg (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        ssbg_chi (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        ssbg_eng (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        t_pop (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    dh: None | str | Unset = UNSET
    oq: float | None | Unset = UNSET
    ssbg: None | str | Unset = UNSET
    ssbg_chi: None | str | Unset = UNSET
    ssbg_eng: None | str | Unset = UNSET
    t_pop: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dh: None | str | Unset
        if isinstance(self.dh, Unset):
            dh = UNSET
        else:
            dh = self.dh

        oq: float | None | Unset
        if isinstance(self.oq, Unset):
            oq = UNSET
        else:
            oq = self.oq

        ssbg: None | str | Unset
        if isinstance(self.ssbg, Unset):
            ssbg = UNSET
        else:
            ssbg = self.ssbg

        ssbg_chi: None | str | Unset
        if isinstance(self.ssbg_chi, Unset):
            ssbg_chi = UNSET
        else:
            ssbg_chi = self.ssbg_chi

        ssbg_eng: None | str | Unset
        if isinstance(self.ssbg_eng, Unset):
            ssbg_eng = UNSET
        else:
            ssbg_eng = self.ssbg_eng

        t_pop: float | None | Unset
        if isinstance(self.t_pop, Unset):
            t_pop = UNSET
        else:
            t_pop = self.t_pop

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
        if dh is not UNSET:
            field_dict["dh"] = dh
        if oq is not UNSET:
            field_dict["oq"] = oq
        if ssbg is not UNSET:
            field_dict["ssbg"] = ssbg
        if ssbg_chi is not UNSET:
            field_dict["ssbg_chi"] = ssbg_chi
        if ssbg_eng is not UNSET:
            field_dict["ssbg_eng"] = ssbg_eng
        if t_pop is not UNSET:
            field_dict["t_pop"] = t_pop
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

        def _parse_dh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dh = _parse_dh(d.pop("dh", UNSET))

        def _parse_oq(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        oq = _parse_oq(d.pop("oq", UNSET))

        def _parse_ssbg(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ssbg = _parse_ssbg(d.pop("ssbg", UNSET))

        def _parse_ssbg_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ssbg_chi = _parse_ssbg_chi(d.pop("ssbg_chi", UNSET))

        def _parse_ssbg_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ssbg_eng = _parse_ssbg_eng(d.pop("ssbg_eng", UNSET))

        def _parse_t_pop(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        t_pop = _parse_t_pop(d.pop("t_pop", UNSET))

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

        wfs_map_server_wfs_ssug21c_attributes = cls(
            dh=dh,
            oq=oq,
            ssbg=ssbg,
            ssbg_chi=ssbg_chi,
            ssbg_eng=ssbg_eng,
            t_pop=t_pop,
            objectid=objectid,
            shape=shape,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_ssug21c_attributes.additional_properties = d
        return wfs_map_server_wfs_ssug21c_attributes

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
