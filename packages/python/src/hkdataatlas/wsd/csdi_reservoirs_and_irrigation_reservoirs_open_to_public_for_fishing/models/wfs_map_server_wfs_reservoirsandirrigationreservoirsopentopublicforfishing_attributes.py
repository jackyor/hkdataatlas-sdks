from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="WfsMapServerWfsReservoirsandirrigationreservoirsopentopublicforfishingAttributes",
)


@_attrs_define
class WfsMapServerWfsReservoirsandirrigationreservoirsopentopublicforfishingAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        installation_id (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        chinese_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        x_coord (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        y_coord (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    installation_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    chinese_name: None | str | Unset = UNSET
    x_coord: float | None | Unset = UNSET
    y_coord: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        installation_id: None | str | Unset
        if isinstance(self.installation_id, Unset):
            installation_id = UNSET
        else:
            installation_id = self.installation_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        chinese_name: None | str | Unset
        if isinstance(self.chinese_name, Unset):
            chinese_name = UNSET
        else:
            chinese_name = self.chinese_name

        x_coord: float | None | Unset
        if isinstance(self.x_coord, Unset):
            x_coord = UNSET
        else:
            x_coord = self.x_coord

        y_coord: float | None | Unset
        if isinstance(self.y_coord, Unset):
            y_coord = UNSET
        else:
            y_coord = self.y_coord

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if installation_id is not UNSET:
            field_dict["INSTALLATION_ID"] = installation_id
        if name is not UNSET:
            field_dict["NAME"] = name
        if chinese_name is not UNSET:
            field_dict["CHINESE_NAME"] = chinese_name
        if x_coord is not UNSET:
            field_dict["X_COORD"] = x_coord
        if y_coord is not UNSET:
            field_dict["Y_COORD"] = y_coord

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("Shape", UNSET)

        def _parse_installation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        installation_id = _parse_installation_id(d.pop("INSTALLATION_ID", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("NAME", UNSET))

        def _parse_chinese_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinese_name = _parse_chinese_name(d.pop("CHINESE_NAME", UNSET))

        def _parse_x_coord(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        x_coord = _parse_x_coord(d.pop("X_COORD", UNSET))

        def _parse_y_coord(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        y_coord = _parse_y_coord(d.pop("Y_COORD", UNSET))

        wfs_map_server_wfs_reservoirsandirrigationreservoirsopentopublicforfishing_attributes = cls(
            objectid=objectid,
            shape=shape,
            installation_id=installation_id,
            name=name,
            chinese_name=chinese_name,
            x_coord=x_coord,
            y_coord=y_coord,
        )

        wfs_map_server_wfs_reservoirsandirrigationreservoirsopentopublicforfishing_attributes.additional_properties = d
        return wfs_map_server_wfs_reservoirsandirrigationreservoirsopentopublicforfishing_attributes

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
