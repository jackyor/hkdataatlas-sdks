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
    from ..models.arcgis_feature_server_arcgis_layer_9_attributes import (
        ArcgisFeatureServerArcgisLayer9Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_10_attributes import (
        ArcgisFeatureServerArcgisLayer10Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_11_attributes import (
        ArcgisFeatureServerArcgisLayer11Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_12_attributes import (
        ArcgisFeatureServerArcgisLayer12Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_13_attributes import (
        ArcgisFeatureServerArcgisLayer13Attributes,
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


T = TypeVar("T", bound="ArcgisFeatureServerArcgisFeatureSetFeaturesItem")


@_attrs_define
class ArcgisFeatureServerArcgisFeatureSetFeaturesItem:
    """
    Attributes:
        attributes (ArcgisFeatureServerArcgisLayer0Attributes | ArcgisFeatureServerArcgisLayer1000Attributes |
            ArcgisFeatureServerArcgisLayer1001Attributes | ArcgisFeatureServerArcgisLayer1002Attributes |
            ArcgisFeatureServerArcgisLayer10Attributes | ArcgisFeatureServerArcgisLayer11Attributes |
            ArcgisFeatureServerArcgisLayer12Attributes | ArcgisFeatureServerArcgisLayer13Attributes |
            ArcgisFeatureServerArcgisLayer1Attributes | ArcgisFeatureServerArcgisLayer2Attributes |
            ArcgisFeatureServerArcgisLayer3Attributes | ArcgisFeatureServerArcgisLayer4Attributes |
            ArcgisFeatureServerArcgisLayer5Attributes | ArcgisFeatureServerArcgisLayer6Attributes |
            ArcgisFeatureServerArcgisLayer7Attributes | ArcgisFeatureServerArcgisLayer8Attributes |
            ArcgisFeatureServerArcgisLayer9Attributes | Unset):
        geometry (Any | Unset): Native geometry and spatial reference are not constrained by attribute metadata.
    """

    attributes: (
        ArcgisFeatureServerArcgisLayer0Attributes
        | ArcgisFeatureServerArcgisLayer1000Attributes
        | ArcgisFeatureServerArcgisLayer1001Attributes
        | ArcgisFeatureServerArcgisLayer1002Attributes
        | ArcgisFeatureServerArcgisLayer10Attributes
        | ArcgisFeatureServerArcgisLayer11Attributes
        | ArcgisFeatureServerArcgisLayer12Attributes
        | ArcgisFeatureServerArcgisLayer13Attributes
        | ArcgisFeatureServerArcgisLayer1Attributes
        | ArcgisFeatureServerArcgisLayer2Attributes
        | ArcgisFeatureServerArcgisLayer3Attributes
        | ArcgisFeatureServerArcgisLayer4Attributes
        | ArcgisFeatureServerArcgisLayer5Attributes
        | ArcgisFeatureServerArcgisLayer6Attributes
        | ArcgisFeatureServerArcgisLayer7Attributes
        | ArcgisFeatureServerArcgisLayer8Attributes
        | ArcgisFeatureServerArcgisLayer9Attributes
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
        from ..models.arcgis_feature_server_arcgis_layer_8_attributes import (
            ArcgisFeatureServerArcgisLayer8Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_10_attributes import (
            ArcgisFeatureServerArcgisLayer10Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_11_attributes import (
            ArcgisFeatureServerArcgisLayer11Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_12_attributes import (
            ArcgisFeatureServerArcgisLayer12Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_13_attributes import (
            ArcgisFeatureServerArcgisLayer13Attributes,
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

        attributes: dict[str, Any] | Unset
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        elif (
            isinstance(self.attributes, ArcgisFeatureServerArcgisLayer0Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer1Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer10Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer1000Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer1001Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer1002Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer11Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer12Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer13Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer2Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer3Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer4Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer5Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer6Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer7Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer8Attributes)
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
        from ..models.arcgis_feature_server_arcgis_layer_9_attributes import (
            ArcgisFeatureServerArcgisLayer9Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_10_attributes import (
            ArcgisFeatureServerArcgisLayer10Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_11_attributes import (
            ArcgisFeatureServerArcgisLayer11Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_12_attributes import (
            ArcgisFeatureServerArcgisLayer12Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_13_attributes import (
            ArcgisFeatureServerArcgisLayer13Attributes,
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

        d = dict(src_dict)

        def _parse_attributes(
            data: object,
        ) -> (
            ArcgisFeatureServerArcgisLayer0Attributes
            | ArcgisFeatureServerArcgisLayer1000Attributes
            | ArcgisFeatureServerArcgisLayer1001Attributes
            | ArcgisFeatureServerArcgisLayer1002Attributes
            | ArcgisFeatureServerArcgisLayer10Attributes
            | ArcgisFeatureServerArcgisLayer11Attributes
            | ArcgisFeatureServerArcgisLayer12Attributes
            | ArcgisFeatureServerArcgisLayer13Attributes
            | ArcgisFeatureServerArcgisLayer1Attributes
            | ArcgisFeatureServerArcgisLayer2Attributes
            | ArcgisFeatureServerArcgisLayer3Attributes
            | ArcgisFeatureServerArcgisLayer4Attributes
            | ArcgisFeatureServerArcgisLayer5Attributes
            | ArcgisFeatureServerArcgisLayer6Attributes
            | ArcgisFeatureServerArcgisLayer7Attributes
            | ArcgisFeatureServerArcgisLayer8Attributes
            | ArcgisFeatureServerArcgisLayer9Attributes
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
                attributes_type_2 = (
                    ArcgisFeatureServerArcgisLayer10Attributes.from_dict(data)
                )

                return attributes_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_3 = (
                    ArcgisFeatureServerArcgisLayer1000Attributes.from_dict(data)
                )

                return attributes_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_4 = (
                    ArcgisFeatureServerArcgisLayer1001Attributes.from_dict(data)
                )

                return attributes_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_5 = (
                    ArcgisFeatureServerArcgisLayer1002Attributes.from_dict(data)
                )

                return attributes_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_6 = (
                    ArcgisFeatureServerArcgisLayer11Attributes.from_dict(data)
                )

                return attributes_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_7 = (
                    ArcgisFeatureServerArcgisLayer12Attributes.from_dict(data)
                )

                return attributes_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_8 = (
                    ArcgisFeatureServerArcgisLayer13Attributes.from_dict(data)
                )

                return attributes_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_9 = ArcgisFeatureServerArcgisLayer2Attributes.from_dict(
                    data
                )

                return attributes_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_10 = (
                    ArcgisFeatureServerArcgisLayer3Attributes.from_dict(data)
                )

                return attributes_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_11 = (
                    ArcgisFeatureServerArcgisLayer4Attributes.from_dict(data)
                )

                return attributes_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_12 = (
                    ArcgisFeatureServerArcgisLayer5Attributes.from_dict(data)
                )

                return attributes_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_13 = (
                    ArcgisFeatureServerArcgisLayer6Attributes.from_dict(data)
                )

                return attributes_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_14 = (
                    ArcgisFeatureServerArcgisLayer7Attributes.from_dict(data)
                )

                return attributes_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_15 = (
                    ArcgisFeatureServerArcgisLayer8Attributes.from_dict(data)
                )

                return attributes_type_15
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            attributes_type_16 = ArcgisFeatureServerArcgisLayer9Attributes.from_dict(
                data
            )

            return attributes_type_16

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
