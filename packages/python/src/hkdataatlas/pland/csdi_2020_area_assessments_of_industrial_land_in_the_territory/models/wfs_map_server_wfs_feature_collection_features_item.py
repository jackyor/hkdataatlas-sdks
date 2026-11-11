from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wfs_map_server_wfs_aa_attributes import WfsMapServerWfsAAAttributes
    from ..models.wfs_map_server_wfs_table_1_attributes import (
        WfsMapServerWfsTable1Attributes,
    )
    from ..models.wfs_map_server_wfs_table_2a_attributes import (
        WfsMapServerWfsTable2AAttributes,
    )
    from ..models.wfs_map_server_wfs_table_2b_attributes import (
        WfsMapServerWfsTable2BAttributes,
    )
    from ..models.wfs_map_server_wfs_table_3a_attributes import (
        WfsMapServerWfsTable3AAttributes,
    )
    from ..models.wfs_map_server_wfs_table_3b_attributes import (
        WfsMapServerWfsTable3BAttributes,
    )
    from ..models.wfs_map_server_wfs_table_3c_attributes import (
        WfsMapServerWfsTable3CAttributes,
    )
    from ..models.wfs_map_server_wfs_table_3d_attributes import (
        WfsMapServerWfsTable3DAttributes,
    )
    from ..models.wfs_map_server_wfs_table_3e_attributes import (
        WfsMapServerWfsTable3EAttributes,
    )
    from ..models.wfs_map_server_wfs_table_4_attributes import (
        WfsMapServerWfsTable4Attributes,
    )
    from ..models.wfs_map_server_wfs_table_5a_attributes import (
        WfsMapServerWfsTable5AAttributes,
    )
    from ..models.wfs_map_server_wfs_table_5b_attributes import (
        WfsMapServerWfsTable5BAttributes,
    )
    from ..models.wfs_map_server_wfs_table_6_attributes import (
        WfsMapServerWfsTable6Attributes,
    )
    from ..models.wfs_map_server_wfs_table_7_attributes import (
        WfsMapServerWfsTable7Attributes,
    )
    from ..models.wfs_map_server_wfs_table_8a_attributes import (
        WfsMapServerWfsTable8AAttributes,
    )
    from ..models.wfs_map_server_wfs_table_8b_attributes import (
        WfsMapServerWfsTable8BAttributes,
    )
    from ..models.wfs_map_server_wfs_table_8c_attributes import (
        WfsMapServerWfsTable8CAttributes,
    )
    from ..models.wfs_map_server_wfs_table_8d_attributes import (
        WfsMapServerWfsTable8DAttributes,
    )
    from ..models.wfs_map_server_wfs_table_9_attributes import (
        WfsMapServerWfsTable9Attributes,
    )


T = TypeVar("T", bound="WfsMapServerWfsFeatureCollectionFeaturesItem")


@_attrs_define
class WfsMapServerWfsFeatureCollectionFeaturesItem:
    """
    Attributes:
        type_ (str | Unset):
        properties (Unset | WfsMapServerWfsAAAttributes | WfsMapServerWfsTable1Attributes |
            WfsMapServerWfsTable2AAttributes | WfsMapServerWfsTable2BAttributes | WfsMapServerWfsTable3AAttributes |
            WfsMapServerWfsTable3BAttributes | WfsMapServerWfsTable3CAttributes | WfsMapServerWfsTable3DAttributes |
            WfsMapServerWfsTable3EAttributes | WfsMapServerWfsTable4Attributes | WfsMapServerWfsTable5AAttributes |
            WfsMapServerWfsTable5BAttributes | WfsMapServerWfsTable6Attributes | WfsMapServerWfsTable7Attributes |
            WfsMapServerWfsTable8AAttributes | WfsMapServerWfsTable8BAttributes | WfsMapServerWfsTable8CAttributes |
            WfsMapServerWfsTable8DAttributes | WfsMapServerWfsTable9Attributes):
        geometry (Any | Unset): Geometry representation is not constrained by the retained attribute metadata.
    """

    type_: str | Unset = UNSET
    properties: (
        Unset
        | WfsMapServerWfsAAAttributes
        | WfsMapServerWfsTable1Attributes
        | WfsMapServerWfsTable2AAttributes
        | WfsMapServerWfsTable2BAttributes
        | WfsMapServerWfsTable3AAttributes
        | WfsMapServerWfsTable3BAttributes
        | WfsMapServerWfsTable3CAttributes
        | WfsMapServerWfsTable3DAttributes
        | WfsMapServerWfsTable3EAttributes
        | WfsMapServerWfsTable4Attributes
        | WfsMapServerWfsTable5AAttributes
        | WfsMapServerWfsTable5BAttributes
        | WfsMapServerWfsTable6Attributes
        | WfsMapServerWfsTable7Attributes
        | WfsMapServerWfsTable8AAttributes
        | WfsMapServerWfsTable8BAttributes
        | WfsMapServerWfsTable8CAttributes
        | WfsMapServerWfsTable8DAttributes
        | WfsMapServerWfsTable9Attributes
    ) = UNSET
    geometry: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wfs_map_server_wfs_aa_attributes import (
            WfsMapServerWfsAAAttributes,
        )
        from ..models.wfs_map_server_wfs_table_2a_attributes import (
            WfsMapServerWfsTable2AAttributes,
        )
        from ..models.wfs_map_server_wfs_table_2b_attributes import (
            WfsMapServerWfsTable2BAttributes,
        )
        from ..models.wfs_map_server_wfs_table_3a_attributes import (
            WfsMapServerWfsTable3AAttributes,
        )
        from ..models.wfs_map_server_wfs_table_3b_attributes import (
            WfsMapServerWfsTable3BAttributes,
        )
        from ..models.wfs_map_server_wfs_table_3c_attributes import (
            WfsMapServerWfsTable3CAttributes,
        )
        from ..models.wfs_map_server_wfs_table_3d_attributes import (
            WfsMapServerWfsTable3DAttributes,
        )
        from ..models.wfs_map_server_wfs_table_3e_attributes import (
            WfsMapServerWfsTable3EAttributes,
        )
        from ..models.wfs_map_server_wfs_table_4_attributes import (
            WfsMapServerWfsTable4Attributes,
        )
        from ..models.wfs_map_server_wfs_table_5a_attributes import (
            WfsMapServerWfsTable5AAttributes,
        )
        from ..models.wfs_map_server_wfs_table_5b_attributes import (
            WfsMapServerWfsTable5BAttributes,
        )
        from ..models.wfs_map_server_wfs_table_6_attributes import (
            WfsMapServerWfsTable6Attributes,
        )
        from ..models.wfs_map_server_wfs_table_7_attributes import (
            WfsMapServerWfsTable7Attributes,
        )
        from ..models.wfs_map_server_wfs_table_8a_attributes import (
            WfsMapServerWfsTable8AAttributes,
        )
        from ..models.wfs_map_server_wfs_table_8b_attributes import (
            WfsMapServerWfsTable8BAttributes,
        )
        from ..models.wfs_map_server_wfs_table_8c_attributes import (
            WfsMapServerWfsTable8CAttributes,
        )
        from ..models.wfs_map_server_wfs_table_8d_attributes import (
            WfsMapServerWfsTable8DAttributes,
        )
        from ..models.wfs_map_server_wfs_table_9_attributes import (
            WfsMapServerWfsTable9Attributes,
        )

        type_ = self.type_

        properties: dict[str, Any] | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif (
            isinstance(self.properties, WfsMapServerWfsAAAttributes)
            or isinstance(self.properties, WfsMapServerWfsTable2BAttributes)
            or isinstance(self.properties, WfsMapServerWfsTable3AAttributes)
            or isinstance(self.properties, WfsMapServerWfsTable3BAttributes)
            or isinstance(self.properties, WfsMapServerWfsTable3CAttributes)
            or isinstance(self.properties, WfsMapServerWfsTable3DAttributes)
            or isinstance(self.properties, WfsMapServerWfsTable3EAttributes)
            or isinstance(self.properties, WfsMapServerWfsTable4Attributes)
            or isinstance(self.properties, WfsMapServerWfsTable5AAttributes)
            or isinstance(self.properties, WfsMapServerWfsTable5BAttributes)
            or isinstance(self.properties, WfsMapServerWfsTable6Attributes)
            or isinstance(self.properties, WfsMapServerWfsTable7Attributes)
            or isinstance(self.properties, WfsMapServerWfsTable8AAttributes)
            or isinstance(self.properties, WfsMapServerWfsTable8BAttributes)
            or isinstance(self.properties, WfsMapServerWfsTable8CAttributes)
            or isinstance(self.properties, WfsMapServerWfsTable8DAttributes)
            or isinstance(self.properties, WfsMapServerWfsTable9Attributes)
            or isinstance(self.properties, WfsMapServerWfsTable2AAttributes)
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
        from ..models.wfs_map_server_wfs_aa_attributes import (
            WfsMapServerWfsAAAttributes,
        )
        from ..models.wfs_map_server_wfs_table_1_attributes import (
            WfsMapServerWfsTable1Attributes,
        )
        from ..models.wfs_map_server_wfs_table_2a_attributes import (
            WfsMapServerWfsTable2AAttributes,
        )
        from ..models.wfs_map_server_wfs_table_2b_attributes import (
            WfsMapServerWfsTable2BAttributes,
        )
        from ..models.wfs_map_server_wfs_table_3a_attributes import (
            WfsMapServerWfsTable3AAttributes,
        )
        from ..models.wfs_map_server_wfs_table_3b_attributes import (
            WfsMapServerWfsTable3BAttributes,
        )
        from ..models.wfs_map_server_wfs_table_3c_attributes import (
            WfsMapServerWfsTable3CAttributes,
        )
        from ..models.wfs_map_server_wfs_table_3d_attributes import (
            WfsMapServerWfsTable3DAttributes,
        )
        from ..models.wfs_map_server_wfs_table_3e_attributes import (
            WfsMapServerWfsTable3EAttributes,
        )
        from ..models.wfs_map_server_wfs_table_4_attributes import (
            WfsMapServerWfsTable4Attributes,
        )
        from ..models.wfs_map_server_wfs_table_5a_attributes import (
            WfsMapServerWfsTable5AAttributes,
        )
        from ..models.wfs_map_server_wfs_table_5b_attributes import (
            WfsMapServerWfsTable5BAttributes,
        )
        from ..models.wfs_map_server_wfs_table_6_attributes import (
            WfsMapServerWfsTable6Attributes,
        )
        from ..models.wfs_map_server_wfs_table_7_attributes import (
            WfsMapServerWfsTable7Attributes,
        )
        from ..models.wfs_map_server_wfs_table_8a_attributes import (
            WfsMapServerWfsTable8AAttributes,
        )
        from ..models.wfs_map_server_wfs_table_8b_attributes import (
            WfsMapServerWfsTable8BAttributes,
        )
        from ..models.wfs_map_server_wfs_table_8c_attributes import (
            WfsMapServerWfsTable8CAttributes,
        )
        from ..models.wfs_map_server_wfs_table_8d_attributes import (
            WfsMapServerWfsTable8DAttributes,
        )
        from ..models.wfs_map_server_wfs_table_9_attributes import (
            WfsMapServerWfsTable9Attributes,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        def _parse_properties(
            data: object,
        ) -> (
            Unset
            | WfsMapServerWfsAAAttributes
            | WfsMapServerWfsTable1Attributes
            | WfsMapServerWfsTable2AAttributes
            | WfsMapServerWfsTable2BAttributes
            | WfsMapServerWfsTable3AAttributes
            | WfsMapServerWfsTable3BAttributes
            | WfsMapServerWfsTable3CAttributes
            | WfsMapServerWfsTable3DAttributes
            | WfsMapServerWfsTable3EAttributes
            | WfsMapServerWfsTable4Attributes
            | WfsMapServerWfsTable5AAttributes
            | WfsMapServerWfsTable5BAttributes
            | WfsMapServerWfsTable6Attributes
            | WfsMapServerWfsTable7Attributes
            | WfsMapServerWfsTable8AAttributes
            | WfsMapServerWfsTable8BAttributes
            | WfsMapServerWfsTable8CAttributes
            | WfsMapServerWfsTable8DAttributes
            | WfsMapServerWfsTable9Attributes
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = WfsMapServerWfsAAAttributes.from_dict(data)

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_1 = WfsMapServerWfsTable2BAttributes.from_dict(data)

                return properties_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_2 = WfsMapServerWfsTable3AAttributes.from_dict(data)

                return properties_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_3 = WfsMapServerWfsTable3BAttributes.from_dict(data)

                return properties_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_4 = WfsMapServerWfsTable3CAttributes.from_dict(data)

                return properties_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_5 = WfsMapServerWfsTable3DAttributes.from_dict(data)

                return properties_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_6 = WfsMapServerWfsTable3EAttributes.from_dict(data)

                return properties_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_7 = WfsMapServerWfsTable4Attributes.from_dict(data)

                return properties_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_8 = WfsMapServerWfsTable5AAttributes.from_dict(data)

                return properties_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_9 = WfsMapServerWfsTable5BAttributes.from_dict(data)

                return properties_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_10 = WfsMapServerWfsTable6Attributes.from_dict(data)

                return properties_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_11 = WfsMapServerWfsTable7Attributes.from_dict(data)

                return properties_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_12 = WfsMapServerWfsTable8AAttributes.from_dict(data)

                return properties_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_13 = WfsMapServerWfsTable8BAttributes.from_dict(data)

                return properties_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_14 = WfsMapServerWfsTable8CAttributes.from_dict(data)

                return properties_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_15 = WfsMapServerWfsTable8DAttributes.from_dict(data)

                return properties_type_15
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_16 = WfsMapServerWfsTable9Attributes.from_dict(data)

                return properties_type_16
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_17 = WfsMapServerWfsTable2AAttributes.from_dict(data)

                return properties_type_17
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            properties_type_18 = WfsMapServerWfsTable1Attributes.from_dict(data)

            return properties_type_18

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
