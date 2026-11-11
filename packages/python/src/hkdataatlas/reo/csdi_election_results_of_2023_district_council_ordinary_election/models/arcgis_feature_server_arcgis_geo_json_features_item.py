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
    from ..models.arcgis_feature_server_arcgis_layer_17_attributes import (
        ArcgisFeatureServerArcgisLayer17Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_18_attributes import (
        ArcgisFeatureServerArcgisLayer18Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_19_attributes import (
        ArcgisFeatureServerArcgisLayer19Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_20_attributes import (
        ArcgisFeatureServerArcgisLayer20Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_21_attributes import (
        ArcgisFeatureServerArcgisLayer21Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_22_attributes import (
        ArcgisFeatureServerArcgisLayer22Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_23_attributes import (
        ArcgisFeatureServerArcgisLayer23Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_24_attributes import (
        ArcgisFeatureServerArcgisLayer24Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_25_attributes import (
        ArcgisFeatureServerArcgisLayer25Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_26_attributes import (
        ArcgisFeatureServerArcgisLayer26Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_27_attributes import (
        ArcgisFeatureServerArcgisLayer27Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_28_attributes import (
        ArcgisFeatureServerArcgisLayer28Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_29_attributes import (
        ArcgisFeatureServerArcgisLayer29Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_30_attributes import (
        ArcgisFeatureServerArcgisLayer30Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_31_attributes import (
        ArcgisFeatureServerArcgisLayer31Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_32_attributes import (
        ArcgisFeatureServerArcgisLayer32Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_33_attributes import (
        ArcgisFeatureServerArcgisLayer33Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_34_attributes import (
        ArcgisFeatureServerArcgisLayer34Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_35_attributes import (
        ArcgisFeatureServerArcgisLayer35Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_36_attributes import (
        ArcgisFeatureServerArcgisLayer36Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_37_attributes import (
        ArcgisFeatureServerArcgisLayer37Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_38_attributes import (
        ArcgisFeatureServerArcgisLayer38Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_39_attributes import (
        ArcgisFeatureServerArcgisLayer39Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_40_attributes import (
        ArcgisFeatureServerArcgisLayer40Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_41_attributes import (
        ArcgisFeatureServerArcgisLayer41Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_42_attributes import (
        ArcgisFeatureServerArcgisLayer42Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_43_attributes import (
        ArcgisFeatureServerArcgisLayer43Attributes,
    )


T = TypeVar("T", bound="ArcgisFeatureServerArcgisGeoJsonFeaturesItem")


@_attrs_define
class ArcgisFeatureServerArcgisGeoJsonFeaturesItem:
    """
    Attributes:
        type_ (str | Unset):
        properties (ArcgisFeatureServerArcgisLayer0Attributes | ArcgisFeatureServerArcgisLayer10Attributes |
            ArcgisFeatureServerArcgisLayer11Attributes | ArcgisFeatureServerArcgisLayer12Attributes |
            ArcgisFeatureServerArcgisLayer13Attributes | ArcgisFeatureServerArcgisLayer14Attributes |
            ArcgisFeatureServerArcgisLayer15Attributes | ArcgisFeatureServerArcgisLayer16Attributes |
            ArcgisFeatureServerArcgisLayer17Attributes | ArcgisFeatureServerArcgisLayer18Attributes |
            ArcgisFeatureServerArcgisLayer19Attributes | ArcgisFeatureServerArcgisLayer1Attributes |
            ArcgisFeatureServerArcgisLayer20Attributes | ArcgisFeatureServerArcgisLayer21Attributes |
            ArcgisFeatureServerArcgisLayer22Attributes | ArcgisFeatureServerArcgisLayer23Attributes |
            ArcgisFeatureServerArcgisLayer24Attributes | ArcgisFeatureServerArcgisLayer25Attributes |
            ArcgisFeatureServerArcgisLayer26Attributes | ArcgisFeatureServerArcgisLayer27Attributes |
            ArcgisFeatureServerArcgisLayer28Attributes | ArcgisFeatureServerArcgisLayer29Attributes |
            ArcgisFeatureServerArcgisLayer2Attributes | ArcgisFeatureServerArcgisLayer30Attributes |
            ArcgisFeatureServerArcgisLayer31Attributes | ArcgisFeatureServerArcgisLayer32Attributes |
            ArcgisFeatureServerArcgisLayer33Attributes | ArcgisFeatureServerArcgisLayer34Attributes |
            ArcgisFeatureServerArcgisLayer35Attributes | ArcgisFeatureServerArcgisLayer36Attributes |
            ArcgisFeatureServerArcgisLayer37Attributes | ArcgisFeatureServerArcgisLayer38Attributes |
            ArcgisFeatureServerArcgisLayer39Attributes | ArcgisFeatureServerArcgisLayer3Attributes |
            ArcgisFeatureServerArcgisLayer40Attributes | ArcgisFeatureServerArcgisLayer41Attributes |
            ArcgisFeatureServerArcgisLayer42Attributes | ArcgisFeatureServerArcgisLayer43Attributes |
            ArcgisFeatureServerArcgisLayer4Attributes | ArcgisFeatureServerArcgisLayer5Attributes |
            ArcgisFeatureServerArcgisLayer6Attributes | ArcgisFeatureServerArcgisLayer7Attributes |
            ArcgisFeatureServerArcgisLayer8Attributes | ArcgisFeatureServerArcgisLayer9Attributes | Unset):
        geometry (Any | Unset): Geometry representation is not constrained by the retained attribute metadata.
    """

    type_: str | Unset = UNSET
    properties: (
        ArcgisFeatureServerArcgisLayer0Attributes
        | ArcgisFeatureServerArcgisLayer10Attributes
        | ArcgisFeatureServerArcgisLayer11Attributes
        | ArcgisFeatureServerArcgisLayer12Attributes
        | ArcgisFeatureServerArcgisLayer13Attributes
        | ArcgisFeatureServerArcgisLayer14Attributes
        | ArcgisFeatureServerArcgisLayer15Attributes
        | ArcgisFeatureServerArcgisLayer16Attributes
        | ArcgisFeatureServerArcgisLayer17Attributes
        | ArcgisFeatureServerArcgisLayer18Attributes
        | ArcgisFeatureServerArcgisLayer19Attributes
        | ArcgisFeatureServerArcgisLayer1Attributes
        | ArcgisFeatureServerArcgisLayer20Attributes
        | ArcgisFeatureServerArcgisLayer21Attributes
        | ArcgisFeatureServerArcgisLayer22Attributes
        | ArcgisFeatureServerArcgisLayer23Attributes
        | ArcgisFeatureServerArcgisLayer24Attributes
        | ArcgisFeatureServerArcgisLayer25Attributes
        | ArcgisFeatureServerArcgisLayer26Attributes
        | ArcgisFeatureServerArcgisLayer27Attributes
        | ArcgisFeatureServerArcgisLayer28Attributes
        | ArcgisFeatureServerArcgisLayer29Attributes
        | ArcgisFeatureServerArcgisLayer2Attributes
        | ArcgisFeatureServerArcgisLayer30Attributes
        | ArcgisFeatureServerArcgisLayer31Attributes
        | ArcgisFeatureServerArcgisLayer32Attributes
        | ArcgisFeatureServerArcgisLayer33Attributes
        | ArcgisFeatureServerArcgisLayer34Attributes
        | ArcgisFeatureServerArcgisLayer35Attributes
        | ArcgisFeatureServerArcgisLayer36Attributes
        | ArcgisFeatureServerArcgisLayer37Attributes
        | ArcgisFeatureServerArcgisLayer38Attributes
        | ArcgisFeatureServerArcgisLayer39Attributes
        | ArcgisFeatureServerArcgisLayer3Attributes
        | ArcgisFeatureServerArcgisLayer40Attributes
        | ArcgisFeatureServerArcgisLayer41Attributes
        | ArcgisFeatureServerArcgisLayer42Attributes
        | ArcgisFeatureServerArcgisLayer43Attributes
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
        from ..models.arcgis_feature_server_arcgis_layer_17_attributes import (
            ArcgisFeatureServerArcgisLayer17Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_18_attributes import (
            ArcgisFeatureServerArcgisLayer18Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_19_attributes import (
            ArcgisFeatureServerArcgisLayer19Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_20_attributes import (
            ArcgisFeatureServerArcgisLayer20Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_21_attributes import (
            ArcgisFeatureServerArcgisLayer21Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_22_attributes import (
            ArcgisFeatureServerArcgisLayer22Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_23_attributes import (
            ArcgisFeatureServerArcgisLayer23Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_24_attributes import (
            ArcgisFeatureServerArcgisLayer24Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_25_attributes import (
            ArcgisFeatureServerArcgisLayer25Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_26_attributes import (
            ArcgisFeatureServerArcgisLayer26Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_27_attributes import (
            ArcgisFeatureServerArcgisLayer27Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_28_attributes import (
            ArcgisFeatureServerArcgisLayer28Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_29_attributes import (
            ArcgisFeatureServerArcgisLayer29Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_30_attributes import (
            ArcgisFeatureServerArcgisLayer30Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_31_attributes import (
            ArcgisFeatureServerArcgisLayer31Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_32_attributes import (
            ArcgisFeatureServerArcgisLayer32Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_33_attributes import (
            ArcgisFeatureServerArcgisLayer33Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_34_attributes import (
            ArcgisFeatureServerArcgisLayer34Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_35_attributes import (
            ArcgisFeatureServerArcgisLayer35Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_36_attributes import (
            ArcgisFeatureServerArcgisLayer36Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_37_attributes import (
            ArcgisFeatureServerArcgisLayer37Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_38_attributes import (
            ArcgisFeatureServerArcgisLayer38Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_39_attributes import (
            ArcgisFeatureServerArcgisLayer39Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_40_attributes import (
            ArcgisFeatureServerArcgisLayer40Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_41_attributes import (
            ArcgisFeatureServerArcgisLayer41Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_42_attributes import (
            ArcgisFeatureServerArcgisLayer42Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_43_attributes import (
            ArcgisFeatureServerArcgisLayer43Attributes,
        )

        type_ = self.type_

        properties: dict[str, Any] | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif (
            isinstance(self.properties, ArcgisFeatureServerArcgisLayer0Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer1Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer10Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer11Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer12Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer13Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer14Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer15Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer16Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer17Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer18Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer19Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer2Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer20Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer21Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer22Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer23Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer24Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer25Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer26Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer27Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer28Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer29Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer3Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer30Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer31Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer32Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer33Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer34Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer35Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer36Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer37Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer38Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer39Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer4Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer40Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer41Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer42Attributes)
            or isinstance(self.properties, ArcgisFeatureServerArcgisLayer43Attributes)
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
        from ..models.arcgis_feature_server_arcgis_layer_17_attributes import (
            ArcgisFeatureServerArcgisLayer17Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_18_attributes import (
            ArcgisFeatureServerArcgisLayer18Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_19_attributes import (
            ArcgisFeatureServerArcgisLayer19Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_20_attributes import (
            ArcgisFeatureServerArcgisLayer20Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_21_attributes import (
            ArcgisFeatureServerArcgisLayer21Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_22_attributes import (
            ArcgisFeatureServerArcgisLayer22Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_23_attributes import (
            ArcgisFeatureServerArcgisLayer23Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_24_attributes import (
            ArcgisFeatureServerArcgisLayer24Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_25_attributes import (
            ArcgisFeatureServerArcgisLayer25Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_26_attributes import (
            ArcgisFeatureServerArcgisLayer26Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_27_attributes import (
            ArcgisFeatureServerArcgisLayer27Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_28_attributes import (
            ArcgisFeatureServerArcgisLayer28Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_29_attributes import (
            ArcgisFeatureServerArcgisLayer29Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_30_attributes import (
            ArcgisFeatureServerArcgisLayer30Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_31_attributes import (
            ArcgisFeatureServerArcgisLayer31Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_32_attributes import (
            ArcgisFeatureServerArcgisLayer32Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_33_attributes import (
            ArcgisFeatureServerArcgisLayer33Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_34_attributes import (
            ArcgisFeatureServerArcgisLayer34Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_35_attributes import (
            ArcgisFeatureServerArcgisLayer35Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_36_attributes import (
            ArcgisFeatureServerArcgisLayer36Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_37_attributes import (
            ArcgisFeatureServerArcgisLayer37Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_38_attributes import (
            ArcgisFeatureServerArcgisLayer38Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_39_attributes import (
            ArcgisFeatureServerArcgisLayer39Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_40_attributes import (
            ArcgisFeatureServerArcgisLayer40Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_41_attributes import (
            ArcgisFeatureServerArcgisLayer41Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_42_attributes import (
            ArcgisFeatureServerArcgisLayer42Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_43_attributes import (
            ArcgisFeatureServerArcgisLayer43Attributes,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        def _parse_properties(
            data: object,
        ) -> (
            ArcgisFeatureServerArcgisLayer0Attributes
            | ArcgisFeatureServerArcgisLayer10Attributes
            | ArcgisFeatureServerArcgisLayer11Attributes
            | ArcgisFeatureServerArcgisLayer12Attributes
            | ArcgisFeatureServerArcgisLayer13Attributes
            | ArcgisFeatureServerArcgisLayer14Attributes
            | ArcgisFeatureServerArcgisLayer15Attributes
            | ArcgisFeatureServerArcgisLayer16Attributes
            | ArcgisFeatureServerArcgisLayer17Attributes
            | ArcgisFeatureServerArcgisLayer18Attributes
            | ArcgisFeatureServerArcgisLayer19Attributes
            | ArcgisFeatureServerArcgisLayer1Attributes
            | ArcgisFeatureServerArcgisLayer20Attributes
            | ArcgisFeatureServerArcgisLayer21Attributes
            | ArcgisFeatureServerArcgisLayer22Attributes
            | ArcgisFeatureServerArcgisLayer23Attributes
            | ArcgisFeatureServerArcgisLayer24Attributes
            | ArcgisFeatureServerArcgisLayer25Attributes
            | ArcgisFeatureServerArcgisLayer26Attributes
            | ArcgisFeatureServerArcgisLayer27Attributes
            | ArcgisFeatureServerArcgisLayer28Attributes
            | ArcgisFeatureServerArcgisLayer29Attributes
            | ArcgisFeatureServerArcgisLayer2Attributes
            | ArcgisFeatureServerArcgisLayer30Attributes
            | ArcgisFeatureServerArcgisLayer31Attributes
            | ArcgisFeatureServerArcgisLayer32Attributes
            | ArcgisFeatureServerArcgisLayer33Attributes
            | ArcgisFeatureServerArcgisLayer34Attributes
            | ArcgisFeatureServerArcgisLayer35Attributes
            | ArcgisFeatureServerArcgisLayer36Attributes
            | ArcgisFeatureServerArcgisLayer37Attributes
            | ArcgisFeatureServerArcgisLayer38Attributes
            | ArcgisFeatureServerArcgisLayer39Attributes
            | ArcgisFeatureServerArcgisLayer3Attributes
            | ArcgisFeatureServerArcgisLayer40Attributes
            | ArcgisFeatureServerArcgisLayer41Attributes
            | ArcgisFeatureServerArcgisLayer42Attributes
            | ArcgisFeatureServerArcgisLayer43Attributes
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
                    ArcgisFeatureServerArcgisLayer11Attributes.from_dict(data)
                )

                return properties_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_4 = (
                    ArcgisFeatureServerArcgisLayer12Attributes.from_dict(data)
                )

                return properties_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_5 = (
                    ArcgisFeatureServerArcgisLayer13Attributes.from_dict(data)
                )

                return properties_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_6 = (
                    ArcgisFeatureServerArcgisLayer14Attributes.from_dict(data)
                )

                return properties_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_7 = (
                    ArcgisFeatureServerArcgisLayer15Attributes.from_dict(data)
                )

                return properties_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_8 = (
                    ArcgisFeatureServerArcgisLayer16Attributes.from_dict(data)
                )

                return properties_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_9 = (
                    ArcgisFeatureServerArcgisLayer17Attributes.from_dict(data)
                )

                return properties_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_10 = (
                    ArcgisFeatureServerArcgisLayer18Attributes.from_dict(data)
                )

                return properties_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_11 = (
                    ArcgisFeatureServerArcgisLayer19Attributes.from_dict(data)
                )

                return properties_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_12 = (
                    ArcgisFeatureServerArcgisLayer2Attributes.from_dict(data)
                )

                return properties_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_13 = (
                    ArcgisFeatureServerArcgisLayer20Attributes.from_dict(data)
                )

                return properties_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_14 = (
                    ArcgisFeatureServerArcgisLayer21Attributes.from_dict(data)
                )

                return properties_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_15 = (
                    ArcgisFeatureServerArcgisLayer22Attributes.from_dict(data)
                )

                return properties_type_15
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_16 = (
                    ArcgisFeatureServerArcgisLayer23Attributes.from_dict(data)
                )

                return properties_type_16
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_17 = (
                    ArcgisFeatureServerArcgisLayer24Attributes.from_dict(data)
                )

                return properties_type_17
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_18 = (
                    ArcgisFeatureServerArcgisLayer25Attributes.from_dict(data)
                )

                return properties_type_18
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_19 = (
                    ArcgisFeatureServerArcgisLayer26Attributes.from_dict(data)
                )

                return properties_type_19
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_20 = (
                    ArcgisFeatureServerArcgisLayer27Attributes.from_dict(data)
                )

                return properties_type_20
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_21 = (
                    ArcgisFeatureServerArcgisLayer28Attributes.from_dict(data)
                )

                return properties_type_21
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_22 = (
                    ArcgisFeatureServerArcgisLayer29Attributes.from_dict(data)
                )

                return properties_type_22
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_23 = (
                    ArcgisFeatureServerArcgisLayer3Attributes.from_dict(data)
                )

                return properties_type_23
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_24 = (
                    ArcgisFeatureServerArcgisLayer30Attributes.from_dict(data)
                )

                return properties_type_24
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_25 = (
                    ArcgisFeatureServerArcgisLayer31Attributes.from_dict(data)
                )

                return properties_type_25
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_26 = (
                    ArcgisFeatureServerArcgisLayer32Attributes.from_dict(data)
                )

                return properties_type_26
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_27 = (
                    ArcgisFeatureServerArcgisLayer33Attributes.from_dict(data)
                )

                return properties_type_27
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_28 = (
                    ArcgisFeatureServerArcgisLayer34Attributes.from_dict(data)
                )

                return properties_type_28
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_29 = (
                    ArcgisFeatureServerArcgisLayer35Attributes.from_dict(data)
                )

                return properties_type_29
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_30 = (
                    ArcgisFeatureServerArcgisLayer36Attributes.from_dict(data)
                )

                return properties_type_30
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_31 = (
                    ArcgisFeatureServerArcgisLayer37Attributes.from_dict(data)
                )

                return properties_type_31
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_32 = (
                    ArcgisFeatureServerArcgisLayer38Attributes.from_dict(data)
                )

                return properties_type_32
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_33 = (
                    ArcgisFeatureServerArcgisLayer39Attributes.from_dict(data)
                )

                return properties_type_33
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_34 = (
                    ArcgisFeatureServerArcgisLayer4Attributes.from_dict(data)
                )

                return properties_type_34
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_35 = (
                    ArcgisFeatureServerArcgisLayer40Attributes.from_dict(data)
                )

                return properties_type_35
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_36 = (
                    ArcgisFeatureServerArcgisLayer41Attributes.from_dict(data)
                )

                return properties_type_36
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_37 = (
                    ArcgisFeatureServerArcgisLayer42Attributes.from_dict(data)
                )

                return properties_type_37
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_38 = (
                    ArcgisFeatureServerArcgisLayer43Attributes.from_dict(data)
                )

                return properties_type_38
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_39 = (
                    ArcgisFeatureServerArcgisLayer5Attributes.from_dict(data)
                )

                return properties_type_39
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_40 = (
                    ArcgisFeatureServerArcgisLayer6Attributes.from_dict(data)
                )

                return properties_type_40
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_41 = (
                    ArcgisFeatureServerArcgisLayer7Attributes.from_dict(data)
                )

                return properties_type_41
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_42 = (
                    ArcgisFeatureServerArcgisLayer8Attributes.from_dict(data)
                )

                return properties_type_42
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            properties_type_43 = ArcgisFeatureServerArcgisLayer9Attributes.from_dict(
                data
            )

            return properties_type_43

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
