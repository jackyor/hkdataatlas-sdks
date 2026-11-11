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
        cmpu_len (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ds_il (float | None | Unset): Publisher field type: esriFieldTypeDouble
        feat_num (None | str | Unset): Publisher field type: esriFieldTypeString
        fr_pnt (None | str | Unset): Publisher field type: esriFieldTypeString
        height (float | None | Unset): Publisher field type: esriFieldTypeDouble
        main_type (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_description (None | str | Unset): Publisher field type: esriFieldTypeString
        to_pnt (None | str | Unset): Publisher field type: esriFieldTypeString
        type_ (None | str | Unset): Publisher field type: esriFieldTypeString
        us_il (float | None | Unset): Publisher field type: esriFieldTypeDouble
        width (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    cmpu_len: float | None | Unset = UNSET
    ds_il: float | None | Unset = UNSET
    feat_num: None | str | Unset = UNSET
    fr_pnt: None | str | Unset = UNSET
    height: float | None | Unset = UNSET
    main_type: None | str | Unset = UNSET
    shape_description: None | str | Unset = UNSET
    to_pnt: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    us_il: float | None | Unset = UNSET
    width: float | None | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        cmpu_len: float | None | Unset
        if isinstance(self.cmpu_len, Unset):
            cmpu_len = UNSET
        else:
            cmpu_len = self.cmpu_len

        ds_il: float | None | Unset
        if isinstance(self.ds_il, Unset):
            ds_il = UNSET
        else:
            ds_il = self.ds_il

        feat_num: None | str | Unset
        if isinstance(self.feat_num, Unset):
            feat_num = UNSET
        else:
            feat_num = self.feat_num

        fr_pnt: None | str | Unset
        if isinstance(self.fr_pnt, Unset):
            fr_pnt = UNSET
        else:
            fr_pnt = self.fr_pnt

        height: float | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        main_type: None | str | Unset
        if isinstance(self.main_type, Unset):
            main_type = UNSET
        else:
            main_type = self.main_type

        shape_description: None | str | Unset
        if isinstance(self.shape_description, Unset):
            shape_description = UNSET
        else:
            shape_description = self.shape_description

        to_pnt: None | str | Unset
        if isinstance(self.to_pnt, Unset):
            to_pnt = UNSET
        else:
            to_pnt = self.to_pnt

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        us_il: float | None | Unset
        if isinstance(self.us_il, Unset):
            us_il = UNSET
        else:
            us_il = self.us_il

        width: float | None | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

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
        if cmpu_len is not UNSET:
            field_dict["CMPU_LEN"] = cmpu_len
        if ds_il is not UNSET:
            field_dict["DS_IL"] = ds_il
        if feat_num is not UNSET:
            field_dict["FEAT_NUM"] = feat_num
        if fr_pnt is not UNSET:
            field_dict["FR_PNT"] = fr_pnt
        if height is not UNSET:
            field_dict["HEIGHT"] = height
        if main_type is not UNSET:
            field_dict["MAIN_TYPE"] = main_type
        if shape_description is not UNSET:
            field_dict["SHAPE_DESCRIPTION"] = shape_description
        if to_pnt is not UNSET:
            field_dict["TO_PNT"] = to_pnt
        if type_ is not UNSET:
            field_dict["TYPE"] = type_
        if us_il is not UNSET:
            field_dict["US_IL"] = us_il
        if width is not UNSET:
            field_dict["WIDTH"] = width
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_cmpu_len(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cmpu_len = _parse_cmpu_len(d.pop("CMPU_LEN", UNSET))

        def _parse_ds_il(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ds_il = _parse_ds_il(d.pop("DS_IL", UNSET))

        def _parse_feat_num(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feat_num = _parse_feat_num(d.pop("FEAT_NUM", UNSET))

        def _parse_fr_pnt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fr_pnt = _parse_fr_pnt(d.pop("FR_PNT", UNSET))

        def _parse_height(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        height = _parse_height(d.pop("HEIGHT", UNSET))

        def _parse_main_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        main_type = _parse_main_type(d.pop("MAIN_TYPE", UNSET))

        def _parse_shape_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shape_description = _parse_shape_description(d.pop("SHAPE_DESCRIPTION", UNSET))

        def _parse_to_pnt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to_pnt = _parse_to_pnt(d.pop("TO_PNT", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("TYPE", UNSET))

        def _parse_us_il(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        us_il = _parse_us_il(d.pop("US_IL", UNSET))

        def _parse_width(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        width = _parse_width(d.pop("WIDTH", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            cmpu_len=cmpu_len,
            ds_il=ds_il,
            feat_num=feat_num,
            fr_pnt=fr_pnt,
            height=height,
            main_type=main_type,
            shape_description=shape_description,
            to_pnt=to_pnt,
            type_=type_,
            us_il=us_il,
            width=width,
            shape_length=shape_length,
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
