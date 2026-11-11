from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wfs_map_server_wfs_bdryanno_attributes import (
        WfsMapServerWfsBDRYANNOAttributes,
    )
    from ..models.wfs_map_server_wfs_bdryline_attributes import (
        WfsMapServerWfsBDRYLINEAttributes,
    )
    from ..models.wfs_map_server_wfs_bldgpoly_attributes import (
        WfsMapServerWfsBLDGPOLYAttributes,
    )
    from ..models.wfs_map_server_wfs_elevanno_attributes import (
        WfsMapServerWfsELEVANNOAttributes,
    )
    from ..models.wfs_map_server_wfs_elevline_attributes import (
        WfsMapServerWfsELEVLINEAttributes,
    )
    from ..models.wfs_map_server_wfs_elevpoly_attributes import (
        WfsMapServerWfsELEVPOLYAttributes,
    )
    from ..models.wfs_map_server_wfs_elevsymbol_attributes import (
        WfsMapServerWfsELEVSYMBOLAttributes,
    )
    from ..models.wfs_map_server_wfs_hydranno_attributes import (
        WfsMapServerWfsHYDRANNOAttributes,
    )
    from ..models.wfs_map_server_wfs_hydrline_attributes import (
        WfsMapServerWfsHYDRLINEAttributes,
    )
    from ..models.wfs_map_server_wfs_hydrpoly_attributes import (
        WfsMapServerWfsHYDRPOLYAttributes,
    )
    from ..models.wfs_map_server_wfs_landpoly_attributes import (
        WfsMapServerWfsLANDPOLYAttributes,
    )
    from ..models.wfs_map_server_wfs_placanno_attributes import (
        WfsMapServerWfsPLACANNOAttributes,
    )
    from ..models.wfs_map_server_wfs_tsptanno_attributes import (
        WfsMapServerWfsTSPTANNOAttributes,
    )
    from ..models.wfs_map_server_wfs_tsptline_attributes import (
        WfsMapServerWfsTSPTLINEAttributes,
    )


T = TypeVar("T", bound="WfsMapServerWfsFeatureCollectionFeaturesItem")


@_attrs_define
class WfsMapServerWfsFeatureCollectionFeaturesItem:
    """
    Attributes:
        type_ (str | Unset):
        properties (Unset | WfsMapServerWfsBDRYANNOAttributes | WfsMapServerWfsBDRYLINEAttributes |
            WfsMapServerWfsBLDGPOLYAttributes | WfsMapServerWfsELEVANNOAttributes | WfsMapServerWfsELEVLINEAttributes |
            WfsMapServerWfsELEVPOLYAttributes | WfsMapServerWfsELEVSYMBOLAttributes | WfsMapServerWfsHYDRANNOAttributes |
            WfsMapServerWfsHYDRLINEAttributes | WfsMapServerWfsHYDRPOLYAttributes | WfsMapServerWfsLANDPOLYAttributes |
            WfsMapServerWfsPLACANNOAttributes | WfsMapServerWfsTSPTANNOAttributes | WfsMapServerWfsTSPTLINEAttributes):
        geometry (Any | Unset): Geometry representation is not constrained by the retained attribute metadata.
    """

    type_: str | Unset = UNSET
    properties: (
        Unset
        | WfsMapServerWfsBDRYANNOAttributes
        | WfsMapServerWfsBDRYLINEAttributes
        | WfsMapServerWfsBLDGPOLYAttributes
        | WfsMapServerWfsELEVANNOAttributes
        | WfsMapServerWfsELEVLINEAttributes
        | WfsMapServerWfsELEVPOLYAttributes
        | WfsMapServerWfsELEVSYMBOLAttributes
        | WfsMapServerWfsHYDRANNOAttributes
        | WfsMapServerWfsHYDRLINEAttributes
        | WfsMapServerWfsHYDRPOLYAttributes
        | WfsMapServerWfsLANDPOLYAttributes
        | WfsMapServerWfsPLACANNOAttributes
        | WfsMapServerWfsTSPTANNOAttributes
        | WfsMapServerWfsTSPTLINEAttributes
    ) = UNSET
    geometry: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wfs_map_server_wfs_bdryanno_attributes import (
            WfsMapServerWfsBDRYANNOAttributes,
        )
        from ..models.wfs_map_server_wfs_bdryline_attributes import (
            WfsMapServerWfsBDRYLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_bldgpoly_attributes import (
            WfsMapServerWfsBLDGPOLYAttributes,
        )
        from ..models.wfs_map_server_wfs_elevanno_attributes import (
            WfsMapServerWfsELEVANNOAttributes,
        )
        from ..models.wfs_map_server_wfs_elevline_attributes import (
            WfsMapServerWfsELEVLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_elevpoly_attributes import (
            WfsMapServerWfsELEVPOLYAttributes,
        )
        from ..models.wfs_map_server_wfs_elevsymbol_attributes import (
            WfsMapServerWfsELEVSYMBOLAttributes,
        )
        from ..models.wfs_map_server_wfs_hydranno_attributes import (
            WfsMapServerWfsHYDRANNOAttributes,
        )
        from ..models.wfs_map_server_wfs_hydrline_attributes import (
            WfsMapServerWfsHYDRLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_hydrpoly_attributes import (
            WfsMapServerWfsHYDRPOLYAttributes,
        )
        from ..models.wfs_map_server_wfs_placanno_attributes import (
            WfsMapServerWfsPLACANNOAttributes,
        )
        from ..models.wfs_map_server_wfs_tsptanno_attributes import (
            WfsMapServerWfsTSPTANNOAttributes,
        )
        from ..models.wfs_map_server_wfs_tsptline_attributes import (
            WfsMapServerWfsTSPTLINEAttributes,
        )

        type_ = self.type_

        properties: dict[str, Any] | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif (
            isinstance(self.properties, WfsMapServerWfsELEVSYMBOLAttributes)
            or isinstance(self.properties, WfsMapServerWfsELEVANNOAttributes)
            or isinstance(self.properties, WfsMapServerWfsTSPTANNOAttributes)
            or isinstance(self.properties, WfsMapServerWfsHYDRANNOAttributes)
            or isinstance(self.properties, WfsMapServerWfsPLACANNOAttributes)
            or isinstance(self.properties, WfsMapServerWfsBDRYANNOAttributes)
            or isinstance(self.properties, WfsMapServerWfsHYDRLINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsELEVLINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsTSPTLINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsBDRYLINEAttributes)
            or isinstance(self.properties, WfsMapServerWfsHYDRPOLYAttributes)
            or isinstance(self.properties, WfsMapServerWfsBLDGPOLYAttributes)
            or isinstance(self.properties, WfsMapServerWfsELEVPOLYAttributes)
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
        from ..models.wfs_map_server_wfs_bdryanno_attributes import (
            WfsMapServerWfsBDRYANNOAttributes,
        )
        from ..models.wfs_map_server_wfs_bdryline_attributes import (
            WfsMapServerWfsBDRYLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_bldgpoly_attributes import (
            WfsMapServerWfsBLDGPOLYAttributes,
        )
        from ..models.wfs_map_server_wfs_elevanno_attributes import (
            WfsMapServerWfsELEVANNOAttributes,
        )
        from ..models.wfs_map_server_wfs_elevline_attributes import (
            WfsMapServerWfsELEVLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_elevpoly_attributes import (
            WfsMapServerWfsELEVPOLYAttributes,
        )
        from ..models.wfs_map_server_wfs_elevsymbol_attributes import (
            WfsMapServerWfsELEVSYMBOLAttributes,
        )
        from ..models.wfs_map_server_wfs_hydranno_attributes import (
            WfsMapServerWfsHYDRANNOAttributes,
        )
        from ..models.wfs_map_server_wfs_hydrline_attributes import (
            WfsMapServerWfsHYDRLINEAttributes,
        )
        from ..models.wfs_map_server_wfs_hydrpoly_attributes import (
            WfsMapServerWfsHYDRPOLYAttributes,
        )
        from ..models.wfs_map_server_wfs_landpoly_attributes import (
            WfsMapServerWfsLANDPOLYAttributes,
        )
        from ..models.wfs_map_server_wfs_placanno_attributes import (
            WfsMapServerWfsPLACANNOAttributes,
        )
        from ..models.wfs_map_server_wfs_tsptanno_attributes import (
            WfsMapServerWfsTSPTANNOAttributes,
        )
        from ..models.wfs_map_server_wfs_tsptline_attributes import (
            WfsMapServerWfsTSPTLINEAttributes,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        def _parse_properties(
            data: object,
        ) -> (
            Unset
            | WfsMapServerWfsBDRYANNOAttributes
            | WfsMapServerWfsBDRYLINEAttributes
            | WfsMapServerWfsBLDGPOLYAttributes
            | WfsMapServerWfsELEVANNOAttributes
            | WfsMapServerWfsELEVLINEAttributes
            | WfsMapServerWfsELEVPOLYAttributes
            | WfsMapServerWfsELEVSYMBOLAttributes
            | WfsMapServerWfsHYDRANNOAttributes
            | WfsMapServerWfsHYDRLINEAttributes
            | WfsMapServerWfsHYDRPOLYAttributes
            | WfsMapServerWfsLANDPOLYAttributes
            | WfsMapServerWfsPLACANNOAttributes
            | WfsMapServerWfsTSPTANNOAttributes
            | WfsMapServerWfsTSPTLINEAttributes
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = WfsMapServerWfsELEVSYMBOLAttributes.from_dict(data)

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_1 = WfsMapServerWfsELEVANNOAttributes.from_dict(data)

                return properties_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_2 = WfsMapServerWfsTSPTANNOAttributes.from_dict(data)

                return properties_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_3 = WfsMapServerWfsHYDRANNOAttributes.from_dict(data)

                return properties_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_4 = WfsMapServerWfsPLACANNOAttributes.from_dict(data)

                return properties_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_5 = WfsMapServerWfsBDRYANNOAttributes.from_dict(data)

                return properties_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_6 = WfsMapServerWfsHYDRLINEAttributes.from_dict(data)

                return properties_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_7 = WfsMapServerWfsELEVLINEAttributes.from_dict(data)

                return properties_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_8 = WfsMapServerWfsTSPTLINEAttributes.from_dict(data)

                return properties_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_9 = WfsMapServerWfsBDRYLINEAttributes.from_dict(data)

                return properties_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_10 = WfsMapServerWfsHYDRPOLYAttributes.from_dict(data)

                return properties_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_11 = WfsMapServerWfsBLDGPOLYAttributes.from_dict(data)

                return properties_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_12 = WfsMapServerWfsELEVPOLYAttributes.from_dict(data)

                return properties_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            properties_type_13 = WfsMapServerWfsLANDPOLYAttributes.from_dict(data)

            return properties_type_13

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
