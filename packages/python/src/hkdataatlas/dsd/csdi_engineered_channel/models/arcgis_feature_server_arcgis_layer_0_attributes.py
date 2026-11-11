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
        objectid (None | str | Unset): Publisher field type: esriFieldTypeString
        feat_num (None | str | Unset): Publisher field type: esriFieldTypeString
        fr_pnt (None | str | Unset): Publisher field type: esriFieldTypeString
        to_pnt (None | str | Unset): Publisher field type: esriFieldTypeString
        width (None | str | Unset): Publisher field type: esriFieldTypeString
        height (None | str | Unset): Publisher field type: esriFieldTypeString
        cmpu_len (float | None | Unset): Publisher field type: esriFieldTypeDouble
        us_il (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ds_il (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_description (None | str | Unset): Publisher field type: esriFieldTypeString
        feature_member_owns (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        objectid_1 (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: None | str | Unset = UNSET
    feat_num: None | str | Unset = UNSET
    fr_pnt: None | str | Unset = UNSET
    to_pnt: None | str | Unset = UNSET
    width: None | str | Unset = UNSET
    height: None | str | Unset = UNSET
    cmpu_len: float | None | Unset = UNSET
    us_il: float | None | Unset = UNSET
    ds_il: float | None | Unset = UNSET
    shape_description: None | str | Unset = UNSET
    feature_member_owns: int | None | Unset = UNSET
    objectid_1: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid: None | str | Unset
        if isinstance(self.objectid, Unset):
            objectid = UNSET
        else:
            objectid = self.objectid

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

        to_pnt: None | str | Unset
        if isinstance(self.to_pnt, Unset):
            to_pnt = UNSET
        else:
            to_pnt = self.to_pnt

        width: None | str | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        height: None | str | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        cmpu_len: float | None | Unset
        if isinstance(self.cmpu_len, Unset):
            cmpu_len = UNSET
        else:
            cmpu_len = self.cmpu_len

        us_il: float | None | Unset
        if isinstance(self.us_il, Unset):
            us_il = UNSET
        else:
            us_il = self.us_il

        ds_il: float | None | Unset
        if isinstance(self.ds_il, Unset):
            ds_il = UNSET
        else:
            ds_il = self.ds_il

        shape_description: None | str | Unset
        if isinstance(self.shape_description, Unset):
            shape_description = UNSET
        else:
            shape_description = self.shape_description

        feature_member_owns: int | None | Unset
        if isinstance(self.feature_member_owns, Unset):
            feature_member_owns = UNSET
        else:
            feature_member_owns = self.feature_member_owns

        objectid_1 = self.objectid_1

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
        if feat_num is not UNSET:
            field_dict["FEAT_NUM"] = feat_num
        if fr_pnt is not UNSET:
            field_dict["FR_PNT"] = fr_pnt
        if to_pnt is not UNSET:
            field_dict["TO_PNT"] = to_pnt
        if width is not UNSET:
            field_dict["WIDTH"] = width
        if height is not UNSET:
            field_dict["HEIGHT"] = height
        if cmpu_len is not UNSET:
            field_dict["CMPU_LEN"] = cmpu_len
        if us_il is not UNSET:
            field_dict["US_IL"] = us_il
        if ds_il is not UNSET:
            field_dict["DS_IL"] = ds_il
        if shape_description is not UNSET:
            field_dict["SHAPE_DESCRIPTION"] = shape_description
        if feature_member_owns is not UNSET:
            field_dict["featureMember___owns"] = feature_member_owns
        if objectid_1 is not UNSET:
            field_dict["OBJECTID_1"] = objectid_1
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_objectid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        objectid = _parse_objectid(d.pop("OBJECTID", UNSET))

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

        def _parse_to_pnt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to_pnt = _parse_to_pnt(d.pop("TO_PNT", UNSET))

        def _parse_width(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        width = _parse_width(d.pop("WIDTH", UNSET))

        def _parse_height(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        height = _parse_height(d.pop("HEIGHT", UNSET))

        def _parse_cmpu_len(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cmpu_len = _parse_cmpu_len(d.pop("CMPU_LEN", UNSET))

        def _parse_us_il(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        us_il = _parse_us_il(d.pop("US_IL", UNSET))

        def _parse_ds_il(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ds_il = _parse_ds_il(d.pop("DS_IL", UNSET))

        def _parse_shape_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shape_description = _parse_shape_description(d.pop("SHAPE_DESCRIPTION", UNSET))

        def _parse_feature_member_owns(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        feature_member_owns = _parse_feature_member_owns(
            d.pop("featureMember___owns", UNSET)
        )

        objectid_1 = d.pop("OBJECTID_1", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            feat_num=feat_num,
            fr_pnt=fr_pnt,
            to_pnt=to_pnt,
            width=width,
            height=height,
            cmpu_len=cmpu_len,
            us_il=us_il,
            ds_il=ds_il,
            shape_description=shape_description,
            feature_member_owns=feature_member_owns,
            objectid_1=objectid_1,
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
