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
    from ..models.arcgis_feature_server_arcgis_layer_14_attributes import (
        ArcgisFeatureServerArcgisLayer14Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_15_attributes import (
        ArcgisFeatureServerArcgisLayer15Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_16_attributes import (
        ArcgisFeatureServerArcgisLayer16Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_1000_attributes import (
        ArcgisFeatureServerArcgisLayer1000Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_1001_attributes import (
        ArcgisFeatureServerArcgisLayer1001Attributes,
    )


T = TypeVar("T", bound="ArcgisFeatureServerArcgisJsonEnvelopeFeaturesItem")


@_attrs_define
class ArcgisFeatureServerArcgisJsonEnvelopeFeaturesItem:
    """
    Attributes:
        type_ (str | Unset):
        attributes (ArcgisFeatureServerArcgisLayer0Attributes | ArcgisFeatureServerArcgisLayer1000Attributes |
            ArcgisFeatureServerArcgisLayer1001Attributes | ArcgisFeatureServerArcgisLayer10Attributes |
            ArcgisFeatureServerArcgisLayer11Attributes | ArcgisFeatureServerArcgisLayer12Attributes |
            ArcgisFeatureServerArcgisLayer13Attributes | ArcgisFeatureServerArcgisLayer14Attributes |
            ArcgisFeatureServerArcgisLayer15Attributes | ArcgisFeatureServerArcgisLayer16Attributes |
            ArcgisFeatureServerArcgisLayer1Attributes | ArcgisFeatureServerArcgisLayer2Attributes |
            ArcgisFeatureServerArcgisLayer3Attributes | ArcgisFeatureServerArcgisLayer4Attributes |
            ArcgisFeatureServerArcgisLayer5Attributes | ArcgisFeatureServerArcgisLayer6Attributes |
            ArcgisFeatureServerArcgisLayer7Attributes | ArcgisFeatureServerArcgisLayer8Attributes |
            ArcgisFeatureServerArcgisLayer9Attributes | Unset):
        properties (ArcgisFeatureServerArcgisLayer0Attributes | ArcgisFeatureServerArcgisLayer1000Attributes |
            ArcgisFeatureServerArcgisLayer1001Attributes | ArcgisFeatureServerArcgisLayer10Attributes |
            ArcgisFeatureServerArcgisLayer11Attributes | ArcgisFeatureServerArcgisLayer12Attributes |
            ArcgisFeatureServerArcgisLayer13Attributes | ArcgisFeatureServerArcgisLayer14Attributes |
            ArcgisFeatureServerArcgisLayer15Attributes | ArcgisFeatureServerArcgisLayer16Attributes |
            ArcgisFeatureServerArcgisLayer1Attributes | ArcgisFeatureServerArcgisLayer2Attributes |
            ArcgisFeatureServerArcgisLayer3Attributes | ArcgisFeatureServerArcgisLayer4Attributes |
            ArcgisFeatureServerArcgisLayer5Attributes | ArcgisFeatureServerArcgisLayer6Attributes |
            ArcgisFeatureServerArcgisLayer7Attributes | ArcgisFeatureServerArcgisLayer8Attributes |
            ArcgisFeatureServerArcgisLayer9Attributes | Unset):
        geometry (Any | Unset): Geometry is not constrained by attribute metadata.
    """

    type_: str | Unset = UNSET
    attributes: (
        ArcgisFeatureServerArcgisLayer0Attributes
        | ArcgisFeatureServerArcgisLayer1000Attributes
        | ArcgisFeatureServerArcgisLayer1001Attributes
        | ArcgisFeatureServerArcgisLayer10Attributes
        | ArcgisFeatureServerArcgisLayer11Attributes
        | ArcgisFeatureServerArcgisLayer12Attributes
        | ArcgisFeatureServerArcgisLayer13Attributes
        | ArcgisFeatureServerArcgisLayer14Attributes
        | ArcgisFeatureServerArcgisLayer15Attributes
        | ArcgisFeatureServerArcgisLayer16Attributes
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
    properties: (
        ArcgisFeatureServerArcgisLayer0Attributes
        | ArcgisFeatureServerArcgisLayer1000Attributes
        | ArcgisFeatureServerArcgisLayer1001Attributes
        | ArcgisFeatureServerArcgisLayer10Attributes
        | ArcgisFeatureServerArcgisLayer11Attributes
        | ArcgisFeatureServerArcgisLayer12Attributes
        | ArcgisFeatureServerArcgisLayer13Attributes
        | ArcgisFeatureServerArcgisLayer14Attributes
        | ArcgisFeatureServerArcgisLayer15Attributes
        | ArcgisFeatureServerArcgisLayer16Attributes
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
        from ..models.arcgis_feature_server_arcgis_layer_14_attributes import (
            ArcgisFeatureServerArcgisLayer14Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_15_attributes import (
            ArcgisFeatureServerArcgisLayer15Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_16_attributes import (
            ArcgisFeatureServerArcgisLayer16Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1000_attributes import (
            ArcgisFeatureServerArcgisLayer1000Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1001_attributes import (
            ArcgisFeatureServerArcgisLayer1001Attributes,
        )

        type_ = self.type_

        attributes: dict[str, Any] | Unset
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        elif (
            isinstance(self.attributes, ArcgisFeatureServerArcgisLayer0Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer1Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer10Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer1000Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer1001Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer11Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer12Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer13Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer14Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer15Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer16Attributes)
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

        properties: dict[str, Any] | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif (
            isinstance(self.properties, ArcgisFeatureServerArcgisLayer0Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer1Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer10Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer1000Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer1001Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer11Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer12Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer13Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer14Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer15Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer16Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer2Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer3Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer4Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer5Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer6Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer7Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer8Attributes)
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
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
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
        from ..models.arcgis_feature_server_arcgis_layer_14_attributes import (
            ArcgisFeatureServerArcgisLayer14Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_15_attributes import (
            ArcgisFeatureServerArcgisLayer15Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_16_attributes import (
            ArcgisFeatureServerArcgisLayer16Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1000_attributes import (
            ArcgisFeatureServerArcgisLayer1000Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_1001_attributes import (
            ArcgisFeatureServerArcgisLayer1001Attributes,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        def _parse_attributes(
            data: object,
        ) -> (
            ArcgisFeatureServerArcgisLayer0Attributes
            | ArcgisFeatureServerArcgisLayer1000Attributes
            | ArcgisFeatureServerArcgisLayer1001Attributes
            | ArcgisFeatureServerArcgisLayer10Attributes
            | ArcgisFeatureServerArcgisLayer11Attributes
            | ArcgisFeatureServerArcgisLayer12Attributes
            | ArcgisFeatureServerArcgisLayer13Attributes
            | ArcgisFeatureServerArcgisLayer14Attributes
            | ArcgisFeatureServerArcgisLayer15Attributes
            | ArcgisFeatureServerArcgisLayer16Attributes
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
                    ArcgisFeatureServerArcgisLayer11Attributes.from_dict(data)
                )

                return attributes_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_6 = (
                    ArcgisFeatureServerArcgisLayer12Attributes.from_dict(data)
                )

                return attributes_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_7 = (
                    ArcgisFeatureServerArcgisLayer13Attributes.from_dict(data)
                )

                return attributes_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_8 = (
                    ArcgisFeatureServerArcgisLayer14Attributes.from_dict(data)
                )

                return attributes_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_9 = (
                    ArcgisFeatureServerArcgisLayer15Attributes.from_dict(data)
                )

                return attributes_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_10 = (
                    ArcgisFeatureServerArcgisLayer16Attributes.from_dict(data)
                )

                return attributes_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_11 = (
                    ArcgisFeatureServerArcgisLayer2Attributes.from_dict(data)
                )

                return attributes_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_12 = (
                    ArcgisFeatureServerArcgisLayer3Attributes.from_dict(data)
                )

                return attributes_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_13 = (
                    ArcgisFeatureServerArcgisLayer4Attributes.from_dict(data)
                )

                return attributes_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_14 = (
                    ArcgisFeatureServerArcgisLayer5Attributes.from_dict(data)
                )

                return attributes_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_15 = (
                    ArcgisFeatureServerArcgisLayer6Attributes.from_dict(data)
                )

                return attributes_type_15
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_16 = (
                    ArcgisFeatureServerArcgisLayer7Attributes.from_dict(data)
                )

                return attributes_type_16
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_17 = (
                    ArcgisFeatureServerArcgisLayer8Attributes.from_dict(data)
                )

                return attributes_type_17
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            attributes_type_18 = ArcgisFeatureServerArcgisLayer9Attributes.from_dict(
                data
            )

            return attributes_type_18

        attributes = _parse_attributes(d.pop("attributes", UNSET))

        def _parse_properties(
            data: object,
        ) -> (
            ArcgisFeatureServerArcgisLayer0Attributes
            | ArcgisFeatureServerArcgisLayer1000Attributes
            | ArcgisFeatureServerArcgisLayer1001Attributes
            | ArcgisFeatureServerArcgisLayer10Attributes
            | ArcgisFeatureServerArcgisLayer11Attributes
            | ArcgisFeatureServerArcgisLayer12Attributes
            | ArcgisFeatureServerArcgisLayer13Attributes
            | ArcgisFeatureServerArcgisLayer14Attributes
            | ArcgisFeatureServerArcgisLayer15Attributes
            | ArcgisFeatureServerArcgisLayer16Attributes
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
                properties_type_2 = (
                    ArcgisFeatureServerArcgisLayer10Attributes.from_dict(data)
                )

                return properties_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_3 = (
                    ArcgisFeatureServerArcgisLayer1000Attributes.from_dict(data)
                )

                return properties_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_4 = (
                    ArcgisFeatureServerArcgisLayer1001Attributes.from_dict(data)
                )

                return properties_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_5 = (
                    ArcgisFeatureServerArcgisLayer11Attributes.from_dict(data)
                )

                return properties_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_6 = (
                    ArcgisFeatureServerArcgisLayer12Attributes.from_dict(data)
                )

                return properties_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_7 = (
                    ArcgisFeatureServerArcgisLayer13Attributes.from_dict(data)
                )

                return properties_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_8 = (
                    ArcgisFeatureServerArcgisLayer14Attributes.from_dict(data)
                )

                return properties_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_9 = (
                    ArcgisFeatureServerArcgisLayer15Attributes.from_dict(data)
                )

                return properties_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_10 = (
                    ArcgisFeatureServerArcgisLayer16Attributes.from_dict(data)
                )

                return properties_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_11 = (
                    ArcgisFeatureServerArcgisLayer2Attributes.from_dict(data)
                )

                return properties_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_12 = (
                    ArcgisFeatureServerArcgisLayer3Attributes.from_dict(data)
                )

                return properties_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_13 = (
                    ArcgisFeatureServerArcgisLayer4Attributes.from_dict(data)
                )

                return properties_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_14 = (
                    ArcgisFeatureServerArcgisLayer5Attributes.from_dict(data)
                )

                return properties_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_15 = (
                    ArcgisFeatureServerArcgisLayer6Attributes.from_dict(data)
                )

                return properties_type_15
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_16 = (
                    ArcgisFeatureServerArcgisLayer7Attributes.from_dict(data)
                )

                return properties_type_16
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_17 = (
                    ArcgisFeatureServerArcgisLayer8Attributes.from_dict(data)
                )

                return properties_type_17
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            properties_type_18 = ArcgisFeatureServerArcgisLayer9Attributes.from_dict(
                data
            )

            return properties_type_18

        properties = _parse_properties(d.pop("properties", UNSET))

        geometry = d.pop("geometry", UNSET)

        arcgis_feature_server_arcgis_json_envelope_features_item = cls(
            type_=type_,
            attributes=attributes,
            properties=properties,
            geometry=geometry,
        )

        arcgis_feature_server_arcgis_json_envelope_features_item.additional_properties = d
        return arcgis_feature_server_arcgis_json_envelope_features_item

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
