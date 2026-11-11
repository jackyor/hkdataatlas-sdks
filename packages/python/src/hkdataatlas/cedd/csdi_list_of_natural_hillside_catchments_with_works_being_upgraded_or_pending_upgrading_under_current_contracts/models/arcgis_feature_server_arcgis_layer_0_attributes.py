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
        sa_feature (None | str | Unset): Publisher field type: esriFieldTypeString
        new_additio (None | str | Unset): Publisher field type: esriFieldTypeString
        st_locatio (None | str | Unset): Publisher field type: esriFieldTypeString
        st_distric (None | str | Unset): Publisher field type: esriFieldTypeString
        wc_contrac (None | str | Unset): Publisher field type: esriFieldTypeString
        date_start (None | str | Unset): Publisher field type: esriFieldTypeString
        date_comp (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    sa_feature: None | str | Unset = UNSET
    new_additio: None | str | Unset = UNSET
    st_locatio: None | str | Unset = UNSET
    st_distric: None | str | Unset = UNSET
    wc_contrac: None | str | Unset = UNSET
    date_start: None | str | Unset = UNSET
    date_comp: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        sa_feature: None | str | Unset
        if isinstance(self.sa_feature, Unset):
            sa_feature = UNSET
        else:
            sa_feature = self.sa_feature

        new_additio: None | str | Unset
        if isinstance(self.new_additio, Unset):
            new_additio = UNSET
        else:
            new_additio = self.new_additio

        st_locatio: None | str | Unset
        if isinstance(self.st_locatio, Unset):
            st_locatio = UNSET
        else:
            st_locatio = self.st_locatio

        st_distric: None | str | Unset
        if isinstance(self.st_distric, Unset):
            st_distric = UNSET
        else:
            st_distric = self.st_distric

        wc_contrac: None | str | Unset
        if isinstance(self.wc_contrac, Unset):
            wc_contrac = UNSET
        else:
            wc_contrac = self.wc_contrac

        date_start: None | str | Unset
        if isinstance(self.date_start, Unset):
            date_start = UNSET
        else:
            date_start = self.date_start

        date_comp: None | str | Unset
        if isinstance(self.date_comp, Unset):
            date_comp = UNSET
        else:
            date_comp = self.date_comp

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
        if sa_feature is not UNSET:
            field_dict["SA_FEATURE"] = sa_feature
        if new_additio is not UNSET:
            field_dict["NewAdditio"] = new_additio
        if st_locatio is not UNSET:
            field_dict["ST_LOCATIO"] = st_locatio
        if st_distric is not UNSET:
            field_dict["ST_DISTRIC"] = st_distric
        if wc_contrac is not UNSET:
            field_dict["WC_CONTRAC"] = wc_contrac
        if date_start is not UNSET:
            field_dict["DATE_START"] = date_start
        if date_comp is not UNSET:
            field_dict["DATE_COMP_"] = date_comp
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_sa_feature(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sa_feature = _parse_sa_feature(d.pop("SA_FEATURE", UNSET))

        def _parse_new_additio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_additio = _parse_new_additio(d.pop("NewAdditio", UNSET))

        def _parse_st_locatio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        st_locatio = _parse_st_locatio(d.pop("ST_LOCATIO", UNSET))

        def _parse_st_distric(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        st_distric = _parse_st_distric(d.pop("ST_DISTRIC", UNSET))

        def _parse_wc_contrac(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wc_contrac = _parse_wc_contrac(d.pop("WC_CONTRAC", UNSET))

        def _parse_date_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_start = _parse_date_start(d.pop("DATE_START", UNSET))

        def _parse_date_comp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_comp = _parse_date_comp(d.pop("DATE_COMP_", UNSET))

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

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            sa_feature=sa_feature,
            new_additio=new_additio,
            st_locatio=st_locatio,
            st_distric=st_distric,
            wc_contrac=wc_contrac,
            date_start=date_start,
            date_comp=date_comp,
            shape_length=shape_length,
            shape_area=shape_area,
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
