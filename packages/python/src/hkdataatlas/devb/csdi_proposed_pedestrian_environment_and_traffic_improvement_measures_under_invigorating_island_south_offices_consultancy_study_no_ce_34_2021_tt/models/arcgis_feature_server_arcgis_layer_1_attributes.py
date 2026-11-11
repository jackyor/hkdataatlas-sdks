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
        proposals_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        items_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        contents_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        item_no (None | str | Unset): Publisher field type: esriFieldTypeString
        proposals_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        proposals_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        items_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        items_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        contents_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        contents_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        drawing_link (None | str | Unset): Publisher field type: esriFieldTypeString
        fid (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    proposals_eng: None | str | Unset = UNSET
    items_eng: None | str | Unset = UNSET
    contents_eng: None | str | Unset = UNSET
    item_no: None | str | Unset = UNSET
    proposals_tc: None | str | Unset = UNSET
    proposals_sc: None | str | Unset = UNSET
    items_tc: None | str | Unset = UNSET
    items_sc: None | str | Unset = UNSET
    contents_tc: None | str | Unset = UNSET
    contents_sc: None | str | Unset = UNSET
    drawing_link: None | str | Unset = UNSET
    fid: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposals_eng: None | str | Unset
        if isinstance(self.proposals_eng, Unset):
            proposals_eng = UNSET
        else:
            proposals_eng = self.proposals_eng

        items_eng: None | str | Unset
        if isinstance(self.items_eng, Unset):
            items_eng = UNSET
        else:
            items_eng = self.items_eng

        contents_eng: None | str | Unset
        if isinstance(self.contents_eng, Unset):
            contents_eng = UNSET
        else:
            contents_eng = self.contents_eng

        item_no: None | str | Unset
        if isinstance(self.item_no, Unset):
            item_no = UNSET
        else:
            item_no = self.item_no

        proposals_tc: None | str | Unset
        if isinstance(self.proposals_tc, Unset):
            proposals_tc = UNSET
        else:
            proposals_tc = self.proposals_tc

        proposals_sc: None | str | Unset
        if isinstance(self.proposals_sc, Unset):
            proposals_sc = UNSET
        else:
            proposals_sc = self.proposals_sc

        items_tc: None | str | Unset
        if isinstance(self.items_tc, Unset):
            items_tc = UNSET
        else:
            items_tc = self.items_tc

        items_sc: None | str | Unset
        if isinstance(self.items_sc, Unset):
            items_sc = UNSET
        else:
            items_sc = self.items_sc

        contents_tc: None | str | Unset
        if isinstance(self.contents_tc, Unset):
            contents_tc = UNSET
        else:
            contents_tc = self.contents_tc

        contents_sc: None | str | Unset
        if isinstance(self.contents_sc, Unset):
            contents_sc = UNSET
        else:
            contents_sc = self.contents_sc

        drawing_link: None | str | Unset
        if isinstance(self.drawing_link, Unset):
            drawing_link = UNSET
        else:
            drawing_link = self.drawing_link

        fid: None | str | Unset
        if isinstance(self.fid, Unset):
            fid = UNSET
        else:
            fid = self.fid

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if proposals_eng is not UNSET:
            field_dict["Proposals_Eng"] = proposals_eng
        if items_eng is not UNSET:
            field_dict["Items_Eng"] = items_eng
        if contents_eng is not UNSET:
            field_dict["Contents_Eng"] = contents_eng
        if item_no is not UNSET:
            field_dict["Item_No"] = item_no
        if proposals_tc is not UNSET:
            field_dict["Proposals_TC"] = proposals_tc
        if proposals_sc is not UNSET:
            field_dict["Proposals_SC"] = proposals_sc
        if items_tc is not UNSET:
            field_dict["Items_TC"] = items_tc
        if items_sc is not UNSET:
            field_dict["Items_SC"] = items_sc
        if contents_tc is not UNSET:
            field_dict["Contents_TC"] = contents_tc
        if contents_sc is not UNSET:
            field_dict["Contents_SC"] = contents_sc
        if drawing_link is not UNSET:
            field_dict["Drawing_link"] = drawing_link
        if fid is not UNSET:
            field_dict["fid"] = fid
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_proposals_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proposals_eng = _parse_proposals_eng(d.pop("Proposals_Eng", UNSET))

        def _parse_items_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        items_eng = _parse_items_eng(d.pop("Items_Eng", UNSET))

        def _parse_contents_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contents_eng = _parse_contents_eng(d.pop("Contents_Eng", UNSET))

        def _parse_item_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        item_no = _parse_item_no(d.pop("Item_No", UNSET))

        def _parse_proposals_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proposals_tc = _parse_proposals_tc(d.pop("Proposals_TC", UNSET))

        def _parse_proposals_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proposals_sc = _parse_proposals_sc(d.pop("Proposals_SC", UNSET))

        def _parse_items_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        items_tc = _parse_items_tc(d.pop("Items_TC", UNSET))

        def _parse_items_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        items_sc = _parse_items_sc(d.pop("Items_SC", UNSET))

        def _parse_contents_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contents_tc = _parse_contents_tc(d.pop("Contents_TC", UNSET))

        def _parse_contents_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contents_sc = _parse_contents_sc(d.pop("Contents_SC", UNSET))

        def _parse_drawing_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        drawing_link = _parse_drawing_link(d.pop("Drawing_link", UNSET))

        def _parse_fid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fid = _parse_fid(d.pop("fid", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_1_attributes = cls(
            proposals_eng=proposals_eng,
            items_eng=items_eng,
            contents_eng=contents_eng,
            item_no=item_no,
            proposals_tc=proposals_tc,
            proposals_sc=proposals_sc,
            items_tc=items_tc,
            items_sc=items_sc,
            contents_tc=contents_tc,
            contents_sc=contents_sc,
            drawing_link=drawing_link,
            fid=fid,
            objectid=objectid,
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
