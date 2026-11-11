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
        fid (float | None | Unset): Publisher field type: esriFieldTypeDouble
        strategy_en (None | str | Unset): Publisher field type: esriFieldTypeString
        strategy_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        layer (None | str | Unset): Publisher field type: esriFieldTypeString
        project_id (int | None | Unset): Publisher field type: esriFieldTypeInteger
        strategy_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        project_en (None | str | Unset): Publisher field type: esriFieldTypeString
        project_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        project_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        content_s_en (None | str | Unset): Publisher field type: esriFieldTypeString
        content_s_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        content_s_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        contents_p_en (None | str | Unset): Publisher field type: esriFieldTypeString
        contents_p_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        contents_p_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    fid: float | None | Unset = UNSET
    strategy_en: None | str | Unset = UNSET
    strategy_tc: None | str | Unset = UNSET
    layer: None | str | Unset = UNSET
    project_id: int | None | Unset = UNSET
    strategy_sc: None | str | Unset = UNSET
    project_en: None | str | Unset = UNSET
    project_tc: None | str | Unset = UNSET
    project_sc: None | str | Unset = UNSET
    content_s_en: None | str | Unset = UNSET
    content_s_tc: None | str | Unset = UNSET
    content_s_sc: None | str | Unset = UNSET
    contents_p_en: None | str | Unset = UNSET
    contents_p_tc: None | str | Unset = UNSET
    contents_p_sc: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        fid: float | None | Unset
        if isinstance(self.fid, Unset):
            fid = UNSET
        else:
            fid = self.fid

        strategy_en: None | str | Unset
        if isinstance(self.strategy_en, Unset):
            strategy_en = UNSET
        else:
            strategy_en = self.strategy_en

        strategy_tc: None | str | Unset
        if isinstance(self.strategy_tc, Unset):
            strategy_tc = UNSET
        else:
            strategy_tc = self.strategy_tc

        layer: None | str | Unset
        if isinstance(self.layer, Unset):
            layer = UNSET
        else:
            layer = self.layer

        project_id: int | None | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        strategy_sc: None | str | Unset
        if isinstance(self.strategy_sc, Unset):
            strategy_sc = UNSET
        else:
            strategy_sc = self.strategy_sc

        project_en: None | str | Unset
        if isinstance(self.project_en, Unset):
            project_en = UNSET
        else:
            project_en = self.project_en

        project_tc: None | str | Unset
        if isinstance(self.project_tc, Unset):
            project_tc = UNSET
        else:
            project_tc = self.project_tc

        project_sc: None | str | Unset
        if isinstance(self.project_sc, Unset):
            project_sc = UNSET
        else:
            project_sc = self.project_sc

        content_s_en: None | str | Unset
        if isinstance(self.content_s_en, Unset):
            content_s_en = UNSET
        else:
            content_s_en = self.content_s_en

        content_s_tc: None | str | Unset
        if isinstance(self.content_s_tc, Unset):
            content_s_tc = UNSET
        else:
            content_s_tc = self.content_s_tc

        content_s_sc: None | str | Unset
        if isinstance(self.content_s_sc, Unset):
            content_s_sc = UNSET
        else:
            content_s_sc = self.content_s_sc

        contents_p_en: None | str | Unset
        if isinstance(self.contents_p_en, Unset):
            contents_p_en = UNSET
        else:
            contents_p_en = self.contents_p_en

        contents_p_tc: None | str | Unset
        if isinstance(self.contents_p_tc, Unset):
            contents_p_tc = UNSET
        else:
            contents_p_tc = self.contents_p_tc

        contents_p_sc: None | str | Unset
        if isinstance(self.contents_p_sc, Unset):
            contents_p_sc = UNSET
        else:
            contents_p_sc = self.contents_p_sc

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
        if fid is not UNSET:
            field_dict["fid"] = fid
        if strategy_en is not UNSET:
            field_dict["Strategy_en"] = strategy_en
        if strategy_tc is not UNSET:
            field_dict["Strategy_tc"] = strategy_tc
        if layer is not UNSET:
            field_dict["Layer"] = layer
        if project_id is not UNSET:
            field_dict["ProjectID"] = project_id
        if strategy_sc is not UNSET:
            field_dict["Strategy_sc"] = strategy_sc
        if project_en is not UNSET:
            field_dict["Project_en"] = project_en
        if project_tc is not UNSET:
            field_dict["Project_tc"] = project_tc
        if project_sc is not UNSET:
            field_dict["Project_sc"] = project_sc
        if content_s_en is not UNSET:
            field_dict["Content_S_en"] = content_s_en
        if content_s_tc is not UNSET:
            field_dict["Content_S_tc"] = content_s_tc
        if content_s_sc is not UNSET:
            field_dict["Content_S_sc"] = content_s_sc
        if contents_p_en is not UNSET:
            field_dict["Contents_P_en"] = contents_p_en
        if contents_p_tc is not UNSET:
            field_dict["Contents_P_tc"] = contents_p_tc
        if contents_p_sc is not UNSET:
            field_dict["Contents_P_sc"] = contents_p_sc
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_fid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fid = _parse_fid(d.pop("fid", UNSET))

        def _parse_strategy_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        strategy_en = _parse_strategy_en(d.pop("Strategy_en", UNSET))

        def _parse_strategy_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        strategy_tc = _parse_strategy_tc(d.pop("Strategy_tc", UNSET))

        def _parse_layer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        layer = _parse_layer(d.pop("Layer", UNSET))

        def _parse_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_id = _parse_project_id(d.pop("ProjectID", UNSET))

        def _parse_strategy_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        strategy_sc = _parse_strategy_sc(d.pop("Strategy_sc", UNSET))

        def _parse_project_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_en = _parse_project_en(d.pop("Project_en", UNSET))

        def _parse_project_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_tc = _parse_project_tc(d.pop("Project_tc", UNSET))

        def _parse_project_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_sc = _parse_project_sc(d.pop("Project_sc", UNSET))

        def _parse_content_s_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_s_en = _parse_content_s_en(d.pop("Content_S_en", UNSET))

        def _parse_content_s_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_s_tc = _parse_content_s_tc(d.pop("Content_S_tc", UNSET))

        def _parse_content_s_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_s_sc = _parse_content_s_sc(d.pop("Content_S_sc", UNSET))

        def _parse_contents_p_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contents_p_en = _parse_contents_p_en(d.pop("Contents_P_en", UNSET))

        def _parse_contents_p_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contents_p_tc = _parse_contents_p_tc(d.pop("Contents_P_tc", UNSET))

        def _parse_contents_p_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contents_p_sc = _parse_contents_p_sc(d.pop("Contents_P_sc", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_3_attributes = cls(
            objectid=objectid,
            fid=fid,
            strategy_en=strategy_en,
            strategy_tc=strategy_tc,
            layer=layer,
            project_id=project_id,
            strategy_sc=strategy_sc,
            project_en=project_en,
            project_tc=project_tc,
            project_sc=project_sc,
            content_s_en=content_s_en,
            content_s_tc=content_s_tc,
            content_s_sc=content_s_sc,
            contents_p_en=contents_p_en,
            contents_p_tc=contents_p_tc,
            contents_p_sc=contents_p_sc,
            shape_length=shape_length,
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
