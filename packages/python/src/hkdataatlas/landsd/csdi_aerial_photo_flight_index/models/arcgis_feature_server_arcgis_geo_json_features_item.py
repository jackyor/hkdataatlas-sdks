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
    from ..models.arcgis_feature_server_arcgis_layer_4_attributes import (
        ArcgisFeatureServerArcgisLayer4Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_5_attributes import (
        ArcgisFeatureServerArcgisLayer5Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_6_attributes import (
        ArcgisFeatureServerArcgisLayer6Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_7_attributes import (
        ArcgisFeatureServerArcgisLayer7Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_8_attributes import (
        ArcgisFeatureServerArcgisLayer8Attributes,
    )


T = TypeVar("T", bound="ArcgisFeatureServerArcgisGeoJsonFeaturesItem")


@_attrs_define
class ArcgisFeatureServerArcgisGeoJsonFeaturesItem:
    """
    Attributes:
        type_ (str | Unset):
        properties (ArcgisFeatureServerArcgisLayer0Attributes | ArcgisFeatureServerArcgisLayer1Attributes |
            ArcgisFeatureServerArcgisLayer2Attributes | ArcgisFeatureServerArcgisLayer3Attributes |
            ArcgisFeatureServerArcgisLayer4Attributes | ArcgisFeatureServerArcgisLayer5Attributes |
            ArcgisFeatureServerArcgisLayer6Attributes | ArcgisFeatureServerArcgisLayer7Attributes |
            ArcgisFeatureServerArcgisLayer8Attributes | Unset):
        geometry (Any | Unset): Geometry representation is not constrained by the retained attribute metadata.
    """

    type_: str | Unset = UNSET
    properties: (
        ArcgisFeatureServerArcgisLayer0Attributes
        | ArcgisFeatureServerArcgisLayer1Attributes
        | ArcgisFeatureServerArcgisLayer2Attributes
        | ArcgisFeatureServerArcgisLayer3Attributes
        | ArcgisFeatureServerArcgisLayer4Attributes
        | ArcgisFeatureServerArcgisLayer5Attributes
        | ArcgisFeatureServerArcgisLayer6Attributes
        | ArcgisFeatureServerArcgisLayer7Attributes
        | ArcgisFeatureServerArcgisLayer8Attributes
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
        from ..models.arcgis_feature_server_arcgis_layer_3_attributes import (
            ArcgisFeatureServerArcgisLayer3Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_4_attributes import (
            ArcgisFeatureServerArcgisLayer4Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_5_attributes import (
            ArcgisFeatureServerArcgisLayer5Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_6_attributes import (
            ArcgisFeatureServerArcgisLayer6Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_7_attributes import (
            ArcgisFeatureServerArcgisLayer7Attributes,
        )

        type_ = self.type_

        properties: dict[str, Any] | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif (
            isinstance(self.properties, ArcgisFeatureServerArcgisLayer0Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer1Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer2Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer3Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer4Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer5Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer6Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer7Attributes)
        ):
            properties = self.properties.to_dict()
        else:
            properties = self.properties.to_dict()

        geometry = self.geometry

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if properties is not UNSET:
            field_dict["properties"] = properties
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
        from ..models.arcgis_feature_server_arcgis_layer_4_attributes import (
            ArcgisFeatureServerArcgisLayer4Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_5_attributes import (
            ArcgisFeatureServerArcgisLayer5Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_6_attributes import (
            ArcgisFeatureServerArcgisLayer6Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_7_attributes import (
            ArcgisFeatureServerArcgisLayer7Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_8_attributes import (
            ArcgisFeatureServerArcgisLayer8Attributes,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        def _parse_properties(
            data: object,
        ) -> (
            ArcgisFeatureServerArcgisLayer0Attributes
            | ArcgisFeatureServerArcgisLayer1Attributes
            | ArcgisFeatureServerArcgisLayer2Attributes
            | ArcgisFeatureServerArcgisLayer3Attributes
            | ArcgisFeatureServerArcgisLayer4Attributes
            | ArcgisFeatureServerArcgisLayer5Attributes
            | ArcgisFeatureServerArcgisLayer6Attributes
            | ArcgisFeatureServerArcgisLayer7Attributes
            | ArcgisFeatureServerArcgisLayer8Attributes
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = ArcgisFeatureServerArcgisLayer0Attributes.from_dict(
                    data
                )

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_1 = ArcgisFeatureServerArcgisLayer1Attributes.from_dict(
                    data
                )

                return properties_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_2 = ArcgisFeatureServerArcgisLayer2Attributes.from_dict(
                    data
                )

                return properties_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_3 = ArcgisFeatureServerArcgisLayer3Attributes.from_dict(
                    data
                )

                return properties_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_4 = ArcgisFeatureServerArcgisLayer4Attributes.from_dict(
                    data
                )

                return properties_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_5 = ArcgisFeatureServerArcgisLayer5Attributes.from_dict(
                    data
                )

                return properties_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_6 = ArcgisFeatureServerArcgisLayer6Attributes.from_dict(
                    data
                )

                return properties_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_7 = ArcgisFeatureServerArcgisLayer7Attributes.from_dict(
                    data
                )

                return properties_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            properties_type_8 = ArcgisFeatureServerArcgisLayer8Attributes.from_dict(
                data
            )

            return properties_type_8

        properties = _parse_properties(d.pop("properties", UNSET))

        geometry = d.pop("geometry", UNSET)

        arcgis_feature_server_arcgis_geo_json_features_item = cls(
            type_=type_,
            properties=properties,
            geometry=geometry,
        )

        arcgis_feature_server_arcgis_geo_json_features_item.additional_properties = d
        return arcgis_feature_server_arcgis_geo_json_features_item

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
