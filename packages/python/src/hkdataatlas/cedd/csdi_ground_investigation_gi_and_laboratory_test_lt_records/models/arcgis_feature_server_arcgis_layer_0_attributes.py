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
        repno (None | str | Unset): Publisher field type: esriFieldTypeString
        statno (None | str | Unset): Publisher field type: esriFieldTypeString
        stattype (None | str | Unset): Publisher field type: esriFieldTypeString
        holeincl (None | str | Unset): Publisher field type: esriFieldTypeString
        e_coord (float | None | Unset): Publisher field type: esriFieldTypeDouble
        n_coord (float | None | Unset): Publisher field type: esriFieldTypeDouble
        sdate (None | str | Unset): Publisher field type: esriFieldTypeString
        edate (None | str | Unset): Publisher field type: esriFieldTypeString
        grdlevel (None | str | Unset): Publisher field type: esriFieldTypeString
        grdunit (None | str | Unset): Publisher field type: esriFieldTypeString
        depth (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    repno: None | str | Unset = UNSET
    statno: None | str | Unset = UNSET
    stattype: None | str | Unset = UNSET
    holeincl: None | str | Unset = UNSET
    e_coord: float | None | Unset = UNSET
    n_coord: float | None | Unset = UNSET
    sdate: None | str | Unset = UNSET
    edate: None | str | Unset = UNSET
    grdlevel: None | str | Unset = UNSET
    grdunit: None | str | Unset = UNSET
    depth: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        repno: None | str | Unset
        if isinstance(self.repno, Unset):
            repno = UNSET
        else:
            repno = self.repno

        statno: None | str | Unset
        if isinstance(self.statno, Unset):
            statno = UNSET
        else:
            statno = self.statno

        stattype: None | str | Unset
        if isinstance(self.stattype, Unset):
            stattype = UNSET
        else:
            stattype = self.stattype

        holeincl: None | str | Unset
        if isinstance(self.holeincl, Unset):
            holeincl = UNSET
        else:
            holeincl = self.holeincl

        e_coord: float | None | Unset
        if isinstance(self.e_coord, Unset):
            e_coord = UNSET
        else:
            e_coord = self.e_coord

        n_coord: float | None | Unset
        if isinstance(self.n_coord, Unset):
            n_coord = UNSET
        else:
            n_coord = self.n_coord

        sdate: None | str | Unset
        if isinstance(self.sdate, Unset):
            sdate = UNSET
        else:
            sdate = self.sdate

        edate: None | str | Unset
        if isinstance(self.edate, Unset):
            edate = UNSET
        else:
            edate = self.edate

        grdlevel: None | str | Unset
        if isinstance(self.grdlevel, Unset):
            grdlevel = UNSET
        else:
            grdlevel = self.grdlevel

        grdunit: None | str | Unset
        if isinstance(self.grdunit, Unset):
            grdunit = UNSET
        else:
            grdunit = self.grdunit

        depth: None | str | Unset
        if isinstance(self.depth, Unset):
            depth = UNSET
        else:
            depth = self.depth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if repno is not UNSET:
            field_dict["REPNO"] = repno
        if statno is not UNSET:
            field_dict["STATNO"] = statno
        if stattype is not UNSET:
            field_dict["STATTYPE"] = stattype
        if holeincl is not UNSET:
            field_dict["HOLEINCL"] = holeincl
        if e_coord is not UNSET:
            field_dict["E_COORD"] = e_coord
        if n_coord is not UNSET:
            field_dict["N_COORD"] = n_coord
        if sdate is not UNSET:
            field_dict["SDATE"] = sdate
        if edate is not UNSET:
            field_dict["EDATE"] = edate
        if grdlevel is not UNSET:
            field_dict["GRDLEVEL"] = grdlevel
        if grdunit is not UNSET:
            field_dict["GRDUNIT"] = grdunit
        if depth is not UNSET:
            field_dict["DEPTH"] = depth

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_repno(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repno = _parse_repno(d.pop("REPNO", UNSET))

        def _parse_statno(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        statno = _parse_statno(d.pop("STATNO", UNSET))

        def _parse_stattype(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stattype = _parse_stattype(d.pop("STATTYPE", UNSET))

        def _parse_holeincl(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        holeincl = _parse_holeincl(d.pop("HOLEINCL", UNSET))

        def _parse_e_coord(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        e_coord = _parse_e_coord(d.pop("E_COORD", UNSET))

        def _parse_n_coord(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        n_coord = _parse_n_coord(d.pop("N_COORD", UNSET))

        def _parse_sdate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sdate = _parse_sdate(d.pop("SDATE", UNSET))

        def _parse_edate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        edate = _parse_edate(d.pop("EDATE", UNSET))

        def _parse_grdlevel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grdlevel = _parse_grdlevel(d.pop("GRDLEVEL", UNSET))

        def _parse_grdunit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grdunit = _parse_grdunit(d.pop("GRDUNIT", UNSET))

        def _parse_depth(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        depth = _parse_depth(d.pop("DEPTH", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            repno=repno,
            statno=statno,
            stattype=stattype,
            holeincl=holeincl,
            e_coord=e_coord,
            n_coord=n_coord,
            sdate=sdate,
            edate=edate,
            grdlevel=grdlevel,
            grdunit=grdunit,
            depth=depth,
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
