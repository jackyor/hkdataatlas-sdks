from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.remark_legend import RemarkLegend
    from ..models.schedule import Schedule


T = TypeVar("T", bound="Activity")


@_attrs_define
class Activity:
    """Activity field dictionary. The source does not establish field requiredness.

    Attributes:
        activity_name_english (str | Unset): Activity type in English. The dictionary lists these English names: General
            Charitable Fund-Raising Activity; Flag Day; Lottery (Obtained Approval for Selling on Public Streets); Lottery
            (Have Not Obtained Approval for Selling on Public Streets); Non-Charitable Fund-Raising Activity; and On-street
            Selling for Fund-Raising Purpose.
        activity_name_s_chinese (str | Unset): Activity type in Simplified Chinese.
        activity_name_t_chinese (str | Unset): Activity type in Traditional Chinese.
        charitable (Any | Unset): Charitable identifier of an activity; wire type is not specified.
        department_name_english (str | Unset): Licence/permit issuing department, in English.
        department_name_s_chinese (str | Unset): Licence/permit issuing department, in Simplified Chinese.
        department_name_t_chinese (str | Unset): Licence/permit issuing department, in Traditional Chinese.
        enquiry_contact (str | Unset): Enquiry/contact information of an activity.
        licence_permit_type_english (str | Unset): Licence/permit type applied for, in English.
        licence_permit_type_s_chinese (str | Unset): Licence/permit type applied for, in Simplified Chinese.
        licence_permit_type_t_chinese (str | Unset): Licence/permit type applied for, in Traditional Chinese.
        organisation_name_english (str | Unset): Organisation name in English.
        organisation_name_s_chinese (str | Unset): Organisation name in Simplified Chinese.
        organisation_name_t_chinese (str | Unset): Organisation name in Traditional Chinese.
        permit_number (str | Unset): Licence/permit number assigned to an activity.
        remark_legends (list[RemarkLegend] | Unset): List of remark legends, if any.
        remarks (list[str] | Unset): List of remark identifiers; legends are included within remarkLegends.
        schedule (list[Schedule] | Unset): Schedule of an activity.
        sub_schedule (Any | Unset): XML-only sub-schedule of an activity.
        supplementary_info_engish (str | Unset): Supplementary information of an activity, in English. The source spells
            the field name 'supplementaryInfoEngish'.
        supplementary_info_s_chinese (str | Unset): Supplementary information of an activity, in Simplified Chinese.
        supplementary_info_t_chinese (str | Unset): Supplementary information of an activity, in Traditional Chinese.
    """

    activity_name_english: str | Unset = UNSET
    activity_name_s_chinese: str | Unset = UNSET
    activity_name_t_chinese: str | Unset = UNSET
    charitable: Any | Unset = UNSET
    department_name_english: str | Unset = UNSET
    department_name_s_chinese: str | Unset = UNSET
    department_name_t_chinese: str | Unset = UNSET
    enquiry_contact: str | Unset = UNSET
    licence_permit_type_english: str | Unset = UNSET
    licence_permit_type_s_chinese: str | Unset = UNSET
    licence_permit_type_t_chinese: str | Unset = UNSET
    organisation_name_english: str | Unset = UNSET
    organisation_name_s_chinese: str | Unset = UNSET
    organisation_name_t_chinese: str | Unset = UNSET
    permit_number: str | Unset = UNSET
    remark_legends: list[RemarkLegend] | Unset = UNSET
    remarks: list[str] | Unset = UNSET
    schedule: list[Schedule] | Unset = UNSET
    sub_schedule: Any | Unset = UNSET
    supplementary_info_engish: str | Unset = UNSET
    supplementary_info_s_chinese: str | Unset = UNSET
    supplementary_info_t_chinese: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_name_english = self.activity_name_english

        activity_name_s_chinese = self.activity_name_s_chinese

        activity_name_t_chinese = self.activity_name_t_chinese

        charitable = self.charitable

        department_name_english = self.department_name_english

        department_name_s_chinese = self.department_name_s_chinese

        department_name_t_chinese = self.department_name_t_chinese

        enquiry_contact = self.enquiry_contact

        licence_permit_type_english = self.licence_permit_type_english

        licence_permit_type_s_chinese = self.licence_permit_type_s_chinese

        licence_permit_type_t_chinese = self.licence_permit_type_t_chinese

        organisation_name_english = self.organisation_name_english

        organisation_name_s_chinese = self.organisation_name_s_chinese

        organisation_name_t_chinese = self.organisation_name_t_chinese

        permit_number = self.permit_number

        remark_legends: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.remark_legends, Unset):
            remark_legends = []
            for remark_legends_item_data in self.remark_legends:
                remark_legends_item = remark_legends_item_data.to_dict()
                remark_legends.append(remark_legends_item)

        remarks: list[str] | Unset = UNSET
        if not isinstance(self.remarks, Unset):
            remarks = self.remarks

        schedule: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = []
            for schedule_item_data in self.schedule:
                schedule_item = schedule_item_data.to_dict()
                schedule.append(schedule_item)

        sub_schedule = self.sub_schedule

        supplementary_info_engish = self.supplementary_info_engish

        supplementary_info_s_chinese = self.supplementary_info_s_chinese

        supplementary_info_t_chinese = self.supplementary_info_t_chinese

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_name_english is not UNSET:
            field_dict["activityNameEnglish"] = activity_name_english
        if activity_name_s_chinese is not UNSET:
            field_dict["activityNameSChinese"] = activity_name_s_chinese
        if activity_name_t_chinese is not UNSET:
            field_dict["activityNameTChinese"] = activity_name_t_chinese
        if charitable is not UNSET:
            field_dict["charitable"] = charitable
        if department_name_english is not UNSET:
            field_dict["departmentNameEnglish"] = department_name_english
        if department_name_s_chinese is not UNSET:
            field_dict["departmentNameSChinese"] = department_name_s_chinese
        if department_name_t_chinese is not UNSET:
            field_dict["departmentNameTChinese"] = department_name_t_chinese
        if enquiry_contact is not UNSET:
            field_dict["enquiryContact"] = enquiry_contact
        if licence_permit_type_english is not UNSET:
            field_dict["licencePermitTypeEnglish"] = licence_permit_type_english
        if licence_permit_type_s_chinese is not UNSET:
            field_dict["licencePermitTypeSChinese"] = licence_permit_type_s_chinese
        if licence_permit_type_t_chinese is not UNSET:
            field_dict["licencePermitTypeTChinese"] = licence_permit_type_t_chinese
        if organisation_name_english is not UNSET:
            field_dict["organisationNameEnglish"] = organisation_name_english
        if organisation_name_s_chinese is not UNSET:
            field_dict["organisationNameSChinese"] = organisation_name_s_chinese
        if organisation_name_t_chinese is not UNSET:
            field_dict["organisationNameTChinese"] = organisation_name_t_chinese
        if permit_number is not UNSET:
            field_dict["permitNumber"] = permit_number
        if remark_legends is not UNSET:
            field_dict["remarkLegends"] = remark_legends
        if remarks is not UNSET:
            field_dict["remarks"] = remarks
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if sub_schedule is not UNSET:
            field_dict["subSchedule"] = sub_schedule
        if supplementary_info_engish is not UNSET:
            field_dict["supplementaryInfoEngish"] = supplementary_info_engish
        if supplementary_info_s_chinese is not UNSET:
            field_dict["supplementaryInfoSChinese"] = supplementary_info_s_chinese
        if supplementary_info_t_chinese is not UNSET:
            field_dict["supplementaryInfoTChinese"] = supplementary_info_t_chinese

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.remark_legend import RemarkLegend
        from ..models.schedule import Schedule

        d = dict(src_dict)
        activity_name_english = d.pop("activityNameEnglish", UNSET)

        activity_name_s_chinese = d.pop("activityNameSChinese", UNSET)

        activity_name_t_chinese = d.pop("activityNameTChinese", UNSET)

        charitable = d.pop("charitable", UNSET)

        department_name_english = d.pop("departmentNameEnglish", UNSET)

        department_name_s_chinese = d.pop("departmentNameSChinese", UNSET)

        department_name_t_chinese = d.pop("departmentNameTChinese", UNSET)

        enquiry_contact = d.pop("enquiryContact", UNSET)

        licence_permit_type_english = d.pop("licencePermitTypeEnglish", UNSET)

        licence_permit_type_s_chinese = d.pop("licencePermitTypeSChinese", UNSET)

        licence_permit_type_t_chinese = d.pop("licencePermitTypeTChinese", UNSET)

        organisation_name_english = d.pop("organisationNameEnglish", UNSET)

        organisation_name_s_chinese = d.pop("organisationNameSChinese", UNSET)

        organisation_name_t_chinese = d.pop("organisationNameTChinese", UNSET)

        permit_number = d.pop("permitNumber", UNSET)

        _remark_legends = d.pop("remarkLegends", UNSET)
        remark_legends: list[RemarkLegend] | Unset = UNSET
        if _remark_legends is not UNSET:
            remark_legends = []
            for remark_legends_item_data in _remark_legends:
                remark_legends_item = RemarkLegend.from_dict(remark_legends_item_data)

                remark_legends.append(remark_legends_item)

        remarks = cast(list[str], d.pop("remarks", UNSET))

        _schedule = d.pop("schedule", UNSET)
        schedule: list[Schedule] | Unset = UNSET
        if _schedule is not UNSET:
            schedule = []
            for schedule_item_data in _schedule:
                schedule_item = Schedule.from_dict(schedule_item_data)

                schedule.append(schedule_item)

        sub_schedule = d.pop("subSchedule", UNSET)

        supplementary_info_engish = d.pop("supplementaryInfoEngish", UNSET)

        supplementary_info_s_chinese = d.pop("supplementaryInfoSChinese", UNSET)

        supplementary_info_t_chinese = d.pop("supplementaryInfoTChinese", UNSET)

        activity = cls(
            activity_name_english=activity_name_english,
            activity_name_s_chinese=activity_name_s_chinese,
            activity_name_t_chinese=activity_name_t_chinese,
            charitable=charitable,
            department_name_english=department_name_english,
            department_name_s_chinese=department_name_s_chinese,
            department_name_t_chinese=department_name_t_chinese,
            enquiry_contact=enquiry_contact,
            licence_permit_type_english=licence_permit_type_english,
            licence_permit_type_s_chinese=licence_permit_type_s_chinese,
            licence_permit_type_t_chinese=licence_permit_type_t_chinese,
            organisation_name_english=organisation_name_english,
            organisation_name_s_chinese=organisation_name_s_chinese,
            organisation_name_t_chinese=organisation_name_t_chinese,
            permit_number=permit_number,
            remark_legends=remark_legends,
            remarks=remarks,
            schedule=schedule,
            sub_schedule=sub_schedule,
            supplementary_info_engish=supplementary_info_engish,
            supplementary_info_s_chinese=supplementary_info_s_chinese,
            supplementary_info_t_chinese=supplementary_info_t_chinese,
        )

        activity.additional_properties = d
        return activity

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
