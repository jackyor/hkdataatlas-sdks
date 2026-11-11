from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        scva_name (None | str | Unset): Publisher field type: esriFieldTypeString
        scva_no (None | str | Unset): Publisher field type: esriFieldTypeString
        portal_no (None | str | Unset): Publisher field type: esriFieldTypeString
        portal_id (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    scva_name: None | str | Unset = UNSET
    scva_no: None | str | Unset = UNSET
    portal_no: None | str | Unset = UNSET
    portal_id: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        scva_name: None | str | Unset
        if isinstance(self.scva_name, Unset):
            scva_name = UNSET
        else:
            scva_name = self.scva_name

        scva_no: None | str | Unset
        if isinstance(self.scva_no, Unset):
            scva_no = UNSET
        else:
            scva_no = self.scva_no

        portal_no: None | str | Unset
        if isinstance(self.portal_no, Unset):
            portal_no = UNSET
        else:
            portal_no = self.portal_no

        portal_id: None | str | Unset
        if isinstance(self.portal_id, Unset):
            portal_id = UNSET
        else:
            portal_id = self.portal_id

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
        if scva_name is not UNSET:
            field_dict["SCVA_Name"] = scva_name
        if scva_no is not UNSET:
            field_dict["SCVA_No"] = scva_no
        if portal_no is not UNSET:
            field_dict["Portal_No"] = portal_no
        if portal_id is not UNSET:
            field_dict["Portal_ID"] = portal_id
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_scva_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scva_name = _parse_scva_name(d.pop("SCVA_Name", UNSET))

        def _parse_scva_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scva_no = _parse_scva_no(d.pop("SCVA_No", UNSET))

        def _parse_portal_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        portal_no = _parse_portal_no(d.pop("Portal_No", UNSET))

        def _parse_portal_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        portal_id = _parse_portal_id(d.pop("Portal_ID", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_1_attributes = cls(
            objectid=objectid,
            scva_name=scva_name,
            scva_no=scva_no,
            portal_no=portal_no,
            portal_id=portal_id,
            shape_length=shape_length,
        )

        arcgis_feature_server_arcgis_layer_1_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1_attributes

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
