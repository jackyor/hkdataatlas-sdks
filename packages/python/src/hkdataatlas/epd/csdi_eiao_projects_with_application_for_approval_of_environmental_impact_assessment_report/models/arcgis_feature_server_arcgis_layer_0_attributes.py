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
        eid (None | str | Unset): Publisher field type: esriFieldTypeString
        eid_x (float | None | Unset): Publisher field type: esriFieldTypeDouble
        eid_y (float | None | Unset): Publisher field type: esriFieldTypeDouble
        applicatio (None | str | Unset): Publisher field type: esriFieldTypeString
        title_of_t (None | str | Unset): Publisher field type: esriFieldTypeString
        chinese_ti (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_th (None | str | Unset): Publisher field type: esriFieldTypeString
        register_n (None | str | Unset): Publisher field type: esriFieldTypeString
        schedule (int | None | Unset): Publisher field type: esriFieldTypeInteger
        eia_applic (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        project_we (None | str | Unset): Publisher field type: esriFieldTypeString
        sch_2_par (None | str | Unset): Publisher field type: esriFieldTypeString
        sch_2_p_1 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        sch_3 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    eid: None | str | Unset = UNSET
    eid_x: float | None | Unset = UNSET
    eid_y: float | None | Unset = UNSET
    applicatio: None | str | Unset = UNSET
    title_of_t: None | str | Unset = UNSET
    chinese_ti: None | str | Unset = UNSET
    name_of_th: None | str | Unset = UNSET
    register_n: None | str | Unset = UNSET
    schedule: int | None | Unset = UNSET
    eia_applic: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    project_we: None | str | Unset = UNSET
    sch_2_par: None | str | Unset = UNSET
    sch_2_p_1: int | None | Unset = UNSET
    sch_3: int | None | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eid: None | str | Unset
        if isinstance(self.eid, Unset):
            eid = UNSET
        else:
            eid = self.eid

        eid_x: float | None | Unset
        if isinstance(self.eid_x, Unset):
            eid_x = UNSET
        else:
            eid_x = self.eid_x

        eid_y: float | None | Unset
        if isinstance(self.eid_y, Unset):
            eid_y = UNSET
        else:
            eid_y = self.eid_y

        applicatio: None | str | Unset
        if isinstance(self.applicatio, Unset):
            applicatio = UNSET
        else:
            applicatio = self.applicatio

        title_of_t: None | str | Unset
        if isinstance(self.title_of_t, Unset):
            title_of_t = UNSET
        else:
            title_of_t = self.title_of_t

        chinese_ti: None | str | Unset
        if isinstance(self.chinese_ti, Unset):
            chinese_ti = UNSET
        else:
            chinese_ti = self.chinese_ti

        name_of_th: None | str | Unset
        if isinstance(self.name_of_th, Unset):
            name_of_th = UNSET
        else:
            name_of_th = self.name_of_th

        register_n: None | str | Unset
        if isinstance(self.register_n, Unset):
            register_n = UNSET
        else:
            register_n = self.register_n

        schedule: int | None | Unset
        if isinstance(self.schedule, Unset):
            schedule = UNSET
        else:
            schedule = self.schedule

        eia_applic: None | str | Unset
        if isinstance(self.eia_applic, Unset):
            eia_applic = UNSET
        else:
            eia_applic = self.eia_applic

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

        project_we: None | str | Unset
        if isinstance(self.project_we, Unset):
            project_we = UNSET
        else:
            project_we = self.project_we

        sch_2_par: None | str | Unset
        if isinstance(self.sch_2_par, Unset):
            sch_2_par = UNSET
        else:
            sch_2_par = self.sch_2_par

        sch_2_p_1: int | None | Unset
        if isinstance(self.sch_2_p_1, Unset):
            sch_2_p_1 = UNSET
        else:
            sch_2_p_1 = self.sch_2_p_1

        sch_3: int | None | Unset
        if isinstance(self.sch_3, Unset):
            sch_3 = UNSET
        else:
            sch_3 = self.sch_3

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eid is not UNSET:
            field_dict["EID"] = eid
        if eid_x is not UNSET:
            field_dict["EID_X"] = eid_x
        if eid_y is not UNSET:
            field_dict["EID_Y"] = eid_y
        if applicatio is not UNSET:
            field_dict["Applicatio"] = applicatio
        if title_of_t is not UNSET:
            field_dict["Title_of_t"] = title_of_t
        if chinese_ti is not UNSET:
            field_dict["Chinese_Ti"] = chinese_ti
        if name_of_th is not UNSET:
            field_dict["Name_of_th"] = name_of_th
        if register_n is not UNSET:
            field_dict["Register_N"] = register_n
        if schedule is not UNSET:
            field_dict["Schedule__"] = schedule
        if eia_applic is not UNSET:
            field_dict["EIA_Applic"] = eia_applic
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if project_we is not UNSET:
            field_dict["Project_We"] = project_we
        if sch_2_par is not UNSET:
            field_dict["Sch__2_Par"] = sch_2_par
        if sch_2_p_1 is not UNSET:
            field_dict["Sch__2_P_1"] = sch_2_p_1
        if sch_3 is not UNSET:
            field_dict["Sch__3"] = sch_3
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_eid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        eid = _parse_eid(d.pop("EID", UNSET))

        def _parse_eid_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        eid_x = _parse_eid_x(d.pop("EID_X", UNSET))

        def _parse_eid_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        eid_y = _parse_eid_y(d.pop("EID_Y", UNSET))

        def _parse_applicatio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        applicatio = _parse_applicatio(d.pop("Applicatio", UNSET))

        def _parse_title_of_t(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_of_t = _parse_title_of_t(d.pop("Title_of_t", UNSET))

        def _parse_chinese_ti(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinese_ti = _parse_chinese_ti(d.pop("Chinese_Ti", UNSET))

        def _parse_name_of_th(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_th = _parse_name_of_th(d.pop("Name_of_th", UNSET))

        def _parse_register_n(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        register_n = _parse_register_n(d.pop("Register_N", UNSET))

        def _parse_schedule(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        schedule = _parse_schedule(d.pop("Schedule__", UNSET))

        def _parse_eia_applic(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        eia_applic = _parse_eia_applic(d.pop("EIA_Applic", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        def _parse_project_we(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_we = _parse_project_we(d.pop("Project_We", UNSET))

        def _parse_sch_2_par(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sch_2_par = _parse_sch_2_par(d.pop("Sch__2_Par", UNSET))

        def _parse_sch_2_p_1(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sch_2_p_1 = _parse_sch_2_p_1(d.pop("Sch__2_P_1", UNSET))

        def _parse_sch_3(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sch_3 = _parse_sch_3(d.pop("Sch__3", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            eid=eid,
            eid_x=eid_x,
            eid_y=eid_y,
            applicatio=applicatio,
            title_of_t=title_of_t,
            chinese_ti=chinese_ti,
            name_of_th=name_of_th,
            register_n=register_n,
            schedule=schedule,
            eia_applic=eia_applic,
            latitude=latitude,
            longitude=longitude,
            project_we=project_we,
            sch_2_par=sch_2_par,
            sch_2_p_1=sch_2_p_1,
            sch_3=sch_3,
            objectid=objectid,
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
