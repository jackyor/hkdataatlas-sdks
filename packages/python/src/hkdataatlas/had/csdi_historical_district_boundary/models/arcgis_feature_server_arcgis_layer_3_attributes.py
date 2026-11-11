from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer3Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer3Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        csdi_admin_area_id (None | str | Unset): Publisher field type: esriFieldTypeString
        area_type (None | str | Unset): Publisher field type: esriFieldTypeString
        area_id (None | str | Unset): Publisher field type: esriFieldTypeString
        area_code (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        data_owner (None | str | Unset): Publisher field type: esriFieldTypeString
        begin_lifespan (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        end_lifespan (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    csdi_admin_area_id: None | str | Unset = UNSET
    area_type: None | str | Unset = UNSET
    area_id: None | str | Unset = UNSET
    area_code: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    data_owner: None | str | Unset = UNSET
    begin_lifespan: Any | Unset = UNSET
    end_lifespan: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        csdi_admin_area_id: None | str | Unset
        if isinstance(self.csdi_admin_area_id, Unset):
            csdi_admin_area_id = UNSET
        else:
            csdi_admin_area_id = self.csdi_admin_area_id

        area_type: None | str | Unset
        if isinstance(self.area_type, Unset):
            area_type = UNSET
        else:
            area_type = self.area_type

        area_id: None | str | Unset
        if isinstance(self.area_id, Unset):
            area_id = UNSET
        else:
            area_id = self.area_id

        area_code: None | str | Unset
        if isinstance(self.area_code, Unset):
            area_code = UNSET
        else:
            area_code = self.area_code

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        data_owner: None | str | Unset
        if isinstance(self.data_owner, Unset):
            data_owner = UNSET
        else:
            data_owner = self.data_owner

        begin_lifespan = self.begin_lifespan

        end_lifespan = self.end_lifespan

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
        if csdi_admin_area_id is not UNSET:
            field_dict["CSDI_ADMIN_AREA_ID"] = csdi_admin_area_id
        if area_type is not UNSET:
            field_dict["AREA_TYPE"] = area_type
        if area_id is not UNSET:
            field_dict["AREA_ID"] = area_id
        if area_code is not UNSET:
            field_dict["AREA_CODE"] = area_code
        if name_tc is not UNSET:
            field_dict["NAME_TC"] = name_tc
        if name_en is not UNSET:
            field_dict["NAME_EN"] = name_en
        if data_owner is not UNSET:
            field_dict["DATA_OWNER"] = data_owner
        if begin_lifespan is not UNSET:
            field_dict["BEGIN_LIFESPAN"] = begin_lifespan
        if end_lifespan is not UNSET:
            field_dict["END_LIFESPAN"] = end_lifespan
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_csdi_admin_area_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        csdi_admin_area_id = _parse_csdi_admin_area_id(
            d.pop("CSDI_ADMIN_AREA_ID", UNSET)
        )

        def _parse_area_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_type = _parse_area_type(d.pop("AREA_TYPE", UNSET))

        def _parse_area_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_id = _parse_area_id(d.pop("AREA_ID", UNSET))

        def _parse_area_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_code = _parse_area_code(d.pop("AREA_CODE", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("NAME_TC", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("NAME_EN", UNSET))

        def _parse_data_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_owner = _parse_data_owner(d.pop("DATA_OWNER", UNSET))

        begin_lifespan = d.pop("BEGIN_LIFESPAN", UNSET)

        end_lifespan = d.pop("END_LIFESPAN", UNSET)

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

        arcgis_feature_server_arcgis_layer_3_attributes = cls(
            objectid=objectid,
            csdi_admin_area_id=csdi_admin_area_id,
            area_type=area_type,
            area_id=area_id,
            area_code=area_code,
            name_tc=name_tc,
            name_en=name_en,
            data_owner=data_owner,
            begin_lifespan=begin_lifespan,
            end_lifespan=end_lifespan,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        arcgis_feature_server_arcgis_layer_3_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_3_attributes

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
