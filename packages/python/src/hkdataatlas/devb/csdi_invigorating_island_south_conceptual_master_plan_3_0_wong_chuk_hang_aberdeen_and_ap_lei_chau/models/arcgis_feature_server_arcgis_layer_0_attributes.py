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
        fid (float | None | Unset): Publisher field type: esriFieldTypeDouble
        quick_win_id (int | None | Unset): Publisher field type: esriFieldTypeInteger
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        layer (None | str | Unset): Publisher field type: esriFieldTypeString
        strategy_en (None | str | Unset): Publisher field type: esriFieldTypeString
        strategy_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        strategy_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        content_strategy_en (None | str | Unset): Publisher field type: esriFieldTypeString
        content_strategy_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        content_strategy_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        quick_win_en (None | str | Unset): Publisher field type: esriFieldTypeString
        quick_win_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        quick_win_sc (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    fid: float | None | Unset = UNSET
    quick_win_id: int | None | Unset = UNSET
    easting: float | None | Unset = UNSET
    northing: float | None | Unset = UNSET
    layer: None | str | Unset = UNSET
    strategy_en: None | str | Unset = UNSET
    strategy_tc: None | str | Unset = UNSET
    strategy_sc: None | str | Unset = UNSET
    content_strategy_en: None | str | Unset = UNSET
    content_strategy_tc: None | str | Unset = UNSET
    content_strategy_sc: None | str | Unset = UNSET
    quick_win_en: None | str | Unset = UNSET
    quick_win_tc: None | str | Unset = UNSET
    quick_win_sc: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        fid: float | None | Unset
        if isinstance(self.fid, Unset):
            fid = UNSET
        else:
            fid = self.fid

        quick_win_id: int | None | Unset
        if isinstance(self.quick_win_id, Unset):
            quick_win_id = UNSET
        else:
            quick_win_id = self.quick_win_id

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        layer: None | str | Unset
        if isinstance(self.layer, Unset):
            layer = UNSET
        else:
            layer = self.layer

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

        strategy_sc: None | str | Unset
        if isinstance(self.strategy_sc, Unset):
            strategy_sc = UNSET
        else:
            strategy_sc = self.strategy_sc

        content_strategy_en: None | str | Unset
        if isinstance(self.content_strategy_en, Unset):
            content_strategy_en = UNSET
        else:
            content_strategy_en = self.content_strategy_en

        content_strategy_tc: None | str | Unset
        if isinstance(self.content_strategy_tc, Unset):
            content_strategy_tc = UNSET
        else:
            content_strategy_tc = self.content_strategy_tc

        content_strategy_sc: None | str | Unset
        if isinstance(self.content_strategy_sc, Unset):
            content_strategy_sc = UNSET
        else:
            content_strategy_sc = self.content_strategy_sc

        quick_win_en: None | str | Unset
        if isinstance(self.quick_win_en, Unset):
            quick_win_en = UNSET
        else:
            quick_win_en = self.quick_win_en

        quick_win_tc: None | str | Unset
        if isinstance(self.quick_win_tc, Unset):
            quick_win_tc = UNSET
        else:
            quick_win_tc = self.quick_win_tc

        quick_win_sc: None | str | Unset
        if isinstance(self.quick_win_sc, Unset):
            quick_win_sc = UNSET
        else:
            quick_win_sc = self.quick_win_sc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if fid is not UNSET:
            field_dict["fid"] = fid
        if quick_win_id is not UNSET:
            field_dict["QuickWinID"] = quick_win_id
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if layer is not UNSET:
            field_dict["Layer"] = layer
        if strategy_en is not UNSET:
            field_dict["Strategy_en"] = strategy_en
        if strategy_tc is not UNSET:
            field_dict["Strategy_tc"] = strategy_tc
        if strategy_sc is not UNSET:
            field_dict["Strategy_sc"] = strategy_sc
        if content_strategy_en is not UNSET:
            field_dict["Content_Strategy_en"] = content_strategy_en
        if content_strategy_tc is not UNSET:
            field_dict["Content_Strategy_tc"] = content_strategy_tc
        if content_strategy_sc is not UNSET:
            field_dict["Content_Strategy_sc"] = content_strategy_sc
        if quick_win_en is not UNSET:
            field_dict["Quick_win_en"] = quick_win_en
        if quick_win_tc is not UNSET:
            field_dict["Quick_win_tc"] = quick_win_tc
        if quick_win_sc is not UNSET:
            field_dict["Quick_win_sc"] = quick_win_sc

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

        def _parse_quick_win_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        quick_win_id = _parse_quick_win_id(d.pop("QuickWinID", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("Easting", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_layer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        layer = _parse_layer(d.pop("Layer", UNSET))

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

        def _parse_strategy_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        strategy_sc = _parse_strategy_sc(d.pop("Strategy_sc", UNSET))

        def _parse_content_strategy_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_strategy_en = _parse_content_strategy_en(
            d.pop("Content_Strategy_en", UNSET)
        )

        def _parse_content_strategy_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_strategy_tc = _parse_content_strategy_tc(
            d.pop("Content_Strategy_tc", UNSET)
        )

        def _parse_content_strategy_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_strategy_sc = _parse_content_strategy_sc(
            d.pop("Content_Strategy_sc", UNSET)
        )

        def _parse_quick_win_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quick_win_en = _parse_quick_win_en(d.pop("Quick_win_en", UNSET))

        def _parse_quick_win_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quick_win_tc = _parse_quick_win_tc(d.pop("Quick_win_tc", UNSET))

        def _parse_quick_win_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quick_win_sc = _parse_quick_win_sc(d.pop("Quick_win_sc", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            fid=fid,
            quick_win_id=quick_win_id,
            easting=easting,
            northing=northing,
            layer=layer,
            strategy_en=strategy_en,
            strategy_tc=strategy_tc,
            strategy_sc=strategy_sc,
            content_strategy_en=content_strategy_en,
            content_strategy_tc=content_strategy_tc,
            content_strategy_sc=content_strategy_sc,
            quick_win_en=quick_win_en,
            quick_win_tc=quick_win_tc,
            quick_win_sc=quick_win_sc,
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
