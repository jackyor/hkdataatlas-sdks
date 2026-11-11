from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wfs_map_server_wfs_kbbaktba_attributes import (
        WfsMapServerWfsKBBAKTBAAttributes,
    )
    from ..models.wfs_map_server_wfs_table_23_attributes import (
        WfsMapServerWfsTable23Attributes,
    )
    from ..models.wfs_map_server_wfs_table_32_attributes import (
        WfsMapServerWfsTable32Attributes,
    )
    from ..models.wfs_map_server_wfs_table_210_attributes import (
        WfsMapServerWfsTable210Attributes,
    )
    from ..models.wfs_map_server_wfs_table_211_attributes import (
        WfsMapServerWfsTable211Attributes,
    )
    from ..models.wfs_map_server_wfs_table_216_attributes import (
        WfsMapServerWfsTable216Attributes,
    )
    from ..models.wfs_map_server_wfs_table_220_attributes import (
        WfsMapServerWfsTable220Attributes,
    )
    from ..models.wfs_map_server_wfs_table_224_attributes import (
        WfsMapServerWfsTable224Attributes,
    )
    from ..models.wfs_map_server_wfs_table_227_attributes import (
        WfsMapServerWfsTable227Attributes,
    )
    from ..models.wfs_map_server_wfs_table_241_attributes import (
        WfsMapServerWfsTable241Attributes,
    )
    from ..models.wfs_map_server_wfs_table_258_attributes import (
        WfsMapServerWfsTable258Attributes,
    )
    from ..models.wfs_map_server_wfs_table_261_attributes import (
        WfsMapServerWfsTable261Attributes,
    )
    from ..models.wfs_map_server_wfs_table_268_attributes import (
        WfsMapServerWfsTable268Attributes,
    )
    from ..models.wfs_map_server_wfs_table_270_attributes import (
        WfsMapServerWfsTable270Attributes,
    )
    from ..models.wfs_map_server_wfs_table_288_attributes import (
        WfsMapServerWfsTable288Attributes,
    )
    from ..models.wfs_map_server_wfs_table_296_attributes import (
        WfsMapServerWfsTable296Attributes,
    )
    from ..models.wfs_map_server_wfs_table_326_attributes import (
        WfsMapServerWfsTable326Attributes,
    )
    from ..models.wfs_map_server_wfs_table_347_attributes import (
        WfsMapServerWfsTable347Attributes,
    )
    from ..models.wfs_map_server_wfs_table_2109_attributes import (
        WfsMapServerWfsTable2109Attributes,
    )


T = TypeVar("T", bound="WfsMapServerWfsFeatureCollectionFeaturesItem")


@_attrs_define
class WfsMapServerWfsFeatureCollectionFeaturesItem:
    """
    Attributes:
        type_ (str | Unset):
        properties (Unset | WfsMapServerWfsKBBAKTBAAttributes | WfsMapServerWfsTable2109Attributes |
            WfsMapServerWfsTable210Attributes | WfsMapServerWfsTable211Attributes | WfsMapServerWfsTable216Attributes |
            WfsMapServerWfsTable220Attributes | WfsMapServerWfsTable224Attributes | WfsMapServerWfsTable227Attributes |
            WfsMapServerWfsTable23Attributes | WfsMapServerWfsTable241Attributes | WfsMapServerWfsTable258Attributes |
            WfsMapServerWfsTable261Attributes | WfsMapServerWfsTable268Attributes | WfsMapServerWfsTable270Attributes |
            WfsMapServerWfsTable288Attributes | WfsMapServerWfsTable296Attributes | WfsMapServerWfsTable326Attributes |
            WfsMapServerWfsTable32Attributes | WfsMapServerWfsTable347Attributes):
        geometry (Any | Unset): Geometry representation is not constrained by the retained attribute metadata.
    """

    type_: str | Unset = UNSET
    properties: (
        Unset
        | WfsMapServerWfsKBBAKTBAAttributes
        | WfsMapServerWfsTable2109Attributes
        | WfsMapServerWfsTable210Attributes
        | WfsMapServerWfsTable211Attributes
        | WfsMapServerWfsTable216Attributes
        | WfsMapServerWfsTable220Attributes
        | WfsMapServerWfsTable224Attributes
        | WfsMapServerWfsTable227Attributes
        | WfsMapServerWfsTable23Attributes
        | WfsMapServerWfsTable241Attributes
        | WfsMapServerWfsTable258Attributes
        | WfsMapServerWfsTable261Attributes
        | WfsMapServerWfsTable268Attributes
        | WfsMapServerWfsTable270Attributes
        | WfsMapServerWfsTable288Attributes
        | WfsMapServerWfsTable296Attributes
        | WfsMapServerWfsTable326Attributes
        | WfsMapServerWfsTable32Attributes
        | WfsMapServerWfsTable347Attributes
    ) = UNSET
    geometry: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wfs_map_server_wfs_kbbaktba_attributes import (
            WfsMapServerWfsKBBAKTBAAttributes,
        )
        from ..models.wfs_map_server_wfs_table_23_attributes import (
            WfsMapServerWfsTable23Attributes,
        )
        from ..models.wfs_map_server_wfs_table_32_attributes import (
            WfsMapServerWfsTable32Attributes,
        )
        from ..models.wfs_map_server_wfs_table_211_attributes import (
            WfsMapServerWfsTable211Attributes,
        )
        from ..models.wfs_map_server_wfs_table_216_attributes import (
            WfsMapServerWfsTable216Attributes,
        )
        from ..models.wfs_map_server_wfs_table_220_attributes import (
            WfsMapServerWfsTable220Attributes,
        )
        from ..models.wfs_map_server_wfs_table_224_attributes import (
            WfsMapServerWfsTable224Attributes,
        )
        from ..models.wfs_map_server_wfs_table_227_attributes import (
            WfsMapServerWfsTable227Attributes,
        )
        from ..models.wfs_map_server_wfs_table_241_attributes import (
            WfsMapServerWfsTable241Attributes,
        )
        from ..models.wfs_map_server_wfs_table_258_attributes import (
            WfsMapServerWfsTable258Attributes,
        )
        from ..models.wfs_map_server_wfs_table_261_attributes import (
            WfsMapServerWfsTable261Attributes,
        )
        from ..models.wfs_map_server_wfs_table_268_attributes import (
            WfsMapServerWfsTable268Attributes,
        )
        from ..models.wfs_map_server_wfs_table_270_attributes import (
            WfsMapServerWfsTable270Attributes,
        )
        from ..models.wfs_map_server_wfs_table_288_attributes import (
            WfsMapServerWfsTable288Attributes,
        )
        from ..models.wfs_map_server_wfs_table_296_attributes import (
            WfsMapServerWfsTable296Attributes,
        )
        from ..models.wfs_map_server_wfs_table_326_attributes import (
            WfsMapServerWfsTable326Attributes,
        )
        from ..models.wfs_map_server_wfs_table_347_attributes import (
            WfsMapServerWfsTable347Attributes,
        )
        from ..models.wfs_map_server_wfs_table_2109_attributes import (
            WfsMapServerWfsTable2109Attributes,
        )

        type_ = self.type_

        properties: dict[str, Any] | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif (
            isinstance(self.properties, WfsMapServerWfsKBBAKTBAAttributes)
            or isinstance(self.properties, WfsMapServerWfsTable347Attributes)
            or isinstance(self.properties, WfsMapServerWfsTable326Attributes)
            or isinstance(self.properties, WfsMapServerWfsTable32Attributes)
            or isinstance(self.properties, WfsMapServerWfsTable288Attributes)
            or isinstance(self.properties, WfsMapServerWfsTable270Attributes)
            or isinstance(self.properties, WfsMapServerWfsTable261Attributes)
            or isinstance(self.properties, WfsMapServerWfsTable258Attributes)
            or isinstance(self.properties, WfsMapServerWfsTable241Attributes)
            or isinstance(self.properties, WfsMapServerWfsTable23Attributes)
            or isinstance(self.properties, WfsMapServerWfsTable227Attributes)
            or isinstance(self.properties, WfsMapServerWfsTable224Attributes)
            or isinstance(self.properties, WfsMapServerWfsTable2109Attributes)
            or isinstance(self.properties, WfsMapServerWfsTable296Attributes)
            or isinstance(self.properties, WfsMapServerWfsTable268Attributes)
            or isinstance(self.properties, WfsMapServerWfsTable220Attributes)
            or isinstance(self.properties, WfsMapServerWfsTable216Attributes)
            or isinstance(self.properties, WfsMapServerWfsTable211Attributes)
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
        from ..models.wfs_map_server_wfs_kbbaktba_attributes import (
            WfsMapServerWfsKBBAKTBAAttributes,
        )
        from ..models.wfs_map_server_wfs_table_23_attributes import (
            WfsMapServerWfsTable23Attributes,
        )
        from ..models.wfs_map_server_wfs_table_32_attributes import (
            WfsMapServerWfsTable32Attributes,
        )
        from ..models.wfs_map_server_wfs_table_210_attributes import (
            WfsMapServerWfsTable210Attributes,
        )
        from ..models.wfs_map_server_wfs_table_211_attributes import (
            WfsMapServerWfsTable211Attributes,
        )
        from ..models.wfs_map_server_wfs_table_216_attributes import (
            WfsMapServerWfsTable216Attributes,
        )
        from ..models.wfs_map_server_wfs_table_220_attributes import (
            WfsMapServerWfsTable220Attributes,
        )
        from ..models.wfs_map_server_wfs_table_224_attributes import (
            WfsMapServerWfsTable224Attributes,
        )
        from ..models.wfs_map_server_wfs_table_227_attributes import (
            WfsMapServerWfsTable227Attributes,
        )
        from ..models.wfs_map_server_wfs_table_241_attributes import (
            WfsMapServerWfsTable241Attributes,
        )
        from ..models.wfs_map_server_wfs_table_258_attributes import (
            WfsMapServerWfsTable258Attributes,
        )
        from ..models.wfs_map_server_wfs_table_261_attributes import (
            WfsMapServerWfsTable261Attributes,
        )
        from ..models.wfs_map_server_wfs_table_268_attributes import (
            WfsMapServerWfsTable268Attributes,
        )
        from ..models.wfs_map_server_wfs_table_270_attributes import (
            WfsMapServerWfsTable270Attributes,
        )
        from ..models.wfs_map_server_wfs_table_288_attributes import (
            WfsMapServerWfsTable288Attributes,
        )
        from ..models.wfs_map_server_wfs_table_296_attributes import (
            WfsMapServerWfsTable296Attributes,
        )
        from ..models.wfs_map_server_wfs_table_326_attributes import (
            WfsMapServerWfsTable326Attributes,
        )
        from ..models.wfs_map_server_wfs_table_347_attributes import (
            WfsMapServerWfsTable347Attributes,
        )
        from ..models.wfs_map_server_wfs_table_2109_attributes import (
            WfsMapServerWfsTable2109Attributes,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        def _parse_properties(
            data: object,
        ) -> (
            Unset
            | WfsMapServerWfsKBBAKTBAAttributes
            | WfsMapServerWfsTable2109Attributes
            | WfsMapServerWfsTable210Attributes
            | WfsMapServerWfsTable211Attributes
            | WfsMapServerWfsTable216Attributes
            | WfsMapServerWfsTable220Attributes
            | WfsMapServerWfsTable224Attributes
            | WfsMapServerWfsTable227Attributes
            | WfsMapServerWfsTable23Attributes
            | WfsMapServerWfsTable241Attributes
            | WfsMapServerWfsTable258Attributes
            | WfsMapServerWfsTable261Attributes
            | WfsMapServerWfsTable268Attributes
            | WfsMapServerWfsTable270Attributes
            | WfsMapServerWfsTable288Attributes
            | WfsMapServerWfsTable296Attributes
            | WfsMapServerWfsTable326Attributes
            | WfsMapServerWfsTable32Attributes
            | WfsMapServerWfsTable347Attributes
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = WfsMapServerWfsKBBAKTBAAttributes.from_dict(data)

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_1 = WfsMapServerWfsTable347Attributes.from_dict(data)

                return properties_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_2 = WfsMapServerWfsTable326Attributes.from_dict(data)

                return properties_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_3 = WfsMapServerWfsTable32Attributes.from_dict(data)

                return properties_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_4 = WfsMapServerWfsTable288Attributes.from_dict(data)

                return properties_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_5 = WfsMapServerWfsTable270Attributes.from_dict(data)

                return properties_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_6 = WfsMapServerWfsTable261Attributes.from_dict(data)

                return properties_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_7 = WfsMapServerWfsTable258Attributes.from_dict(data)

                return properties_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_8 = WfsMapServerWfsTable241Attributes.from_dict(data)

                return properties_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_9 = WfsMapServerWfsTable23Attributes.from_dict(data)

                return properties_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_10 = WfsMapServerWfsTable227Attributes.from_dict(data)

                return properties_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_11 = WfsMapServerWfsTable224Attributes.from_dict(data)

                return properties_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_12 = WfsMapServerWfsTable2109Attributes.from_dict(data)

                return properties_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_13 = WfsMapServerWfsTable296Attributes.from_dict(data)

                return properties_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_14 = WfsMapServerWfsTable268Attributes.from_dict(data)

                return properties_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_15 = WfsMapServerWfsTable220Attributes.from_dict(data)

                return properties_type_15
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_16 = WfsMapServerWfsTable216Attributes.from_dict(data)

                return properties_type_16
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_17 = WfsMapServerWfsTable211Attributes.from_dict(data)

                return properties_type_17
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            properties_type_18 = WfsMapServerWfsTable210Attributes.from_dict(data)

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
