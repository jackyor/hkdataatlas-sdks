from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTPUAttributes")


@_attrs_define
class WfsMapServerWfsTPUAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        csdi_tpu_id (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        tpu_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        spu_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        ppu_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        data_owner (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        begin_lifespan (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    csdi_tpu_id: int | None | Unset = UNSET
    tpu_number: None | str | Unset = UNSET
    spu_number: None | str | Unset = UNSET
    ppu_number: None | str | Unset = UNSET
    data_owner: None | str | Unset = UNSET
    begin_lifespan: int | None | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        csdi_tpu_id: int | None | Unset
        if isinstance(self.csdi_tpu_id, Unset):
            csdi_tpu_id = UNSET
        else:
            csdi_tpu_id = self.csdi_tpu_id

        tpu_number: None | str | Unset
        if isinstance(self.tpu_number, Unset):
            tpu_number = UNSET
        else:
            tpu_number = self.tpu_number

        spu_number: None | str | Unset
        if isinstance(self.spu_number, Unset):
            spu_number = UNSET
        else:
            spu_number = self.spu_number

        ppu_number: None | str | Unset
        if isinstance(self.ppu_number, Unset):
            ppu_number = UNSET
        else:
            ppu_number = self.ppu_number

        data_owner: None | str | Unset
        if isinstance(self.data_owner, Unset):
            data_owner = UNSET
        else:
            data_owner = self.data_owner

        begin_lifespan: int | None | Unset
        if isinstance(self.begin_lifespan, Unset):
            begin_lifespan = UNSET
        else:
            begin_lifespan = self.begin_lifespan

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
        if csdi_tpu_id is not UNSET:
            field_dict["CSDI_TPU_ID"] = csdi_tpu_id
        if tpu_number is not UNSET:
            field_dict["TPU_NUMBER"] = tpu_number
        if spu_number is not UNSET:
            field_dict["SPU_NUMBER"] = spu_number
        if ppu_number is not UNSET:
            field_dict["PPU_NUMBER"] = ppu_number
        if data_owner is not UNSET:
            field_dict["DATA_OWNER"] = data_owner
        if begin_lifespan is not UNSET:
            field_dict["BEGIN_LIFESPAN"] = begin_lifespan
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

        def _parse_csdi_tpu_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        csdi_tpu_id = _parse_csdi_tpu_id(d.pop("CSDI_TPU_ID", UNSET))

        def _parse_tpu_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tpu_number = _parse_tpu_number(d.pop("TPU_NUMBER", UNSET))

        def _parse_spu_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        spu_number = _parse_spu_number(d.pop("SPU_NUMBER", UNSET))

        def _parse_ppu_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ppu_number = _parse_ppu_number(d.pop("PPU_NUMBER", UNSET))

        def _parse_data_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_owner = _parse_data_owner(d.pop("DATA_OWNER", UNSET))

        def _parse_begin_lifespan(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        begin_lifespan = _parse_begin_lifespan(d.pop("BEGIN_LIFESPAN", UNSET))

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

        wfs_map_server_wfs_tpu_attributes = cls(
            objectid=objectid,
            shape=shape,
            csdi_tpu_id=csdi_tpu_id,
            tpu_number=tpu_number,
            spu_number=spu_number,
            ppu_number=ppu_number,
            data_owner=data_owner,
            begin_lifespan=begin_lifespan,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_tpu_attributes.additional_properties = d
        return wfs_map_server_wfs_tpu_attributes

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
