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
        addres_of_the_building_in_chn (None | str | Unset): Publisher field type: esriFieldTypeString
        addres_of_the_building_in_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        corporation_num (None | str | Unset): Publisher field type: esriFieldTypeString
        the_incorporated_owners_of_in_chn (None | str | Unset): Publisher field type: esriFieldTypeString
        the_incorporated_owners_of_in_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    addres_of_the_building_in_chn: None | str | Unset = UNSET
    addres_of_the_building_in_eng: None | str | Unset = UNSET
    corporation_num: None | str | Unset = UNSET
    the_incorporated_owners_of_in_chn: None | str | Unset = UNSET
    the_incorporated_owners_of_in_eng: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        addres_of_the_building_in_chn: None | str | Unset
        if isinstance(self.addres_of_the_building_in_chn, Unset):
            addres_of_the_building_in_chn = UNSET
        else:
            addres_of_the_building_in_chn = self.addres_of_the_building_in_chn

        addres_of_the_building_in_eng: None | str | Unset
        if isinstance(self.addres_of_the_building_in_eng, Unset):
            addres_of_the_building_in_eng = UNSET
        else:
            addres_of_the_building_in_eng = self.addres_of_the_building_in_eng

        corporation_num: None | str | Unset
        if isinstance(self.corporation_num, Unset):
            corporation_num = UNSET
        else:
            corporation_num = self.corporation_num

        the_incorporated_owners_of_in_chn: None | str | Unset
        if isinstance(self.the_incorporated_owners_of_in_chn, Unset):
            the_incorporated_owners_of_in_chn = UNSET
        else:
            the_incorporated_owners_of_in_chn = self.the_incorporated_owners_of_in_chn

        the_incorporated_owners_of_in_eng: None | str | Unset
        if isinstance(self.the_incorporated_owners_of_in_eng, Unset):
            the_incorporated_owners_of_in_eng = UNSET
        else:
            the_incorporated_owners_of_in_eng = self.the_incorporated_owners_of_in_eng

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if addres_of_the_building_in_chn is not UNSET:
            field_dict["ADDRES_OF_THE_BUILDING_IN_CHN"] = addres_of_the_building_in_chn
        if addres_of_the_building_in_eng is not UNSET:
            field_dict["ADDRES_OF_THE_BUILDING_IN_ENG"] = addres_of_the_building_in_eng
        if corporation_num is not UNSET:
            field_dict["CORPORATION_NUM"] = corporation_num
        if the_incorporated_owners_of_in_chn is not UNSET:
            field_dict["THE_INCORPORATED_OWNERS_OF_IN_CHN"] = (
                the_incorporated_owners_of_in_chn
            )
        if the_incorporated_owners_of_in_eng is not UNSET:
            field_dict["THE_INCORPORATED_OWNERS_OF_IN_ENG"] = (
                the_incorporated_owners_of_in_eng
            )
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_addres_of_the_building_in_chn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        addres_of_the_building_in_chn = _parse_addres_of_the_building_in_chn(
            d.pop("ADDRES_OF_THE_BUILDING_IN_CHN", UNSET)
        )

        def _parse_addres_of_the_building_in_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        addres_of_the_building_in_eng = _parse_addres_of_the_building_in_eng(
            d.pop("ADDRES_OF_THE_BUILDING_IN_ENG", UNSET)
        )

        def _parse_corporation_num(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        corporation_num = _parse_corporation_num(d.pop("CORPORATION_NUM", UNSET))

        def _parse_the_incorporated_owners_of_in_chn(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        the_incorporated_owners_of_in_chn = _parse_the_incorporated_owners_of_in_chn(
            d.pop("THE_INCORPORATED_OWNERS_OF_IN_CHN", UNSET)
        )

        def _parse_the_incorporated_owners_of_in_eng(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        the_incorporated_owners_of_in_eng = _parse_the_incorporated_owners_of_in_eng(
            d.pop("THE_INCORPORATED_OWNERS_OF_IN_ENG", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            addres_of_the_building_in_chn=addres_of_the_building_in_chn,
            addres_of_the_building_in_eng=addres_of_the_building_in_eng,
            corporation_num=corporation_num,
            the_incorporated_owners_of_in_chn=the_incorporated_owners_of_in_chn,
            the_incorporated_owners_of_in_eng=the_incorporated_owners_of_in_eng,
            objectid=objectid,
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
