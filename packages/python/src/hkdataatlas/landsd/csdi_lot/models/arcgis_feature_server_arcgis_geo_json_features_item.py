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
    from ..models.arcgis_feature_server_arcgis_layer_1000_attributes import (
        ArcgisFeatureServerArcgisLayer1000Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_1001_attributes import (
        ArcgisFeatureServerArcgisLayer1001Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_1002_attributes import (
        ArcgisFeatureServerArcgisLayer1002Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_1003_attributes import (
        ArcgisFeatureServerArcgisLayer1003Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_1004_attributes import (
        ArcgisFeatureServerArcgisLayer1004Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_1005_attributes import (
        ArcgisFeatureServerArcgisLayer1005Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_1006_attributes import (
        ArcgisFeatureServerArcgisLayer1006Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_1007_attributes import (
        ArcgisFeatureServerArcgisLayer1007Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_1008_attributes import (
        ArcgisFeatureServerArcgisLayer1008Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_1009_attributes import (
        ArcgisFeatureServerArcgisLayer1009Attributes,
    )


T = TypeVar("T", bound="ArcgisFeatureServerArcgisGeoJsonFeaturesItem")


@_attrs_define
class ArcgisFeatureServerArcgisGeoJsonFeaturesItem:
    """
    Attributes:
        type_ (str | Unset):
        properties (ArcgisFeatureServerArcgisLayer0Attributes | ArcgisFeatureServerArcgisLayer1000Attributes |
            ArcgisFeatureServerArcgisLayer1001Attributes | ArcgisFeatureServerArcgisLayer1002Attributes |
            ArcgisFeatureServerArcgisLayer1003Attributes | ArcgisFeatureServerArcgisLayer1004Attributes |
            ArcgisFeatureServerArcgisLayer1005Attributes | ArcgisFeatureServerArcgisLayer1006Attributes |
            ArcgisFeatureServerArcgisLayer1007Attributes | ArcgisFeatureServerArcgisLayer1008Attributes |
            ArcgisFeatureServerArcgisLayer1009Attributes | Unset):
        geometry (Any | Unset): Geometry representation is not constrained by the retained attribute metadata.
    """

    type_: str | Unset = UNSET
    properties: (
        ArcgisFeatureServerArcgisLayer0Attributes
        | ArcgisFeatureServerArcgisLayer1000Attributes
        | ArcgisFeatureServerArcgisLayer1001Attributes
        | ArcgisFeatureServerArcgisLayer1002Attributes
        | ArcgisFeatureServerArcgisLayer1003Attributes
        | ArcgisFeatureServerArcgisLayer1004Attributes
        | ArcgisFeatureServerArcgisLayer1005Attributes
        | ArcgisFeatureServerArcgisLayer1006Attributes
        | ArcgisFeatureServerArcgisLayer1007Attributes
        | ArcgisFeatureServerArcgisLayer1008Attributes
        | ArcgisFeatureServerArcgisLayer1009Attributes
        | Unset
    ) = UNSET
    geometry: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.arcgis_feature_server_arcgis_layer_0_attributes import (
            ArcgisFeatureServerArcgisLayer0Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1000_attributes import (
            ArcgisFeatureServerArcgisLayer1000Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1001_attributes import (
            ArcgisFeatureServerArcgisLayer1001Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1002_attributes import (
            ArcgisFeatureServerArcgisLayer1002Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1003_attributes import (
            ArcgisFeatureServerArcgisLayer1003Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1004_attributes import (
            ArcgisFeatureServerArcgisLayer1004Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1005_attributes import (
            ArcgisFeatureServerArcgisLayer1005Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1006_attributes import (
            ArcgisFeatureServerArcgisLayer1006Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1007_attributes import (
            ArcgisFeatureServerArcgisLayer1007Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1008_attributes import (
            ArcgisFeatureServerArcgisLayer1008Attributes,
        )

        type_ = self.type_

        properties: dict[str, Any] | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif (
            isinstance(self.properties, ArcgisFeatureServerArcgisLayer0Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer1000Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer1001Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer1002Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer1003Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer1004Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer1005Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer1006Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer1007Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer1008Attributes)
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
        from ..models.arcgis_feature_server_arcgis_layer_1000_attributes import (
            ArcgisFeatureServerArcgisLayer1000Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1001_attributes import (
            ArcgisFeatureServerArcgisLayer1001Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1002_attributes import (
            ArcgisFeatureServerArcgisLayer1002Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1003_attributes import (
            ArcgisFeatureServerArcgisLayer1003Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1004_attributes import (
            ArcgisFeatureServerArcgisLayer1004Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1005_attributes import (
            ArcgisFeatureServerArcgisLayer1005Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1006_attributes import (
            ArcgisFeatureServerArcgisLayer1006Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1007_attributes import (
            ArcgisFeatureServerArcgisLayer1007Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1008_attributes import (
            ArcgisFeatureServerArcgisLayer1008Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1009_attributes import (
            ArcgisFeatureServerArcgisLayer1009Attributes,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        def _parse_properties(
            data: object,
        ) -> (
            ArcgisFeatureServerArcgisLayer0Attributes
            | ArcgisFeatureServerArcgisLayer1000Attributes
            | ArcgisFeatureServerArcgisLayer1001Attributes
            | ArcgisFeatureServerArcgisLayer1002Attributes
            | ArcgisFeatureServerArcgisLayer1003Attributes
            | ArcgisFeatureServerArcgisLayer1004Attributes
            | ArcgisFeatureServerArcgisLayer1005Attributes
            | ArcgisFeatureServerArcgisLayer1006Attributes
            | ArcgisFeatureServerArcgisLayer1007Attributes
            | ArcgisFeatureServerArcgisLayer1008Attributes
            | ArcgisFeatureServerArcgisLayer1009Attributes
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
                properties_type_1 = (
                    ArcgisFeatureServerArcgisLayer1000Attributes.from_dict(data)
                )

                return properties_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_2 = (
                    ArcgisFeatureServerArcgisLayer1001Attributes.from_dict(data)
                )

                return properties_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_3 = (
                    ArcgisFeatureServerArcgisLayer1002Attributes.from_dict(data)
                )

                return properties_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_4 = (
                    ArcgisFeatureServerArcgisLayer1003Attributes.from_dict(data)
                )

                return properties_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_5 = (
                    ArcgisFeatureServerArcgisLayer1004Attributes.from_dict(data)
                )

                return properties_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_6 = (
                    ArcgisFeatureServerArcgisLayer1005Attributes.from_dict(data)
                )

                return properties_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_7 = (
                    ArcgisFeatureServerArcgisLayer1006Attributes.from_dict(data)
                )

                return properties_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_8 = (
                    ArcgisFeatureServerArcgisLayer1007Attributes.from_dict(data)
                )

                return properties_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_9 = (
                    ArcgisFeatureServerArcgisLayer1008Attributes.from_dict(data)
                )

                return properties_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            properties_type_10 = ArcgisFeatureServerArcgisLayer1009Attributes.from_dict(
                data
            )

            return properties_type_10

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
