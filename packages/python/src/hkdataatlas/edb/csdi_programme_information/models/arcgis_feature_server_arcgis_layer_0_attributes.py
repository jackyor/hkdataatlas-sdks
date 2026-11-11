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
        dataset_en (None | str | Unset): Publisher field type: esriFieldTypeString
        dataset_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        academic_year_en (None | str | Unset): Publisher field type: esriFieldTypeString
        academic_year_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        levelofstudy_en (None | str | Unset): Publisher field type: esriFieldTypeString
        levelofstudy_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        programmetype_en (None | str | Unset): Publisher field type: esriFieldTypeString
        programmetype_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        programmename_en (None | str | Unset): Publisher field type: esriFieldTypeString
        programmename_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        areasof_study_en (None | str | Unset): Publisher field type: esriFieldTypeString
        areasof_study_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        normalprogrammeduration_en (None | str | Unset): Publisher field type: esriFieldTypeString
        normalprogrammeduration_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        last_update (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
    """

    objectid: int | Unset = UNSET
    dataset_en: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    academic_year_en: None | str | Unset = UNSET
    academic_year_tc: None | str | Unset = UNSET
    levelofstudy_en: None | str | Unset = UNSET
    levelofstudy_tc: None | str | Unset = UNSET
    programmetype_en: None | str | Unset = UNSET
    programmetype_tc: None | str | Unset = UNSET
    programmename_en: None | str | Unset = UNSET
    programmename_tc: None | str | Unset = UNSET
    areasof_study_en: None | str | Unset = UNSET
    areasof_study_tc: None | str | Unset = UNSET
    normalprogrammeduration_en: None | str | Unset = UNSET
    normalprogrammeduration_tc: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    easting: float | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    last_update: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        dataset_en: None | str | Unset
        if isinstance(self.dataset_en, Unset):
            dataset_en = UNSET
        else:
            dataset_en = self.dataset_en

        dataset_tc: None | str | Unset
        if isinstance(self.dataset_tc, Unset):
            dataset_tc = UNSET
        else:
            dataset_tc = self.dataset_tc

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        academic_year_en: None | str | Unset
        if isinstance(self.academic_year_en, Unset):
            academic_year_en = UNSET
        else:
            academic_year_en = self.academic_year_en

        academic_year_tc: None | str | Unset
        if isinstance(self.academic_year_tc, Unset):
            academic_year_tc = UNSET
        else:
            academic_year_tc = self.academic_year_tc

        levelofstudy_en: None | str | Unset
        if isinstance(self.levelofstudy_en, Unset):
            levelofstudy_en = UNSET
        else:
            levelofstudy_en = self.levelofstudy_en

        levelofstudy_tc: None | str | Unset
        if isinstance(self.levelofstudy_tc, Unset):
            levelofstudy_tc = UNSET
        else:
            levelofstudy_tc = self.levelofstudy_tc

        programmetype_en: None | str | Unset
        if isinstance(self.programmetype_en, Unset):
            programmetype_en = UNSET
        else:
            programmetype_en = self.programmetype_en

        programmetype_tc: None | str | Unset
        if isinstance(self.programmetype_tc, Unset):
            programmetype_tc = UNSET
        else:
            programmetype_tc = self.programmetype_tc

        programmename_en: None | str | Unset
        if isinstance(self.programmename_en, Unset):
            programmename_en = UNSET
        else:
            programmename_en = self.programmename_en

        programmename_tc: None | str | Unset
        if isinstance(self.programmename_tc, Unset):
            programmename_tc = UNSET
        else:
            programmename_tc = self.programmename_tc

        areasof_study_en: None | str | Unset
        if isinstance(self.areasof_study_en, Unset):
            areasof_study_en = UNSET
        else:
            areasof_study_en = self.areasof_study_en

        areasof_study_tc: None | str | Unset
        if isinstance(self.areasof_study_tc, Unset):
            areasof_study_tc = UNSET
        else:
            areasof_study_tc = self.areasof_study_tc

        normalprogrammeduration_en: None | str | Unset
        if isinstance(self.normalprogrammeduration_en, Unset):
            normalprogrammeduration_en = UNSET
        else:
            normalprogrammeduration_en = self.normalprogrammeduration_en

        normalprogrammeduration_tc: None | str | Unset
        if isinstance(self.normalprogrammeduration_tc, Unset):
            normalprogrammeduration_tc = UNSET
        else:
            normalprogrammeduration_tc = self.normalprogrammeduration_tc

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

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

        last_update = self.last_update

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if dataset_en is not UNSET:
            field_dict["DatasetEN"] = dataset_en
        if dataset_tc is not UNSET:
            field_dict["DatasetTC"] = dataset_tc
        if name_en is not UNSET:
            field_dict["NameEN"] = name_en
        if address_en is not UNSET:
            field_dict["AddressEN"] = address_en
        if name_tc is not UNSET:
            field_dict["NameTC"] = name_tc
        if address_tc is not UNSET:
            field_dict["AddressTC"] = address_tc
        if academic_year_en is not UNSET:
            field_dict["AcademicYearEN"] = academic_year_en
        if academic_year_tc is not UNSET:
            field_dict["AcademicYearTC"] = academic_year_tc
        if levelofstudy_en is not UNSET:
            field_dict["LevelofstudyEN"] = levelofstudy_en
        if levelofstudy_tc is not UNSET:
            field_dict["LevelofstudyTC"] = levelofstudy_tc
        if programmetype_en is not UNSET:
            field_dict["ProgrammetypeEN"] = programmetype_en
        if programmetype_tc is not UNSET:
            field_dict["ProgrammetypeTC"] = programmetype_tc
        if programmename_en is not UNSET:
            field_dict["ProgrammenameEN"] = programmename_en
        if programmename_tc is not UNSET:
            field_dict["ProgrammenameTC"] = programmename_tc
        if areasof_study_en is not UNSET:
            field_dict["AreasofStudyEN"] = areasof_study_en
        if areasof_study_tc is not UNSET:
            field_dict["AreasofStudyTC"] = areasof_study_tc
        if normalprogrammeduration_en is not UNSET:
            field_dict["NormalprogrammedurationEN"] = normalprogrammeduration_en
        if normalprogrammeduration_tc is not UNSET:
            field_dict["NormalprogrammedurationTC"] = normalprogrammeduration_tc
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if last_update is not UNSET:
            field_dict["LastUpdate"] = last_update

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_dataset_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_en = _parse_dataset_en(d.pop("DatasetEN", UNSET))

        def _parse_dataset_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_tc = _parse_dataset_tc(d.pop("DatasetTC", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("NameEN", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("AddressEN", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("NameTC", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("AddressTC", UNSET))

        def _parse_academic_year_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        academic_year_en = _parse_academic_year_en(d.pop("AcademicYearEN", UNSET))

        def _parse_academic_year_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        academic_year_tc = _parse_academic_year_tc(d.pop("AcademicYearTC", UNSET))

        def _parse_levelofstudy_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        levelofstudy_en = _parse_levelofstudy_en(d.pop("LevelofstudyEN", UNSET))

        def _parse_levelofstudy_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        levelofstudy_tc = _parse_levelofstudy_tc(d.pop("LevelofstudyTC", UNSET))

        def _parse_programmetype_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        programmetype_en = _parse_programmetype_en(d.pop("ProgrammetypeEN", UNSET))

        def _parse_programmetype_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        programmetype_tc = _parse_programmetype_tc(d.pop("ProgrammetypeTC", UNSET))

        def _parse_programmename_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        programmename_en = _parse_programmename_en(d.pop("ProgrammenameEN", UNSET))

        def _parse_programmename_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        programmename_tc = _parse_programmename_tc(d.pop("ProgrammenameTC", UNSET))

        def _parse_areasof_study_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        areasof_study_en = _parse_areasof_study_en(d.pop("AreasofStudyEN", UNSET))

        def _parse_areasof_study_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        areasof_study_tc = _parse_areasof_study_tc(d.pop("AreasofStudyTC", UNSET))

        def _parse_normalprogrammeduration_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        normalprogrammeduration_en = _parse_normalprogrammeduration_en(
            d.pop("NormalprogrammedurationEN", UNSET)
        )

        def _parse_normalprogrammeduration_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        normalprogrammeduration_tc = _parse_normalprogrammeduration_tc(
            d.pop("NormalprogrammedurationTC", UNSET)
        )

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("Easting", UNSET))

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

        last_update = d.pop("LastUpdate", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            dataset_en=dataset_en,
            dataset_tc=dataset_tc,
            name_en=name_en,
            address_en=address_en,
            name_tc=name_tc,
            address_tc=address_tc,
            academic_year_en=academic_year_en,
            academic_year_tc=academic_year_tc,
            levelofstudy_en=levelofstudy_en,
            levelofstudy_tc=levelofstudy_tc,
            programmetype_en=programmetype_en,
            programmetype_tc=programmetype_tc,
            programmename_en=programmename_en,
            programmename_tc=programmename_tc,
            areasof_study_en=areasof_study_en,
            areasof_study_tc=areasof_study_tc,
            normalprogrammeduration_en=normalprogrammeduration_en,
            normalprogrammeduration_tc=normalprogrammeduration_tc,
            northing=northing,
            easting=easting,
            latitude=latitude,
            longitude=longitude,
            last_update=last_update,
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
