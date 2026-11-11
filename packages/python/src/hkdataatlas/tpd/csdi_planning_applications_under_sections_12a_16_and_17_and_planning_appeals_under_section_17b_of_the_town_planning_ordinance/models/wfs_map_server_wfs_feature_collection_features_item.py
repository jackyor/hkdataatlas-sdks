from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wfs_map_server_wfs_amendcrt_attributes import (
        WfsMapServerWfsAMENDCRTAttributes,
    )
    from ..models.wfs_map_server_wfs_amendpast_attributes import (
        WfsMapServerWfsAMENDPASTAttributes,
    )
    from ..models.wfs_map_server_wfs_appcrt_attributes import (
        WfsMapServerWfsAPPCRTAttributes,
    )
    from ..models.wfs_map_server_wfs_apppast_attributes import (
        WfsMapServerWfsAPPPASTAttributes,
    )


T = TypeVar("T", bound="WfsMapServerWfsFeatureCollectionFeaturesItem")


@_attrs_define
class WfsMapServerWfsFeatureCollectionFeaturesItem:
    """
    Attributes:
        type_ (str | Unset):
        properties (Unset | WfsMapServerWfsAMENDCRTAttributes | WfsMapServerWfsAMENDPASTAttributes |
            WfsMapServerWfsAPPCRTAttributes | WfsMapServerWfsAPPPASTAttributes):
        geometry (Any | Unset): Geometry representation is not constrained by the retained attribute metadata.
    """

    type_: str | Unset = UNSET
    properties: (
        Unset
        | WfsMapServerWfsAMENDCRTAttributes
        | WfsMapServerWfsAMENDPASTAttributes
        | WfsMapServerWfsAPPCRTAttributes
        | WfsMapServerWfsAPPPASTAttributes
    ) = UNSET
    geometry: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wfs_map_server_wfs_amendcrt_attributes import (
            WfsMapServerWfsAMENDCRTAttributes,
        )
        from ..models.wfs_map_server_wfs_amendpast_attributes import (
            WfsMapServerWfsAMENDPASTAttributes,
        )
        from ..models.wfs_map_server_wfs_apppast_attributes import (
            WfsMapServerWfsAPPPASTAttributes,
        )

        type_ = self.type_

        properties: dict[str, Any] | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif (
            isinstance(self.properties, WfsMapServerWfsAMENDPASTAttributes)
            or isinstance(self.properties, WfsMapServerWfsAMENDCRTAttributes)
            or isinstance(self.properties, WfsMapServerWfsAPPPASTAttributes)
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
        from ..models.wfs_map_server_wfs_amendcrt_attributes import (
            WfsMapServerWfsAMENDCRTAttributes,
        )
        from ..models.wfs_map_server_wfs_amendpast_attributes import (
            WfsMapServerWfsAMENDPASTAttributes,
        )
        from ..models.wfs_map_server_wfs_appcrt_attributes import (
            WfsMapServerWfsAPPCRTAttributes,
        )
        from ..models.wfs_map_server_wfs_apppast_attributes import (
            WfsMapServerWfsAPPPASTAttributes,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        def _parse_properties(
            data: object,
        ) -> (
            Unset
            | WfsMapServerWfsAMENDCRTAttributes
            | WfsMapServerWfsAMENDPASTAttributes
            | WfsMapServerWfsAPPCRTAttributes
            | WfsMapServerWfsAPPPASTAttributes
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = WfsMapServerWfsAMENDPASTAttributes.from_dict(data)

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_1 = WfsMapServerWfsAMENDCRTAttributes.from_dict(data)

                return properties_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_2 = WfsMapServerWfsAPPPASTAttributes.from_dict(data)

                return properties_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            properties_type_3 = WfsMapServerWfsAPPCRTAttributes.from_dict(data)

            return properties_type_3

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
