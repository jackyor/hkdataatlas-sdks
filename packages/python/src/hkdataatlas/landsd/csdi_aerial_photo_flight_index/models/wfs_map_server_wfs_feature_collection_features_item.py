from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wfs_map_server_wfs_flight_point_2016_attributes import (
        WfsMapServerWfsFlightPoint2016Attributes,
    )
    from ..models.wfs_map_server_wfs_flight_point_2017_attributes import (
        WfsMapServerWfsFlightPoint2017Attributes,
    )
    from ..models.wfs_map_server_wfs_flight_point_2018_attributes import (
        WfsMapServerWfsFlightPoint2018Attributes,
    )
    from ..models.wfs_map_server_wfs_flight_point_2019_attributes import (
        WfsMapServerWfsFlightPoint2019Attributes,
    )
    from ..models.wfs_map_server_wfs_flight_point_2020_attributes import (
        WfsMapServerWfsFlightPoint2020Attributes,
    )
    from ..models.wfs_map_server_wfs_flight_point_2021_attributes import (
        WfsMapServerWfsFlightPoint2021Attributes,
    )
    from ..models.wfs_map_server_wfs_flight_point_2022_attributes import (
        WfsMapServerWfsFlightPoint2022Attributes,
    )
    from ..models.wfs_map_server_wfs_flight_point_2023_attributes import (
        WfsMapServerWfsFlightPoint2023Attributes,
    )
    from ..models.wfs_map_server_wfs_flight_point_2024_attributes import (
        WfsMapServerWfsFlightPoint2024Attributes,
    )


T = TypeVar("T", bound="WfsMapServerWfsFeatureCollectionFeaturesItem")


@_attrs_define
class WfsMapServerWfsFeatureCollectionFeaturesItem:
    """
    Attributes:
        type_ (str | Unset):
        properties (Unset | WfsMapServerWfsFlightPoint2016Attributes | WfsMapServerWfsFlightPoint2017Attributes |
            WfsMapServerWfsFlightPoint2018Attributes | WfsMapServerWfsFlightPoint2019Attributes |
            WfsMapServerWfsFlightPoint2020Attributes | WfsMapServerWfsFlightPoint2021Attributes |
            WfsMapServerWfsFlightPoint2022Attributes | WfsMapServerWfsFlightPoint2023Attributes |
            WfsMapServerWfsFlightPoint2024Attributes):
        geometry (Any | Unset): Geometry representation is not constrained by the retained attribute metadata.
    """

    type_: str | Unset = UNSET
    properties: (
        Unset
        | WfsMapServerWfsFlightPoint2016Attributes
        | WfsMapServerWfsFlightPoint2017Attributes
        | WfsMapServerWfsFlightPoint2018Attributes
        | WfsMapServerWfsFlightPoint2019Attributes
        | WfsMapServerWfsFlightPoint2020Attributes
        | WfsMapServerWfsFlightPoint2021Attributes
        | WfsMapServerWfsFlightPoint2022Attributes
        | WfsMapServerWfsFlightPoint2023Attributes
        | WfsMapServerWfsFlightPoint2024Attributes
    ) = UNSET
    geometry: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wfs_map_server_wfs_flight_point_2017_attributes import (
            WfsMapServerWfsFlightPoint2017Attributes,
        )
        from ..models.wfs_map_server_wfs_flight_point_2018_attributes import (
            WfsMapServerWfsFlightPoint2018Attributes,
        )
        from ..models.wfs_map_server_wfs_flight_point_2019_attributes import (
            WfsMapServerWfsFlightPoint2019Attributes,
        )
        from ..models.wfs_map_server_wfs_flight_point_2020_attributes import (
            WfsMapServerWfsFlightPoint2020Attributes,
        )
        from ..models.wfs_map_server_wfs_flight_point_2021_attributes import (
            WfsMapServerWfsFlightPoint2021Attributes,
        )
        from ..models.wfs_map_server_wfs_flight_point_2022_attributes import (
            WfsMapServerWfsFlightPoint2022Attributes,
        )
        from ..models.wfs_map_server_wfs_flight_point_2023_attributes import (
            WfsMapServerWfsFlightPoint2023Attributes,
        )
        from ..models.wfs_map_server_wfs_flight_point_2024_attributes import (
            WfsMapServerWfsFlightPoint2024Attributes,
        )

        type_ = self.type_

        properties: dict[str, Any] | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif (
            isinstance(self.properties, WfsMapServerWfsFlightPoint2024Attributes)
            or isinstance(self.properties, WfsMapServerWfsFlightPoint2023Attributes)
            or isinstance(self.properties, WfsMapServerWfsFlightPoint2022Attributes)
            or isinstance(self.properties, WfsMapServerWfsFlightPoint2021Attributes)
            or isinstance(self.properties, WfsMapServerWfsFlightPoint2020Attributes)
            or isinstance(self.properties, WfsMapServerWfsFlightPoint2019Attributes)
            or isinstance(self.properties, WfsMapServerWfsFlightPoint2018Attributes)
            or isinstance(self.properties, WfsMapServerWfsFlightPoint2017Attributes)
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
        from ..models.wfs_map_server_wfs_flight_point_2016_attributes import (
            WfsMapServerWfsFlightPoint2016Attributes,
        )
        from ..models.wfs_map_server_wfs_flight_point_2017_attributes import (
            WfsMapServerWfsFlightPoint2017Attributes,
        )
        from ..models.wfs_map_server_wfs_flight_point_2018_attributes import (
            WfsMapServerWfsFlightPoint2018Attributes,
        )
        from ..models.wfs_map_server_wfs_flight_point_2019_attributes import (
            WfsMapServerWfsFlightPoint2019Attributes,
        )
        from ..models.wfs_map_server_wfs_flight_point_2020_attributes import (
            WfsMapServerWfsFlightPoint2020Attributes,
        )
        from ..models.wfs_map_server_wfs_flight_point_2021_attributes import (
            WfsMapServerWfsFlightPoint2021Attributes,
        )
        from ..models.wfs_map_server_wfs_flight_point_2022_attributes import (
            WfsMapServerWfsFlightPoint2022Attributes,
        )
        from ..models.wfs_map_server_wfs_flight_point_2023_attributes import (
            WfsMapServerWfsFlightPoint2023Attributes,
        )
        from ..models.wfs_map_server_wfs_flight_point_2024_attributes import (
            WfsMapServerWfsFlightPoint2024Attributes,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        def _parse_properties(
            data: object,
        ) -> (
            Unset
            | WfsMapServerWfsFlightPoint2016Attributes
            | WfsMapServerWfsFlightPoint2017Attributes
            | WfsMapServerWfsFlightPoint2018Attributes
            | WfsMapServerWfsFlightPoint2019Attributes
            | WfsMapServerWfsFlightPoint2020Attributes
            | WfsMapServerWfsFlightPoint2021Attributes
            | WfsMapServerWfsFlightPoint2022Attributes
            | WfsMapServerWfsFlightPoint2023Attributes
            | WfsMapServerWfsFlightPoint2024Attributes
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = WfsMapServerWfsFlightPoint2024Attributes.from_dict(
                    data
                )

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_1 = WfsMapServerWfsFlightPoint2023Attributes.from_dict(
                    data
                )

                return properties_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_2 = WfsMapServerWfsFlightPoint2022Attributes.from_dict(
                    data
                )

                return properties_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_3 = WfsMapServerWfsFlightPoint2021Attributes.from_dict(
                    data
                )

                return properties_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_4 = WfsMapServerWfsFlightPoint2020Attributes.from_dict(
                    data
                )

                return properties_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_5 = WfsMapServerWfsFlightPoint2019Attributes.from_dict(
                    data
                )

                return properties_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_6 = WfsMapServerWfsFlightPoint2018Attributes.from_dict(
                    data
                )

                return properties_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_7 = WfsMapServerWfsFlightPoint2017Attributes.from_dict(
                    data
                )

                return properties_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            properties_type_8 = WfsMapServerWfsFlightPoint2016Attributes.from_dict(data)

            return properties_type_8

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
