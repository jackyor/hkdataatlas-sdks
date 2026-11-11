from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        route_id (int | None | Unset): Publisher field type: esriFieldTypeInteger
        route_seq (int | None | Unset): Publisher field type: esriFieldTypeInteger
        public_transport (None | str | Unset): Publisher field type: esriFieldTypeString
        route_name (None | str | Unset): Publisher field type: esriFieldTypeString
        st_stop_id (int | None | Unset): Publisher field type: esriFieldTypeInteger
        st_stop_namee (None | str | Unset): Publisher field type: esriFieldTypeString
        st_stop_namec (None | str | Unset): Publisher field type: esriFieldTypeString
        st_stop_names (None | str | Unset): Publisher field type: esriFieldTypeString
        ed_stop_id (int | None | Unset): Publisher field type: esriFieldTypeInteger
        ed_stop_namee (None | str | Unset): Publisher field type: esriFieldTypeString
        ed_stop_namec (None | str | Unset): Publisher field type: esriFieldTypeString
        ed_stop_names (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    route_id: int | None | Unset = UNSET
    route_seq: int | None | Unset = UNSET
    public_transport: None | str | Unset = UNSET
    route_name: None | str | Unset = UNSET
    st_stop_id: int | None | Unset = UNSET
    st_stop_namee: None | str | Unset = UNSET
    st_stop_namec: None | str | Unset = UNSET
    st_stop_names: None | str | Unset = UNSET
    ed_stop_id: int | None | Unset = UNSET
    ed_stop_namee: None | str | Unset = UNSET
    ed_stop_namec: None | str | Unset = UNSET
    ed_stop_names: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        route_id: int | None | Unset
        if isinstance(self.route_id, Unset):
            route_id = UNSET
        else:
            route_id = self.route_id

        route_seq: int | None | Unset
        if isinstance(self.route_seq, Unset):
            route_seq = UNSET
        else:
            route_seq = self.route_seq

        public_transport: None | str | Unset
        if isinstance(self.public_transport, Unset):
            public_transport = UNSET
        else:
            public_transport = self.public_transport

        route_name: None | str | Unset
        if isinstance(self.route_name, Unset):
            route_name = UNSET
        else:
            route_name = self.route_name

        st_stop_id: int | None | Unset
        if isinstance(self.st_stop_id, Unset):
            st_stop_id = UNSET
        else:
            st_stop_id = self.st_stop_id

        st_stop_namee: None | str | Unset
        if isinstance(self.st_stop_namee, Unset):
            st_stop_namee = UNSET
        else:
            st_stop_namee = self.st_stop_namee

        st_stop_namec: None | str | Unset
        if isinstance(self.st_stop_namec, Unset):
            st_stop_namec = UNSET
        else:
            st_stop_namec = self.st_stop_namec

        st_stop_names: None | str | Unset
        if isinstance(self.st_stop_names, Unset):
            st_stop_names = UNSET
        else:
            st_stop_names = self.st_stop_names

        ed_stop_id: int | None | Unset
        if isinstance(self.ed_stop_id, Unset):
            ed_stop_id = UNSET
        else:
            ed_stop_id = self.ed_stop_id

        ed_stop_namee: None | str | Unset
        if isinstance(self.ed_stop_namee, Unset):
            ed_stop_namee = UNSET
        else:
            ed_stop_namee = self.ed_stop_namee

        ed_stop_namec: None | str | Unset
        if isinstance(self.ed_stop_namec, Unset):
            ed_stop_namec = UNSET
        else:
            ed_stop_namec = self.ed_stop_namec

        ed_stop_names: None | str | Unset
        if isinstance(self.ed_stop_names, Unset):
            ed_stop_names = UNSET
        else:
            ed_stop_names = self.ed_stop_names

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if route_id is not UNSET:
            field_dict["ROUTE_ID"] = route_id
        if route_seq is not UNSET:
            field_dict["ROUTE_SEQ"] = route_seq
        if public_transport is not UNSET:
            field_dict["PUBLIC_TRANSPORT"] = public_transport
        if route_name is not UNSET:
            field_dict["ROUTE_NAME"] = route_name
        if st_stop_id is not UNSET:
            field_dict["ST_STOP_ID"] = st_stop_id
        if st_stop_namee is not UNSET:
            field_dict["ST_STOP_NAMEE"] = st_stop_namee
        if st_stop_namec is not UNSET:
            field_dict["ST_STOP_NAMEC"] = st_stop_namec
        if st_stop_names is not UNSET:
            field_dict["ST_STOP_NAMES"] = st_stop_names
        if ed_stop_id is not UNSET:
            field_dict["ED_STOP_ID"] = ed_stop_id
        if ed_stop_namee is not UNSET:
            field_dict["ED_STOP_NAMEE"] = ed_stop_namee
        if ed_stop_namec is not UNSET:
            field_dict["ED_STOP_NAMEC"] = ed_stop_namec
        if ed_stop_names is not UNSET:
            field_dict["ED_STOP_NAMES"] = ed_stop_names
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_route_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        route_id = _parse_route_id(d.pop("ROUTE_ID", UNSET))

        def _parse_route_seq(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        route_seq = _parse_route_seq(d.pop("ROUTE_SEQ", UNSET))

        def _parse_public_transport(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_transport = _parse_public_transport(d.pop("PUBLIC_TRANSPORT", UNSET))

        def _parse_route_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        route_name = _parse_route_name(d.pop("ROUTE_NAME", UNSET))

        def _parse_st_stop_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        st_stop_id = _parse_st_stop_id(d.pop("ST_STOP_ID", UNSET))

        def _parse_st_stop_namee(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        st_stop_namee = _parse_st_stop_namee(d.pop("ST_STOP_NAMEE", UNSET))

        def _parse_st_stop_namec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        st_stop_namec = _parse_st_stop_namec(d.pop("ST_STOP_NAMEC", UNSET))

        def _parse_st_stop_names(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        st_stop_names = _parse_st_stop_names(d.pop("ST_STOP_NAMES", UNSET))

        def _parse_ed_stop_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ed_stop_id = _parse_ed_stop_id(d.pop("ED_STOP_ID", UNSET))

        def _parse_ed_stop_namee(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ed_stop_namee = _parse_ed_stop_namee(d.pop("ED_STOP_NAMEE", UNSET))

        def _parse_ed_stop_namec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ed_stop_namec = _parse_ed_stop_namec(d.pop("ED_STOP_NAMEC", UNSET))

        def _parse_ed_stop_names(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ed_stop_names = _parse_ed_stop_names(d.pop("ED_STOP_NAMES", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            route_id=route_id,
            route_seq=route_seq,
            public_transport=public_transport,
            route_name=route_name,
            st_stop_id=st_stop_id,
            st_stop_namee=st_stop_namee,
            st_stop_namec=st_stop_namec,
            st_stop_names=st_stop_names,
            ed_stop_id=ed_stop_id,
            ed_stop_namee=ed_stop_namee,
            ed_stop_namec=ed_stop_namec,
            ed_stop_names=ed_stop_names,
            shape_length=shape_length,
        )

        arcgis_feature_server_arcgis_layer_0_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_0_attributes

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
