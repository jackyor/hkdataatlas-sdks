from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsVISINVTREEAttributes")


@_attrs_define
class WfsMapServerWfsVISINVTREEAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        veg_id (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        tree_id (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        easting (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        northing (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dbh (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        maint_dist (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        ovt_id (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        road_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        spec_type (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML occurrence
            into all JSON queries.
        feat_type (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML occurrence
            into all JSON queries.
        height (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        spread (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        tr_level (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    veg_id: None | str | Unset = UNSET
    tree_id: None | str | Unset = UNSET
    easting: float | None | Unset = UNSET
    northing: float | None | Unset = UNSET
    dbh: int | None | Unset = UNSET
    maint_dist: None | str | Unset = UNSET
    ovt_id: None | str | Unset = UNSET
    road_name: None | str | Unset = UNSET
    spec_type: int | None | Unset = UNSET
    feat_type: int | None | Unset = UNSET
    height: float | None | Unset = UNSET
    spread: float | None | Unset = UNSET
    tr_level: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        veg_id: None | str | Unset
        if isinstance(self.veg_id, Unset):
            veg_id = UNSET
        else:
            veg_id = self.veg_id

        tree_id: None | str | Unset
        if isinstance(self.tree_id, Unset):
            tree_id = UNSET
        else:
            tree_id = self.tree_id

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        dbh: int | None | Unset
        if isinstance(self.dbh, Unset):
            dbh = UNSET
        else:
            dbh = self.dbh

        maint_dist: None | str | Unset
        if isinstance(self.maint_dist, Unset):
            maint_dist = UNSET
        else:
            maint_dist = self.maint_dist

        ovt_id: None | str | Unset
        if isinstance(self.ovt_id, Unset):
            ovt_id = UNSET
        else:
            ovt_id = self.ovt_id

        road_name: None | str | Unset
        if isinstance(self.road_name, Unset):
            road_name = UNSET
        else:
            road_name = self.road_name

        spec_type: int | None | Unset
        if isinstance(self.spec_type, Unset):
            spec_type = UNSET
        else:
            spec_type = self.spec_type

        feat_type: int | None | Unset
        if isinstance(self.feat_type, Unset):
            feat_type = UNSET
        else:
            feat_type = self.feat_type

        height: float | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        spread: float | None | Unset
        if isinstance(self.spread, Unset):
            spread = UNSET
        else:
            spread = self.spread

        tr_level: float | None | Unset
        if isinstance(self.tr_level, Unset):
            tr_level = UNSET
        else:
            tr_level = self.tr_level

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if veg_id is not UNSET:
            field_dict["VEG_ID"] = veg_id
        if tree_id is not UNSET:
            field_dict["TREE_ID"] = tree_id
        if easting is not UNSET:
            field_dict["EASTING"] = easting
        if northing is not UNSET:
            field_dict["NORTHING"] = northing
        if dbh is not UNSET:
            field_dict["DBH"] = dbh
        if maint_dist is not UNSET:
            field_dict["MAINT_DIST"] = maint_dist
        if ovt_id is not UNSET:
            field_dict["OVT_ID"] = ovt_id
        if road_name is not UNSET:
            field_dict["ROAD_NAME"] = road_name
        if spec_type is not UNSET:
            field_dict["SPEC_TYPE"] = spec_type
        if feat_type is not UNSET:
            field_dict["FEAT_TYPE"] = feat_type
        if height is not UNSET:
            field_dict["HEIGHT"] = height
        if spread is not UNSET:
            field_dict["SPREAD"] = spread
        if tr_level is not UNSET:
            field_dict["TR_LEVEL"] = tr_level

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("Shape", UNSET)

        def _parse_veg_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        veg_id = _parse_veg_id(d.pop("VEG_ID", UNSET))

        def _parse_tree_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tree_id = _parse_tree_id(d.pop("TREE_ID", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("EASTING", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("NORTHING", UNSET))

        def _parse_dbh(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dbh = _parse_dbh(d.pop("DBH", UNSET))

        def _parse_maint_dist(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        maint_dist = _parse_maint_dist(d.pop("MAINT_DIST", UNSET))

        def _parse_ovt_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ovt_id = _parse_ovt_id(d.pop("OVT_ID", UNSET))

        def _parse_road_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        road_name = _parse_road_name(d.pop("ROAD_NAME", UNSET))

        def _parse_spec_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        spec_type = _parse_spec_type(d.pop("SPEC_TYPE", UNSET))

        def _parse_feat_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        feat_type = _parse_feat_type(d.pop("FEAT_TYPE", UNSET))

        def _parse_height(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        height = _parse_height(d.pop("HEIGHT", UNSET))

        def _parse_spread(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        spread = _parse_spread(d.pop("SPREAD", UNSET))

        def _parse_tr_level(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tr_level = _parse_tr_level(d.pop("TR_LEVEL", UNSET))

        wfs_map_server_wfs_visinvtree_attributes = cls(
            objectid=objectid,
            shape=shape,
            veg_id=veg_id,
            tree_id=tree_id,
            easting=easting,
            northing=northing,
            dbh=dbh,
            maint_dist=maint_dist,
            ovt_id=ovt_id,
            road_name=road_name,
            spec_type=spec_type,
            feat_type=feat_type,
            height=height,
            spread=spread,
            tr_level=tr_level,
        )

        wfs_map_server_wfs_visinvtree_attributes.additional_properties = d
        return wfs_map_server_wfs_visinvtree_attributes

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
