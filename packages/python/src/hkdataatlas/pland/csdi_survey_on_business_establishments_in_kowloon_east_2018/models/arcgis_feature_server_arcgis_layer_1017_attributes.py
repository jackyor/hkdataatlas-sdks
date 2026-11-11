from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1017Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1017Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        area_en (None | str | Unset): Publisher field type: esriFieldTypeString
        area_smaller_100_sq_ft (int | None | Unset): Publisher field type: esriFieldTypeInteger
        area_100_199_sq_ft (int | None | Unset): Publisher field type: esriFieldTypeInteger
        area_200_249_sq_ft (int | None | Unset): Publisher field type: esriFieldTypeInteger
        area_250_499_sq_ft (int | None | Unset): Publisher field type: esriFieldTypeInteger
        area_500_999_sq_ft (int | None | Unset): Publisher field type: esriFieldTypeInteger
        area_1000_2999_sq_ft (int | None | Unset): Publisher field type: esriFieldTypeInteger
        area_3000_4999_sq_ft (int | None | Unset): Publisher field type: esriFieldTypeInteger
        area_5000_9999_sq_ft (int | None | Unset): Publisher field type: esriFieldTypeInteger
        area_larger_10000_sq_ft (int | None | Unset): Publisher field type: esriFieldTypeInteger
        information_cannot_be_provided (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    area_en: None | str | Unset = UNSET
    area_smaller_100_sq_ft: int | None | Unset = UNSET
    area_100_199_sq_ft: int | None | Unset = UNSET
    area_200_249_sq_ft: int | None | Unset = UNSET
    area_250_499_sq_ft: int | None | Unset = UNSET
    area_500_999_sq_ft: int | None | Unset = UNSET
    area_1000_2999_sq_ft: int | None | Unset = UNSET
    area_3000_4999_sq_ft: int | None | Unset = UNSET
    area_5000_9999_sq_ft: int | None | Unset = UNSET
    area_larger_10000_sq_ft: int | None | Unset = UNSET
    information_cannot_be_provided: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        area_en: None | str | Unset
        if isinstance(self.area_en, Unset):
            area_en = UNSET
        else:
            area_en = self.area_en

        area_smaller_100_sq_ft: int | None | Unset
        if isinstance(self.area_smaller_100_sq_ft, Unset):
            area_smaller_100_sq_ft = UNSET
        else:
            area_smaller_100_sq_ft = self.area_smaller_100_sq_ft

        area_100_199_sq_ft: int | None | Unset
        if isinstance(self.area_100_199_sq_ft, Unset):
            area_100_199_sq_ft = UNSET
        else:
            area_100_199_sq_ft = self.area_100_199_sq_ft

        area_200_249_sq_ft: int | None | Unset
        if isinstance(self.area_200_249_sq_ft, Unset):
            area_200_249_sq_ft = UNSET
        else:
            area_200_249_sq_ft = self.area_200_249_sq_ft

        area_250_499_sq_ft: int | None | Unset
        if isinstance(self.area_250_499_sq_ft, Unset):
            area_250_499_sq_ft = UNSET
        else:
            area_250_499_sq_ft = self.area_250_499_sq_ft

        area_500_999_sq_ft: int | None | Unset
        if isinstance(self.area_500_999_sq_ft, Unset):
            area_500_999_sq_ft = UNSET
        else:
            area_500_999_sq_ft = self.area_500_999_sq_ft

        area_1000_2999_sq_ft: int | None | Unset
        if isinstance(self.area_1000_2999_sq_ft, Unset):
            area_1000_2999_sq_ft = UNSET
        else:
            area_1000_2999_sq_ft = self.area_1000_2999_sq_ft

        area_3000_4999_sq_ft: int | None | Unset
        if isinstance(self.area_3000_4999_sq_ft, Unset):
            area_3000_4999_sq_ft = UNSET
        else:
            area_3000_4999_sq_ft = self.area_3000_4999_sq_ft

        area_5000_9999_sq_ft: int | None | Unset
        if isinstance(self.area_5000_9999_sq_ft, Unset):
            area_5000_9999_sq_ft = UNSET
        else:
            area_5000_9999_sq_ft = self.area_5000_9999_sq_ft

        area_larger_10000_sq_ft: int | None | Unset
        if isinstance(self.area_larger_10000_sq_ft, Unset):
            area_larger_10000_sq_ft = UNSET
        else:
            area_larger_10000_sq_ft = self.area_larger_10000_sq_ft

        information_cannot_be_provided: None | str | Unset
        if isinstance(self.information_cannot_be_provided, Unset):
            information_cannot_be_provided = UNSET
        else:
            information_cannot_be_provided = self.information_cannot_be_provided

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if area_en is not UNSET:
            field_dict["Area_En"] = area_en
        if area_smaller_100_sq_ft is not UNSET:
            field_dict["Area_smaller_100_sq_ft"] = area_smaller_100_sq_ft
        if area_100_199_sq_ft is not UNSET:
            field_dict["Area_100_199_sq_ft"] = area_100_199_sq_ft
        if area_200_249_sq_ft is not UNSET:
            field_dict["Area_200_249_sq_ft"] = area_200_249_sq_ft
        if area_250_499_sq_ft is not UNSET:
            field_dict["Area_250_499_sq_ft"] = area_250_499_sq_ft
        if area_500_999_sq_ft is not UNSET:
            field_dict["Area_500_999_sq_ft"] = area_500_999_sq_ft
        if area_1000_2999_sq_ft is not UNSET:
            field_dict["Area_1000_2999_sq_ft"] = area_1000_2999_sq_ft
        if area_3000_4999_sq_ft is not UNSET:
            field_dict["Area_3000_4999_sq_ft"] = area_3000_4999_sq_ft
        if area_5000_9999_sq_ft is not UNSET:
            field_dict["Area_5000_9999_sq_ft"] = area_5000_9999_sq_ft
        if area_larger_10000_sq_ft is not UNSET:
            field_dict["Area_larger_10000_sq_ft"] = area_larger_10000_sq_ft
        if information_cannot_be_provided is not UNSET:
            field_dict["Information_cannot_be_provided"] = (
                information_cannot_be_provided
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_area_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_en = _parse_area_en(d.pop("Area_En", UNSET))

        def _parse_area_smaller_100_sq_ft(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_smaller_100_sq_ft = _parse_area_smaller_100_sq_ft(
            d.pop("Area_smaller_100_sq_ft", UNSET)
        )

        def _parse_area_100_199_sq_ft(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_100_199_sq_ft = _parse_area_100_199_sq_ft(
            d.pop("Area_100_199_sq_ft", UNSET)
        )

        def _parse_area_200_249_sq_ft(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_200_249_sq_ft = _parse_area_200_249_sq_ft(
            d.pop("Area_200_249_sq_ft", UNSET)
        )

        def _parse_area_250_499_sq_ft(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_250_499_sq_ft = _parse_area_250_499_sq_ft(
            d.pop("Area_250_499_sq_ft", UNSET)
        )

        def _parse_area_500_999_sq_ft(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_500_999_sq_ft = _parse_area_500_999_sq_ft(
            d.pop("Area_500_999_sq_ft", UNSET)
        )

        def _parse_area_1000_2999_sq_ft(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_1000_2999_sq_ft = _parse_area_1000_2999_sq_ft(
            d.pop("Area_1000_2999_sq_ft", UNSET)
        )

        def _parse_area_3000_4999_sq_ft(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_3000_4999_sq_ft = _parse_area_3000_4999_sq_ft(
            d.pop("Area_3000_4999_sq_ft", UNSET)
        )

        def _parse_area_5000_9999_sq_ft(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_5000_9999_sq_ft = _parse_area_5000_9999_sq_ft(
            d.pop("Area_5000_9999_sq_ft", UNSET)
        )

        def _parse_area_larger_10000_sq_ft(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_larger_10000_sq_ft = _parse_area_larger_10000_sq_ft(
            d.pop("Area_larger_10000_sq_ft", UNSET)
        )

        def _parse_information_cannot_be_provided(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        information_cannot_be_provided = _parse_information_cannot_be_provided(
            d.pop("Information_cannot_be_provided", UNSET)
        )

        arcgis_feature_server_arcgis_layer_1017_attributes = cls(
            objectid=objectid,
            area_en=area_en,
            area_smaller_100_sq_ft=area_smaller_100_sq_ft,
            area_100_199_sq_ft=area_100_199_sq_ft,
            area_200_249_sq_ft=area_200_249_sq_ft,
            area_250_499_sq_ft=area_250_499_sq_ft,
            area_500_999_sq_ft=area_500_999_sq_ft,
            area_1000_2999_sq_ft=area_1000_2999_sq_ft,
            area_3000_4999_sq_ft=area_3000_4999_sq_ft,
            area_5000_9999_sq_ft=area_5000_9999_sq_ft,
            area_larger_10000_sq_ft=area_larger_10000_sq_ft,
            information_cannot_be_provided=information_cannot_be_provided,
        )

        arcgis_feature_server_arcgis_layer_1017_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1017_attributes

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
