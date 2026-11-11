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
        cell_num (float | None | Unset): Publisher field type: esriFieldTypeDouble
        cmpu_len (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ds_il (float | None | Unset): Publisher field type: esriFieldTypeDouble
        feat_num (None | str | Unset): Publisher field type: esriFieldTypeString
        fr_pnt (None | str | Unset): Publisher field type: esriFieldTypeString
        height (float | None | Unset): Publisher field type: esriFieldTypeDouble
        main_type (None | str | Unset): Publisher field type: esriFieldTypeString
        material (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (float | None | Unset): Publisher field type: esriFieldTypeDouble
        parent_featurenumber (None | str | Unset): Publisher field type: esriFieldTypeString
        pl_fd (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_description (None | str | Unset): Publisher field type: esriFieldTypeString
        to_pnt (None | str | Unset): Publisher field type: esriFieldTypeString
        type_ (None | str | Unset): Publisher field type: esriFieldTypeString
        us_il (float | None | Unset): Publisher field type: esriFieldTypeDouble
        width (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid_1 (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    cell_num: float | None | Unset = UNSET
    cmpu_len: float | None | Unset = UNSET
    ds_il: float | None | Unset = UNSET
    feat_num: None | str | Unset = UNSET
    fr_pnt: None | str | Unset = UNSET
    height: float | None | Unset = UNSET
    main_type: None | str | Unset = UNSET
    material: None | str | Unset = UNSET
    objectid: float | None | Unset = UNSET
    parent_featurenumber: None | str | Unset = UNSET
    pl_fd: None | str | Unset = UNSET
    shape_description: None | str | Unset = UNSET
    to_pnt: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    us_il: float | None | Unset = UNSET
    width: float | None | Unset = UNSET
    objectid_1: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cell_num: float | None | Unset
        if isinstance(self.cell_num, Unset):
            cell_num = UNSET
        else:
            cell_num = self.cell_num

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

        material: None | str | Unset
        if isinstance(self.material, Unset):
            material = UNSET
        else:
            material = self.material

        objectid: float | None | Unset
        if isinstance(self.objectid, Unset):
            objectid = UNSET
        else:
            objectid = self.objectid

        parent_featurenumber: None | str | Unset
        if isinstance(self.parent_featurenumber, Unset):
            parent_featurenumber = UNSET
        else:
            parent_featurenumber = self.parent_featurenumber

        pl_fd: None | str | Unset
        if isinstance(self.pl_fd, Unset):
            pl_fd = UNSET
        else:
            pl_fd = self.pl_fd

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

        objectid_1 = self.objectid_1

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cell_num is not UNSET:
            field_dict["CELL_NUM"] = cell_num
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
        if material is not UNSET:
            field_dict["MATERIAL"] = material
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if parent_featurenumber is not UNSET:
            field_dict["PARENT_FEATURENUMBER"] = parent_featurenumber
        if pl_fd is not UNSET:
            field_dict["PL_FD"] = pl_fd
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
        if objectid_1 is not UNSET:
            field_dict["OBJECTID_1"] = objectid_1
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_cell_num(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cell_num = _parse_cell_num(d.pop("CELL_NUM", UNSET))

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

        def _parse_material(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        material = _parse_material(d.pop("MATERIAL", UNSET))

        def _parse_objectid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        objectid = _parse_objectid(d.pop("OBJECTID", UNSET))

        def _parse_parent_featurenumber(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_featurenumber = _parse_parent_featurenumber(
            d.pop("PARENT_FEATURENUMBER", UNSET)
        )

        def _parse_pl_fd(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pl_fd = _parse_pl_fd(d.pop("PL_FD", UNSET))

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

        objectid_1 = d.pop("OBJECTID_1", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            cell_num=cell_num,
            cmpu_len=cmpu_len,
            ds_il=ds_il,
            feat_num=feat_num,
            fr_pnt=fr_pnt,
            height=height,
            main_type=main_type,
            material=material,
            objectid=objectid,
            parent_featurenumber=parent_featurenumber,
            pl_fd=pl_fd,
            shape_description=shape_description,
            to_pnt=to_pnt,
            type_=type_,
            us_il=us_il,
            width=width,
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
