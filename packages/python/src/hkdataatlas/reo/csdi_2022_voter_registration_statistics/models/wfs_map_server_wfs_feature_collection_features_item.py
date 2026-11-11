from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wfs_map_server_wfs_vr2022dccafull_attributes import (
        WfsMapServerWfsVR2022DCCAFULLAttributes,
    )
    from ..models.wfs_map_server_wfs_vr2022dccanr_attributes import (
        WfsMapServerWfsVR2022DCCANRAttributes,
    )
    from ..models.wfs_map_server_wfs_vr2022dcfull_attributes import (
        WfsMapServerWfsVR2022DCFULLAttributes,
    )
    from ..models.wfs_map_server_wfs_vr2022dcnr_attributes import (
        WfsMapServerWfsVR2022DCNRAttributes,
    )
    from ..models.wfs_map_server_wfs_vr2022gcfull_attributes import (
        WfsMapServerWfsVR2022GCFULLAttributes,
    )
    from ..models.wfs_map_server_wfs_vr2022lcfull_attributes import (
        WfsMapServerWfsVR2022LCFULLAttributes,
    )
    from ..models.wfs_map_server_wfs_vr2022lcnr_attributes import (
        WfsMapServerWfsVR2022LCNRAttributes,
    )


T = TypeVar("T", bound="WfsMapServerWfsFeatureCollectionFeaturesItem")


@_attrs_define
class WfsMapServerWfsFeatureCollectionFeaturesItem:
    """
    Attributes:
        type_ (str | Unset):
        properties (Unset | WfsMapServerWfsVR2022DCCAFULLAttributes | WfsMapServerWfsVR2022DCCANRAttributes |
            WfsMapServerWfsVR2022DCFULLAttributes | WfsMapServerWfsVR2022DCNRAttributes |
            WfsMapServerWfsVR2022GCFULLAttributes | WfsMapServerWfsVR2022LCFULLAttributes |
            WfsMapServerWfsVR2022LCNRAttributes):
        geometry (Any | Unset): Geometry representation is not constrained by the retained attribute metadata.
    """

    type_: str | Unset = UNSET
    properties: (
        Unset
        | WfsMapServerWfsVR2022DCCAFULLAttributes
        | WfsMapServerWfsVR2022DCCANRAttributes
        | WfsMapServerWfsVR2022DCFULLAttributes
        | WfsMapServerWfsVR2022DCNRAttributes
        | WfsMapServerWfsVR2022GCFULLAttributes
        | WfsMapServerWfsVR2022LCFULLAttributes
        | WfsMapServerWfsVR2022LCNRAttributes
    ) = UNSET
    geometry: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wfs_map_server_wfs_vr2022dccafull_attributes import (
            WfsMapServerWfsVR2022DCCAFULLAttributes,
        )
        from ..models.wfs_map_server_wfs_vr2022dccanr_attributes import (
            WfsMapServerWfsVR2022DCCANRAttributes,
        )
        from ..models.wfs_map_server_wfs_vr2022dcnr_attributes import (
            WfsMapServerWfsVR2022DCNRAttributes,
        )
        from ..models.wfs_map_server_wfs_vr2022gcfull_attributes import (
            WfsMapServerWfsVR2022GCFULLAttributes,
        )
        from ..models.wfs_map_server_wfs_vr2022lcfull_attributes import (
            WfsMapServerWfsVR2022LCFULLAttributes,
        )
        from ..models.wfs_map_server_wfs_vr2022lcnr_attributes import (
            WfsMapServerWfsVR2022LCNRAttributes,
        )

        type_ = self.type_

        properties: dict[str, Any] | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif (
            isinstance(self.properties, WfsMapServerWfsVR2022LCNRAttributes)
            or isinstance(self.properties, WfsMapServerWfsVR2022LCFULLAttributes)
            or isinstance(self.properties, WfsMapServerWfsVR2022GCFULLAttributes)
            or isinstance(self.properties, WfsMapServerWfsVR2022DCCANRAttributes)
            or isinstance(self.properties, WfsMapServerWfsVR2022DCCAFULLAttributes)
            or isinstance(self.properties, WfsMapServerWfsVR2022DCNRAttributes)
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
        from ..models.wfs_map_server_wfs_vr2022dccafull_attributes import (
            WfsMapServerWfsVR2022DCCAFULLAttributes,
        )
        from ..models.wfs_map_server_wfs_vr2022dccanr_attributes import (
            WfsMapServerWfsVR2022DCCANRAttributes,
        )
        from ..models.wfs_map_server_wfs_vr2022dcfull_attributes import (
            WfsMapServerWfsVR2022DCFULLAttributes,
        )
        from ..models.wfs_map_server_wfs_vr2022dcnr_attributes import (
            WfsMapServerWfsVR2022DCNRAttributes,
        )
        from ..models.wfs_map_server_wfs_vr2022gcfull_attributes import (
            WfsMapServerWfsVR2022GCFULLAttributes,
        )
        from ..models.wfs_map_server_wfs_vr2022lcfull_attributes import (
            WfsMapServerWfsVR2022LCFULLAttributes,
        )
        from ..models.wfs_map_server_wfs_vr2022lcnr_attributes import (
            WfsMapServerWfsVR2022LCNRAttributes,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        def _parse_properties(
            data: object,
        ) -> (
            Unset
            | WfsMapServerWfsVR2022DCCAFULLAttributes
            | WfsMapServerWfsVR2022DCCANRAttributes
            | WfsMapServerWfsVR2022DCFULLAttributes
            | WfsMapServerWfsVR2022DCNRAttributes
            | WfsMapServerWfsVR2022GCFULLAttributes
            | WfsMapServerWfsVR2022LCFULLAttributes
            | WfsMapServerWfsVR2022LCNRAttributes
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = WfsMapServerWfsVR2022LCNRAttributes.from_dict(data)

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_1 = WfsMapServerWfsVR2022LCFULLAttributes.from_dict(
                    data
                )

                return properties_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_2 = WfsMapServerWfsVR2022GCFULLAttributes.from_dict(
                    data
                )

                return properties_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_3 = WfsMapServerWfsVR2022DCCANRAttributes.from_dict(
                    data
                )

                return properties_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_4 = WfsMapServerWfsVR2022DCCAFULLAttributes.from_dict(
                    data
                )

                return properties_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_5 = WfsMapServerWfsVR2022DCNRAttributes.from_dict(data)

                return properties_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            properties_type_6 = WfsMapServerWfsVR2022DCFULLAttributes.from_dict(data)

            return properties_type_6

        properties = _parse_properties(d.pop("properties", UNSET))

        geometry = d.pop("geometry", UNSET)

        wfs_map_server_wfs_feature_collection_features_item = cls(
            type_=type_,
            properties=properties,
            geometry=geometry,
        )

        wfs_map_server_wfs_feature_collection_features_item.additional_properties = d
        return wfs_map_server_wfs_feature_collection_features_item

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
