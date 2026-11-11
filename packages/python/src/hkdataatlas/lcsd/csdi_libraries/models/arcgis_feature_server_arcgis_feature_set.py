from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.arcgis_feature_server_arcgis_feature_set_features_item import (
        ArcgisFeatureServerArcgisFeatureSetFeaturesItem,
    )


T = TypeVar("T", bound="ArcgisFeatureServerArcgisFeatureSet")


@_attrs_define
class ArcgisFeatureServerArcgisFeatureSet:
    """
    Attributes:
        features (list[ArcgisFeatureServerArcgisFeatureSetFeaturesItem] | Unset):
        exceeded_transfer_limit (bool | Unset):
    """

    features: list[ArcgisFeatureServerArcgisFeatureSetFeaturesItem] | Unset = UNSET
    exceeded_transfer_limit: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        features: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item = features_item_data.to_dict()
                features.append(features_item)

        exceeded_transfer_limit = self.exceeded_transfer_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if features is not UNSET:
            field_dict["features"] = features
        if exceeded_transfer_limit is not UNSET:
            field_dict["exceededTransferLimit"] = exceeded_transfer_limit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.arcgis_feature_server_arcgis_feature_set_features_item import (
            ArcgisFeatureServerArcgisFeatureSetFeaturesItem,
        )

        d = dict(src_dict)
        _features = d.pop("features", UNSET)
        features: list[ArcgisFeatureServerArcgisFeatureSetFeaturesItem] | Unset = UNSET
        if _features is not UNSET:
            features = []
            for features_item_data in _features:
                features_item = (
                    ArcgisFeatureServerArcgisFeatureSetFeaturesItem.from_dict(
                        features_item_data
                    )
                )

                features.append(features_item)

        exceeded_transfer_limit = d.pop("exceededTransferLimit", UNSET)

        arcgis_feature_server_arcgis_feature_set = cls(
            features=features,
            exceeded_transfer_limit=exceeded_transfer_limit,
        )

        arcgis_feature_server_arcgis_feature_set.additional_properties = d
        return arcgis_feature_server_arcgis_feature_set

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
