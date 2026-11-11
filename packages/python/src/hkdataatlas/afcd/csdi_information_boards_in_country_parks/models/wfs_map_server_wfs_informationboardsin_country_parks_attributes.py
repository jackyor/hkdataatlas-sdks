from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsInformationboardsinCountryParksAttributes")


@_attrs_define
class WfsMapServerWfsInformationboardsinCountryParksAttributes:
    """
    Attributes:
        fac_id (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        x_ground (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        y_ground (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    fac_id: None | str | Unset = UNSET
    x_ground: float | None | Unset = UNSET
    y_ground: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fac_id: None | str | Unset
        if isinstance(self.fac_id, Unset):
            fac_id = UNSET
        else:
            fac_id = self.fac_id

        x_ground: float | None | Unset
        if isinstance(self.x_ground, Unset):
            x_ground = UNSET
        else:
            x_ground = self.x_ground

        y_ground: float | None | Unset
        if isinstance(self.y_ground, Unset):
            y_ground = UNSET
        else:
            y_ground = self.y_ground

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fac_id is not UNSET:
            field_dict["FAC_ID"] = fac_id
        if x_ground is not UNSET:
            field_dict["X_GROUND"] = x_ground
        if y_ground is not UNSET:
            field_dict["Y_GROUND"] = y_ground
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["Shape"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_fac_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_id = _parse_fac_id(d.pop("FAC_ID", UNSET))

        def _parse_x_ground(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        x_ground = _parse_x_ground(d.pop("X_GROUND", UNSET))

        def _parse_y_ground(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        y_ground = _parse_y_ground(d.pop("Y_GROUND", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("Shape", UNSET)

        wfs_map_server_wfs_informationboardsin_country_parks_attributes = cls(
            fac_id=fac_id,
            x_ground=x_ground,
            y_ground=y_ground,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfs_informationboardsin_country_parks_attributes.additional_properties = d
        return wfs_map_server_wfs_informationboardsin_country_parks_attributes

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
