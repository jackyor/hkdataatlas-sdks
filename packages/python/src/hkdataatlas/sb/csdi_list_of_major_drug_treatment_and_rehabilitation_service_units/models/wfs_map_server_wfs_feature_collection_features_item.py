from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wfs_map_server_wfs_ccps_as_attributes import (
        WfsMapServerWfsCCPSAsAttributes,
    )
    from ..models.wfs_map_server_wfs_cd_cs_attributes import (
        WfsMapServerWfsCDCsAttributes,
    )
    from ..models.wfs_map_server_wfs_dat_cs_attributes import (
        WfsMapServerWfsDATCsAttributes,
    )
    from ..models.wfs_map_server_wfs_m_cs_attributes import WfsMapServerWfsMCsAttributes
    from ..models.wfs_map_server_wfs_sa_cs_attributes import (
        WfsMapServerWfsSACsAttributes,
    )


T = TypeVar("T", bound="WfsMapServerWfsFeatureCollectionFeaturesItem")


@_attrs_define
class WfsMapServerWfsFeatureCollectionFeaturesItem:
    """
    Attributes:
        type_ (str | Unset):
        properties (Unset | WfsMapServerWfsCCPSAsAttributes | WfsMapServerWfsCDCsAttributes |
            WfsMapServerWfsDATCsAttributes | WfsMapServerWfsMCsAttributes | WfsMapServerWfsSACsAttributes):
        geometry (Any | Unset): Geometry representation is not constrained by the retained attribute metadata.
    """

    type_: str | Unset = UNSET
    properties: (
        Unset
        | WfsMapServerWfsCCPSAsAttributes
        | WfsMapServerWfsCDCsAttributes
        | WfsMapServerWfsDATCsAttributes
        | WfsMapServerWfsMCsAttributes
        | WfsMapServerWfsSACsAttributes
    ) = UNSET
    geometry: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wfs_map_server_wfs_ccps_as_attributes import (
            WfsMapServerWfsCCPSAsAttributes,
        )
        from ..models.wfs_map_server_wfs_cd_cs_attributes import (
            WfsMapServerWfsCDCsAttributes,
        )
        from ..models.wfs_map_server_wfs_m_cs_attributes import (
            WfsMapServerWfsMCsAttributes,
        )
        from ..models.wfs_map_server_wfs_sa_cs_attributes import (
            WfsMapServerWfsSACsAttributes,
        )

        type_ = self.type_

        properties: dict[str, Any] | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif (
            isinstance(self.properties, WfsMapServerWfsCCPSAsAttributes)
            or isinstance(self.properties, WfsMapServerWfsCDCsAttributes)
            or isinstance(self.properties, WfsMapServerWfsSACsAttributes)
            or isinstance(self.properties, WfsMapServerWfsMCsAttributes)
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
        from ..models.wfs_map_server_wfs_ccps_as_attributes import (
            WfsMapServerWfsCCPSAsAttributes,
        )
        from ..models.wfs_map_server_wfs_cd_cs_attributes import (
            WfsMapServerWfsCDCsAttributes,
        )
        from ..models.wfs_map_server_wfs_dat_cs_attributes import (
            WfsMapServerWfsDATCsAttributes,
        )
        from ..models.wfs_map_server_wfs_m_cs_attributes import (
            WfsMapServerWfsMCsAttributes,
        )
        from ..models.wfs_map_server_wfs_sa_cs_attributes import (
            WfsMapServerWfsSACsAttributes,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        def _parse_properties(
            data: object,
        ) -> (
            Unset
            | WfsMapServerWfsCCPSAsAttributes
            | WfsMapServerWfsCDCsAttributes
            | WfsMapServerWfsDATCsAttributes
            | WfsMapServerWfsMCsAttributes
            | WfsMapServerWfsSACsAttributes
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = WfsMapServerWfsCCPSAsAttributes.from_dict(data)

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_1 = WfsMapServerWfsCDCsAttributes.from_dict(data)

                return properties_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_2 = WfsMapServerWfsSACsAttributes.from_dict(data)

                return properties_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_3 = WfsMapServerWfsMCsAttributes.from_dict(data)

                return properties_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            properties_type_4 = WfsMapServerWfsDATCsAttributes.from_dict(data)

            return properties_type_4

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
