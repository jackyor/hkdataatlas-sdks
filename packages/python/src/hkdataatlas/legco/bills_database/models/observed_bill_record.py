from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObservedBillRecord")


@_attrs_define
class ObservedBillRecord:
    """Observed response-record derivative of the publisher PDF dictionary. It retains documented Text and local DateTime
    representations, allows null only where present in the complete saved body, and omits URI formatting only on fields
    with observed empty strings. The documented BillRecord component remains unchanged.

        Attributes:
            additional_information_chi (str | Unset): Additional information in Chinese.
            additional_information_eng (str | Unset): Additional information in English.
            bill_content_url_2_chi (str | Unset): Second URL of the content of the bill in Chinese. Publisher dictionary
                type is Text; the complete retained response includes empty strings, so the generated absolute-URI format
                constraint is not applied in this observed derivative.
            bill_content_url_2_eng (str | Unset): Second URL of the content of the bill in English. Publisher dictionary
                type is Text; the complete retained response includes empty strings, so the generated absolute-URI format
                constraint is not applied in this observed derivative.
            bill_content_url_3_chi (str | Unset): Third URL of the content of the bill in Chinese. Publisher dictionary type
                is Text; the complete retained response includes empty strings, so the generated absolute-URI format constraint
                is not applied in this observed derivative.
            bill_content_url_3_eng (str | Unset): Third URL of the content of the bill in English. Publisher dictionary type
                is Text; the complete retained response includes empty strings, so the generated absolute-URI format constraint
                is not applied in this observed derivative.
            bill_content_url_chi (str | Unset): URL of the content of the bill in Chinese.
            bill_content_url_eng (str | Unset): URL of the content of the bill in English.
            bill_gazette_date (str | Unset): The PDF specifies YYYY-MM-DDThh:mm:ss without a timezone, and the retained
                response uses these local timestamp strings. RFC3339 date-time format is not asserted; values are not coerced or
                assigned a timezone.
            bill_gazette_date_2 (None | str | Unset): Publisher-documented field representation plus null observed in the
                complete retained response; optionality is not inferred from this sample.
            bill_gazette_date_3 (None | str | Unset): Publisher-documented field representation plus null observed in the
                complete retained response; optionality is not inferred from this sample.
            bill_title_chi (str | Unset): Title of the bill in Chinese.
            bill_title_eng (str | Unset): Title of the bill in English.
            bills_committee_formation_date (None | str | Unset): Publisher-documented field representation plus null
                observed in the complete retained response; optionality is not inferred from this sample.
            bills_committee_report_url_chi (str | Unset): URL of the Chinese report of the bills committee. Publisher
                dictionary type is Text; the complete retained response includes empty strings, so the generated absolute-URI
                format constraint is not applied in this observed derivative.
            bills_committee_report_url_eng (str | Unset): URL of the English report of the bills committee. Publisher
                dictionary type is Text; the complete retained response includes empty strings, so the generated absolute-URI
                format constraint is not applied in this observed derivative.
            bills_committee_title_chi (str | Unset): Chinese title of the bills committee.
            bills_committee_title_eng (str | Unset): English title of the bills committee.
            bills_committee_url_chi (str | Unset): URL of the Chinese home page of the bills committee. Publisher dictionary
                type is Text; the complete retained response includes empty strings, so the generated absolute-URI format
                constraint is not applied in this observed derivative.
            bills_committee_url_eng (str | Unset): URL of the English home page of the bills committee. Publisher dictionary
                type is Text; the complete retained response includes empty strings, so the generated absolute-URI format
                constraint is not applied in this observed derivative.
            first_reading_date (str | Unset): The PDF specifies YYYY-MM-DDThh:mm:ss without a timezone, and the retained
                response uses these local timestamp strings. RFC3339 date-time format is not asserted; values are not coerced or
                assigned a timezone.
            first_reading_date_2 (None | str | Unset): Publisher-documented field representation plus null observed in the
                complete retained response; optionality is not inferred from this sample.
            first_reading_date_2_hansard_url_chi (str | Unset): URL of the Chinese Hansard regarding the second date of the
                First Reading of the bill. Publisher dictionary type is Text; the complete retained response includes empty
                strings, so the generated absolute-URI format constraint is not applied in this observed derivative.
            first_reading_date_2_hansard_url_eng (str | Unset): URL of the English Hansard regarding the second date of the
                First Reading of the bill. Publisher dictionary type is Text; the complete retained response includes empty
                strings, so the generated absolute-URI format constraint is not applied in this observed derivative.
            first_reading_date_hansard_url_chi (str | Unset): URL of the Chinese Hansard regarding the First Reading of the
                bill.
            first_reading_date_hansard_url_eng (str | Unset): URL of the English Hansard regarding the First Reading of the
                bill.
            internal_key (str | Unset): Bill identifier.
            legco_brief_file_reference (str | Unset): File reference of the Legislative Council Brief.
            legco_brief_url_chi (str | Unset): URL of the Legislative Council Brief in Chinese. Publisher dictionary type is
                Text; the complete retained response includes empty strings, so the generated absolute-URI format constraint is
                not applied in this observed derivative.
            legco_brief_url_eng (str | Unset): URL of the Legislative Council Brief in English. Publisher dictionary type is
                Text; the complete retained response includes empty strings, so the generated absolute-URI format constraint is
                not applied in this observed derivative.
            ordinace_gazette_content_url_eng (str | Unset): URL of the content of the ordinance in the Gazette in English.
                The property spelling follows the publisher dictionary, which spells this name “ordinace”.
            ordinance_content_url_chi (str | Unset): URL of the content of the ordinance in Chinese. Publisher dictionary
                type is Text; the complete retained response includes empty strings, so the generated absolute-URI format
                constraint is not applied in this observed derivative.
            ordinance_content_url_eng (str | Unset): URL of the content of the ordinance in English. Publisher dictionary
                type is Text; the complete retained response includes empty strings, so the generated absolute-URI format
                constraint is not applied in this observed derivative.
            ordinance_gazette_content_url_chi (str | Unset): URL of the content of the ordinance in the Gazette in Chinese.
                The dictionary's printed property name is line-wrapped as “ordinance_gazette_content_url_chi”.
            ordinance_gazette_date (str | Unset): The PDF specifies YYYY-MM-DDThh:mm:ss without a timezone, and the retained
                response uses these local timestamp strings. RFC3339 date-time format is not asserted; values are not coerced or
                assigned a timezone.
            ordinance_title_chi (str | Unset): Title of the ordinance in Chinese.
            ordinance_title_eng (str | Unset): Title of the ordinance in English.
            ordinance_year_number_chi (str | Unset): Ordinance number in Chinese.
            ordinance_year_number_eng (str | Unset): Ordinance number in English.
            proposed_by_chi (str | Unset): Name of the proposer in Chinese.
            proposed_by_eng (str | Unset): Name of the proposer in English.
            remarks_chi (str | Unset): Remarks in Chinese.
            remarks_eng (str | Unset): Remarks in English.
            second_reading_date (str | Unset): The PDF specifies YYYY-MM-DDThh:mm:ss without a timezone, and the retained
                response uses these local timestamp strings. RFC3339 date-time format is not asserted; values are not coerced or
                assigned a timezone.
            second_reading_date_2 (None | str | Unset): Publisher-documented field representation plus null observed in the
                complete retained response; optionality is not inferred from this sample.
            second_reading_date_2_hansard_url_chi (str | Unset): URL of the Chinese Hansard regarding the second date of the
                Second Reading of the bill. Publisher dictionary type is Text; the complete retained response includes empty
                strings, so the generated absolute-URI format constraint is not applied in this observed derivative.
            second_reading_date_2_hansard_url_eng (str | Unset): URL of the English Hansard regarding the second date of the
                Second Reading of the bill. Publisher dictionary type is Text; the complete retained response includes empty
                strings, so the generated absolute-URI format constraint is not applied in this observed derivative.
            second_reading_date_3 (None | str | Unset): Publisher-documented field representation plus null observed in the
                complete retained response; optionality is not inferred from this sample.
            second_reading_date_3_hansard_url_chi (str | Unset): URL of the Chinese Hansard regarding the third date of the
                Second Reading of the bill. Publisher dictionary type is Text; the complete retained response includes empty
                strings, so the generated absolute-URI format constraint is not applied in this observed derivative.
            second_reading_date_3_hansard_url_eng (str | Unset): URL of the English Hansard regarding the third date of the
                Second Reading of the bill. Publisher dictionary type is Text; the complete retained response includes empty
                strings, so the generated absolute-URI format constraint is not applied in this observed derivative.
            second_reading_date_4 (None | str | Unset): Publisher-documented field representation plus null observed in the
                complete retained response; optionality is not inferred from this sample.
            second_reading_date_4_hansard_url_chi (str | Unset): URL of the Chinese Hansard regarding the fourth date of the
                Second Reading of the bill. Publisher dictionary type is Text; the complete retained response includes empty
                strings, so the generated absolute-URI format constraint is not applied in this observed derivative.
            second_reading_date_4_hansard_url_eng (str | Unset): URL of the English Hansard regarding the fourth date of the
                Second Reading of the bill. Publisher dictionary type is Text; the complete retained response includes empty
                strings, so the generated absolute-URI format constraint is not applied in this observed derivative.
            second_reading_date_5 (None | str | Unset): Publisher-documented field representation plus null observed in the
                complete retained response; optionality is not inferred from this sample.
            second_reading_date_5_hansard_url_chi (str | Unset): URL of the Chinese Hansard regarding the fifth date of the
                Second Reading of the bill. Publisher dictionary type is Text; the complete retained response includes empty
                strings, so the generated absolute-URI format constraint is not applied in this observed derivative.
            second_reading_date_5_hansard_url_eng (str | Unset): URL of the English Hansard regarding the fifth date of the
                Second Reading of the bill. Publisher dictionary type is Text; the complete retained response includes empty
                strings, so the generated absolute-URI format constraint is not applied in this observed derivative.
            second_reading_date_hansard_url_chi (str | Unset): URL of the Chinese Hansard regarding the Second Reading of
                the bill.
            second_reading_date_hansard_url_eng (str | Unset): URL of the English Hansard regarding the Second Reading of
                the bill.
            third_reading_date (str | Unset): The PDF specifies YYYY-MM-DDThh:mm:ss without a timezone, and the retained
                response uses these local timestamp strings. RFC3339 date-time format is not asserted; values are not coerced or
                assigned a timezone.
            third_reading_date_hansard_url_chi (str | Unset): URL of the Chinese Hansard regarding the Third Reading of the
                bill.
            third_reading_date_hansard_url_eng (str | Unset): URL of the English Hansard regarding the Third Reading of the
                bill.
    """

    additional_information_chi: str | Unset = UNSET
    additional_information_eng: str | Unset = UNSET
    bill_content_url_2_chi: str | Unset = UNSET
    bill_content_url_2_eng: str | Unset = UNSET
    bill_content_url_3_chi: str | Unset = UNSET
    bill_content_url_3_eng: str | Unset = UNSET
    bill_content_url_chi: str | Unset = UNSET
    bill_content_url_eng: str | Unset = UNSET
    bill_gazette_date: str | Unset = UNSET
    bill_gazette_date_2: None | str | Unset = UNSET
    bill_gazette_date_3: None | str | Unset = UNSET
    bill_title_chi: str | Unset = UNSET
    bill_title_eng: str | Unset = UNSET
    bills_committee_formation_date: None | str | Unset = UNSET
    bills_committee_report_url_chi: str | Unset = UNSET
    bills_committee_report_url_eng: str | Unset = UNSET
    bills_committee_title_chi: str | Unset = UNSET
    bills_committee_title_eng: str | Unset = UNSET
    bills_committee_url_chi: str | Unset = UNSET
    bills_committee_url_eng: str | Unset = UNSET
    first_reading_date: str | Unset = UNSET
    first_reading_date_2: None | str | Unset = UNSET
    first_reading_date_2_hansard_url_chi: str | Unset = UNSET
    first_reading_date_2_hansard_url_eng: str | Unset = UNSET
    first_reading_date_hansard_url_chi: str | Unset = UNSET
    first_reading_date_hansard_url_eng: str | Unset = UNSET
    internal_key: str | Unset = UNSET
    legco_brief_file_reference: str | Unset = UNSET
    legco_brief_url_chi: str | Unset = UNSET
    legco_brief_url_eng: str | Unset = UNSET
    ordinace_gazette_content_url_eng: str | Unset = UNSET
    ordinance_content_url_chi: str | Unset = UNSET
    ordinance_content_url_eng: str | Unset = UNSET
    ordinance_gazette_content_url_chi: str | Unset = UNSET
    ordinance_gazette_date: str | Unset = UNSET
    ordinance_title_chi: str | Unset = UNSET
    ordinance_title_eng: str | Unset = UNSET
    ordinance_year_number_chi: str | Unset = UNSET
    ordinance_year_number_eng: str | Unset = UNSET
    proposed_by_chi: str | Unset = UNSET
    proposed_by_eng: str | Unset = UNSET
    remarks_chi: str | Unset = UNSET
    remarks_eng: str | Unset = UNSET
    second_reading_date: str | Unset = UNSET
    second_reading_date_2: None | str | Unset = UNSET
    second_reading_date_2_hansard_url_chi: str | Unset = UNSET
    second_reading_date_2_hansard_url_eng: str | Unset = UNSET
    second_reading_date_3: None | str | Unset = UNSET
    second_reading_date_3_hansard_url_chi: str | Unset = UNSET
    second_reading_date_3_hansard_url_eng: str | Unset = UNSET
    second_reading_date_4: None | str | Unset = UNSET
    second_reading_date_4_hansard_url_chi: str | Unset = UNSET
    second_reading_date_4_hansard_url_eng: str | Unset = UNSET
    second_reading_date_5: None | str | Unset = UNSET
    second_reading_date_5_hansard_url_chi: str | Unset = UNSET
    second_reading_date_5_hansard_url_eng: str | Unset = UNSET
    second_reading_date_hansard_url_chi: str | Unset = UNSET
    second_reading_date_hansard_url_eng: str | Unset = UNSET
    third_reading_date: str | Unset = UNSET
    third_reading_date_hansard_url_chi: str | Unset = UNSET
    third_reading_date_hansard_url_eng: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_information_chi = self.additional_information_chi

        additional_information_eng = self.additional_information_eng

        bill_content_url_2_chi = self.bill_content_url_2_chi

        bill_content_url_2_eng = self.bill_content_url_2_eng

        bill_content_url_3_chi = self.bill_content_url_3_chi

        bill_content_url_3_eng = self.bill_content_url_3_eng

        bill_content_url_chi = self.bill_content_url_chi

        bill_content_url_eng = self.bill_content_url_eng

        bill_gazette_date = self.bill_gazette_date

        bill_gazette_date_2: None | str | Unset
        if isinstance(self.bill_gazette_date_2, Unset):
            bill_gazette_date_2 = UNSET
        else:
            bill_gazette_date_2 = self.bill_gazette_date_2

        bill_gazette_date_3: None | str | Unset
        if isinstance(self.bill_gazette_date_3, Unset):
            bill_gazette_date_3 = UNSET
        else:
            bill_gazette_date_3 = self.bill_gazette_date_3

        bill_title_chi = self.bill_title_chi

        bill_title_eng = self.bill_title_eng

        bills_committee_formation_date: None | str | Unset
        if isinstance(self.bills_committee_formation_date, Unset):
            bills_committee_formation_date = UNSET
        else:
            bills_committee_formation_date = self.bills_committee_formation_date

        bills_committee_report_url_chi = self.bills_committee_report_url_chi

        bills_committee_report_url_eng = self.bills_committee_report_url_eng

        bills_committee_title_chi = self.bills_committee_title_chi

        bills_committee_title_eng = self.bills_committee_title_eng

        bills_committee_url_chi = self.bills_committee_url_chi

        bills_committee_url_eng = self.bills_committee_url_eng

        first_reading_date = self.first_reading_date

        first_reading_date_2: None | str | Unset
        if isinstance(self.first_reading_date_2, Unset):
            first_reading_date_2 = UNSET
        else:
            first_reading_date_2 = self.first_reading_date_2

        first_reading_date_2_hansard_url_chi = self.first_reading_date_2_hansard_url_chi

        first_reading_date_2_hansard_url_eng = self.first_reading_date_2_hansard_url_eng

        first_reading_date_hansard_url_chi = self.first_reading_date_hansard_url_chi

        first_reading_date_hansard_url_eng = self.first_reading_date_hansard_url_eng

        internal_key = self.internal_key

        legco_brief_file_reference = self.legco_brief_file_reference

        legco_brief_url_chi = self.legco_brief_url_chi

        legco_brief_url_eng = self.legco_brief_url_eng

        ordinace_gazette_content_url_eng = self.ordinace_gazette_content_url_eng

        ordinance_content_url_chi = self.ordinance_content_url_chi

        ordinance_content_url_eng = self.ordinance_content_url_eng

        ordinance_gazette_content_url_chi = self.ordinance_gazette_content_url_chi

        ordinance_gazette_date = self.ordinance_gazette_date

        ordinance_title_chi = self.ordinance_title_chi

        ordinance_title_eng = self.ordinance_title_eng

        ordinance_year_number_chi = self.ordinance_year_number_chi

        ordinance_year_number_eng = self.ordinance_year_number_eng

        proposed_by_chi = self.proposed_by_chi

        proposed_by_eng = self.proposed_by_eng

        remarks_chi = self.remarks_chi

        remarks_eng = self.remarks_eng

        second_reading_date = self.second_reading_date

        second_reading_date_2: None | str | Unset
        if isinstance(self.second_reading_date_2, Unset):
            second_reading_date_2 = UNSET
        else:
            second_reading_date_2 = self.second_reading_date_2

        second_reading_date_2_hansard_url_chi = (
            self.second_reading_date_2_hansard_url_chi
        )

        second_reading_date_2_hansard_url_eng = (
            self.second_reading_date_2_hansard_url_eng
        )

        second_reading_date_3: None | str | Unset
        if isinstance(self.second_reading_date_3, Unset):
            second_reading_date_3 = UNSET
        else:
            second_reading_date_3 = self.second_reading_date_3

        second_reading_date_3_hansard_url_chi = (
            self.second_reading_date_3_hansard_url_chi
        )

        second_reading_date_3_hansard_url_eng = (
            self.second_reading_date_3_hansard_url_eng
        )

        second_reading_date_4: None | str | Unset
        if isinstance(self.second_reading_date_4, Unset):
            second_reading_date_4 = UNSET
        else:
            second_reading_date_4 = self.second_reading_date_4

        second_reading_date_4_hansard_url_chi = (
            self.second_reading_date_4_hansard_url_chi
        )

        second_reading_date_4_hansard_url_eng = (
            self.second_reading_date_4_hansard_url_eng
        )

        second_reading_date_5: None | str | Unset
        if isinstance(self.second_reading_date_5, Unset):
            second_reading_date_5 = UNSET
        else:
            second_reading_date_5 = self.second_reading_date_5

        second_reading_date_5_hansard_url_chi = (
            self.second_reading_date_5_hansard_url_chi
        )

        second_reading_date_5_hansard_url_eng = (
            self.second_reading_date_5_hansard_url_eng
        )

        second_reading_date_hansard_url_chi = self.second_reading_date_hansard_url_chi

        second_reading_date_hansard_url_eng = self.second_reading_date_hansard_url_eng

        third_reading_date = self.third_reading_date

        third_reading_date_hansard_url_chi = self.third_reading_date_hansard_url_chi

        third_reading_date_hansard_url_eng = self.third_reading_date_hansard_url_eng

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_information_chi is not UNSET:
            field_dict["additional_information_chi"] = additional_information_chi
        if additional_information_eng is not UNSET:
            field_dict["additional_information_eng"] = additional_information_eng
        if bill_content_url_2_chi is not UNSET:
            field_dict["bill_content_url_2_chi"] = bill_content_url_2_chi
        if bill_content_url_2_eng is not UNSET:
            field_dict["bill_content_url_2_eng"] = bill_content_url_2_eng
        if bill_content_url_3_chi is not UNSET:
            field_dict["bill_content_url_3_chi"] = bill_content_url_3_chi
        if bill_content_url_3_eng is not UNSET:
            field_dict["bill_content_url_3_eng"] = bill_content_url_3_eng
        if bill_content_url_chi is not UNSET:
            field_dict["bill_content_url_chi"] = bill_content_url_chi
        if bill_content_url_eng is not UNSET:
            field_dict["bill_content_url_eng"] = bill_content_url_eng
        if bill_gazette_date is not UNSET:
            field_dict["bill_gazette_date"] = bill_gazette_date
        if bill_gazette_date_2 is not UNSET:
            field_dict["bill_gazette_date_2"] = bill_gazette_date_2
        if bill_gazette_date_3 is not UNSET:
            field_dict["bill_gazette_date_3"] = bill_gazette_date_3
        if bill_title_chi is not UNSET:
            field_dict["bill_title_chi"] = bill_title_chi
        if bill_title_eng is not UNSET:
            field_dict["bill_title_eng"] = bill_title_eng
        if bills_committee_formation_date is not UNSET:
            field_dict["bills_committee_formation_date"] = (
                bills_committee_formation_date
            )
        if bills_committee_report_url_chi is not UNSET:
            field_dict["bills_committee_report_url_chi"] = (
                bills_committee_report_url_chi
            )
        if bills_committee_report_url_eng is not UNSET:
            field_dict["bills_committee_report_url_eng"] = (
                bills_committee_report_url_eng
            )
        if bills_committee_title_chi is not UNSET:
            field_dict["bills_committee_title_chi"] = bills_committee_title_chi
        if bills_committee_title_eng is not UNSET:
            field_dict["bills_committee_title_eng"] = bills_committee_title_eng
        if bills_committee_url_chi is not UNSET:
            field_dict["bills_committee_url_chi"] = bills_committee_url_chi
        if bills_committee_url_eng is not UNSET:
            field_dict["bills_committee_url_eng"] = bills_committee_url_eng
        if first_reading_date is not UNSET:
            field_dict["first_reading_date"] = first_reading_date
        if first_reading_date_2 is not UNSET:
            field_dict["first_reading_date_2"] = first_reading_date_2
        if first_reading_date_2_hansard_url_chi is not UNSET:
            field_dict["first_reading_date_2_hansard_url_chi"] = (
                first_reading_date_2_hansard_url_chi
            )
        if first_reading_date_2_hansard_url_eng is not UNSET:
            field_dict["first_reading_date_2_hansard_url_eng"] = (
                first_reading_date_2_hansard_url_eng
            )
        if first_reading_date_hansard_url_chi is not UNSET:
            field_dict["first_reading_date_hansard_url_chi"] = (
                first_reading_date_hansard_url_chi
            )
        if first_reading_date_hansard_url_eng is not UNSET:
            field_dict["first_reading_date_hansard_url_eng"] = (
                first_reading_date_hansard_url_eng
            )
        if internal_key is not UNSET:
            field_dict["internal_key"] = internal_key
        if legco_brief_file_reference is not UNSET:
            field_dict["legco_brief_file_reference"] = legco_brief_file_reference
        if legco_brief_url_chi is not UNSET:
            field_dict["legco_brief_url_chi"] = legco_brief_url_chi
        if legco_brief_url_eng is not UNSET:
            field_dict["legco_brief_url_eng"] = legco_brief_url_eng
        if ordinace_gazette_content_url_eng is not UNSET:
            field_dict["ordinace_gazette_content_url_eng"] = (
                ordinace_gazette_content_url_eng
            )
        if ordinance_content_url_chi is not UNSET:
            field_dict["ordinance_content_url_chi"] = ordinance_content_url_chi
        if ordinance_content_url_eng is not UNSET:
            field_dict["ordinance_content_url_eng"] = ordinance_content_url_eng
        if ordinance_gazette_content_url_chi is not UNSET:
            field_dict["ordinance_gazette_content_url_chi"] = (
                ordinance_gazette_content_url_chi
            )
        if ordinance_gazette_date is not UNSET:
            field_dict["ordinance_gazette_date"] = ordinance_gazette_date
        if ordinance_title_chi is not UNSET:
            field_dict["ordinance_title_chi"] = ordinance_title_chi
        if ordinance_title_eng is not UNSET:
            field_dict["ordinance_title_eng"] = ordinance_title_eng
        if ordinance_year_number_chi is not UNSET:
            field_dict["ordinance_year_number_chi"] = ordinance_year_number_chi
        if ordinance_year_number_eng is not UNSET:
            field_dict["ordinance_year_number_eng"] = ordinance_year_number_eng
        if proposed_by_chi is not UNSET:
            field_dict["proposed_by_chi"] = proposed_by_chi
        if proposed_by_eng is not UNSET:
            field_dict["proposed_by_eng"] = proposed_by_eng
        if remarks_chi is not UNSET:
            field_dict["remarks_chi"] = remarks_chi
        if remarks_eng is not UNSET:
            field_dict["remarks_eng"] = remarks_eng
        if second_reading_date is not UNSET:
            field_dict["second_reading_date"] = second_reading_date
        if second_reading_date_2 is not UNSET:
            field_dict["second_reading_date_2"] = second_reading_date_2
        if second_reading_date_2_hansard_url_chi is not UNSET:
            field_dict["second_reading_date_2_hansard_url_chi"] = (
                second_reading_date_2_hansard_url_chi
            )
        if second_reading_date_2_hansard_url_eng is not UNSET:
            field_dict["second_reading_date_2_hansard_url_eng"] = (
                second_reading_date_2_hansard_url_eng
            )
        if second_reading_date_3 is not UNSET:
            field_dict["second_reading_date_3"] = second_reading_date_3
        if second_reading_date_3_hansard_url_chi is not UNSET:
            field_dict["second_reading_date_3_hansard_url_chi"] = (
                second_reading_date_3_hansard_url_chi
            )
        if second_reading_date_3_hansard_url_eng is not UNSET:
            field_dict["second_reading_date_3_hansard_url_eng"] = (
                second_reading_date_3_hansard_url_eng
            )
        if second_reading_date_4 is not UNSET:
            field_dict["second_reading_date_4"] = second_reading_date_4
        if second_reading_date_4_hansard_url_chi is not UNSET:
            field_dict["second_reading_date_4_hansard_url_chi"] = (
                second_reading_date_4_hansard_url_chi
            )
        if second_reading_date_4_hansard_url_eng is not UNSET:
            field_dict["second_reading_date_4_hansard_url_eng"] = (
                second_reading_date_4_hansard_url_eng
            )
        if second_reading_date_5 is not UNSET:
            field_dict["second_reading_date_5"] = second_reading_date_5
        if second_reading_date_5_hansard_url_chi is not UNSET:
            field_dict["second_reading_date_5_hansard_url_chi"] = (
                second_reading_date_5_hansard_url_chi
            )
        if second_reading_date_5_hansard_url_eng is not UNSET:
            field_dict["second_reading_date_5_hansard_url_eng"] = (
                second_reading_date_5_hansard_url_eng
            )
        if second_reading_date_hansard_url_chi is not UNSET:
            field_dict["second_reading_date_hansard_url_chi"] = (
                second_reading_date_hansard_url_chi
            )
        if second_reading_date_hansard_url_eng is not UNSET:
            field_dict["second_reading_date_hansard_url_eng"] = (
                second_reading_date_hansard_url_eng
            )
        if third_reading_date is not UNSET:
            field_dict["third_reading_date"] = third_reading_date
        if third_reading_date_hansard_url_chi is not UNSET:
            field_dict["third_reading_date_hansard_url_chi"] = (
                third_reading_date_hansard_url_chi
            )
        if third_reading_date_hansard_url_eng is not UNSET:
            field_dict["third_reading_date_hansard_url_eng"] = (
                third_reading_date_hansard_url_eng
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        additional_information_chi = d.pop("additional_information_chi", UNSET)

        additional_information_eng = d.pop("additional_information_eng", UNSET)

        bill_content_url_2_chi = d.pop("bill_content_url_2_chi", UNSET)

        bill_content_url_2_eng = d.pop("bill_content_url_2_eng", UNSET)

        bill_content_url_3_chi = d.pop("bill_content_url_3_chi", UNSET)

        bill_content_url_3_eng = d.pop("bill_content_url_3_eng", UNSET)

        bill_content_url_chi = d.pop("bill_content_url_chi", UNSET)

        bill_content_url_eng = d.pop("bill_content_url_eng", UNSET)

        bill_gazette_date = d.pop("bill_gazette_date", UNSET)

        def _parse_bill_gazette_date_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bill_gazette_date_2 = _parse_bill_gazette_date_2(
            d.pop("bill_gazette_date_2", UNSET)
        )

        def _parse_bill_gazette_date_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bill_gazette_date_3 = _parse_bill_gazette_date_3(
            d.pop("bill_gazette_date_3", UNSET)
        )

        bill_title_chi = d.pop("bill_title_chi", UNSET)

        bill_title_eng = d.pop("bill_title_eng", UNSET)

        def _parse_bills_committee_formation_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bills_committee_formation_date = _parse_bills_committee_formation_date(
            d.pop("bills_committee_formation_date", UNSET)
        )

        bills_committee_report_url_chi = d.pop("bills_committee_report_url_chi", UNSET)

        bills_committee_report_url_eng = d.pop("bills_committee_report_url_eng", UNSET)

        bills_committee_title_chi = d.pop("bills_committee_title_chi", UNSET)

        bills_committee_title_eng = d.pop("bills_committee_title_eng", UNSET)

        bills_committee_url_chi = d.pop("bills_committee_url_chi", UNSET)

        bills_committee_url_eng = d.pop("bills_committee_url_eng", UNSET)

        first_reading_date = d.pop("first_reading_date", UNSET)

        def _parse_first_reading_date_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_reading_date_2 = _parse_first_reading_date_2(
            d.pop("first_reading_date_2", UNSET)
        )

        first_reading_date_2_hansard_url_chi = d.pop(
            "first_reading_date_2_hansard_url_chi", UNSET
        )

        first_reading_date_2_hansard_url_eng = d.pop(
            "first_reading_date_2_hansard_url_eng", UNSET
        )

        first_reading_date_hansard_url_chi = d.pop(
            "first_reading_date_hansard_url_chi", UNSET
        )

        first_reading_date_hansard_url_eng = d.pop(
            "first_reading_date_hansard_url_eng", UNSET
        )

        internal_key = d.pop("internal_key", UNSET)

        legco_brief_file_reference = d.pop("legco_brief_file_reference", UNSET)

        legco_brief_url_chi = d.pop("legco_brief_url_chi", UNSET)

        legco_brief_url_eng = d.pop("legco_brief_url_eng", UNSET)

        ordinace_gazette_content_url_eng = d.pop(
            "ordinace_gazette_content_url_eng", UNSET
        )

        ordinance_content_url_chi = d.pop("ordinance_content_url_chi", UNSET)

        ordinance_content_url_eng = d.pop("ordinance_content_url_eng", UNSET)

        ordinance_gazette_content_url_chi = d.pop(
            "ordinance_gazette_content_url_chi", UNSET
        )

        ordinance_gazette_date = d.pop("ordinance_gazette_date", UNSET)

        ordinance_title_chi = d.pop("ordinance_title_chi", UNSET)

        ordinance_title_eng = d.pop("ordinance_title_eng", UNSET)

        ordinance_year_number_chi = d.pop("ordinance_year_number_chi", UNSET)

        ordinance_year_number_eng = d.pop("ordinance_year_number_eng", UNSET)

        proposed_by_chi = d.pop("proposed_by_chi", UNSET)

        proposed_by_eng = d.pop("proposed_by_eng", UNSET)

        remarks_chi = d.pop("remarks_chi", UNSET)

        remarks_eng = d.pop("remarks_eng", UNSET)

        second_reading_date = d.pop("second_reading_date", UNSET)

        def _parse_second_reading_date_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        second_reading_date_2 = _parse_second_reading_date_2(
            d.pop("second_reading_date_2", UNSET)
        )

        second_reading_date_2_hansard_url_chi = d.pop(
            "second_reading_date_2_hansard_url_chi", UNSET
        )

        second_reading_date_2_hansard_url_eng = d.pop(
            "second_reading_date_2_hansard_url_eng", UNSET
        )

        def _parse_second_reading_date_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        second_reading_date_3 = _parse_second_reading_date_3(
            d.pop("second_reading_date_3", UNSET)
        )

        second_reading_date_3_hansard_url_chi = d.pop(
            "second_reading_date_3_hansard_url_chi", UNSET
        )

        second_reading_date_3_hansard_url_eng = d.pop(
            "second_reading_date_3_hansard_url_eng", UNSET
        )

        def _parse_second_reading_date_4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        second_reading_date_4 = _parse_second_reading_date_4(
            d.pop("second_reading_date_4", UNSET)
        )

        second_reading_date_4_hansard_url_chi = d.pop(
            "second_reading_date_4_hansard_url_chi", UNSET
        )

        second_reading_date_4_hansard_url_eng = d.pop(
            "second_reading_date_4_hansard_url_eng", UNSET
        )

        def _parse_second_reading_date_5(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        second_reading_date_5 = _parse_second_reading_date_5(
            d.pop("second_reading_date_5", UNSET)
        )

        second_reading_date_5_hansard_url_chi = d.pop(
            "second_reading_date_5_hansard_url_chi", UNSET
        )

        second_reading_date_5_hansard_url_eng = d.pop(
            "second_reading_date_5_hansard_url_eng", UNSET
        )

        second_reading_date_hansard_url_chi = d.pop(
            "second_reading_date_hansard_url_chi", UNSET
        )

        second_reading_date_hansard_url_eng = d.pop(
            "second_reading_date_hansard_url_eng", UNSET
        )

        third_reading_date = d.pop("third_reading_date", UNSET)

        third_reading_date_hansard_url_chi = d.pop(
            "third_reading_date_hansard_url_chi", UNSET
        )

        third_reading_date_hansard_url_eng = d.pop(
            "third_reading_date_hansard_url_eng", UNSET
        )

        observed_bill_record = cls(
            additional_information_chi=additional_information_chi,
            additional_information_eng=additional_information_eng,
            bill_content_url_2_chi=bill_content_url_2_chi,
            bill_content_url_2_eng=bill_content_url_2_eng,
            bill_content_url_3_chi=bill_content_url_3_chi,
            bill_content_url_3_eng=bill_content_url_3_eng,
            bill_content_url_chi=bill_content_url_chi,
            bill_content_url_eng=bill_content_url_eng,
            bill_gazette_date=bill_gazette_date,
            bill_gazette_date_2=bill_gazette_date_2,
            bill_gazette_date_3=bill_gazette_date_3,
            bill_title_chi=bill_title_chi,
            bill_title_eng=bill_title_eng,
            bills_committee_formation_date=bills_committee_formation_date,
            bills_committee_report_url_chi=bills_committee_report_url_chi,
            bills_committee_report_url_eng=bills_committee_report_url_eng,
            bills_committee_title_chi=bills_committee_title_chi,
            bills_committee_title_eng=bills_committee_title_eng,
            bills_committee_url_chi=bills_committee_url_chi,
            bills_committee_url_eng=bills_committee_url_eng,
            first_reading_date=first_reading_date,
            first_reading_date_2=first_reading_date_2,
            first_reading_date_2_hansard_url_chi=first_reading_date_2_hansard_url_chi,
            first_reading_date_2_hansard_url_eng=first_reading_date_2_hansard_url_eng,
            first_reading_date_hansard_url_chi=first_reading_date_hansard_url_chi,
            first_reading_date_hansard_url_eng=first_reading_date_hansard_url_eng,
            internal_key=internal_key,
            legco_brief_file_reference=legco_brief_file_reference,
            legco_brief_url_chi=legco_brief_url_chi,
            legco_brief_url_eng=legco_brief_url_eng,
            ordinace_gazette_content_url_eng=ordinace_gazette_content_url_eng,
            ordinance_content_url_chi=ordinance_content_url_chi,
            ordinance_content_url_eng=ordinance_content_url_eng,
            ordinance_gazette_content_url_chi=ordinance_gazette_content_url_chi,
            ordinance_gazette_date=ordinance_gazette_date,
            ordinance_title_chi=ordinance_title_chi,
            ordinance_title_eng=ordinance_title_eng,
            ordinance_year_number_chi=ordinance_year_number_chi,
            ordinance_year_number_eng=ordinance_year_number_eng,
            proposed_by_chi=proposed_by_chi,
            proposed_by_eng=proposed_by_eng,
            remarks_chi=remarks_chi,
            remarks_eng=remarks_eng,
            second_reading_date=second_reading_date,
            second_reading_date_2=second_reading_date_2,
            second_reading_date_2_hansard_url_chi=second_reading_date_2_hansard_url_chi,
            second_reading_date_2_hansard_url_eng=second_reading_date_2_hansard_url_eng,
            second_reading_date_3=second_reading_date_3,
            second_reading_date_3_hansard_url_chi=second_reading_date_3_hansard_url_chi,
            second_reading_date_3_hansard_url_eng=second_reading_date_3_hansard_url_eng,
            second_reading_date_4=second_reading_date_4,
            second_reading_date_4_hansard_url_chi=second_reading_date_4_hansard_url_chi,
            second_reading_date_4_hansard_url_eng=second_reading_date_4_hansard_url_eng,
            second_reading_date_5=second_reading_date_5,
            second_reading_date_5_hansard_url_chi=second_reading_date_5_hansard_url_chi,
            second_reading_date_5_hansard_url_eng=second_reading_date_5_hansard_url_eng,
            second_reading_date_hansard_url_chi=second_reading_date_hansard_url_chi,
            second_reading_date_hansard_url_eng=second_reading_date_hansard_url_eng,
            third_reading_date=third_reading_date,
            third_reading_date_hansard_url_chi=third_reading_date_hansard_url_chi,
            third_reading_date_hansard_url_eng=third_reading_date_hansard_url_eng,
        )

        observed_bill_record.additional_properties = d
        return observed_bill_record

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
