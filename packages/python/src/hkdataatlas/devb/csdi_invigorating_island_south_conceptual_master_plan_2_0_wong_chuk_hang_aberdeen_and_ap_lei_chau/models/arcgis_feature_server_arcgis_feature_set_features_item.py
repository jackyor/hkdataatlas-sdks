from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.arcgis_feature_server_arcgis_layer_0_attributes import (
        ArcgisFeatureServerArcgisLayer0Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_1_attributes import (
        ArcgisFeatureServerArcgisLayer1Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_2_attributes import (
        ArcgisFeatureServerArcgisLayer2Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_3_attributes import (
        ArcgisFeatureServerArcgisLayer3Attributes,
    )


T = TypeVar("T", bound="ArcgisFeatureServerArcgisFeatureSetFeaturesItem")


@_attrs_define
class ArcgisFeatureServerArcgisFeatureSetFeaturesItem:
    """
    Attributes:
        attributes (ArcgisFeatureServerArcgisLayer0Attributes | ArcgisFeatureServerArcgisLayer1Attributes |
            ArcgisFeatureServerArcgisLayer2Attributes | ArcgisFeatureServerArcgisLayer3Attributes | Unset):
        geometry (Any | Unset): Native geometry and spatial reference are not constrained by attribute metadata.
    """

    attributes: (
        ArcgisFeatureServerArcgisLayer0Attributes
        | ArcgisFeatureServerArcgisLayer1Attributes
        | ArcgisFeatureServerArcgisLayer2Attributes
        | ArcgisFeatureServerArcgisLayer3Attributes
        | Unset
    ) = UNSET
    geometry: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.arcgis_feature_server_arcgis_layer_0_attributes import (
            ArcgisFeatureServerArcgisLayer0Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1_attributes import (
            ArcgisFeatureServerArcgisLayer1Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_2_attributes import (
            ArcgisFeatureServerArcgisLayer2Attributes,
        )

        attributes: dict[str, Any] | Unset
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        elif (
            isinstance(self.attributes, ArcgisFeatureServerArcgisLayer0Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer1Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer2Attributes)
        ):
            attributes = self.attributes.to_dict()
        else:
            attributes = self.attributes.to_dict()

        geometry = self.geometry

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if geometry is not UNSET:
            field_dict["geometry"] = geometry

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.arcgis_feature_server_arcgis_layer_0_attributes import (
            ArcgisFeatureServerArcgisLayer0Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1_attributes import (
            ArcgisFeatureServerArcgisLayer1Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_2_attributes import (
            ArcgisFeatureServerArcgisLayer2Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_3_attributes import (
            ArcgisFeatureServerArcgisLayer3Attributes,
        )

        d = dict(src_dict)

        def _parse_attributes(
            data: object,
        ) -> (
            ArcgisFeatureServerArcgisLayer0Attributes
            | ArcgisFeatureServerArcgisLayer1Attributes
            | ArcgisFeatureServerArcgisLayer2Attributes
            | ArcgisFeatureServerArcgisLayer3Attributes
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_0 = ArcgisFeatureServerArcgisLayer0Attributes.from_dict(
                    data
                )

                return attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_1 = ArcgisFeatureServerArcgisLayer1Attributes.from_dict(
                    data
                )

                return attributes_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_2 = ArcgisFeatureServerArcgisLayer2Attributes.from_dict(
                    data
                )

                return attributes_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            attributes_type_3 = ArcgisFeatureServerArcgisLayer3Attributes.from_dict(
                data
            )

            return attributes_type_3

        attributes = _parse_attributes(d.pop("attributes", UNSET))

        geometry = d.pop("geometry", UNSET)

        arcgis_feature_server_arcgis_feature_set_features_item = cls(
            attributes=attributes,
            geometry=geometry,
        )

        arcgis_feature_server_arcgis_feature_set_features_item.additional_properties = d
        return arcgis_feature_server_arcgis_feature_set_features_item

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
