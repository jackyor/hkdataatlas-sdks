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
        roadworks_id (None | str | Unset): Publisher field type: esriFieldTypeString
        datasource (None | str | Unset): Publisher field type: esriFieldTypeString
        datasource_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        datasource_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        workstype (None | str | Unset): Publisher field type: esriFieldTypeString
        workstype_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        workstype_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        starttime (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        endtime (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        district (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        roadname (None | str | Unset): Publisher field type: esriFieldTypeString
        roadname_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        roadname_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        locdesc (None | str | Unset): Publisher field type: esriFieldTypeString
        locdesc_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        locdesc_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        bound (None | str | Unset): Publisher field type: esriFieldTypeString
        bound_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        bound_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        lane (None | str | Unset): Publisher field type: esriFieldTypeString
        lane_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        lane_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        remark (None | str | Unset): Publisher field type: esriFieldTypeString
        remark_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        remark_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        worksstatus (None | str | Unset): Publisher field type: esriFieldTypeString
        worksstatus_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        worksstatus_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        disclaimer (None | str | Unset): Publisher field type: esriFieldTypeString
        disclaimer_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        disclaimer_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        lastupdatetime (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
    """

    objectid: int | Unset = UNSET
    roadworks_id: None | str | Unset = UNSET
    datasource: None | str | Unset = UNSET
    datasource_tc: None | str | Unset = UNSET
    datasource_sc: None | str | Unset = UNSET
    workstype: None | str | Unset = UNSET
    workstype_tc: None | str | Unset = UNSET
    workstype_sc: None | str | Unset = UNSET
    starttime: Any | Unset = UNSET
    endtime: Any | Unset = UNSET
    district: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    district_sc: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    roadname: None | str | Unset = UNSET
    roadname_tc: None | str | Unset = UNSET
    roadname_sc: None | str | Unset = UNSET
    locdesc: None | str | Unset = UNSET
    locdesc_tc: None | str | Unset = UNSET
    locdesc_sc: None | str | Unset = UNSET
    bound: None | str | Unset = UNSET
    bound_tc: None | str | Unset = UNSET
    bound_sc: None | str | Unset = UNSET
    lane: None | str | Unset = UNSET
    lane_tc: None | str | Unset = UNSET
    lane_sc: None | str | Unset = UNSET
    remark: None | str | Unset = UNSET
    remark_tc: None | str | Unset = UNSET
    remark_sc: None | str | Unset = UNSET
    worksstatus: None | str | Unset = UNSET
    worksstatus_tc: None | str | Unset = UNSET
    worksstatus_sc: None | str | Unset = UNSET
    disclaimer: None | str | Unset = UNSET
    disclaimer_tc: None | str | Unset = UNSET
    disclaimer_sc: None | str | Unset = UNSET
    lastupdatetime: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        roadworks_id: None | str | Unset
        if isinstance(self.roadworks_id, Unset):
            roadworks_id = UNSET
        else:
            roadworks_id = self.roadworks_id

        datasource: None | str | Unset
        if isinstance(self.datasource, Unset):
            datasource = UNSET
        else:
            datasource = self.datasource

        datasource_tc: None | str | Unset
        if isinstance(self.datasource_tc, Unset):
            datasource_tc = UNSET
        else:
            datasource_tc = self.datasource_tc

        datasource_sc: None | str | Unset
        if isinstance(self.datasource_sc, Unset):
            datasource_sc = UNSET
        else:
            datasource_sc = self.datasource_sc

        workstype: None | str | Unset
        if isinstance(self.workstype, Unset):
            workstype = UNSET
        else:
            workstype = self.workstype

        workstype_tc: None | str | Unset
        if isinstance(self.workstype_tc, Unset):
            workstype_tc = UNSET
        else:
            workstype_tc = self.workstype_tc

        workstype_sc: None | str | Unset
        if isinstance(self.workstype_sc, Unset):
            workstype_sc = UNSET
        else:
            workstype_sc = self.workstype_sc

        starttime = self.starttime

        endtime = self.endtime

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        district_sc: None | str | Unset
        if isinstance(self.district_sc, Unset):
            district_sc = UNSET
        else:
            district_sc = self.district_sc

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        roadname: None | str | Unset
        if isinstance(self.roadname, Unset):
            roadname = UNSET
        else:
            roadname = self.roadname

        roadname_tc: None | str | Unset
        if isinstance(self.roadname_tc, Unset):
            roadname_tc = UNSET
        else:
            roadname_tc = self.roadname_tc

        roadname_sc: None | str | Unset
        if isinstance(self.roadname_sc, Unset):
            roadname_sc = UNSET
        else:
            roadname_sc = self.roadname_sc

        locdesc: None | str | Unset
        if isinstance(self.locdesc, Unset):
            locdesc = UNSET
        else:
            locdesc = self.locdesc

        locdesc_tc: None | str | Unset
        if isinstance(self.locdesc_tc, Unset):
            locdesc_tc = UNSET
        else:
            locdesc_tc = self.locdesc_tc

        locdesc_sc: None | str | Unset
        if isinstance(self.locdesc_sc, Unset):
            locdesc_sc = UNSET
        else:
            locdesc_sc = self.locdesc_sc

        bound: None | str | Unset
        if isinstance(self.bound, Unset):
            bound = UNSET
        else:
            bound = self.bound

        bound_tc: None | str | Unset
        if isinstance(self.bound_tc, Unset):
            bound_tc = UNSET
        else:
            bound_tc = self.bound_tc

        bound_sc: None | str | Unset
        if isinstance(self.bound_sc, Unset):
            bound_sc = UNSET
        else:
            bound_sc = self.bound_sc

        lane: None | str | Unset
        if isinstance(self.lane, Unset):
            lane = UNSET
        else:
            lane = self.lane

        lane_tc: None | str | Unset
        if isinstance(self.lane_tc, Unset):
            lane_tc = UNSET
        else:
            lane_tc = self.lane_tc

        lane_sc: None | str | Unset
        if isinstance(self.lane_sc, Unset):
            lane_sc = UNSET
        else:
            lane_sc = self.lane_sc

        remark: None | str | Unset
        if isinstance(self.remark, Unset):
            remark = UNSET
        else:
            remark = self.remark

        remark_tc: None | str | Unset
        if isinstance(self.remark_tc, Unset):
            remark_tc = UNSET
        else:
            remark_tc = self.remark_tc

        remark_sc: None | str | Unset
        if isinstance(self.remark_sc, Unset):
            remark_sc = UNSET
        else:
            remark_sc = self.remark_sc

        worksstatus: None | str | Unset
        if isinstance(self.worksstatus, Unset):
            worksstatus = UNSET
        else:
            worksstatus = self.worksstatus

        worksstatus_tc: None | str | Unset
        if isinstance(self.worksstatus_tc, Unset):
            worksstatus_tc = UNSET
        else:
            worksstatus_tc = self.worksstatus_tc

        worksstatus_sc: None | str | Unset
        if isinstance(self.worksstatus_sc, Unset):
            worksstatus_sc = UNSET
        else:
            worksstatus_sc = self.worksstatus_sc

        disclaimer: None | str | Unset
        if isinstance(self.disclaimer, Unset):
            disclaimer = UNSET
        else:
            disclaimer = self.disclaimer

        disclaimer_tc: None | str | Unset
        if isinstance(self.disclaimer_tc, Unset):
            disclaimer_tc = UNSET
        else:
            disclaimer_tc = self.disclaimer_tc

        disclaimer_sc: None | str | Unset
        if isinstance(self.disclaimer_sc, Unset):
            disclaimer_sc = UNSET
        else:
            disclaimer_sc = self.disclaimer_sc

        lastupdatetime = self.lastupdatetime

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if roadworks_id is not UNSET:
            field_dict["roadworks_id"] = roadworks_id
        if datasource is not UNSET:
            field_dict["datasource"] = datasource
        if datasource_tc is not UNSET:
            field_dict["datasource_tc"] = datasource_tc
        if datasource_sc is not UNSET:
            field_dict["datasource_sc"] = datasource_sc
        if workstype is not UNSET:
            field_dict["workstype"] = workstype
        if workstype_tc is not UNSET:
            field_dict["workstype_tc"] = workstype_tc
        if workstype_sc is not UNSET:
            field_dict["workstype_sc"] = workstype_sc
        if starttime is not UNSET:
            field_dict["starttime"] = starttime
        if endtime is not UNSET:
            field_dict["endtime"] = endtime
        if district is not UNSET:
            field_dict["district"] = district
        if district_tc is not UNSET:
            field_dict["district_tc"] = district_tc
        if district_sc is not UNSET:
            field_dict["district_sc"] = district_sc
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if roadname is not UNSET:
            field_dict["roadname"] = roadname
        if roadname_tc is not UNSET:
            field_dict["roadname_tc"] = roadname_tc
        if roadname_sc is not UNSET:
            field_dict["roadname_sc"] = roadname_sc
        if locdesc is not UNSET:
            field_dict["locdesc"] = locdesc
        if locdesc_tc is not UNSET:
            field_dict["locdesc_tc"] = locdesc_tc
        if locdesc_sc is not UNSET:
            field_dict["locdesc_sc"] = locdesc_sc
        if bound is not UNSET:
            field_dict["bound"] = bound
        if bound_tc is not UNSET:
            field_dict["bound_tc"] = bound_tc
        if bound_sc is not UNSET:
            field_dict["bound_sc"] = bound_sc
        if lane is not UNSET:
            field_dict["lane"] = lane
        if lane_tc is not UNSET:
            field_dict["lane_tc"] = lane_tc
        if lane_sc is not UNSET:
            field_dict["lane_sc"] = lane_sc
        if remark is not UNSET:
            field_dict["remark"] = remark
        if remark_tc is not UNSET:
            field_dict["remark_tc"] = remark_tc
        if remark_sc is not UNSET:
            field_dict["remark_sc"] = remark_sc
        if worksstatus is not UNSET:
            field_dict["worksstatus"] = worksstatus
        if worksstatus_tc is not UNSET:
            field_dict["worksstatus_tc"] = worksstatus_tc
        if worksstatus_sc is not UNSET:
            field_dict["worksstatus_sc"] = worksstatus_sc
        if disclaimer is not UNSET:
            field_dict["disclaimer"] = disclaimer
        if disclaimer_tc is not UNSET:
            field_dict["disclaimer_tc"] = disclaimer_tc
        if disclaimer_sc is not UNSET:
            field_dict["disclaimer_sc"] = disclaimer_sc
        if lastupdatetime is not UNSET:
            field_dict["lastupdatetime"] = lastupdatetime

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_roadworks_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        roadworks_id = _parse_roadworks_id(d.pop("roadworks_id", UNSET))

        def _parse_datasource(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        datasource = _parse_datasource(d.pop("datasource", UNSET))

        def _parse_datasource_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        datasource_tc = _parse_datasource_tc(d.pop("datasource_tc", UNSET))

        def _parse_datasource_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        datasource_sc = _parse_datasource_sc(d.pop("datasource_sc", UNSET))

        def _parse_workstype(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        workstype = _parse_workstype(d.pop("workstype", UNSET))

        def _parse_workstype_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        workstype_tc = _parse_workstype_tc(d.pop("workstype_tc", UNSET))

        def _parse_workstype_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        workstype_sc = _parse_workstype_sc(d.pop("workstype_sc", UNSET))

        starttime = d.pop("starttime", UNSET)

        endtime = d.pop("endtime", UNSET)

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("district", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("district_tc", UNSET))

        def _parse_district_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_sc = _parse_district_sc(d.pop("district_sc", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        def _parse_roadname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        roadname = _parse_roadname(d.pop("roadname", UNSET))

        def _parse_roadname_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        roadname_tc = _parse_roadname_tc(d.pop("roadname_tc", UNSET))

        def _parse_roadname_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        roadname_sc = _parse_roadname_sc(d.pop("roadname_sc", UNSET))

        def _parse_locdesc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locdesc = _parse_locdesc(d.pop("locdesc", UNSET))

        def _parse_locdesc_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locdesc_tc = _parse_locdesc_tc(d.pop("locdesc_tc", UNSET))

        def _parse_locdesc_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locdesc_sc = _parse_locdesc_sc(d.pop("locdesc_sc", UNSET))

        def _parse_bound(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bound = _parse_bound(d.pop("bound", UNSET))

        def _parse_bound_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bound_tc = _parse_bound_tc(d.pop("bound_tc", UNSET))

        def _parse_bound_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bound_sc = _parse_bound_sc(d.pop("bound_sc", UNSET))

        def _parse_lane(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lane = _parse_lane(d.pop("lane", UNSET))

        def _parse_lane_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lane_tc = _parse_lane_tc(d.pop("lane_tc", UNSET))

        def _parse_lane_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lane_sc = _parse_lane_sc(d.pop("lane_sc", UNSET))

        def _parse_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark = _parse_remark(d.pop("remark", UNSET))

        def _parse_remark_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark_tc = _parse_remark_tc(d.pop("remark_tc", UNSET))

        def _parse_remark_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark_sc = _parse_remark_sc(d.pop("remark_sc", UNSET))

        def _parse_worksstatus(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        worksstatus = _parse_worksstatus(d.pop("worksstatus", UNSET))

        def _parse_worksstatus_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        worksstatus_tc = _parse_worksstatus_tc(d.pop("worksstatus_tc", UNSET))

        def _parse_worksstatus_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        worksstatus_sc = _parse_worksstatus_sc(d.pop("worksstatus_sc", UNSET))

        def _parse_disclaimer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disclaimer = _parse_disclaimer(d.pop("disclaimer", UNSET))

        def _parse_disclaimer_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disclaimer_tc = _parse_disclaimer_tc(d.pop("disclaimer_tc", UNSET))

        def _parse_disclaimer_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disclaimer_sc = _parse_disclaimer_sc(d.pop("disclaimer_sc", UNSET))

        lastupdatetime = d.pop("lastupdatetime", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            roadworks_id=roadworks_id,
            datasource=datasource,
            datasource_tc=datasource_tc,
            datasource_sc=datasource_sc,
            workstype=workstype,
            workstype_tc=workstype_tc,
            workstype_sc=workstype_sc,
            starttime=starttime,
            endtime=endtime,
            district=district,
            district_tc=district_tc,
            district_sc=district_sc,
            latitude=latitude,
            longitude=longitude,
            roadname=roadname,
            roadname_tc=roadname_tc,
            roadname_sc=roadname_sc,
            locdesc=locdesc,
            locdesc_tc=locdesc_tc,
            locdesc_sc=locdesc_sc,
            bound=bound,
            bound_tc=bound_tc,
            bound_sc=bound_sc,
            lane=lane,
            lane_tc=lane_tc,
            lane_sc=lane_sc,
            remark=remark,
            remark_tc=remark_tc,
            remark_sc=remark_sc,
            worksstatus=worksstatus,
            worksstatus_tc=worksstatus_tc,
            worksstatus_sc=worksstatus_sc,
            disclaimer=disclaimer,
            disclaimer_tc=disclaimer_tc,
            disclaimer_sc=disclaimer_sc,
            lastupdatetime=lastupdatetime,
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
