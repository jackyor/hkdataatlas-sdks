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
        numberof_classrooms_en (None | str | Unset): Publisher field type: esriFieldTypeString
        numberof_classrooms_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        numberof_lecture_threaters_en (None | str | Unset): Publisher field type: esriFieldTypeString
        numberof_lecture_threaters_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        numberof_lab_en (None | str | Unset): Publisher field type: esriFieldTypeString
        numberof_lab_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        numberof_books_en (None | str | Unset): Publisher field type: esriFieldTypeString
        numberof_books_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        other_teaching_facilities_en (None | str | Unset): Publisher field type: esriFieldTypeString
        other_teaching_facilities_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        othernon_teaching_facilities_en (None | str | Unset): Publisher field type: esriFieldTypeString
        othernon_teaching_facilities_tc (None | str | Unset): Publisher field type: esriFieldTypeString
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
    numberof_classrooms_en: None | str | Unset = UNSET
    numberof_classrooms_tc: None | str | Unset = UNSET
    numberof_lecture_threaters_en: None | str | Unset = UNSET
    numberof_lecture_threaters_tc: None | str | Unset = UNSET
    numberof_lab_en: None | str | Unset = UNSET
    numberof_lab_tc: None | str | Unset = UNSET
    numberof_books_en: None | str | Unset = UNSET
    numberof_books_tc: None | str | Unset = UNSET
    other_teaching_facilities_en: None | str | Unset = UNSET
    other_teaching_facilities_tc: None | str | Unset = UNSET
    othernon_teaching_facilities_en: None | str | Unset = UNSET
    othernon_teaching_facilities_tc: None | str | Unset = UNSET
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

        numberof_classrooms_en: None | str | Unset
        if isinstance(self.numberof_classrooms_en, Unset):
            numberof_classrooms_en = UNSET
        else:
            numberof_classrooms_en = self.numberof_classrooms_en

        numberof_classrooms_tc: None | str | Unset
        if isinstance(self.numberof_classrooms_tc, Unset):
            numberof_classrooms_tc = UNSET
        else:
            numberof_classrooms_tc = self.numberof_classrooms_tc

        numberof_lecture_threaters_en: None | str | Unset
        if isinstance(self.numberof_lecture_threaters_en, Unset):
            numberof_lecture_threaters_en = UNSET
        else:
            numberof_lecture_threaters_en = self.numberof_lecture_threaters_en

        numberof_lecture_threaters_tc: None | str | Unset
        if isinstance(self.numberof_lecture_threaters_tc, Unset):
            numberof_lecture_threaters_tc = UNSET
        else:
            numberof_lecture_threaters_tc = self.numberof_lecture_threaters_tc

        numberof_lab_en: None | str | Unset
        if isinstance(self.numberof_lab_en, Unset):
            numberof_lab_en = UNSET
        else:
            numberof_lab_en = self.numberof_lab_en

        numberof_lab_tc: None | str | Unset
        if isinstance(self.numberof_lab_tc, Unset):
            numberof_lab_tc = UNSET
        else:
            numberof_lab_tc = self.numberof_lab_tc

        numberof_books_en: None | str | Unset
        if isinstance(self.numberof_books_en, Unset):
            numberof_books_en = UNSET
        else:
            numberof_books_en = self.numberof_books_en

        numberof_books_tc: None | str | Unset
        if isinstance(self.numberof_books_tc, Unset):
            numberof_books_tc = UNSET
        else:
            numberof_books_tc = self.numberof_books_tc

        other_teaching_facilities_en: None | str | Unset
        if isinstance(self.other_teaching_facilities_en, Unset):
            other_teaching_facilities_en = UNSET
        else:
            other_teaching_facilities_en = self.other_teaching_facilities_en

        other_teaching_facilities_tc: None | str | Unset
        if isinstance(self.other_teaching_facilities_tc, Unset):
            other_teaching_facilities_tc = UNSET
        else:
            other_teaching_facilities_tc = self.other_teaching_facilities_tc

        othernon_teaching_facilities_en: None | str | Unset
        if isinstance(self.othernon_teaching_facilities_en, Unset):
            othernon_teaching_facilities_en = UNSET
        else:
            othernon_teaching_facilities_en = self.othernon_teaching_facilities_en

        othernon_teaching_facilities_tc: None | str | Unset
        if isinstance(self.othernon_teaching_facilities_tc, Unset):
            othernon_teaching_facilities_tc = UNSET
        else:
            othernon_teaching_facilities_tc = self.othernon_teaching_facilities_tc

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
        if numberof_classrooms_en is not UNSET:
            field_dict["NumberofClassroomsEN"] = numberof_classrooms_en
        if numberof_classrooms_tc is not UNSET:
            field_dict["NumberofClassroomsTC"] = numberof_classrooms_tc
        if numberof_lecture_threaters_en is not UNSET:
            field_dict["NumberofLectureThreatersEN"] = numberof_lecture_threaters_en
        if numberof_lecture_threaters_tc is not UNSET:
            field_dict["NumberofLectureThreatersTC"] = numberof_lecture_threaters_tc
        if numberof_lab_en is not UNSET:
            field_dict["NumberofLabEN"] = numberof_lab_en
        if numberof_lab_tc is not UNSET:
            field_dict["NumberofLabTC"] = numberof_lab_tc
        if numberof_books_en is not UNSET:
            field_dict["NumberofBooksEN"] = numberof_books_en
        if numberof_books_tc is not UNSET:
            field_dict["NumberofBooksTC"] = numberof_books_tc
        if other_teaching_facilities_en is not UNSET:
            field_dict["OtherTeachingFacilitiesEN"] = other_teaching_facilities_en
        if other_teaching_facilities_tc is not UNSET:
            field_dict["OtherTeachingFacilitiesTC"] = other_teaching_facilities_tc
        if othernon_teaching_facilities_en is not UNSET:
            field_dict["OthernonTeachingFacilitiesEN"] = othernon_teaching_facilities_en
        if othernon_teaching_facilities_tc is not UNSET:
            field_dict["OthernonTeachingFacilitiesTC"] = othernon_teaching_facilities_tc
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

        def _parse_numberof_classrooms_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numberof_classrooms_en = _parse_numberof_classrooms_en(
            d.pop("NumberofClassroomsEN", UNSET)
        )

        def _parse_numberof_classrooms_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numberof_classrooms_tc = _parse_numberof_classrooms_tc(
            d.pop("NumberofClassroomsTC", UNSET)
        )

        def _parse_numberof_lecture_threaters_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numberof_lecture_threaters_en = _parse_numberof_lecture_threaters_en(
            d.pop("NumberofLectureThreatersEN", UNSET)
        )

        def _parse_numberof_lecture_threaters_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numberof_lecture_threaters_tc = _parse_numberof_lecture_threaters_tc(
            d.pop("NumberofLectureThreatersTC", UNSET)
        )

        def _parse_numberof_lab_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numberof_lab_en = _parse_numberof_lab_en(d.pop("NumberofLabEN", UNSET))

        def _parse_numberof_lab_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numberof_lab_tc = _parse_numberof_lab_tc(d.pop("NumberofLabTC", UNSET))

        def _parse_numberof_books_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numberof_books_en = _parse_numberof_books_en(d.pop("NumberofBooksEN", UNSET))

        def _parse_numberof_books_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numberof_books_tc = _parse_numberof_books_tc(d.pop("NumberofBooksTC", UNSET))

        def _parse_other_teaching_facilities_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_teaching_facilities_en = _parse_other_teaching_facilities_en(
            d.pop("OtherTeachingFacilitiesEN", UNSET)
        )

        def _parse_other_teaching_facilities_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_teaching_facilities_tc = _parse_other_teaching_facilities_tc(
            d.pop("OtherTeachingFacilitiesTC", UNSET)
        )

        def _parse_othernon_teaching_facilities_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        othernon_teaching_facilities_en = _parse_othernon_teaching_facilities_en(
            d.pop("OthernonTeachingFacilitiesEN", UNSET)
        )

        def _parse_othernon_teaching_facilities_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        othernon_teaching_facilities_tc = _parse_othernon_teaching_facilities_tc(
            d.pop("OthernonTeachingFacilitiesTC", UNSET)
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
            numberof_classrooms_en=numberof_classrooms_en,
            numberof_classrooms_tc=numberof_classrooms_tc,
            numberof_lecture_threaters_en=numberof_lecture_threaters_en,
            numberof_lecture_threaters_tc=numberof_lecture_threaters_tc,
            numberof_lab_en=numberof_lab_en,
            numberof_lab_tc=numberof_lab_tc,
            numberof_books_en=numberof_books_en,
            numberof_books_tc=numberof_books_tc,
            other_teaching_facilities_en=other_teaching_facilities_en,
            other_teaching_facilities_tc=other_teaching_facilities_tc,
            othernon_teaching_facilities_en=othernon_teaching_facilities_en,
            othernon_teaching_facilities_tc=othernon_teaching_facilities_tc,
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
