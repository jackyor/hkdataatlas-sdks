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


T = TypeVar("T", bound="ArcgisFeatureServerArcgisJsonEnvelopeFeaturesItem")


@_attrs_define
class ArcgisFeatureServerArcgisJsonEnvelopeFeaturesItem:
    """
    Attributes:
        type_ (str | Unset):
        attributes (ArcgisFeatureServerArcgisLayer0Attributes | ArcgisFeatureServerArcgisLayer1Attributes | Unset):
        properties (ArcgisFeatureServerArcgisLayer0Attributes | ArcgisFeatureServerArcgisLayer1Attributes | Unset):
        geometry (Any | Unset): Geometry is not constrained by attribute metadata.
    """

    type_: str | Unset = UNSET
    attributes: (
        ArcgisFeatureServerArcgisLayer0Attributes
        | ArcgisFeatureServerArcgisLayer1Attributes
        | Unset
    ) = UNSET
    properties: (
        ArcgisFeatureServerArcgisLayer0Attributes
        | ArcgisFeatureServerArcgisLayer1Attributes
        | Unset
    ) = UNSET
    geometry: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.arcgis_feature_server_arcgis_layer_0_attributes import (
            ArcgisFeatureServerArcgisLayer0Attributes,
        )

        type_ = self.type_

        attributes: dict[str, Any] | Unset
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        elif isinstance(self.attributes, ArcgisFeatureServerArcgisLayer0Attributes):
            attributes = self.attributes.to_dict()
        else:
            attributes = self.attributes.to_dict()

        properties: dict[str, Any] | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif isinstance(self.properties, ArcgisFeatureServerArcgisLayer0Attributes):
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

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        def _parse_attributes(
            data: object,
        ) -> (
            ArcgisFeatureServerArcgisLayer0Attributes
            | ArcgisFeatureServerArcgisLayer1Attributes
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
            if not isinstance(data, dict):
                raise TypeError()
            attributes_type_1 = ArcgisFeatureServerArcgisLayer1Attributes.from_dict(
                data
            )

            return attributes_type_1

        attributes = _parse_attributes(d.pop("attributes", UNSET))

        def _parse_properties(
            data: object,
        ) -> (
            ArcgisFeatureServerArcgisLayer0Attributes
            | ArcgisFeatureServerArcgisLayer1Attributes
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
            if not isinstance(data, dict):
                raise TypeError()
            properties_type_1 = ArcgisFeatureServerArcgisLayer1Attributes.from_dict(
                data
            )

            return properties_type_1

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
