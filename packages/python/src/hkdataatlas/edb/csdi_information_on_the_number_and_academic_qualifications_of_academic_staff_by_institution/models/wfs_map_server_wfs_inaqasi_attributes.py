from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsINAQASIAttributes")


@_attrs_define
class WfsMapServerWfsINAQASIAttributes:
    """
    Attributes:
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        dataset_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        dataset_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        address_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        numberof_ft_staff_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        numberof_ft_staff_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        numberof_ft_staff_equivalent_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        numberof_ft_staff_equivalent_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        numberof_pt_staff_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        numberof_pt_staff_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        numberof_pt_staff_equivalent_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        numberof_pt_staff_equivalent_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        highest_qualifi_masterdegree_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        highest_qualifi_masterdegree_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        highest_qualifi_bachelordegree_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        highest_qualifi_bachelordegree_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        highest_qualifi_other_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        highest_qualifi_other_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        academic_staffto_student_ratio_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        academic_staffto_student_ratio_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        academic_staffwith_prof_quali_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        academic_staffwith_prof_quali_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        northing (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        easting (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        latitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        longitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        last_update (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    shape: Any | Unset = UNSET
    objectid: int | Unset = UNSET
    dataset_en: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    numberof_ft_staff_en: None | str | Unset = UNSET
    numberof_ft_staff_tc: None | str | Unset = UNSET
    numberof_ft_staff_equivalent_en: None | str | Unset = UNSET
    numberof_ft_staff_equivalent_tc: None | str | Unset = UNSET
    numberof_pt_staff_en: None | str | Unset = UNSET
    numberof_pt_staff_tc: None | str | Unset = UNSET
    numberof_pt_staff_equivalent_en: None | str | Unset = UNSET
    numberof_pt_staff_equivalent_tc: None | str | Unset = UNSET
    highest_qualifi_masterdegree_en: None | str | Unset = UNSET
    highest_qualifi_masterdegree_tc: None | str | Unset = UNSET
    highest_qualifi_bachelordegree_en: None | str | Unset = UNSET
    highest_qualifi_bachelordegree_tc: None | str | Unset = UNSET
    highest_qualifi_other_en: None | str | Unset = UNSET
    highest_qualifi_other_tc: None | str | Unset = UNSET
    academic_staffto_student_ratio_en: None | str | Unset = UNSET
    academic_staffto_student_ratio_tc: None | str | Unset = UNSET
    academic_staffwith_prof_quali_en: None | str | Unset = UNSET
    academic_staffwith_prof_quali_tc: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    easting: float | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    last_update: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shape = self.shape

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

        numberof_ft_staff_en: None | str | Unset
        if isinstance(self.numberof_ft_staff_en, Unset):
            numberof_ft_staff_en = UNSET
        else:
            numberof_ft_staff_en = self.numberof_ft_staff_en

        numberof_ft_staff_tc: None | str | Unset
        if isinstance(self.numberof_ft_staff_tc, Unset):
            numberof_ft_staff_tc = UNSET
        else:
            numberof_ft_staff_tc = self.numberof_ft_staff_tc

        numberof_ft_staff_equivalent_en: None | str | Unset
        if isinstance(self.numberof_ft_staff_equivalent_en, Unset):
            numberof_ft_staff_equivalent_en = UNSET
        else:
            numberof_ft_staff_equivalent_en = self.numberof_ft_staff_equivalent_en

        numberof_ft_staff_equivalent_tc: None | str | Unset
        if isinstance(self.numberof_ft_staff_equivalent_tc, Unset):
            numberof_ft_staff_equivalent_tc = UNSET
        else:
            numberof_ft_staff_equivalent_tc = self.numberof_ft_staff_equivalent_tc

        numberof_pt_staff_en: None | str | Unset
        if isinstance(self.numberof_pt_staff_en, Unset):
            numberof_pt_staff_en = UNSET
        else:
            numberof_pt_staff_en = self.numberof_pt_staff_en

        numberof_pt_staff_tc: None | str | Unset
        if isinstance(self.numberof_pt_staff_tc, Unset):
            numberof_pt_staff_tc = UNSET
        else:
            numberof_pt_staff_tc = self.numberof_pt_staff_tc

        numberof_pt_staff_equivalent_en: None | str | Unset
        if isinstance(self.numberof_pt_staff_equivalent_en, Unset):
            numberof_pt_staff_equivalent_en = UNSET
        else:
            numberof_pt_staff_equivalent_en = self.numberof_pt_staff_equivalent_en

        numberof_pt_staff_equivalent_tc: None | str | Unset
        if isinstance(self.numberof_pt_staff_equivalent_tc, Unset):
            numberof_pt_staff_equivalent_tc = UNSET
        else:
            numberof_pt_staff_equivalent_tc = self.numberof_pt_staff_equivalent_tc

        highest_qualifi_masterdegree_en: None | str | Unset
        if isinstance(self.highest_qualifi_masterdegree_en, Unset):
            highest_qualifi_masterdegree_en = UNSET
        else:
            highest_qualifi_masterdegree_en = self.highest_qualifi_masterdegree_en

        highest_qualifi_masterdegree_tc: None | str | Unset
        if isinstance(self.highest_qualifi_masterdegree_tc, Unset):
            highest_qualifi_masterdegree_tc = UNSET
        else:
            highest_qualifi_masterdegree_tc = self.highest_qualifi_masterdegree_tc

        highest_qualifi_bachelordegree_en: None | str | Unset
        if isinstance(self.highest_qualifi_bachelordegree_en, Unset):
            highest_qualifi_bachelordegree_en = UNSET
        else:
            highest_qualifi_bachelordegree_en = self.highest_qualifi_bachelordegree_en

        highest_qualifi_bachelordegree_tc: None | str | Unset
        if isinstance(self.highest_qualifi_bachelordegree_tc, Unset):
            highest_qualifi_bachelordegree_tc = UNSET
        else:
            highest_qualifi_bachelordegree_tc = self.highest_qualifi_bachelordegree_tc

        highest_qualifi_other_en: None | str | Unset
        if isinstance(self.highest_qualifi_other_en, Unset):
            highest_qualifi_other_en = UNSET
        else:
            highest_qualifi_other_en = self.highest_qualifi_other_en

        highest_qualifi_other_tc: None | str | Unset
        if isinstance(self.highest_qualifi_other_tc, Unset):
            highest_qualifi_other_tc = UNSET
        else:
            highest_qualifi_other_tc = self.highest_qualifi_other_tc

        academic_staffto_student_ratio_en: None | str | Unset
        if isinstance(self.academic_staffto_student_ratio_en, Unset):
            academic_staffto_student_ratio_en = UNSET
        else:
            academic_staffto_student_ratio_en = self.academic_staffto_student_ratio_en

        academic_staffto_student_ratio_tc: None | str | Unset
        if isinstance(self.academic_staffto_student_ratio_tc, Unset):
            academic_staffto_student_ratio_tc = UNSET
        else:
            academic_staffto_student_ratio_tc = self.academic_staffto_student_ratio_tc

        academic_staffwith_prof_quali_en: None | str | Unset
        if isinstance(self.academic_staffwith_prof_quali_en, Unset):
            academic_staffwith_prof_quali_en = UNSET
        else:
            academic_staffwith_prof_quali_en = self.academic_staffwith_prof_quali_en

        academic_staffwith_prof_quali_tc: None | str | Unset
        if isinstance(self.academic_staffwith_prof_quali_tc, Unset):
            academic_staffwith_prof_quali_tc = UNSET
        else:
            academic_staffwith_prof_quali_tc = self.academic_staffwith_prof_quali_tc

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

        last_update: None | str | Unset
        if isinstance(self.last_update, Unset):
            last_update = UNSET
        else:
            last_update = self.last_update

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shape is not UNSET:
            field_dict["shape"] = shape
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
        if numberof_ft_staff_en is not UNSET:
            field_dict["NumberofFTStaffEN"] = numberof_ft_staff_en
        if numberof_ft_staff_tc is not UNSET:
            field_dict["NumberofFTStaffTC"] = numberof_ft_staff_tc
        if numberof_ft_staff_equivalent_en is not UNSET:
            field_dict["NumberofFTStaffEquivalentEN"] = numberof_ft_staff_equivalent_en
        if numberof_ft_staff_equivalent_tc is not UNSET:
            field_dict["NumberofFTStaffEquivalentTC"] = numberof_ft_staff_equivalent_tc
        if numberof_pt_staff_en is not UNSET:
            field_dict["NumberofPTStaffEN"] = numberof_pt_staff_en
        if numberof_pt_staff_tc is not UNSET:
            field_dict["NumberofPTStaffTC"] = numberof_pt_staff_tc
        if numberof_pt_staff_equivalent_en is not UNSET:
            field_dict["NumberofPTStaffEquivalentEN"] = numberof_pt_staff_equivalent_en
        if numberof_pt_staff_equivalent_tc is not UNSET:
            field_dict["NumberofPTStaffEquivalentTC"] = numberof_pt_staff_equivalent_tc
        if highest_qualifi_masterdegree_en is not UNSET:
            field_dict["HighestQualifiMasterdegreeEN"] = highest_qualifi_masterdegree_en
        if highest_qualifi_masterdegree_tc is not UNSET:
            field_dict["HighestQualifiMasterdegreeTC"] = highest_qualifi_masterdegree_tc
        if highest_qualifi_bachelordegree_en is not UNSET:
            field_dict["HighestQualifiBachelordegreeEN"] = (
                highest_qualifi_bachelordegree_en
            )
        if highest_qualifi_bachelordegree_tc is not UNSET:
            field_dict["HighestQualifiBachelordegreeTC"] = (
                highest_qualifi_bachelordegree_tc
            )
        if highest_qualifi_other_en is not UNSET:
            field_dict["HighestQualifiOtherEN"] = highest_qualifi_other_en
        if highest_qualifi_other_tc is not UNSET:
            field_dict["HighestQualifiOtherTC"] = highest_qualifi_other_tc
        if academic_staffto_student_ratio_en is not UNSET:
            field_dict["AcademicStafftoStudentRatioEN"] = (
                academic_staffto_student_ratio_en
            )
        if academic_staffto_student_ratio_tc is not UNSET:
            field_dict["AcademicStafftoStudentRatioTC"] = (
                academic_staffto_student_ratio_tc
            )
        if academic_staffwith_prof_quali_en is not UNSET:
            field_dict["AcademicStaffwithProfQualiEN"] = (
                academic_staffwith_prof_quali_en
            )
        if academic_staffwith_prof_quali_tc is not UNSET:
            field_dict["AcademicStaffwithProfQualiTC"] = (
                academic_staffwith_prof_quali_tc
            )
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
        shape = d.pop("shape", UNSET)

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

        def _parse_numberof_ft_staff_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numberof_ft_staff_en = _parse_numberof_ft_staff_en(
            d.pop("NumberofFTStaffEN", UNSET)
        )

        def _parse_numberof_ft_staff_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numberof_ft_staff_tc = _parse_numberof_ft_staff_tc(
            d.pop("NumberofFTStaffTC", UNSET)
        )

        def _parse_numberof_ft_staff_equivalent_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numberof_ft_staff_equivalent_en = _parse_numberof_ft_staff_equivalent_en(
            d.pop("NumberofFTStaffEquivalentEN", UNSET)
        )

        def _parse_numberof_ft_staff_equivalent_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numberof_ft_staff_equivalent_tc = _parse_numberof_ft_staff_equivalent_tc(
            d.pop("NumberofFTStaffEquivalentTC", UNSET)
        )

        def _parse_numberof_pt_staff_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numberof_pt_staff_en = _parse_numberof_pt_staff_en(
            d.pop("NumberofPTStaffEN", UNSET)
        )

        def _parse_numberof_pt_staff_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numberof_pt_staff_tc = _parse_numberof_pt_staff_tc(
            d.pop("NumberofPTStaffTC", UNSET)
        )

        def _parse_numberof_pt_staff_equivalent_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numberof_pt_staff_equivalent_en = _parse_numberof_pt_staff_equivalent_en(
            d.pop("NumberofPTStaffEquivalentEN", UNSET)
        )

        def _parse_numberof_pt_staff_equivalent_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numberof_pt_staff_equivalent_tc = _parse_numberof_pt_staff_equivalent_tc(
            d.pop("NumberofPTStaffEquivalentTC", UNSET)
        )

        def _parse_highest_qualifi_masterdegree_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        highest_qualifi_masterdegree_en = _parse_highest_qualifi_masterdegree_en(
            d.pop("HighestQualifiMasterdegreeEN", UNSET)
        )

        def _parse_highest_qualifi_masterdegree_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        highest_qualifi_masterdegree_tc = _parse_highest_qualifi_masterdegree_tc(
            d.pop("HighestQualifiMasterdegreeTC", UNSET)
        )

        def _parse_highest_qualifi_bachelordegree_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        highest_qualifi_bachelordegree_en = _parse_highest_qualifi_bachelordegree_en(
            d.pop("HighestQualifiBachelordegreeEN", UNSET)
        )

        def _parse_highest_qualifi_bachelordegree_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        highest_qualifi_bachelordegree_tc = _parse_highest_qualifi_bachelordegree_tc(
            d.pop("HighestQualifiBachelordegreeTC", UNSET)
        )

        def _parse_highest_qualifi_other_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        highest_qualifi_other_en = _parse_highest_qualifi_other_en(
            d.pop("HighestQualifiOtherEN", UNSET)
        )

        def _parse_highest_qualifi_other_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        highest_qualifi_other_tc = _parse_highest_qualifi_other_tc(
            d.pop("HighestQualifiOtherTC", UNSET)
        )

        def _parse_academic_staffto_student_ratio_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        academic_staffto_student_ratio_en = _parse_academic_staffto_student_ratio_en(
            d.pop("AcademicStafftoStudentRatioEN", UNSET)
        )

        def _parse_academic_staffto_student_ratio_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        academic_staffto_student_ratio_tc = _parse_academic_staffto_student_ratio_tc(
            d.pop("AcademicStafftoStudentRatioTC", UNSET)
        )

        def _parse_academic_staffwith_prof_quali_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        academic_staffwith_prof_quali_en = _parse_academic_staffwith_prof_quali_en(
            d.pop("AcademicStaffwithProfQualiEN", UNSET)
        )

        def _parse_academic_staffwith_prof_quali_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        academic_staffwith_prof_quali_tc = _parse_academic_staffwith_prof_quali_tc(
            d.pop("AcademicStaffwithProfQualiTC", UNSET)
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

        def _parse_last_update(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_update = _parse_last_update(d.pop("LastUpdate", UNSET))

        wfs_map_server_wfs_inaqasi_attributes = cls(
            shape=shape,
            objectid=objectid,
            dataset_en=dataset_en,
            dataset_tc=dataset_tc,
            name_en=name_en,
            address_en=address_en,
            name_tc=name_tc,
            address_tc=address_tc,
            numberof_ft_staff_en=numberof_ft_staff_en,
            numberof_ft_staff_tc=numberof_ft_staff_tc,
            numberof_ft_staff_equivalent_en=numberof_ft_staff_equivalent_en,
            numberof_ft_staff_equivalent_tc=numberof_ft_staff_equivalent_tc,
            numberof_pt_staff_en=numberof_pt_staff_en,
            numberof_pt_staff_tc=numberof_pt_staff_tc,
            numberof_pt_staff_equivalent_en=numberof_pt_staff_equivalent_en,
            numberof_pt_staff_equivalent_tc=numberof_pt_staff_equivalent_tc,
            highest_qualifi_masterdegree_en=highest_qualifi_masterdegree_en,
            highest_qualifi_masterdegree_tc=highest_qualifi_masterdegree_tc,
            highest_qualifi_bachelordegree_en=highest_qualifi_bachelordegree_en,
            highest_qualifi_bachelordegree_tc=highest_qualifi_bachelordegree_tc,
            highest_qualifi_other_en=highest_qualifi_other_en,
            highest_qualifi_other_tc=highest_qualifi_other_tc,
            academic_staffto_student_ratio_en=academic_staffto_student_ratio_en,
            academic_staffto_student_ratio_tc=academic_staffto_student_ratio_tc,
            academic_staffwith_prof_quali_en=academic_staffwith_prof_quali_en,
            academic_staffwith_prof_quali_tc=academic_staffwith_prof_quali_tc,
            northing=northing,
            easting=easting,
            latitude=latitude,
            longitude=longitude,
            last_update=last_update,
        )

        wfs_map_server_wfs_inaqasi_attributes.additional_properties = d
        return wfs_map_server_wfs_inaqasi_attributes

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
