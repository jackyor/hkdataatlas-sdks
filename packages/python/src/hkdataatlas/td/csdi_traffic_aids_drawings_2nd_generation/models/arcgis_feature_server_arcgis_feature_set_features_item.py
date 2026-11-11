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
    from ..models.arcgis_feature_server_arcgis_layer_44_attributes import (
        ArcgisFeatureServerArcgisLayer44Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_45_attributes import (
        ArcgisFeatureServerArcgisLayer45Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_46_attributes import (
        ArcgisFeatureServerArcgisLayer46Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_47_attributes import (
        ArcgisFeatureServerArcgisLayer47Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_48_attributes import (
        ArcgisFeatureServerArcgisLayer48Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_49_attributes import (
        ArcgisFeatureServerArcgisLayer49Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_50_attributes import (
        ArcgisFeatureServerArcgisLayer50Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_51_attributes import (
        ArcgisFeatureServerArcgisLayer51Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_52_attributes import (
        ArcgisFeatureServerArcgisLayer52Attributes,
    )
    from ..models.arcgis_feature_server_arcgis_layer_53_attributes import (
        ArcgisFeatureServerArcgisLayer53Attributes,
    )


T = TypeVar("T", bound="ArcgisFeatureServerArcgisFeatureSetFeaturesItem")


@_attrs_define
class ArcgisFeatureServerArcgisFeatureSetFeaturesItem:
    """
    Attributes:
        attributes (ArcgisFeatureServerArcgisLayer0Attributes | ArcgisFeatureServerArcgisLayer10Attributes |
            ArcgisFeatureServerArcgisLayer11Attributes | ArcgisFeatureServerArcgisLayer12Attributes |
            ArcgisFeatureServerArcgisLayer13Attributes | ArcgisFeatureServerArcgisLayer14Attributes |
            ArcgisFeatureServerArcgisLayer15Attributes | ArcgisFeatureServerArcgisLayer16Attributes |
            ArcgisFeatureServerArcgisLayer17Attributes | ArcgisFeatureServerArcgisLayer18Attributes |
            ArcgisFeatureServerArcgisLayer19Attributes | ArcgisFeatureServerArcgisLayer1Attributes |
            ArcgisFeatureServerArcgisLayer20Attributes | ArcgisFeatureServerArcgisLayer21Attributes |
            ArcgisFeatureServerArcgisLayer24Attributes | ArcgisFeatureServerArcgisLayer25Attributes |
            ArcgisFeatureServerArcgisLayer26Attributes | ArcgisFeatureServerArcgisLayer27Attributes |
            ArcgisFeatureServerArcgisLayer28Attributes | ArcgisFeatureServerArcgisLayer29Attributes |
            ArcgisFeatureServerArcgisLayer2Attributes | ArcgisFeatureServerArcgisLayer32Attributes |
            ArcgisFeatureServerArcgisLayer33Attributes | ArcgisFeatureServerArcgisLayer34Attributes |
            ArcgisFeatureServerArcgisLayer35Attributes | ArcgisFeatureServerArcgisLayer36Attributes |
            ArcgisFeatureServerArcgisLayer37Attributes | ArcgisFeatureServerArcgisLayer3Attributes |
            ArcgisFeatureServerArcgisLayer40Attributes | ArcgisFeatureServerArcgisLayer41Attributes |
            ArcgisFeatureServerArcgisLayer42Attributes | ArcgisFeatureServerArcgisLayer43Attributes |
            ArcgisFeatureServerArcgisLayer44Attributes | ArcgisFeatureServerArcgisLayer45Attributes |
            ArcgisFeatureServerArcgisLayer46Attributes | ArcgisFeatureServerArcgisLayer47Attributes |
            ArcgisFeatureServerArcgisLayer48Attributes | ArcgisFeatureServerArcgisLayer49Attributes |
            ArcgisFeatureServerArcgisLayer4Attributes | ArcgisFeatureServerArcgisLayer50Attributes |
            ArcgisFeatureServerArcgisLayer51Attributes | ArcgisFeatureServerArcgisLayer52Attributes |
            ArcgisFeatureServerArcgisLayer53Attributes | ArcgisFeatureServerArcgisLayer5Attributes |
            ArcgisFeatureServerArcgisLayer6Attributes | ArcgisFeatureServerArcgisLayer7Attributes |
            ArcgisFeatureServerArcgisLayer8Attributes | ArcgisFeatureServerArcgisLayer9Attributes | Unset):
        geometry (Any | Unset): Native geometry and spatial reference are not constrained by attribute metadata.
    """

    attributes: (
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
        | ArcgisFeatureServerArcgisLayer24Attributes
        | ArcgisFeatureServerArcgisLayer25Attributes
        | ArcgisFeatureServerArcgisLayer26Attributes
        | ArcgisFeatureServerArcgisLayer27Attributes
        | ArcgisFeatureServerArcgisLayer28Attributes
        | ArcgisFeatureServerArcgisLayer29Attributes
        | ArcgisFeatureServerArcgisLayer2Attributes
        | ArcgisFeatureServerArcgisLayer32Attributes
        | ArcgisFeatureServerArcgisLayer33Attributes
        | ArcgisFeatureServerArcgisLayer34Attributes
        | ArcgisFeatureServerArcgisLayer35Attributes
        | ArcgisFeatureServerArcgisLayer36Attributes
        | ArcgisFeatureServerArcgisLayer37Attributes
        | ArcgisFeatureServerArcgisLayer3Attributes
        | ArcgisFeatureServerArcgisLayer40Attributes
        | ArcgisFeatureServerArcgisLayer41Attributes
        | ArcgisFeatureServerArcgisLayer42Attributes
        | ArcgisFeatureServerArcgisLayer43Attributes
        | ArcgisFeatureServerArcgisLayer44Attributes
        | ArcgisFeatureServerArcgisLayer45Attributes
        | ArcgisFeatureServerArcgisLayer46Attributes
        | ArcgisFeatureServerArcgisLayer47Attributes
        | ArcgisFeatureServerArcgisLayer48Attributes
        | ArcgisFeatureServerArcgisLayer49Attributes
        | ArcgisFeatureServerArcgisLayer4Attributes
        | ArcgisFeatureServerArcgisLayer50Attributes
        | ArcgisFeatureServerArcgisLayer51Attributes
        | ArcgisFeatureServerArcgisLayer52Attributes
        | ArcgisFeatureServerArcgisLayer53Attributes
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
        from ..models.arcgis_feature_server_arcgis_layer_44_attributes import (
            ArcgisFeatureServerArcgisLayer44Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_45_attributes import (
            ArcgisFeatureServerArcgisLayer45Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_46_attributes import (
            ArcgisFeatureServerArcgisLayer46Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_47_attributes import (
            ArcgisFeatureServerArcgisLayer47Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_48_attributes import (
            ArcgisFeatureServerArcgisLayer48Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_49_attributes import (
            ArcgisFeatureServerArcgisLayer49Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_50_attributes import (
            ArcgisFeatureServerArcgisLayer50Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_51_attributes import (
            ArcgisFeatureServerArcgisLayer51Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_52_attributes import (
            ArcgisFeatureServerArcgisLayer52Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_53_attributes import (
            ArcgisFeatureServerArcgisLayer53Attributes,
        )

        attributes: dict[str, Any] | Unset
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        elif (
            isinstance(self.attributes, ArcgisFeatureServerArcgisLayer0Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer1Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer10Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer11Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer12Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer13Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer14Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer15Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer16Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer17Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer18Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer19Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer2Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer20Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer21Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer24Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer25Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer26Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer27Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer28Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer29Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer3Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer32Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer33Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer34Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer35Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer36Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer37Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer4Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer40Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer41Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer42Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer43Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer44Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer45Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer46Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer47Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer48Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer49Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer5Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer50Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer51Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer52Attributes)
            or isinstance(self.attributes, ArcgisFeatureServerArcgisLayer53Attributes)
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
        from ..models.arcgis_feature_server_arcgis_layer_44_attributes import (
            ArcgisFeatureServerArcgisLayer44Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_45_attributes import (
            ArcgisFeatureServerArcgisLayer45Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_46_attributes import (
            ArcgisFeatureServerArcgisLayer46Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_47_attributes import (
            ArcgisFeatureServerArcgisLayer47Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_48_attributes import (
            ArcgisFeatureServerArcgisLayer48Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_49_attributes import (
            ArcgisFeatureServerArcgisLayer49Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_50_attributes import (
            ArcgisFeatureServerArcgisLayer50Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_51_attributes import (
            ArcgisFeatureServerArcgisLayer51Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_52_attributes import (
            ArcgisFeatureServerArcgisLayer52Attributes,
        )
        from ..models.arcgis_feature_server_arcgis_layer_53_attributes import (
            ArcgisFeatureServerArcgisLayer53Attributes,
        )

        d = dict(src_dict)

        def _parse_attributes(
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
            | ArcgisFeatureServerArcgisLayer24Attributes
            | ArcgisFeatureServerArcgisLayer25Attributes
            | ArcgisFeatureServerArcgisLayer26Attributes
            | ArcgisFeatureServerArcgisLayer27Attributes
            | ArcgisFeatureServerArcgisLayer28Attributes
            | ArcgisFeatureServerArcgisLayer29Attributes
            | ArcgisFeatureServerArcgisLayer2Attributes
            | ArcgisFeatureServerArcgisLayer32Attributes
            | ArcgisFeatureServerArcgisLayer33Attributes
            | ArcgisFeatureServerArcgisLayer34Attributes
            | ArcgisFeatureServerArcgisLayer35Attributes
            | ArcgisFeatureServerArcgisLayer36Attributes
            | ArcgisFeatureServerArcgisLayer37Attributes
            | ArcgisFeatureServerArcgisLayer3Attributes
            | ArcgisFeatureServerArcgisLayer40Attributes
            | ArcgisFeatureServerArcgisLayer41Attributes
            | ArcgisFeatureServerArcgisLayer42Attributes
            | ArcgisFeatureServerArcgisLayer43Attributes
            | ArcgisFeatureServerArcgisLayer44Attributes
            | ArcgisFeatureServerArcgisLayer45Attributes
            | ArcgisFeatureServerArcgisLayer46Attributes
            | ArcgisFeatureServerArcgisLayer47Attributes
            | ArcgisFeatureServerArcgisLayer48Attributes
            | ArcgisFeatureServerArcgisLayer49Attributes
            | ArcgisFeatureServerArcgisLayer4Attributes
            | ArcgisFeatureServerArcgisLayer50Attributes
            | ArcgisFeatureServerArcgisLayer51Attributes
            | ArcgisFeatureServerArcgisLayer52Attributes
            | ArcgisFeatureServerArcgisLayer53Attributes
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
                    ArcgisFeatureServerArcgisLayer11Attributes.from_dict(data)
                )

                return attributes_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_4 = (
                    ArcgisFeatureServerArcgisLayer12Attributes.from_dict(data)
                )

                return attributes_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_5 = (
                    ArcgisFeatureServerArcgisLayer13Attributes.from_dict(data)
                )

                return attributes_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_6 = (
                    ArcgisFeatureServerArcgisLayer14Attributes.from_dict(data)
                )

                return attributes_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_7 = (
                    ArcgisFeatureServerArcgisLayer15Attributes.from_dict(data)
                )

                return attributes_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_8 = (
                    ArcgisFeatureServerArcgisLayer16Attributes.from_dict(data)
                )

                return attributes_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_9 = (
                    ArcgisFeatureServerArcgisLayer17Attributes.from_dict(data)
                )

                return attributes_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_10 = (
                    ArcgisFeatureServerArcgisLayer18Attributes.from_dict(data)
                )

                return attributes_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_11 = (
                    ArcgisFeatureServerArcgisLayer19Attributes.from_dict(data)
                )

                return attributes_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_12 = (
                    ArcgisFeatureServerArcgisLayer2Attributes.from_dict(data)
                )

                return attributes_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_13 = (
                    ArcgisFeatureServerArcgisLayer20Attributes.from_dict(data)
                )

                return attributes_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_14 = (
                    ArcgisFeatureServerArcgisLayer21Attributes.from_dict(data)
                )

                return attributes_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_15 = (
                    ArcgisFeatureServerArcgisLayer24Attributes.from_dict(data)
                )

                return attributes_type_15
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_16 = (
                    ArcgisFeatureServerArcgisLayer25Attributes.from_dict(data)
                )

                return attributes_type_16
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_17 = (
                    ArcgisFeatureServerArcgisLayer26Attributes.from_dict(data)
                )

                return attributes_type_17
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_18 = (
                    ArcgisFeatureServerArcgisLayer27Attributes.from_dict(data)
                )

                return attributes_type_18
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_19 = (
                    ArcgisFeatureServerArcgisLayer28Attributes.from_dict(data)
                )

                return attributes_type_19
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_20 = (
                    ArcgisFeatureServerArcgisLayer29Attributes.from_dict(data)
                )

                return attributes_type_20
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_21 = (
                    ArcgisFeatureServerArcgisLayer3Attributes.from_dict(data)
                )

                return attributes_type_21
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_22 = (
                    ArcgisFeatureServerArcgisLayer32Attributes.from_dict(data)
                )

                return attributes_type_22
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_23 = (
                    ArcgisFeatureServerArcgisLayer33Attributes.from_dict(data)
                )

                return attributes_type_23
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_24 = (
                    ArcgisFeatureServerArcgisLayer34Attributes.from_dict(data)
                )

                return attributes_type_24
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_25 = (
                    ArcgisFeatureServerArcgisLayer35Attributes.from_dict(data)
                )

                return attributes_type_25
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_26 = (
                    ArcgisFeatureServerArcgisLayer36Attributes.from_dict(data)
                )

                return attributes_type_26
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_27 = (
                    ArcgisFeatureServerArcgisLayer37Attributes.from_dict(data)
                )

                return attributes_type_27
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_28 = (
                    ArcgisFeatureServerArcgisLayer4Attributes.from_dict(data)
                )

                return attributes_type_28
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_29 = (
                    ArcgisFeatureServerArcgisLayer40Attributes.from_dict(data)
                )

                return attributes_type_29
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_30 = (
                    ArcgisFeatureServerArcgisLayer41Attributes.from_dict(data)
                )

                return attributes_type_30
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_31 = (
                    ArcgisFeatureServerArcgisLayer42Attributes.from_dict(data)
                )

                return attributes_type_31
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_32 = (
                    ArcgisFeatureServerArcgisLayer43Attributes.from_dict(data)
                )

                return attributes_type_32
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_33 = (
                    ArcgisFeatureServerArcgisLayer44Attributes.from_dict(data)
                )

                return attributes_type_33
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_34 = (
                    ArcgisFeatureServerArcgisLayer45Attributes.from_dict(data)
                )

                return attributes_type_34
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_35 = (
                    ArcgisFeatureServerArcgisLayer46Attributes.from_dict(data)
                )

                return attributes_type_35
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_36 = (
                    ArcgisFeatureServerArcgisLayer47Attributes.from_dict(data)
                )

                return attributes_type_36
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_37 = (
                    ArcgisFeatureServerArcgisLayer48Attributes.from_dict(data)
                )

                return attributes_type_37
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_38 = (
                    ArcgisFeatureServerArcgisLayer49Attributes.from_dict(data)
                )

                return attributes_type_38
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_39 = (
                    ArcgisFeatureServerArcgisLayer5Attributes.from_dict(data)
                )

                return attributes_type_39
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_40 = (
                    ArcgisFeatureServerArcgisLayer50Attributes.from_dict(data)
                )

                return attributes_type_40
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_41 = (
                    ArcgisFeatureServerArcgisLayer51Attributes.from_dict(data)
                )

                return attributes_type_41
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_42 = (
                    ArcgisFeatureServerArcgisLayer52Attributes.from_dict(data)
                )

                return attributes_type_42
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_43 = (
                    ArcgisFeatureServerArcgisLayer53Attributes.from_dict(data)
                )

                return attributes_type_43
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_44 = (
                    ArcgisFeatureServerArcgisLayer6Attributes.from_dict(data)
                )

                return attributes_type_44
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_45 = (
                    ArcgisFeatureServerArcgisLayer7Attributes.from_dict(data)
                )

                return attributes_type_45
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_46 = (
                    ArcgisFeatureServerArcgisLayer8Attributes.from_dict(data)
                )

                return attributes_type_46
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            attributes_type_47 = ArcgisFeatureServerArcgisLayer9Attributes.from_dict(
                data
            )

            return attributes_type_47

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
