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
        id (None | str | Unset): Publisher field type: esriFieldTypeString
        applicatio (None | str | Unset): Publisher field type: esriFieldTypeString
        title_of_t (None | str | Unset): Publisher field type: esriFieldTypeString
        chinese_ti (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_th (None | str | Unset): Publisher field type: esriFieldTypeString
        dir_applic (None | str | Unset): Publisher field type: esriFieldTypeString
        ep_status (None | str | Unset): Publisher field type: esriFieldTypeString
        project_we (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        sch_2_par (None | str | Unset): Publisher field type: esriFieldTypeString
        sch_2_p_1 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        sch_3 (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    id: None | str | Unset = UNSET
    applicatio: None | str | Unset = UNSET
    title_of_t: None | str | Unset = UNSET
    chinese_ti: None | str | Unset = UNSET
    name_of_th: None | str | Unset = UNSET
    dir_applic: None | str | Unset = UNSET
    ep_status: None | str | Unset = UNSET
    project_we: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    sch_2_par: None | str | Unset = UNSET
    sch_2_p_1: int | None | Unset = UNSET
    sch_3: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

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

        dir_applic: None | str | Unset
        if isinstance(self.dir_applic, Unset):
            dir_applic = UNSET
        else:
            dir_applic = self.dir_applic

        ep_status: None | str | Unset
        if isinstance(self.ep_status, Unset):
            ep_status = UNSET
        else:
            ep_status = self.ep_status

        project_we: None | str | Unset
        if isinstance(self.project_we, Unset):
            project_we = UNSET
        else:
            project_we = self.project_we

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

        sch_3: None | str | Unset
        if isinstance(self.sch_3, Unset):
            sch_3 = UNSET
        else:
            sch_3 = self.sch_3

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["ID"] = id
        if applicatio is not UNSET:
            field_dict["Applicatio"] = applicatio
        if title_of_t is not UNSET:
            field_dict["Title_of_t"] = title_of_t
        if chinese_ti is not UNSET:
            field_dict["Chinese_Ti"] = chinese_ti
        if name_of_th is not UNSET:
            field_dict["Name_of_th"] = name_of_th
        if dir_applic is not UNSET:
            field_dict["Dir_Applic"] = dir_applic
        if ep_status is not UNSET:
            field_dict["EP_status"] = ep_status
        if project_we is not UNSET:
            field_dict["Project_We"] = project_we
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
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

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("ID", UNSET))

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

        def _parse_dir_applic(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dir_applic = _parse_dir_applic(d.pop("Dir_Applic", UNSET))

        def _parse_ep_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ep_status = _parse_ep_status(d.pop("EP_status", UNSET))

        def _parse_project_we(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_we = _parse_project_we(d.pop("Project_We", UNSET))

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

        def _parse_sch_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sch_3 = _parse_sch_3(d.pop("Sch__3", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            id=id,
            applicatio=applicatio,
            title_of_t=title_of_t,
            chinese_ti=chinese_ti,
            name_of_th=name_of_th,
            dir_applic=dir_applic,
            ep_status=ep_status,
            project_we=project_we,
            latitude=latitude,
            longitude=longitude,
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
