from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wfs_map_server_wfs_fill_attributes import (
        WfsMapServerWfsFillAttributes,
    )
    from ..models.wfs_map_server_wfs_geolandstrulines_attributes import (
        WfsMapServerWfsGeolandstrulinesAttributes,
    )
    from ..models.wfs_map_server_wfs_mineralannotations_attributes import (
        WfsMapServerWfsMineralannotationsAttributes,
    )
    from ..models.wfs_map_server_wfs_misclines_attributes import (
        WfsMapServerWfsMisclinesAttributes,
    )
    from ..models.wfs_map_server_wfs_miscsymbols_attributes import (
        WfsMapServerWfsMiscsymbolsAttributes,
    )
    from ..models.wfs_map_server_wfs_solidgeology_attributes import (
        WfsMapServerWfsSolidgeologyAttributes,
    )
    from ..models.wfs_map_server_wfs_structuralsymbols_attributes import (
        WfsMapServerWfsStructuralsymbolsAttributes,
    )
    from ..models.wfs_map_server_wfs_superficialgeology_attributes import (
        WfsMapServerWfsSuperficialgeologyAttributes,
    )
    from ..models.wfs_map_server_wfs_textureandmeta_attributes import (
        WfsMapServerWfsTextureandmetaAttributes,
    )
    from ..models.wfs_map_server_wfshkgrid_20k_attributes import (
        WfsMapServerWfshkgrid20KAttributes,
    )


T = TypeVar("T", bound="WfsMapServerWfsFeatureCollectionFeaturesItem")


@_attrs_define
class WfsMapServerWfsFeatureCollectionFeaturesItem:
    """
    Attributes:
        type_ (str | Unset):
        properties (Unset | WfsMapServerWfsFillAttributes | WfsMapServerWfsGeolandstrulinesAttributes |
            WfsMapServerWfshkgrid20KAttributes | WfsMapServerWfsMineralannotationsAttributes |
            WfsMapServerWfsMisclinesAttributes | WfsMapServerWfsMiscsymbolsAttributes |
            WfsMapServerWfsSolidgeologyAttributes | WfsMapServerWfsStructuralsymbolsAttributes |
            WfsMapServerWfsSuperficialgeologyAttributes | WfsMapServerWfsTextureandmetaAttributes):
        geometry (Any | Unset): Geometry representation is not constrained by the retained attribute metadata.
    """

    type_: str | Unset = UNSET
    properties: (
        Unset
        | WfsMapServerWfsFillAttributes
        | WfsMapServerWfsGeolandstrulinesAttributes
        | WfsMapServerWfshkgrid20KAttributes
        | WfsMapServerWfsMineralannotationsAttributes
        | WfsMapServerWfsMisclinesAttributes
        | WfsMapServerWfsMiscsymbolsAttributes
        | WfsMapServerWfsSolidgeologyAttributes
        | WfsMapServerWfsStructuralsymbolsAttributes
        | WfsMapServerWfsSuperficialgeologyAttributes
        | WfsMapServerWfsTextureandmetaAttributes
    ) = UNSET
    geometry: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wfs_map_server_wfs_fill_attributes import (
            WfsMapServerWfsFillAttributes,
        )
        from ..models.wfs_map_server_wfs_geolandstrulines_attributes import (
            WfsMapServerWfsGeolandstrulinesAttributes,
        )
        from ..models.wfs_map_server_wfs_mineralannotations_attributes import (
            WfsMapServerWfsMineralannotationsAttributes,
        )
        from ..models.wfs_map_server_wfs_misclines_attributes import (
            WfsMapServerWfsMisclinesAttributes,
        )
        from ..models.wfs_map_server_wfs_miscsymbols_attributes import (
            WfsMapServerWfsMiscsymbolsAttributes,
        )
        from ..models.wfs_map_server_wfs_solidgeology_attributes import (
            WfsMapServerWfsSolidgeologyAttributes,
        )
        from ..models.wfs_map_server_wfs_structuralsymbols_attributes import (
            WfsMapServerWfsStructuralsymbolsAttributes,
        )
        from ..models.wfs_map_server_wfs_superficialgeology_attributes import (
            WfsMapServerWfsSuperficialgeologyAttributes,
        )
        from ..models.wfs_map_server_wfs_textureandmeta_attributes import (
            WfsMapServerWfsTextureandmetaAttributes,
        )

        type_ = self.type_

        properties: dict[str, Any] | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif (
            isinstance(self.properties, WfsMapServerWfsStructuralsymbolsAttributes)
            or isinstance(self.properties, WfsMapServerWfsMiscsymbolsAttributes)
            or isinstance(self.properties, WfsMapServerWfsGeolandstrulinesAttributes)
            or isinstance(self.properties, WfsMapServerWfsMineralannotationsAttributes)
            or isinstance(self.properties, WfsMapServerWfsMisclinesAttributes)
            or isinstance(self.properties, WfsMapServerWfsSolidgeologyAttributes)
            or isinstance(self.properties, WfsMapServerWfsTextureandmetaAttributes)
            or isinstance(self.properties, WfsMapServerWfsSuperficialgeologyAttributes)
            or isinstance(self.properties, WfsMapServerWfsFillAttributes)
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
        from ..models.wfs_map_server_wfs_fill_attributes import (
            WfsMapServerWfsFillAttributes,
        )
        from ..models.wfs_map_server_wfs_geolandstrulines_attributes import (
            WfsMapServerWfsGeolandstrulinesAttributes,
        )
        from ..models.wfs_map_server_wfs_mineralannotations_attributes import (
            WfsMapServerWfsMineralannotationsAttributes,
        )
        from ..models.wfs_map_server_wfs_misclines_attributes import (
            WfsMapServerWfsMisclinesAttributes,
        )
        from ..models.wfs_map_server_wfs_miscsymbols_attributes import (
            WfsMapServerWfsMiscsymbolsAttributes,
        )
        from ..models.wfs_map_server_wfs_solidgeology_attributes import (
            WfsMapServerWfsSolidgeologyAttributes,
        )
        from ..models.wfs_map_server_wfs_structuralsymbols_attributes import (
            WfsMapServerWfsStructuralsymbolsAttributes,
        )
        from ..models.wfs_map_server_wfs_superficialgeology_attributes import (
            WfsMapServerWfsSuperficialgeologyAttributes,
        )
        from ..models.wfs_map_server_wfs_textureandmeta_attributes import (
            WfsMapServerWfsTextureandmetaAttributes,
        )
        from ..models.wfs_map_server_wfshkgrid_20k_attributes import (
            WfsMapServerWfshkgrid20KAttributes,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        def _parse_properties(
            data: object,
        ) -> (
            Unset
            | WfsMapServerWfsFillAttributes
            | WfsMapServerWfsGeolandstrulinesAttributes
            | WfsMapServerWfshkgrid20KAttributes
            | WfsMapServerWfsMineralannotationsAttributes
            | WfsMapServerWfsMisclinesAttributes
            | WfsMapServerWfsMiscsymbolsAttributes
            | WfsMapServerWfsSolidgeologyAttributes
            | WfsMapServerWfsStructuralsymbolsAttributes
            | WfsMapServerWfsSuperficialgeologyAttributes
            | WfsMapServerWfsTextureandmetaAttributes
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = (
                    WfsMapServerWfsStructuralsymbolsAttributes.from_dict(data)
                )

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_1 = WfsMapServerWfsMiscsymbolsAttributes.from_dict(data)

                return properties_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_2 = WfsMapServerWfsGeolandstrulinesAttributes.from_dict(
                    data
                )

                return properties_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_3 = (
                    WfsMapServerWfsMineralannotationsAttributes.from_dict(data)
                )

                return properties_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_4 = WfsMapServerWfsMisclinesAttributes.from_dict(data)

                return properties_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_5 = WfsMapServerWfsSolidgeologyAttributes.from_dict(
                    data
                )

                return properties_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_6 = WfsMapServerWfsTextureandmetaAttributes.from_dict(
                    data
                )

                return properties_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_7 = (
                    WfsMapServerWfsSuperficialgeologyAttributes.from_dict(data)
                )

                return properties_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_8 = WfsMapServerWfsFillAttributes.from_dict(data)

                return properties_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            properties_type_9 = WfsMapServerWfshkgrid20KAttributes.from_dict(data)

            return properties_type_9

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
