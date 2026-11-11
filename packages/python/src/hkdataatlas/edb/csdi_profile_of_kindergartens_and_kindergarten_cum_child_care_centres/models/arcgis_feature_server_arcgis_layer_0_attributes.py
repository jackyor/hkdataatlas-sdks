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
        school_no (int | None | Unset): Publisher field type: esriFieldTypeInteger
        location_no (None | str | Unset): Publisher field type: esriFieldTypeString
        school_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        school_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        joining_kg_edu_scheme_en (None | str | Unset): Publisher field type: esriFieldTypeString
        joining_kg_edu_scheme_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        received_grant_for_support_to_ncs_students (None | str | Unset): Publisher field type: esriFieldTypeString
        application_date_from (None | str | Unset): Publisher field type: esriFieldTypeString
        application_date_to (None | str | Unset): Publisher field type: esriFieldTypeString
        application_form_type_en (None | str | Unset): Publisher field type: esriFieldTypeString
        application_form_type_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        application_period_type_en (None | str | Unset): Publisher field type: esriFieldTypeString
        application_period_type_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        school_category_en (None | str | Unset): Publisher field type: esriFieldTypeString
        school_category_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        student_category_en (None | str | Unset): Publisher field type: esriFieldTypeString
        student_category_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        tel (None | str | Unset): Publisher field type: esriFieldTypeString
        fax (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_school_supervisor_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_school_supervisor_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        title_of_school_supervisor_en (None | str | Unset): Publisher field type: esriFieldTypeString
        title_of_school_supervisor_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_school_principal_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_school_principal_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        title_of_school_principal_en (None | str | Unset): Publisher field type: esriFieldTypeString
        title_of_school_principal_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_registered_classrooms_tc (int | None | Unset): Publisher field type: esriFieldTypeInteger
        no_of_registered_classrooms_remarks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_registered_classrooms_remarks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        outdoor_playground_en (None | str | Unset): Publisher field type: esriFieldTypeString
        outdoor_playground_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        indoor_playground_en (None | str | Unset): Publisher field type: esriFieldTypeString
        indoor_playground_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        music_room_en (None | str | Unset): Publisher field type: esriFieldTypeString
        music_room_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        other_special_rooms_or_areas_en (None | str | Unset): Publisher field type: esriFieldTypeString
        other_special_rooms_or_areas_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        school_founding_year (int | None | Unset): Publisher field type: esriFieldTypeInteger
        school_founding_year_remarks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        school_founding_year_remarks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        school_website (None | str | Unset): Publisher field type: esriFieldTypeString
        working_hd_30000_or_below (None | str | Unset): Publisher field type: esriFieldTypeString
        working_hd_30001_to_40000 (None | str | Unset): Publisher field type: esriFieldTypeString
        working_hd_40000_above (None | str | Unset): Publisher field type: esriFieldTypeString
        working_hd_remarks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        working_hd_remarks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        working_wd_30000_or_below (None | str | Unset): Publisher field type: esriFieldTypeString
        working_wd_30001_to_40000 (None | str | Unset): Publisher field type: esriFieldTypeString
        working_wd_40000_above (None | str | Unset): Publisher field type: esriFieldTypeString
        working_wd_remarks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        working_wd_remarks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        working_exp_of_principal_and_teaching_staff_below_4_yrs (None | str | Unset): Publisher field type:
            esriFieldTypeString
        principal_and_teaching_staff_working_exp_fm_4_to_7_yrs (None | str | Unset): Publisher field type:
            esriFieldTypeString
        working_exp_of_principal_and_teaching_staff_above_7_yrs (None | str | Unset): Publisher field type:
            esriFieldTypeString
        working_exp_of_principal_and_teaching_staff_remarks_en (None | str | Unset): Publisher field type:
            esriFieldTypeString
        working_exp_of_principal_and_teaching_staff_remarks_tc (None | str | Unset): Publisher field type:
            esriFieldTypeString
        summer_uniform_en (None | str | Unset): Publisher field type: esriFieldTypeString
        summer_uniform_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        winter_uniform_en (None | str | Unset): Publisher field type: esriFieldTypeString
        winter_uniform_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        school_bag_en (None | str | Unset): Publisher field type: esriFieldTypeString
        school_bag_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        tea_and_snacks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        tea_and_snacks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        textbooks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        textbooks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        exercise_books_or_workbooks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        exercise_books_or_workbooks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        stationery_en (None | str | Unset): Publisher field type: esriFieldTypeString
        stationery_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        bedding_items_en (None | str | Unset): Publisher field type: esriFieldTypeString
        bedding_items_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        salary_of_principal_and_teaching_staff (None | str | Unset): Publisher field type: esriFieldTypeString
        non_teaching_staff_salary (None | str | Unset): Publisher field type: esriFieldTypeString
        rent_management_fees_rates_and_government_rent (None | str | Unset): Publisher field type: esriFieldTypeString
        teaching_resources (None | str | Unset): Publisher field type: esriFieldTypeString
        staff_training_and_professional_development (None | str | Unset): Publisher field type: esriFieldTypeString
        other_expenses (None | str | Unset): Publisher field type: esriFieldTypeString
        expenditure_information_remarks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        expenditure_information_remarks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        expenditure_information_based_on_audited_account_en (None | str | Unset): Publisher field type:
            esriFieldTypeString
        expenditure_information_based_on_audited_account_tc (None | str | Unset): Publisher field type:
            esriFieldTypeString
        curriculum_type_en (None | str | Unset): Publisher field type: esriFieldTypeString
        curriculum_type_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        curriculum_planning_en (None | str | Unset): Publisher field type: esriFieldTypeString
        curriculum_planning_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        learning_or_teaching_approach_and_activities_en (None | str | Unset): Publisher field type: esriFieldTypeString
        learning_or_teaching_approach_and_activities_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        assessment_of_children_learning_experiences_en (None | str | Unset): Publisher field type: esriFieldTypeString
        assessment_of_children_learning_experiences_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        school_vision_and_mission_en (None | str | Unset): Publisher field type: esriFieldTypeString
        school_vision_and_mission_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        support_to_students_en (None | str | Unset): Publisher field type: esriFieldTypeString
        support_to_students_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        parent_teacher_association_en (None | str | Unset): Publisher field type: esriFieldTypeString
        parent_teacher_association_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        other_activities_or_communication_with_parents_en (None | str | Unset): Publisher field type:
            esriFieldTypeString
        other_activities_or_communication_with_parents_tc (None | str | Unset): Publisher field type:
            esriFieldTypeString
        support_to_non_chinese_speaking_ncs_students_en (None | str | Unset): Publisher field type: esriFieldTypeString
        support_to_non_chinese_speaking_ncs_students_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        support_to_students_with_special_needs_en (None | str | Unset): Publisher field type: esriFieldTypeString
        support_to_students_with_special_needs_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        nursery_classes_not_writing (None | str | Unset): Publisher field type: esriFieldTypeString
        total_no_of_permitted_accommodation_of_class_rm_in_use (None | str | Unset): Publisher field type:
            esriFieldTypeString
        no_of_students_in_nursery_am (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_students_in_lkg_am (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_students_ukg_am (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_students_in_nursery_pm (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_students_in_lkg_pm (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_students_ukg_pm (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_students_in_nursery_wd (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_students_in_lkg_wd (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_students_in_ukg_wd (None | str | Unset): Publisher field type: esriFieldTypeString
        teacher_to_pupil_ratio_in_morning_session (None | str | Unset): Publisher field type: esriFieldTypeString
        teacher_to_pupil_ratio_in_afternoon_session (None | str | Unset): Publisher field type: esriFieldTypeString
        teacher_to_pupil_ratio_remarks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        teacher_to_pupil_ratio_remarks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_principal_and_teaching_staff_with_degree (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_principal_and_teaching_staff_w_non_degree (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_prin_n_teaching_staff_w_c_ece_or_above (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_principal_and_teaching_staff_w_qkt (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_prin_n_teaching_staff_w_other_t_training (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_principal_and_teaching_staff_w_qakt (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_principal_and_teaching_staff_others (None | str | Unset): Publisher field type: esriFieldTypeString
        total_no_of_principal_and_teaching_staff (None | str | Unset): Publisher field type: esriFieldTypeString
        fees_certificate (None | str | Unset): Publisher field type: esriFieldTypeString
        quality_review_result_and_report_chi_en (None | str | Unset): Publisher field type: esriFieldTypeString
        quality_review_result_and_report_chi_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        quality_review_result_and_report_eng_en (None | str | Unset): Publisher field type: esriFieldTypeString
        quality_review_result_and_report_eng_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        child_care_service_for_aged_under_2_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        child_care_service_for_aged_under_2_en (None | str | Unset): Publisher field type: esriFieldTypeString
        child_care_service_for_aged_2_to_3_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        child_care_service_for_aged_2_to_3_en (None | str | Unset): Publisher field type: esriFieldTypeString
        no_for_enrolment_aged_2_to_3 (None | str | Unset): Publisher field type: esriFieldTypeString
        cc_service_fee_level_annum_hd (None | str | Unset): Publisher field type: esriFieldTypeString
        cc_service_fee_level_annum_wd (None | str | Unset): Publisher field type: esriFieldTypeString
        join_ccc_subsidy_scheme_en (None | str | Unset): Publisher field type: esriFieldTypeString
        join_ccc_subsidy_scheme_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        provide_occasional_cc_service_en (None | str | Unset): Publisher field type: esriFieldTypeString
        provide_occasional_cc_service_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        provide_extended_hour_service_en (None | str | Unset): Publisher field type: esriFieldTypeString
        provide_extended_hour_service_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        other_approved_fees_application_fee_en (None | str | Unset): Publisher field type: esriFieldTypeString
        other_approved_fees_application_fee_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        other_approved_fees_registration_fee_hd (None | str | Unset): Publisher field type: esriFieldTypeString
        no_hd_session_remarks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        no_hd_session_remarks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        other_approved_fees_registration_fee_wd (None | str | Unset): Publisher field type: esriFieldTypeString
        no_wd_session_remarks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        no_wd_session_remarks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        geometry_longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        geometry_latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        fid (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    school_no: int | None | Unset = UNSET
    location_no: None | str | Unset = UNSET
    school_name_en: None | str | Unset = UNSET
    school_name_tc: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    joining_kg_edu_scheme_en: None | str | Unset = UNSET
    joining_kg_edu_scheme_tc: None | str | Unset = UNSET
    received_grant_for_support_to_ncs_students: None | str | Unset = UNSET
    application_date_from: None | str | Unset = UNSET
    application_date_to: None | str | Unset = UNSET
    application_form_type_en: None | str | Unset = UNSET
    application_form_type_tc: None | str | Unset = UNSET
    application_period_type_en: None | str | Unset = UNSET
    application_period_type_tc: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    school_category_en: None | str | Unset = UNSET
    school_category_tc: None | str | Unset = UNSET
    student_category_en: None | str | Unset = UNSET
    student_category_tc: None | str | Unset = UNSET
    tel: None | str | Unset = UNSET
    fax: None | str | Unset = UNSET
    name_of_school_supervisor_en: None | str | Unset = UNSET
    name_of_school_supervisor_tc: None | str | Unset = UNSET
    title_of_school_supervisor_en: None | str | Unset = UNSET
    title_of_school_supervisor_tc: None | str | Unset = UNSET
    name_of_school_principal_en: None | str | Unset = UNSET
    name_of_school_principal_tc: None | str | Unset = UNSET
    title_of_school_principal_en: None | str | Unset = UNSET
    title_of_school_principal_tc: None | str | Unset = UNSET
    no_of_registered_classrooms_tc: int | None | Unset = UNSET
    no_of_registered_classrooms_remarks_en: None | str | Unset = UNSET
    no_of_registered_classrooms_remarks_tc: None | str | Unset = UNSET
    outdoor_playground_en: None | str | Unset = UNSET
    outdoor_playground_tc: None | str | Unset = UNSET
    indoor_playground_en: None | str | Unset = UNSET
    indoor_playground_tc: None | str | Unset = UNSET
    music_room_en: None | str | Unset = UNSET
    music_room_tc: None | str | Unset = UNSET
    other_special_rooms_or_areas_en: None | str | Unset = UNSET
    other_special_rooms_or_areas_tc: None | str | Unset = UNSET
    school_founding_year: int | None | Unset = UNSET
    school_founding_year_remarks_en: None | str | Unset = UNSET
    school_founding_year_remarks_tc: None | str | Unset = UNSET
    school_website: None | str | Unset = UNSET
    working_hd_30000_or_below: None | str | Unset = UNSET
    working_hd_30001_to_40000: None | str | Unset = UNSET
    working_hd_40000_above: None | str | Unset = UNSET
    working_hd_remarks_en: None | str | Unset = UNSET
    working_hd_remarks_tc: None | str | Unset = UNSET
    working_wd_30000_or_below: None | str | Unset = UNSET
    working_wd_30001_to_40000: None | str | Unset = UNSET
    working_wd_40000_above: None | str | Unset = UNSET
    working_wd_remarks_en: None | str | Unset = UNSET
    working_wd_remarks_tc: None | str | Unset = UNSET
    working_exp_of_principal_and_teaching_staff_below_4_yrs: None | str | Unset = UNSET
    principal_and_teaching_staff_working_exp_fm_4_to_7_yrs: None | str | Unset = UNSET
    working_exp_of_principal_and_teaching_staff_above_7_yrs: None | str | Unset = UNSET
    working_exp_of_principal_and_teaching_staff_remarks_en: None | str | Unset = UNSET
    working_exp_of_principal_and_teaching_staff_remarks_tc: None | str | Unset = UNSET
    summer_uniform_en: None | str | Unset = UNSET
    summer_uniform_tc: None | str | Unset = UNSET
    winter_uniform_en: None | str | Unset = UNSET
    winter_uniform_tc: None | str | Unset = UNSET
    school_bag_en: None | str | Unset = UNSET
    school_bag_tc: None | str | Unset = UNSET
    tea_and_snacks_en: None | str | Unset = UNSET
    tea_and_snacks_tc: None | str | Unset = UNSET
    textbooks_en: None | str | Unset = UNSET
    textbooks_tc: None | str | Unset = UNSET
    exercise_books_or_workbooks_en: None | str | Unset = UNSET
    exercise_books_or_workbooks_tc: None | str | Unset = UNSET
    stationery_en: None | str | Unset = UNSET
    stationery_tc: None | str | Unset = UNSET
    bedding_items_en: None | str | Unset = UNSET
    bedding_items_tc: None | str | Unset = UNSET
    salary_of_principal_and_teaching_staff: None | str | Unset = UNSET
    non_teaching_staff_salary: None | str | Unset = UNSET
    rent_management_fees_rates_and_government_rent: None | str | Unset = UNSET
    teaching_resources: None | str | Unset = UNSET
    staff_training_and_professional_development: None | str | Unset = UNSET
    other_expenses: None | str | Unset = UNSET
    expenditure_information_remarks_en: None | str | Unset = UNSET
    expenditure_information_remarks_tc: None | str | Unset = UNSET
    expenditure_information_based_on_audited_account_en: None | str | Unset = UNSET
    expenditure_information_based_on_audited_account_tc: None | str | Unset = UNSET
    curriculum_type_en: None | str | Unset = UNSET
    curriculum_type_tc: None | str | Unset = UNSET
    curriculum_planning_en: None | str | Unset = UNSET
    curriculum_planning_tc: None | str | Unset = UNSET
    learning_or_teaching_approach_and_activities_en: None | str | Unset = UNSET
    learning_or_teaching_approach_and_activities_tc: None | str | Unset = UNSET
    assessment_of_children_learning_experiences_en: None | str | Unset = UNSET
    assessment_of_children_learning_experiences_tc: None | str | Unset = UNSET
    school_vision_and_mission_en: None | str | Unset = UNSET
    school_vision_and_mission_tc: None | str | Unset = UNSET
    support_to_students_en: None | str | Unset = UNSET
    support_to_students_tc: None | str | Unset = UNSET
    parent_teacher_association_en: None | str | Unset = UNSET
    parent_teacher_association_tc: None | str | Unset = UNSET
    other_activities_or_communication_with_parents_en: None | str | Unset = UNSET
    other_activities_or_communication_with_parents_tc: None | str | Unset = UNSET
    support_to_non_chinese_speaking_ncs_students_en: None | str | Unset = UNSET
    support_to_non_chinese_speaking_ncs_students_tc: None | str | Unset = UNSET
    support_to_students_with_special_needs_en: None | str | Unset = UNSET
    support_to_students_with_special_needs_tc: None | str | Unset = UNSET
    nursery_classes_not_writing: None | str | Unset = UNSET
    total_no_of_permitted_accommodation_of_class_rm_in_use: None | str | Unset = UNSET
    no_of_students_in_nursery_am: None | str | Unset = UNSET
    no_of_students_in_lkg_am: None | str | Unset = UNSET
    no_of_students_ukg_am: None | str | Unset = UNSET
    no_of_students_in_nursery_pm: None | str | Unset = UNSET
    no_of_students_in_lkg_pm: None | str | Unset = UNSET
    no_of_students_ukg_pm: None | str | Unset = UNSET
    no_of_students_in_nursery_wd: None | str | Unset = UNSET
    no_of_students_in_lkg_wd: None | str | Unset = UNSET
    no_of_students_in_ukg_wd: None | str | Unset = UNSET
    teacher_to_pupil_ratio_in_morning_session: None | str | Unset = UNSET
    teacher_to_pupil_ratio_in_afternoon_session: None | str | Unset = UNSET
    teacher_to_pupil_ratio_remarks_en: None | str | Unset = UNSET
    teacher_to_pupil_ratio_remarks_tc: None | str | Unset = UNSET
    no_of_principal_and_teaching_staff_with_degree: None | str | Unset = UNSET
    no_of_principal_and_teaching_staff_w_non_degree: None | str | Unset = UNSET
    no_of_prin_n_teaching_staff_w_c_ece_or_above: None | str | Unset = UNSET
    no_of_principal_and_teaching_staff_w_qkt: None | str | Unset = UNSET
    no_of_prin_n_teaching_staff_w_other_t_training: None | str | Unset = UNSET
    no_of_principal_and_teaching_staff_w_qakt: None | str | Unset = UNSET
    no_of_principal_and_teaching_staff_others: None | str | Unset = UNSET
    total_no_of_principal_and_teaching_staff: None | str | Unset = UNSET
    fees_certificate: None | str | Unset = UNSET
    quality_review_result_and_report_chi_en: None | str | Unset = UNSET
    quality_review_result_and_report_chi_tc: None | str | Unset = UNSET
    quality_review_result_and_report_eng_en: None | str | Unset = UNSET
    quality_review_result_and_report_eng_tc: None | str | Unset = UNSET
    child_care_service_for_aged_under_2_tc: None | str | Unset = UNSET
    child_care_service_for_aged_under_2_en: None | str | Unset = UNSET
    child_care_service_for_aged_2_to_3_tc: None | str | Unset = UNSET
    child_care_service_for_aged_2_to_3_en: None | str | Unset = UNSET
    no_for_enrolment_aged_2_to_3: None | str | Unset = UNSET
    cc_service_fee_level_annum_hd: None | str | Unset = UNSET
    cc_service_fee_level_annum_wd: None | str | Unset = UNSET
    join_ccc_subsidy_scheme_en: None | str | Unset = UNSET
    join_ccc_subsidy_scheme_tc: None | str | Unset = UNSET
    provide_occasional_cc_service_en: None | str | Unset = UNSET
    provide_occasional_cc_service_tc: None | str | Unset = UNSET
    provide_extended_hour_service_en: None | str | Unset = UNSET
    provide_extended_hour_service_tc: None | str | Unset = UNSET
    other_approved_fees_application_fee_en: None | str | Unset = UNSET
    other_approved_fees_application_fee_tc: None | str | Unset = UNSET
    other_approved_fees_registration_fee_hd: None | str | Unset = UNSET
    no_hd_session_remarks_en: None | str | Unset = UNSET
    no_hd_session_remarks_tc: None | str | Unset = UNSET
    other_approved_fees_registration_fee_wd: None | str | Unset = UNSET
    no_wd_session_remarks_en: None | str | Unset = UNSET
    no_wd_session_remarks_tc: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    easting: float | None | Unset = UNSET
    geometry_longitude: float | None | Unset = UNSET
    geometry_latitude: float | None | Unset = UNSET
    fid: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        school_no: int | None | Unset
        if isinstance(self.school_no, Unset):
            school_no = UNSET
        else:
            school_no = self.school_no

        location_no: None | str | Unset
        if isinstance(self.location_no, Unset):
            location_no = UNSET
        else:
            location_no = self.location_no

        school_name_en: None | str | Unset
        if isinstance(self.school_name_en, Unset):
            school_name_en = UNSET
        else:
            school_name_en = self.school_name_en

        school_name_tc: None | str | Unset
        if isinstance(self.school_name_tc, Unset):
            school_name_tc = UNSET
        else:
            school_name_tc = self.school_name_tc

        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        joining_kg_edu_scheme_en: None | str | Unset
        if isinstance(self.joining_kg_edu_scheme_en, Unset):
            joining_kg_edu_scheme_en = UNSET
        else:
            joining_kg_edu_scheme_en = self.joining_kg_edu_scheme_en

        joining_kg_edu_scheme_tc: None | str | Unset
        if isinstance(self.joining_kg_edu_scheme_tc, Unset):
            joining_kg_edu_scheme_tc = UNSET
        else:
            joining_kg_edu_scheme_tc = self.joining_kg_edu_scheme_tc

        received_grant_for_support_to_ncs_students: None | str | Unset
        if isinstance(self.received_grant_for_support_to_ncs_students, Unset):
            received_grant_for_support_to_ncs_students = UNSET
        else:
            received_grant_for_support_to_ncs_students = (
                self.received_grant_for_support_to_ncs_students
            )

        application_date_from: None | str | Unset
        if isinstance(self.application_date_from, Unset):
            application_date_from = UNSET
        else:
            application_date_from = self.application_date_from

        application_date_to: None | str | Unset
        if isinstance(self.application_date_to, Unset):
            application_date_to = UNSET
        else:
            application_date_to = self.application_date_to

        application_form_type_en: None | str | Unset
        if isinstance(self.application_form_type_en, Unset):
            application_form_type_en = UNSET
        else:
            application_form_type_en = self.application_form_type_en

        application_form_type_tc: None | str | Unset
        if isinstance(self.application_form_type_tc, Unset):
            application_form_type_tc = UNSET
        else:
            application_form_type_tc = self.application_form_type_tc

        application_period_type_en: None | str | Unset
        if isinstance(self.application_period_type_en, Unset):
            application_period_type_en = UNSET
        else:
            application_period_type_en = self.application_period_type_en

        application_period_type_tc: None | str | Unset
        if isinstance(self.application_period_type_tc, Unset):
            application_period_type_tc = UNSET
        else:
            application_period_type_tc = self.application_period_type_tc

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        school_category_en: None | str | Unset
        if isinstance(self.school_category_en, Unset):
            school_category_en = UNSET
        else:
            school_category_en = self.school_category_en

        school_category_tc: None | str | Unset
        if isinstance(self.school_category_tc, Unset):
            school_category_tc = UNSET
        else:
            school_category_tc = self.school_category_tc

        student_category_en: None | str | Unset
        if isinstance(self.student_category_en, Unset):
            student_category_en = UNSET
        else:
            student_category_en = self.student_category_en

        student_category_tc: None | str | Unset
        if isinstance(self.student_category_tc, Unset):
            student_category_tc = UNSET
        else:
            student_category_tc = self.student_category_tc

        tel: None | str | Unset
        if isinstance(self.tel, Unset):
            tel = UNSET
        else:
            tel = self.tel

        fax: None | str | Unset
        if isinstance(self.fax, Unset):
            fax = UNSET
        else:
            fax = self.fax

        name_of_school_supervisor_en: None | str | Unset
        if isinstance(self.name_of_school_supervisor_en, Unset):
            name_of_school_supervisor_en = UNSET
        else:
            name_of_school_supervisor_en = self.name_of_school_supervisor_en

        name_of_school_supervisor_tc: None | str | Unset
        if isinstance(self.name_of_school_supervisor_tc, Unset):
            name_of_school_supervisor_tc = UNSET
        else:
            name_of_school_supervisor_tc = self.name_of_school_supervisor_tc

        title_of_school_supervisor_en: None | str | Unset
        if isinstance(self.title_of_school_supervisor_en, Unset):
            title_of_school_supervisor_en = UNSET
        else:
            title_of_school_supervisor_en = self.title_of_school_supervisor_en

        title_of_school_supervisor_tc: None | str | Unset
        if isinstance(self.title_of_school_supervisor_tc, Unset):
            title_of_school_supervisor_tc = UNSET
        else:
            title_of_school_supervisor_tc = self.title_of_school_supervisor_tc

        name_of_school_principal_en: None | str | Unset
        if isinstance(self.name_of_school_principal_en, Unset):
            name_of_school_principal_en = UNSET
        else:
            name_of_school_principal_en = self.name_of_school_principal_en

        name_of_school_principal_tc: None | str | Unset
        if isinstance(self.name_of_school_principal_tc, Unset):
            name_of_school_principal_tc = UNSET
        else:
            name_of_school_principal_tc = self.name_of_school_principal_tc

        title_of_school_principal_en: None | str | Unset
        if isinstance(self.title_of_school_principal_en, Unset):
            title_of_school_principal_en = UNSET
        else:
            title_of_school_principal_en = self.title_of_school_principal_en

        title_of_school_principal_tc: None | str | Unset
        if isinstance(self.title_of_school_principal_tc, Unset):
            title_of_school_principal_tc = UNSET
        else:
            title_of_school_principal_tc = self.title_of_school_principal_tc

        no_of_registered_classrooms_tc: int | None | Unset
        if isinstance(self.no_of_registered_classrooms_tc, Unset):
            no_of_registered_classrooms_tc = UNSET
        else:
            no_of_registered_classrooms_tc = self.no_of_registered_classrooms_tc

        no_of_registered_classrooms_remarks_en: None | str | Unset
        if isinstance(self.no_of_registered_classrooms_remarks_en, Unset):
            no_of_registered_classrooms_remarks_en = UNSET
        else:
            no_of_registered_classrooms_remarks_en = (
                self.no_of_registered_classrooms_remarks_en
            )

        no_of_registered_classrooms_remarks_tc: None | str | Unset
        if isinstance(self.no_of_registered_classrooms_remarks_tc, Unset):
            no_of_registered_classrooms_remarks_tc = UNSET
        else:
            no_of_registered_classrooms_remarks_tc = (
                self.no_of_registered_classrooms_remarks_tc
            )

        outdoor_playground_en: None | str | Unset
        if isinstance(self.outdoor_playground_en, Unset):
            outdoor_playground_en = UNSET
        else:
            outdoor_playground_en = self.outdoor_playground_en

        outdoor_playground_tc: None | str | Unset
        if isinstance(self.outdoor_playground_tc, Unset):
            outdoor_playground_tc = UNSET
        else:
            outdoor_playground_tc = self.outdoor_playground_tc

        indoor_playground_en: None | str | Unset
        if isinstance(self.indoor_playground_en, Unset):
            indoor_playground_en = UNSET
        else:
            indoor_playground_en = self.indoor_playground_en

        indoor_playground_tc: None | str | Unset
        if isinstance(self.indoor_playground_tc, Unset):
            indoor_playground_tc = UNSET
        else:
            indoor_playground_tc = self.indoor_playground_tc

        music_room_en: None | str | Unset
        if isinstance(self.music_room_en, Unset):
            music_room_en = UNSET
        else:
            music_room_en = self.music_room_en

        music_room_tc: None | str | Unset
        if isinstance(self.music_room_tc, Unset):
            music_room_tc = UNSET
        else:
            music_room_tc = self.music_room_tc

        other_special_rooms_or_areas_en: None | str | Unset
        if isinstance(self.other_special_rooms_or_areas_en, Unset):
            other_special_rooms_or_areas_en = UNSET
        else:
            other_special_rooms_or_areas_en = self.other_special_rooms_or_areas_en

        other_special_rooms_or_areas_tc: None | str | Unset
        if isinstance(self.other_special_rooms_or_areas_tc, Unset):
            other_special_rooms_or_areas_tc = UNSET
        else:
            other_special_rooms_or_areas_tc = self.other_special_rooms_or_areas_tc

        school_founding_year: int | None | Unset
        if isinstance(self.school_founding_year, Unset):
            school_founding_year = UNSET
        else:
            school_founding_year = self.school_founding_year

        school_founding_year_remarks_en: None | str | Unset
        if isinstance(self.school_founding_year_remarks_en, Unset):
            school_founding_year_remarks_en = UNSET
        else:
            school_founding_year_remarks_en = self.school_founding_year_remarks_en

        school_founding_year_remarks_tc: None | str | Unset
        if isinstance(self.school_founding_year_remarks_tc, Unset):
            school_founding_year_remarks_tc = UNSET
        else:
            school_founding_year_remarks_tc = self.school_founding_year_remarks_tc

        school_website: None | str | Unset
        if isinstance(self.school_website, Unset):
            school_website = UNSET
        else:
            school_website = self.school_website

        working_hd_30000_or_below: None | str | Unset
        if isinstance(self.working_hd_30000_or_below, Unset):
            working_hd_30000_or_below = UNSET
        else:
            working_hd_30000_or_below = self.working_hd_30000_or_below

        working_hd_30001_to_40000: None | str | Unset
        if isinstance(self.working_hd_30001_to_40000, Unset):
            working_hd_30001_to_40000 = UNSET
        else:
            working_hd_30001_to_40000 = self.working_hd_30001_to_40000

        working_hd_40000_above: None | str | Unset
        if isinstance(self.working_hd_40000_above, Unset):
            working_hd_40000_above = UNSET
        else:
            working_hd_40000_above = self.working_hd_40000_above

        working_hd_remarks_en: None | str | Unset
        if isinstance(self.working_hd_remarks_en, Unset):
            working_hd_remarks_en = UNSET
        else:
            working_hd_remarks_en = self.working_hd_remarks_en

        working_hd_remarks_tc: None | str | Unset
        if isinstance(self.working_hd_remarks_tc, Unset):
            working_hd_remarks_tc = UNSET
        else:
            working_hd_remarks_tc = self.working_hd_remarks_tc

        working_wd_30000_or_below: None | str | Unset
        if isinstance(self.working_wd_30000_or_below, Unset):
            working_wd_30000_or_below = UNSET
        else:
            working_wd_30000_or_below = self.working_wd_30000_or_below

        working_wd_30001_to_40000: None | str | Unset
        if isinstance(self.working_wd_30001_to_40000, Unset):
            working_wd_30001_to_40000 = UNSET
        else:
            working_wd_30001_to_40000 = self.working_wd_30001_to_40000

        working_wd_40000_above: None | str | Unset
        if isinstance(self.working_wd_40000_above, Unset):
            working_wd_40000_above = UNSET
        else:
            working_wd_40000_above = self.working_wd_40000_above

        working_wd_remarks_en: None | str | Unset
        if isinstance(self.working_wd_remarks_en, Unset):
            working_wd_remarks_en = UNSET
        else:
            working_wd_remarks_en = self.working_wd_remarks_en

        working_wd_remarks_tc: None | str | Unset
        if isinstance(self.working_wd_remarks_tc, Unset):
            working_wd_remarks_tc = UNSET
        else:
            working_wd_remarks_tc = self.working_wd_remarks_tc

        working_exp_of_principal_and_teaching_staff_below_4_yrs: None | str | Unset
        if isinstance(
            self.working_exp_of_principal_and_teaching_staff_below_4_yrs, Unset
        ):
            working_exp_of_principal_and_teaching_staff_below_4_yrs = UNSET
        else:
            working_exp_of_principal_and_teaching_staff_below_4_yrs = (
                self.working_exp_of_principal_and_teaching_staff_below_4_yrs
            )

        principal_and_teaching_staff_working_exp_fm_4_to_7_yrs: None | str | Unset
        if isinstance(
            self.principal_and_teaching_staff_working_exp_fm_4_to_7_yrs, Unset
        ):
            principal_and_teaching_staff_working_exp_fm_4_to_7_yrs = UNSET
        else:
            principal_and_teaching_staff_working_exp_fm_4_to_7_yrs = (
                self.principal_and_teaching_staff_working_exp_fm_4_to_7_yrs
            )

        working_exp_of_principal_and_teaching_staff_above_7_yrs: None | str | Unset
        if isinstance(
            self.working_exp_of_principal_and_teaching_staff_above_7_yrs, Unset
        ):
            working_exp_of_principal_and_teaching_staff_above_7_yrs = UNSET
        else:
            working_exp_of_principal_and_teaching_staff_above_7_yrs = (
                self.working_exp_of_principal_and_teaching_staff_above_7_yrs
            )

        working_exp_of_principal_and_teaching_staff_remarks_en: None | str | Unset
        if isinstance(
            self.working_exp_of_principal_and_teaching_staff_remarks_en, Unset
        ):
            working_exp_of_principal_and_teaching_staff_remarks_en = UNSET
        else:
            working_exp_of_principal_and_teaching_staff_remarks_en = (
                self.working_exp_of_principal_and_teaching_staff_remarks_en
            )

        working_exp_of_principal_and_teaching_staff_remarks_tc: None | str | Unset
        if isinstance(
            self.working_exp_of_principal_and_teaching_staff_remarks_tc, Unset
        ):
            working_exp_of_principal_and_teaching_staff_remarks_tc = UNSET
        else:
            working_exp_of_principal_and_teaching_staff_remarks_tc = (
                self.working_exp_of_principal_and_teaching_staff_remarks_tc
            )

        summer_uniform_en: None | str | Unset
        if isinstance(self.summer_uniform_en, Unset):
            summer_uniform_en = UNSET
        else:
            summer_uniform_en = self.summer_uniform_en

        summer_uniform_tc: None | str | Unset
        if isinstance(self.summer_uniform_tc, Unset):
            summer_uniform_tc = UNSET
        else:
            summer_uniform_tc = self.summer_uniform_tc

        winter_uniform_en: None | str | Unset
        if isinstance(self.winter_uniform_en, Unset):
            winter_uniform_en = UNSET
        else:
            winter_uniform_en = self.winter_uniform_en

        winter_uniform_tc: None | str | Unset
        if isinstance(self.winter_uniform_tc, Unset):
            winter_uniform_tc = UNSET
        else:
            winter_uniform_tc = self.winter_uniform_tc

        school_bag_en: None | str | Unset
        if isinstance(self.school_bag_en, Unset):
            school_bag_en = UNSET
        else:
            school_bag_en = self.school_bag_en

        school_bag_tc: None | str | Unset
        if isinstance(self.school_bag_tc, Unset):
            school_bag_tc = UNSET
        else:
            school_bag_tc = self.school_bag_tc

        tea_and_snacks_en: None | str | Unset
        if isinstance(self.tea_and_snacks_en, Unset):
            tea_and_snacks_en = UNSET
        else:
            tea_and_snacks_en = self.tea_and_snacks_en

        tea_and_snacks_tc: None | str | Unset
        if isinstance(self.tea_and_snacks_tc, Unset):
            tea_and_snacks_tc = UNSET
        else:
            tea_and_snacks_tc = self.tea_and_snacks_tc

        textbooks_en: None | str | Unset
        if isinstance(self.textbooks_en, Unset):
            textbooks_en = UNSET
        else:
            textbooks_en = self.textbooks_en

        textbooks_tc: None | str | Unset
        if isinstance(self.textbooks_tc, Unset):
            textbooks_tc = UNSET
        else:
            textbooks_tc = self.textbooks_tc

        exercise_books_or_workbooks_en: None | str | Unset
        if isinstance(self.exercise_books_or_workbooks_en, Unset):
            exercise_books_or_workbooks_en = UNSET
        else:
            exercise_books_or_workbooks_en = self.exercise_books_or_workbooks_en

        exercise_books_or_workbooks_tc: None | str | Unset
        if isinstance(self.exercise_books_or_workbooks_tc, Unset):
            exercise_books_or_workbooks_tc = UNSET
        else:
            exercise_books_or_workbooks_tc = self.exercise_books_or_workbooks_tc

        stationery_en: None | str | Unset
        if isinstance(self.stationery_en, Unset):
            stationery_en = UNSET
        else:
            stationery_en = self.stationery_en

        stationery_tc: None | str | Unset
        if isinstance(self.stationery_tc, Unset):
            stationery_tc = UNSET
        else:
            stationery_tc = self.stationery_tc

        bedding_items_en: None | str | Unset
        if isinstance(self.bedding_items_en, Unset):
            bedding_items_en = UNSET
        else:
            bedding_items_en = self.bedding_items_en

        bedding_items_tc: None | str | Unset
        if isinstance(self.bedding_items_tc, Unset):
            bedding_items_tc = UNSET
        else:
            bedding_items_tc = self.bedding_items_tc

        salary_of_principal_and_teaching_staff: None | str | Unset
        if isinstance(self.salary_of_principal_and_teaching_staff, Unset):
            salary_of_principal_and_teaching_staff = UNSET
        else:
            salary_of_principal_and_teaching_staff = (
                self.salary_of_principal_and_teaching_staff
            )

        non_teaching_staff_salary: None | str | Unset
        if isinstance(self.non_teaching_staff_salary, Unset):
            non_teaching_staff_salary = UNSET
        else:
            non_teaching_staff_salary = self.non_teaching_staff_salary

        rent_management_fees_rates_and_government_rent: None | str | Unset
        if isinstance(self.rent_management_fees_rates_and_government_rent, Unset):
            rent_management_fees_rates_and_government_rent = UNSET
        else:
            rent_management_fees_rates_and_government_rent = (
                self.rent_management_fees_rates_and_government_rent
            )

        teaching_resources: None | str | Unset
        if isinstance(self.teaching_resources, Unset):
            teaching_resources = UNSET
        else:
            teaching_resources = self.teaching_resources

        staff_training_and_professional_development: None | str | Unset
        if isinstance(self.staff_training_and_professional_development, Unset):
            staff_training_and_professional_development = UNSET
        else:
            staff_training_and_professional_development = (
                self.staff_training_and_professional_development
            )

        other_expenses: None | str | Unset
        if isinstance(self.other_expenses, Unset):
            other_expenses = UNSET
        else:
            other_expenses = self.other_expenses

        expenditure_information_remarks_en: None | str | Unset
        if isinstance(self.expenditure_information_remarks_en, Unset):
            expenditure_information_remarks_en = UNSET
        else:
            expenditure_information_remarks_en = self.expenditure_information_remarks_en

        expenditure_information_remarks_tc: None | str | Unset
        if isinstance(self.expenditure_information_remarks_tc, Unset):
            expenditure_information_remarks_tc = UNSET
        else:
            expenditure_information_remarks_tc = self.expenditure_information_remarks_tc

        expenditure_information_based_on_audited_account_en: None | str | Unset
        if isinstance(self.expenditure_information_based_on_audited_account_en, Unset):
            expenditure_information_based_on_audited_account_en = UNSET
        else:
            expenditure_information_based_on_audited_account_en = (
                self.expenditure_information_based_on_audited_account_en
            )

        expenditure_information_based_on_audited_account_tc: None | str | Unset
        if isinstance(self.expenditure_information_based_on_audited_account_tc, Unset):
            expenditure_information_based_on_audited_account_tc = UNSET
        else:
            expenditure_information_based_on_audited_account_tc = (
                self.expenditure_information_based_on_audited_account_tc
            )

        curriculum_type_en: None | str | Unset
        if isinstance(self.curriculum_type_en, Unset):
            curriculum_type_en = UNSET
        else:
            curriculum_type_en = self.curriculum_type_en

        curriculum_type_tc: None | str | Unset
        if isinstance(self.curriculum_type_tc, Unset):
            curriculum_type_tc = UNSET
        else:
            curriculum_type_tc = self.curriculum_type_tc

        curriculum_planning_en: None | str | Unset
        if isinstance(self.curriculum_planning_en, Unset):
            curriculum_planning_en = UNSET
        else:
            curriculum_planning_en = self.curriculum_planning_en

        curriculum_planning_tc: None | str | Unset
        if isinstance(self.curriculum_planning_tc, Unset):
            curriculum_planning_tc = UNSET
        else:
            curriculum_planning_tc = self.curriculum_planning_tc

        learning_or_teaching_approach_and_activities_en: None | str | Unset
        if isinstance(self.learning_or_teaching_approach_and_activities_en, Unset):
            learning_or_teaching_approach_and_activities_en = UNSET
        else:
            learning_or_teaching_approach_and_activities_en = (
                self.learning_or_teaching_approach_and_activities_en
            )

        learning_or_teaching_approach_and_activities_tc: None | str | Unset
        if isinstance(self.learning_or_teaching_approach_and_activities_tc, Unset):
            learning_or_teaching_approach_and_activities_tc = UNSET
        else:
            learning_or_teaching_approach_and_activities_tc = (
                self.learning_or_teaching_approach_and_activities_tc
            )

        assessment_of_children_learning_experiences_en: None | str | Unset
        if isinstance(self.assessment_of_children_learning_experiences_en, Unset):
            assessment_of_children_learning_experiences_en = UNSET
        else:
            assessment_of_children_learning_experiences_en = (
                self.assessment_of_children_learning_experiences_en
            )

        assessment_of_children_learning_experiences_tc: None | str | Unset
        if isinstance(self.assessment_of_children_learning_experiences_tc, Unset):
            assessment_of_children_learning_experiences_tc = UNSET
        else:
            assessment_of_children_learning_experiences_tc = (
                self.assessment_of_children_learning_experiences_tc
            )

        school_vision_and_mission_en: None | str | Unset
        if isinstance(self.school_vision_and_mission_en, Unset):
            school_vision_and_mission_en = UNSET
        else:
            school_vision_and_mission_en = self.school_vision_and_mission_en

        school_vision_and_mission_tc: None | str | Unset
        if isinstance(self.school_vision_and_mission_tc, Unset):
            school_vision_and_mission_tc = UNSET
        else:
            school_vision_and_mission_tc = self.school_vision_and_mission_tc

        support_to_students_en: None | str | Unset
        if isinstance(self.support_to_students_en, Unset):
            support_to_students_en = UNSET
        else:
            support_to_students_en = self.support_to_students_en

        support_to_students_tc: None | str | Unset
        if isinstance(self.support_to_students_tc, Unset):
            support_to_students_tc = UNSET
        else:
            support_to_students_tc = self.support_to_students_tc

        parent_teacher_association_en: None | str | Unset
        if isinstance(self.parent_teacher_association_en, Unset):
            parent_teacher_association_en = UNSET
        else:
            parent_teacher_association_en = self.parent_teacher_association_en

        parent_teacher_association_tc: None | str | Unset
        if isinstance(self.parent_teacher_association_tc, Unset):
            parent_teacher_association_tc = UNSET
        else:
            parent_teacher_association_tc = self.parent_teacher_association_tc

        other_activities_or_communication_with_parents_en: None | str | Unset
        if isinstance(self.other_activities_or_communication_with_parents_en, Unset):
            other_activities_or_communication_with_parents_en = UNSET
        else:
            other_activities_or_communication_with_parents_en = (
                self.other_activities_or_communication_with_parents_en
            )

        other_activities_or_communication_with_parents_tc: None | str | Unset
        if isinstance(self.other_activities_or_communication_with_parents_tc, Unset):
            other_activities_or_communication_with_parents_tc = UNSET
        else:
            other_activities_or_communication_with_parents_tc = (
                self.other_activities_or_communication_with_parents_tc
            )

        support_to_non_chinese_speaking_ncs_students_en: None | str | Unset
        if isinstance(self.support_to_non_chinese_speaking_ncs_students_en, Unset):
            support_to_non_chinese_speaking_ncs_students_en = UNSET
        else:
            support_to_non_chinese_speaking_ncs_students_en = (
                self.support_to_non_chinese_speaking_ncs_students_en
            )

        support_to_non_chinese_speaking_ncs_students_tc: None | str | Unset
        if isinstance(self.support_to_non_chinese_speaking_ncs_students_tc, Unset):
            support_to_non_chinese_speaking_ncs_students_tc = UNSET
        else:
            support_to_non_chinese_speaking_ncs_students_tc = (
                self.support_to_non_chinese_speaking_ncs_students_tc
            )

        support_to_students_with_special_needs_en: None | str | Unset
        if isinstance(self.support_to_students_with_special_needs_en, Unset):
            support_to_students_with_special_needs_en = UNSET
        else:
            support_to_students_with_special_needs_en = (
                self.support_to_students_with_special_needs_en
            )

        support_to_students_with_special_needs_tc: None | str | Unset
        if isinstance(self.support_to_students_with_special_needs_tc, Unset):
            support_to_students_with_special_needs_tc = UNSET
        else:
            support_to_students_with_special_needs_tc = (
                self.support_to_students_with_special_needs_tc
            )

        nursery_classes_not_writing: None | str | Unset
        if isinstance(self.nursery_classes_not_writing, Unset):
            nursery_classes_not_writing = UNSET
        else:
            nursery_classes_not_writing = self.nursery_classes_not_writing

        total_no_of_permitted_accommodation_of_class_rm_in_use: None | str | Unset
        if isinstance(
            self.total_no_of_permitted_accommodation_of_class_rm_in_use, Unset
        ):
            total_no_of_permitted_accommodation_of_class_rm_in_use = UNSET
        else:
            total_no_of_permitted_accommodation_of_class_rm_in_use = (
                self.total_no_of_permitted_accommodation_of_class_rm_in_use
            )

        no_of_students_in_nursery_am: None | str | Unset
        if isinstance(self.no_of_students_in_nursery_am, Unset):
            no_of_students_in_nursery_am = UNSET
        else:
            no_of_students_in_nursery_am = self.no_of_students_in_nursery_am

        no_of_students_in_lkg_am: None | str | Unset
        if isinstance(self.no_of_students_in_lkg_am, Unset):
            no_of_students_in_lkg_am = UNSET
        else:
            no_of_students_in_lkg_am = self.no_of_students_in_lkg_am

        no_of_students_ukg_am: None | str | Unset
        if isinstance(self.no_of_students_ukg_am, Unset):
            no_of_students_ukg_am = UNSET
        else:
            no_of_students_ukg_am = self.no_of_students_ukg_am

        no_of_students_in_nursery_pm: None | str | Unset
        if isinstance(self.no_of_students_in_nursery_pm, Unset):
            no_of_students_in_nursery_pm = UNSET
        else:
            no_of_students_in_nursery_pm = self.no_of_students_in_nursery_pm

        no_of_students_in_lkg_pm: None | str | Unset
        if isinstance(self.no_of_students_in_lkg_pm, Unset):
            no_of_students_in_lkg_pm = UNSET
        else:
            no_of_students_in_lkg_pm = self.no_of_students_in_lkg_pm

        no_of_students_ukg_pm: None | str | Unset
        if isinstance(self.no_of_students_ukg_pm, Unset):
            no_of_students_ukg_pm = UNSET
        else:
            no_of_students_ukg_pm = self.no_of_students_ukg_pm

        no_of_students_in_nursery_wd: None | str | Unset
        if isinstance(self.no_of_students_in_nursery_wd, Unset):
            no_of_students_in_nursery_wd = UNSET
        else:
            no_of_students_in_nursery_wd = self.no_of_students_in_nursery_wd

        no_of_students_in_lkg_wd: None | str | Unset
        if isinstance(self.no_of_students_in_lkg_wd, Unset):
            no_of_students_in_lkg_wd = UNSET
        else:
            no_of_students_in_lkg_wd = self.no_of_students_in_lkg_wd

        no_of_students_in_ukg_wd: None | str | Unset
        if isinstance(self.no_of_students_in_ukg_wd, Unset):
            no_of_students_in_ukg_wd = UNSET
        else:
            no_of_students_in_ukg_wd = self.no_of_students_in_ukg_wd

        teacher_to_pupil_ratio_in_morning_session: None | str | Unset
        if isinstance(self.teacher_to_pupil_ratio_in_morning_session, Unset):
            teacher_to_pupil_ratio_in_morning_session = UNSET
        else:
            teacher_to_pupil_ratio_in_morning_session = (
                self.teacher_to_pupil_ratio_in_morning_session
            )

        teacher_to_pupil_ratio_in_afternoon_session: None | str | Unset
        if isinstance(self.teacher_to_pupil_ratio_in_afternoon_session, Unset):
            teacher_to_pupil_ratio_in_afternoon_session = UNSET
        else:
            teacher_to_pupil_ratio_in_afternoon_session = (
                self.teacher_to_pupil_ratio_in_afternoon_session
            )

        teacher_to_pupil_ratio_remarks_en: None | str | Unset
        if isinstance(self.teacher_to_pupil_ratio_remarks_en, Unset):
            teacher_to_pupil_ratio_remarks_en = UNSET
        else:
            teacher_to_pupil_ratio_remarks_en = self.teacher_to_pupil_ratio_remarks_en

        teacher_to_pupil_ratio_remarks_tc: None | str | Unset
        if isinstance(self.teacher_to_pupil_ratio_remarks_tc, Unset):
            teacher_to_pupil_ratio_remarks_tc = UNSET
        else:
            teacher_to_pupil_ratio_remarks_tc = self.teacher_to_pupil_ratio_remarks_tc

        no_of_principal_and_teaching_staff_with_degree: None | str | Unset
        if isinstance(self.no_of_principal_and_teaching_staff_with_degree, Unset):
            no_of_principal_and_teaching_staff_with_degree = UNSET
        else:
            no_of_principal_and_teaching_staff_with_degree = (
                self.no_of_principal_and_teaching_staff_with_degree
            )

        no_of_principal_and_teaching_staff_w_non_degree: None | str | Unset
        if isinstance(self.no_of_principal_and_teaching_staff_w_non_degree, Unset):
            no_of_principal_and_teaching_staff_w_non_degree = UNSET
        else:
            no_of_principal_and_teaching_staff_w_non_degree = (
                self.no_of_principal_and_teaching_staff_w_non_degree
            )

        no_of_prin_n_teaching_staff_w_c_ece_or_above: None | str | Unset
        if isinstance(self.no_of_prin_n_teaching_staff_w_c_ece_or_above, Unset):
            no_of_prin_n_teaching_staff_w_c_ece_or_above = UNSET
        else:
            no_of_prin_n_teaching_staff_w_c_ece_or_above = (
                self.no_of_prin_n_teaching_staff_w_c_ece_or_above
            )

        no_of_principal_and_teaching_staff_w_qkt: None | str | Unset
        if isinstance(self.no_of_principal_and_teaching_staff_w_qkt, Unset):
            no_of_principal_and_teaching_staff_w_qkt = UNSET
        else:
            no_of_principal_and_teaching_staff_w_qkt = (
                self.no_of_principal_and_teaching_staff_w_qkt
            )

        no_of_prin_n_teaching_staff_w_other_t_training: None | str | Unset
        if isinstance(self.no_of_prin_n_teaching_staff_w_other_t_training, Unset):
            no_of_prin_n_teaching_staff_w_other_t_training = UNSET
        else:
            no_of_prin_n_teaching_staff_w_other_t_training = (
                self.no_of_prin_n_teaching_staff_w_other_t_training
            )

        no_of_principal_and_teaching_staff_w_qakt: None | str | Unset
        if isinstance(self.no_of_principal_and_teaching_staff_w_qakt, Unset):
            no_of_principal_and_teaching_staff_w_qakt = UNSET
        else:
            no_of_principal_and_teaching_staff_w_qakt = (
                self.no_of_principal_and_teaching_staff_w_qakt
            )

        no_of_principal_and_teaching_staff_others: None | str | Unset
        if isinstance(self.no_of_principal_and_teaching_staff_others, Unset):
            no_of_principal_and_teaching_staff_others = UNSET
        else:
            no_of_principal_and_teaching_staff_others = (
                self.no_of_principal_and_teaching_staff_others
            )

        total_no_of_principal_and_teaching_staff: None | str | Unset
        if isinstance(self.total_no_of_principal_and_teaching_staff, Unset):
            total_no_of_principal_and_teaching_staff = UNSET
        else:
            total_no_of_principal_and_teaching_staff = (
                self.total_no_of_principal_and_teaching_staff
            )

        fees_certificate: None | str | Unset
        if isinstance(self.fees_certificate, Unset):
            fees_certificate = UNSET
        else:
            fees_certificate = self.fees_certificate

        quality_review_result_and_report_chi_en: None | str | Unset
        if isinstance(self.quality_review_result_and_report_chi_en, Unset):
            quality_review_result_and_report_chi_en = UNSET
        else:
            quality_review_result_and_report_chi_en = (
                self.quality_review_result_and_report_chi_en
            )

        quality_review_result_and_report_chi_tc: None | str | Unset
        if isinstance(self.quality_review_result_and_report_chi_tc, Unset):
            quality_review_result_and_report_chi_tc = UNSET
        else:
            quality_review_result_and_report_chi_tc = (
                self.quality_review_result_and_report_chi_tc
            )

        quality_review_result_and_report_eng_en: None | str | Unset
        if isinstance(self.quality_review_result_and_report_eng_en, Unset):
            quality_review_result_and_report_eng_en = UNSET
        else:
            quality_review_result_and_report_eng_en = (
                self.quality_review_result_and_report_eng_en
            )

        quality_review_result_and_report_eng_tc: None | str | Unset
        if isinstance(self.quality_review_result_and_report_eng_tc, Unset):
            quality_review_result_and_report_eng_tc = UNSET
        else:
            quality_review_result_and_report_eng_tc = (
                self.quality_review_result_and_report_eng_tc
            )

        child_care_service_for_aged_under_2_tc: None | str | Unset
        if isinstance(self.child_care_service_for_aged_under_2_tc, Unset):
            child_care_service_for_aged_under_2_tc = UNSET
        else:
            child_care_service_for_aged_under_2_tc = (
                self.child_care_service_for_aged_under_2_tc
            )

        child_care_service_for_aged_under_2_en: None | str | Unset
        if isinstance(self.child_care_service_for_aged_under_2_en, Unset):
            child_care_service_for_aged_under_2_en = UNSET
        else:
            child_care_service_for_aged_under_2_en = (
                self.child_care_service_for_aged_under_2_en
            )

        child_care_service_for_aged_2_to_3_tc: None | str | Unset
        if isinstance(self.child_care_service_for_aged_2_to_3_tc, Unset):
            child_care_service_for_aged_2_to_3_tc = UNSET
        else:
            child_care_service_for_aged_2_to_3_tc = (
                self.child_care_service_for_aged_2_to_3_tc
            )

        child_care_service_for_aged_2_to_3_en: None | str | Unset
        if isinstance(self.child_care_service_for_aged_2_to_3_en, Unset):
            child_care_service_for_aged_2_to_3_en = UNSET
        else:
            child_care_service_for_aged_2_to_3_en = (
                self.child_care_service_for_aged_2_to_3_en
            )

        no_for_enrolment_aged_2_to_3: None | str | Unset
        if isinstance(self.no_for_enrolment_aged_2_to_3, Unset):
            no_for_enrolment_aged_2_to_3 = UNSET
        else:
            no_for_enrolment_aged_2_to_3 = self.no_for_enrolment_aged_2_to_3

        cc_service_fee_level_annum_hd: None | str | Unset
        if isinstance(self.cc_service_fee_level_annum_hd, Unset):
            cc_service_fee_level_annum_hd = UNSET
        else:
            cc_service_fee_level_annum_hd = self.cc_service_fee_level_annum_hd

        cc_service_fee_level_annum_wd: None | str | Unset
        if isinstance(self.cc_service_fee_level_annum_wd, Unset):
            cc_service_fee_level_annum_wd = UNSET
        else:
            cc_service_fee_level_annum_wd = self.cc_service_fee_level_annum_wd

        join_ccc_subsidy_scheme_en: None | str | Unset
        if isinstance(self.join_ccc_subsidy_scheme_en, Unset):
            join_ccc_subsidy_scheme_en = UNSET
        else:
            join_ccc_subsidy_scheme_en = self.join_ccc_subsidy_scheme_en

        join_ccc_subsidy_scheme_tc: None | str | Unset
        if isinstance(self.join_ccc_subsidy_scheme_tc, Unset):
            join_ccc_subsidy_scheme_tc = UNSET
        else:
            join_ccc_subsidy_scheme_tc = self.join_ccc_subsidy_scheme_tc

        provide_occasional_cc_service_en: None | str | Unset
        if isinstance(self.provide_occasional_cc_service_en, Unset):
            provide_occasional_cc_service_en = UNSET
        else:
            provide_occasional_cc_service_en = self.provide_occasional_cc_service_en

        provide_occasional_cc_service_tc: None | str | Unset
        if isinstance(self.provide_occasional_cc_service_tc, Unset):
            provide_occasional_cc_service_tc = UNSET
        else:
            provide_occasional_cc_service_tc = self.provide_occasional_cc_service_tc

        provide_extended_hour_service_en: None | str | Unset
        if isinstance(self.provide_extended_hour_service_en, Unset):
            provide_extended_hour_service_en = UNSET
        else:
            provide_extended_hour_service_en = self.provide_extended_hour_service_en

        provide_extended_hour_service_tc: None | str | Unset
        if isinstance(self.provide_extended_hour_service_tc, Unset):
            provide_extended_hour_service_tc = UNSET
        else:
            provide_extended_hour_service_tc = self.provide_extended_hour_service_tc

        other_approved_fees_application_fee_en: None | str | Unset
        if isinstance(self.other_approved_fees_application_fee_en, Unset):
            other_approved_fees_application_fee_en = UNSET
        else:
            other_approved_fees_application_fee_en = (
                self.other_approved_fees_application_fee_en
            )

        other_approved_fees_application_fee_tc: None | str | Unset
        if isinstance(self.other_approved_fees_application_fee_tc, Unset):
            other_approved_fees_application_fee_tc = UNSET
        else:
            other_approved_fees_application_fee_tc = (
                self.other_approved_fees_application_fee_tc
            )

        other_approved_fees_registration_fee_hd: None | str | Unset
        if isinstance(self.other_approved_fees_registration_fee_hd, Unset):
            other_approved_fees_registration_fee_hd = UNSET
        else:
            other_approved_fees_registration_fee_hd = (
                self.other_approved_fees_registration_fee_hd
            )

        no_hd_session_remarks_en: None | str | Unset
        if isinstance(self.no_hd_session_remarks_en, Unset):
            no_hd_session_remarks_en = UNSET
        else:
            no_hd_session_remarks_en = self.no_hd_session_remarks_en

        no_hd_session_remarks_tc: None | str | Unset
        if isinstance(self.no_hd_session_remarks_tc, Unset):
            no_hd_session_remarks_tc = UNSET
        else:
            no_hd_session_remarks_tc = self.no_hd_session_remarks_tc

        other_approved_fees_registration_fee_wd: None | str | Unset
        if isinstance(self.other_approved_fees_registration_fee_wd, Unset):
            other_approved_fees_registration_fee_wd = UNSET
        else:
            other_approved_fees_registration_fee_wd = (
                self.other_approved_fees_registration_fee_wd
            )

        no_wd_session_remarks_en: None | str | Unset
        if isinstance(self.no_wd_session_remarks_en, Unset):
            no_wd_session_remarks_en = UNSET
        else:
            no_wd_session_remarks_en = self.no_wd_session_remarks_en

        no_wd_session_remarks_tc: None | str | Unset
        if isinstance(self.no_wd_session_remarks_tc, Unset):
            no_wd_session_remarks_tc = UNSET
        else:
            no_wd_session_remarks_tc = self.no_wd_session_remarks_tc

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

        geometry_longitude: float | None | Unset
        if isinstance(self.geometry_longitude, Unset):
            geometry_longitude = UNSET
        else:
            geometry_longitude = self.geometry_longitude

        geometry_latitude: float | None | Unset
        if isinstance(self.geometry_latitude, Unset):
            geometry_latitude = UNSET
        else:
            geometry_latitude = self.geometry_latitude

        fid: None | str | Unset
        if isinstance(self.fid, Unset):
            fid = UNSET
        else:
            fid = self.fid

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if school_no is not UNSET:
            field_dict["school_no"] = school_no
        if location_no is not UNSET:
            field_dict["location_no"] = location_no
        if school_name_en is not UNSET:
            field_dict["school_name_en"] = school_name_en
        if school_name_tc is not UNSET:
            field_dict["school_name_tc"] = school_name_tc
        if district_en is not UNSET:
            field_dict["district_en"] = district_en
        if district_tc is not UNSET:
            field_dict["district_tc"] = district_tc
        if joining_kg_edu_scheme_en is not UNSET:
            field_dict["joining_kg_edu_scheme_en"] = joining_kg_edu_scheme_en
        if joining_kg_edu_scheme_tc is not UNSET:
            field_dict["joining_kg_edu_scheme_tc"] = joining_kg_edu_scheme_tc
        if received_grant_for_support_to_ncs_students is not UNSET:
            field_dict["received_grant_for_support_to_ncs_students"] = (
                received_grant_for_support_to_ncs_students
            )
        if application_date_from is not UNSET:
            field_dict["application_date_from"] = application_date_from
        if application_date_to is not UNSET:
            field_dict["application_date_to"] = application_date_to
        if application_form_type_en is not UNSET:
            field_dict["application_form_type_en"] = application_form_type_en
        if application_form_type_tc is not UNSET:
            field_dict["application_form_type_tc"] = application_form_type_tc
        if application_period_type_en is not UNSET:
            field_dict["application_period_type_en"] = application_period_type_en
        if application_period_type_tc is not UNSET:
            field_dict["application_period_type_tc"] = application_period_type_tc
        if address_en is not UNSET:
            field_dict["address_en"] = address_en
        if address_tc is not UNSET:
            field_dict["address_tc"] = address_tc
        if school_category_en is not UNSET:
            field_dict["school_category_en"] = school_category_en
        if school_category_tc is not UNSET:
            field_dict["school_category_tc"] = school_category_tc
        if student_category_en is not UNSET:
            field_dict["student_category_en"] = student_category_en
        if student_category_tc is not UNSET:
            field_dict["student_category_tc"] = student_category_tc
        if tel is not UNSET:
            field_dict["tel"] = tel
        if fax is not UNSET:
            field_dict["fax"] = fax
        if name_of_school_supervisor_en is not UNSET:
            field_dict["name_of_school_supervisor_en"] = name_of_school_supervisor_en
        if name_of_school_supervisor_tc is not UNSET:
            field_dict["name_of_school_supervisor_tc"] = name_of_school_supervisor_tc
        if title_of_school_supervisor_en is not UNSET:
            field_dict["title_of_school_supervisor_en"] = title_of_school_supervisor_en
        if title_of_school_supervisor_tc is not UNSET:
            field_dict["title_of_school_supervisor_tc"] = title_of_school_supervisor_tc
        if name_of_school_principal_en is not UNSET:
            field_dict["name_of_school_principal_en"] = name_of_school_principal_en
        if name_of_school_principal_tc is not UNSET:
            field_dict["name_of_school_principal_tc"] = name_of_school_principal_tc
        if title_of_school_principal_en is not UNSET:
            field_dict["title_of_school_principal_en"] = title_of_school_principal_en
        if title_of_school_principal_tc is not UNSET:
            field_dict["title_of_school_principal_tc"] = title_of_school_principal_tc
        if no_of_registered_classrooms_tc is not UNSET:
            field_dict["no_of_registered_classrooms_tc"] = (
                no_of_registered_classrooms_tc
            )
        if no_of_registered_classrooms_remarks_en is not UNSET:
            field_dict["no_of_registered_classrooms_remarks_en"] = (
                no_of_registered_classrooms_remarks_en
            )
        if no_of_registered_classrooms_remarks_tc is not UNSET:
            field_dict["no_of_registered_classrooms_remarks_tc"] = (
                no_of_registered_classrooms_remarks_tc
            )
        if outdoor_playground_en is not UNSET:
            field_dict["outdoor_playground_en"] = outdoor_playground_en
        if outdoor_playground_tc is not UNSET:
            field_dict["outdoor_playground_tc"] = outdoor_playground_tc
        if indoor_playground_en is not UNSET:
            field_dict["indoor_playground_en"] = indoor_playground_en
        if indoor_playground_tc is not UNSET:
            field_dict["indoor_playground_tc"] = indoor_playground_tc
        if music_room_en is not UNSET:
            field_dict["music_room_en"] = music_room_en
        if music_room_tc is not UNSET:
            field_dict["music_room_tc"] = music_room_tc
        if other_special_rooms_or_areas_en is not UNSET:
            field_dict["other_special_rooms_or_areas_en"] = (
                other_special_rooms_or_areas_en
            )
        if other_special_rooms_or_areas_tc is not UNSET:
            field_dict["other_special_rooms_or_areas_tc"] = (
                other_special_rooms_or_areas_tc
            )
        if school_founding_year is not UNSET:
            field_dict["school_founding_year"] = school_founding_year
        if school_founding_year_remarks_en is not UNSET:
            field_dict["school_founding_year_remarks_en"] = (
                school_founding_year_remarks_en
            )
        if school_founding_year_remarks_tc is not UNSET:
            field_dict["school_founding_year_remarks_tc"] = (
                school_founding_year_remarks_tc
            )
        if school_website is not UNSET:
            field_dict["school_website"] = school_website
        if working_hd_30000_or_below is not UNSET:
            field_dict["working_hd_30000_or_below"] = working_hd_30000_or_below
        if working_hd_30001_to_40000 is not UNSET:
            field_dict["working_hd_30001_to_40000"] = working_hd_30001_to_40000
        if working_hd_40000_above is not UNSET:
            field_dict["working_hd_40000_above"] = working_hd_40000_above
        if working_hd_remarks_en is not UNSET:
            field_dict["working_hd_remarks_en"] = working_hd_remarks_en
        if working_hd_remarks_tc is not UNSET:
            field_dict["working_hd_remarks_tc"] = working_hd_remarks_tc
        if working_wd_30000_or_below is not UNSET:
            field_dict["working_wd_30000_or_below"] = working_wd_30000_or_below
        if working_wd_30001_to_40000 is not UNSET:
            field_dict["working_wd_30001_to_40000"] = working_wd_30001_to_40000
        if working_wd_40000_above is not UNSET:
            field_dict["working_wd_40000_above"] = working_wd_40000_above
        if working_wd_remarks_en is not UNSET:
            field_dict["working_wd_remarks_en"] = working_wd_remarks_en
        if working_wd_remarks_tc is not UNSET:
            field_dict["working_wd_remarks_tc"] = working_wd_remarks_tc
        if working_exp_of_principal_and_teaching_staff_below_4_yrs is not UNSET:
            field_dict["working_exp_of_principal_and_teaching_staff_below_4_yrs"] = (
                working_exp_of_principal_and_teaching_staff_below_4_yrs
            )
        if principal_and_teaching_staff_working_exp_fm_4_to_7_yrs is not UNSET:
            field_dict["principal_and_teaching_staff_working_exp_fm_4_to_7_yrs"] = (
                principal_and_teaching_staff_working_exp_fm_4_to_7_yrs
            )
        if working_exp_of_principal_and_teaching_staff_above_7_yrs is not UNSET:
            field_dict["working_exp_of_principal_and_teaching_staff_above_7_yrs"] = (
                working_exp_of_principal_and_teaching_staff_above_7_yrs
            )
        if working_exp_of_principal_and_teaching_staff_remarks_en is not UNSET:
            field_dict["working_exp_of_principal_and_teaching_staff_remarks_en"] = (
                working_exp_of_principal_and_teaching_staff_remarks_en
            )
        if working_exp_of_principal_and_teaching_staff_remarks_tc is not UNSET:
            field_dict["working_exp_of_principal_and_teaching_staff_remarks_tc"] = (
                working_exp_of_principal_and_teaching_staff_remarks_tc
            )
        if summer_uniform_en is not UNSET:
            field_dict["summer_uniform_en"] = summer_uniform_en
        if summer_uniform_tc is not UNSET:
            field_dict["summer_uniform_tc"] = summer_uniform_tc
        if winter_uniform_en is not UNSET:
            field_dict["winter_uniform_en"] = winter_uniform_en
        if winter_uniform_tc is not UNSET:
            field_dict["winter_uniform_tc"] = winter_uniform_tc
        if school_bag_en is not UNSET:
            field_dict["school_bag_en"] = school_bag_en
        if school_bag_tc is not UNSET:
            field_dict["school_bag_tc"] = school_bag_tc
        if tea_and_snacks_en is not UNSET:
            field_dict["tea_and_snacks_en"] = tea_and_snacks_en
        if tea_and_snacks_tc is not UNSET:
            field_dict["tea_and_snacks_tc"] = tea_and_snacks_tc
        if textbooks_en is not UNSET:
            field_dict["textbooks_en"] = textbooks_en
        if textbooks_tc is not UNSET:
            field_dict["textbooks_tc"] = textbooks_tc
        if exercise_books_or_workbooks_en is not UNSET:
            field_dict["exercise_books_or_workbooks_en"] = (
                exercise_books_or_workbooks_en
            )
        if exercise_books_or_workbooks_tc is not UNSET:
            field_dict["exercise_books_or_workbooks_tc"] = (
                exercise_books_or_workbooks_tc
            )
        if stationery_en is not UNSET:
            field_dict["stationery_en"] = stationery_en
        if stationery_tc is not UNSET:
            field_dict["stationery_tc"] = stationery_tc
        if bedding_items_en is not UNSET:
            field_dict["bedding_items_en"] = bedding_items_en
        if bedding_items_tc is not UNSET:
            field_dict["bedding_items_tc"] = bedding_items_tc
        if salary_of_principal_and_teaching_staff is not UNSET:
            field_dict["salary_of_principal_and_teaching_staff"] = (
                salary_of_principal_and_teaching_staff
            )
        if non_teaching_staff_salary is not UNSET:
            field_dict["non_teaching_staff_salary"] = non_teaching_staff_salary
        if rent_management_fees_rates_and_government_rent is not UNSET:
            field_dict["rent_management_fees_rates_and_government_rent"] = (
                rent_management_fees_rates_and_government_rent
            )
        if teaching_resources is not UNSET:
            field_dict["teaching_resources"] = teaching_resources
        if staff_training_and_professional_development is not UNSET:
            field_dict["staff_training_and_professional_development"] = (
                staff_training_and_professional_development
            )
        if other_expenses is not UNSET:
            field_dict["other_expenses"] = other_expenses
        if expenditure_information_remarks_en is not UNSET:
            field_dict["expenditure_information_remarks_en"] = (
                expenditure_information_remarks_en
            )
        if expenditure_information_remarks_tc is not UNSET:
            field_dict["expenditure_information_remarks_tc"] = (
                expenditure_information_remarks_tc
            )
        if expenditure_information_based_on_audited_account_en is not UNSET:
            field_dict["expenditure_information_based_on_audited_account_en"] = (
                expenditure_information_based_on_audited_account_en
            )
        if expenditure_information_based_on_audited_account_tc is not UNSET:
            field_dict["expenditure_information_based_on_audited_account_tc"] = (
                expenditure_information_based_on_audited_account_tc
            )
        if curriculum_type_en is not UNSET:
            field_dict["curriculum_type_en"] = curriculum_type_en
        if curriculum_type_tc is not UNSET:
            field_dict["curriculum_type_tc"] = curriculum_type_tc
        if curriculum_planning_en is not UNSET:
            field_dict["curriculum_planning_en"] = curriculum_planning_en
        if curriculum_planning_tc is not UNSET:
            field_dict["curriculum_planning_tc"] = curriculum_planning_tc
        if learning_or_teaching_approach_and_activities_en is not UNSET:
            field_dict["learning_or_teaching_approach_and_activities_en"] = (
                learning_or_teaching_approach_and_activities_en
            )
        if learning_or_teaching_approach_and_activities_tc is not UNSET:
            field_dict["learning_or_teaching_approach_and_activities_tc"] = (
                learning_or_teaching_approach_and_activities_tc
            )
        if assessment_of_children_learning_experiences_en is not UNSET:
            field_dict["assessment_of_children_learning_experiences_en"] = (
                assessment_of_children_learning_experiences_en
            )
        if assessment_of_children_learning_experiences_tc is not UNSET:
            field_dict["assessment_of_children_learning_experiences_tc"] = (
                assessment_of_children_learning_experiences_tc
            )
        if school_vision_and_mission_en is not UNSET:
            field_dict["school_vision_and_mission_en"] = school_vision_and_mission_en
        if school_vision_and_mission_tc is not UNSET:
            field_dict["school_vision_and_mission_tc"] = school_vision_and_mission_tc
        if support_to_students_en is not UNSET:
            field_dict["support_to_students_en"] = support_to_students_en
        if support_to_students_tc is not UNSET:
            field_dict["support_to_students_tc"] = support_to_students_tc
        if parent_teacher_association_en is not UNSET:
            field_dict["parent_teacher_association_en"] = parent_teacher_association_en
        if parent_teacher_association_tc is not UNSET:
            field_dict["parent_teacher_association_tc"] = parent_teacher_association_tc
        if other_activities_or_communication_with_parents_en is not UNSET:
            field_dict["other_activities_or_communication_with_parents_en"] = (
                other_activities_or_communication_with_parents_en
            )
        if other_activities_or_communication_with_parents_tc is not UNSET:
            field_dict["other_activities_or_communication_with_parents_tc"] = (
                other_activities_or_communication_with_parents_tc
            )
        if support_to_non_chinese_speaking_ncs_students_en is not UNSET:
            field_dict["support_to_non_chinese_speaking_ncs_students_en"] = (
                support_to_non_chinese_speaking_ncs_students_en
            )
        if support_to_non_chinese_speaking_ncs_students_tc is not UNSET:
            field_dict["support_to_non_chinese_speaking_ncs_students_tc"] = (
                support_to_non_chinese_speaking_ncs_students_tc
            )
        if support_to_students_with_special_needs_en is not UNSET:
            field_dict["support_to_students_with_special_needs_en"] = (
                support_to_students_with_special_needs_en
            )
        if support_to_students_with_special_needs_tc is not UNSET:
            field_dict["support_to_students_with_special_needs_tc"] = (
                support_to_students_with_special_needs_tc
            )
        if nursery_classes_not_writing is not UNSET:
            field_dict["nursery_classes_not_writing"] = nursery_classes_not_writing
        if total_no_of_permitted_accommodation_of_class_rm_in_use is not UNSET:
            field_dict["total_no_of_permitted_accommodation_of_class_rm_in_use"] = (
                total_no_of_permitted_accommodation_of_class_rm_in_use
            )
        if no_of_students_in_nursery_am is not UNSET:
            field_dict["no_of_students_in_nursery_am"] = no_of_students_in_nursery_am
        if no_of_students_in_lkg_am is not UNSET:
            field_dict["no_of_students_in_lkg_am"] = no_of_students_in_lkg_am
        if no_of_students_ukg_am is not UNSET:
            field_dict["no_of_students_ukg_am"] = no_of_students_ukg_am
        if no_of_students_in_nursery_pm is not UNSET:
            field_dict["no_of_students_in_nursery_pm"] = no_of_students_in_nursery_pm
        if no_of_students_in_lkg_pm is not UNSET:
            field_dict["no_of_students_in_lkg_pm"] = no_of_students_in_lkg_pm
        if no_of_students_ukg_pm is not UNSET:
            field_dict["no_of_students_ukg_pm"] = no_of_students_ukg_pm
        if no_of_students_in_nursery_wd is not UNSET:
            field_dict["no_of_students_in_nursery_wd"] = no_of_students_in_nursery_wd
        if no_of_students_in_lkg_wd is not UNSET:
            field_dict["no_of_students_in_lkg_wd"] = no_of_students_in_lkg_wd
        if no_of_students_in_ukg_wd is not UNSET:
            field_dict["no_of_students_in_ukg_wd"] = no_of_students_in_ukg_wd
        if teacher_to_pupil_ratio_in_morning_session is not UNSET:
            field_dict["teacher_to_pupil_ratio_in_morning_session"] = (
                teacher_to_pupil_ratio_in_morning_session
            )
        if teacher_to_pupil_ratio_in_afternoon_session is not UNSET:
            field_dict["teacher_to_pupil_ratio_in_afternoon_session"] = (
                teacher_to_pupil_ratio_in_afternoon_session
            )
        if teacher_to_pupil_ratio_remarks_en is not UNSET:
            field_dict["teacher_to_pupil_ratio_remarks_en"] = (
                teacher_to_pupil_ratio_remarks_en
            )
        if teacher_to_pupil_ratio_remarks_tc is not UNSET:
            field_dict["teacher_to_pupil_ratio_remarks_tc"] = (
                teacher_to_pupil_ratio_remarks_tc
            )
        if no_of_principal_and_teaching_staff_with_degree is not UNSET:
            field_dict["no_of_principal_and_teaching_staff_with_degree"] = (
                no_of_principal_and_teaching_staff_with_degree
            )
        if no_of_principal_and_teaching_staff_w_non_degree is not UNSET:
            field_dict["no_of_principal_and_teaching_staff_w_non_degree"] = (
                no_of_principal_and_teaching_staff_w_non_degree
            )
        if no_of_prin_n_teaching_staff_w_c_ece_or_above is not UNSET:
            field_dict["no_of_prin_n_teaching_staff_w_c_ece_or_above"] = (
                no_of_prin_n_teaching_staff_w_c_ece_or_above
            )
        if no_of_principal_and_teaching_staff_w_qkt is not UNSET:
            field_dict["no_of_principal_and_teaching_staff_w_qkt"] = (
                no_of_principal_and_teaching_staff_w_qkt
            )
        if no_of_prin_n_teaching_staff_w_other_t_training is not UNSET:
            field_dict["no_of_prin_n_teaching_staff_w_other_t_training"] = (
                no_of_prin_n_teaching_staff_w_other_t_training
            )
        if no_of_principal_and_teaching_staff_w_qakt is not UNSET:
            field_dict["no_of_principal_and_teaching_staff_w_qakt"] = (
                no_of_principal_and_teaching_staff_w_qakt
            )
        if no_of_principal_and_teaching_staff_others is not UNSET:
            field_dict["no_of_principal_and_teaching_staff_others"] = (
                no_of_principal_and_teaching_staff_others
            )
        if total_no_of_principal_and_teaching_staff is not UNSET:
            field_dict["total_no_of_principal_and_teaching_staff"] = (
                total_no_of_principal_and_teaching_staff
            )
        if fees_certificate is not UNSET:
            field_dict["fees_certificate"] = fees_certificate
        if quality_review_result_and_report_chi_en is not UNSET:
            field_dict["quality_review_result_and_report_chi_en"] = (
                quality_review_result_and_report_chi_en
            )
        if quality_review_result_and_report_chi_tc is not UNSET:
            field_dict["quality_review_result_and_report_chi_tc"] = (
                quality_review_result_and_report_chi_tc
            )
        if quality_review_result_and_report_eng_en is not UNSET:
            field_dict["quality_review_result_and_report_eng_en"] = (
                quality_review_result_and_report_eng_en
            )
        if quality_review_result_and_report_eng_tc is not UNSET:
            field_dict["quality_review_result_and_report_eng_tc"] = (
                quality_review_result_and_report_eng_tc
            )
        if child_care_service_for_aged_under_2_tc is not UNSET:
            field_dict["child_care_service_for_aged_under_2_tc"] = (
                child_care_service_for_aged_under_2_tc
            )
        if child_care_service_for_aged_under_2_en is not UNSET:
            field_dict["child_care_service_for_aged_under_2_en"] = (
                child_care_service_for_aged_under_2_en
            )
        if child_care_service_for_aged_2_to_3_tc is not UNSET:
            field_dict["child_care_service_for_aged_2_to_3_tc"] = (
                child_care_service_for_aged_2_to_3_tc
            )
        if child_care_service_for_aged_2_to_3_en is not UNSET:
            field_dict["child_care_service_for_aged_2_to_3_en"] = (
                child_care_service_for_aged_2_to_3_en
            )
        if no_for_enrolment_aged_2_to_3 is not UNSET:
            field_dict["no_for_enrolment_aged_2_to_3"] = no_for_enrolment_aged_2_to_3
        if cc_service_fee_level_annum_hd is not UNSET:
            field_dict["cc_service_fee_level_annum_hd"] = cc_service_fee_level_annum_hd
        if cc_service_fee_level_annum_wd is not UNSET:
            field_dict["cc_service_fee_level_annum_wd"] = cc_service_fee_level_annum_wd
        if join_ccc_subsidy_scheme_en is not UNSET:
            field_dict["join_ccc_subsidy_scheme_en"] = join_ccc_subsidy_scheme_en
        if join_ccc_subsidy_scheme_tc is not UNSET:
            field_dict["join_ccc_subsidy_scheme_tc"] = join_ccc_subsidy_scheme_tc
        if provide_occasional_cc_service_en is not UNSET:
            field_dict["provide_occasional_cc_service_en"] = (
                provide_occasional_cc_service_en
            )
        if provide_occasional_cc_service_tc is not UNSET:
            field_dict["provide_occasional_cc_service_tc"] = (
                provide_occasional_cc_service_tc
            )
        if provide_extended_hour_service_en is not UNSET:
            field_dict["provide_extended_hour_service_en"] = (
                provide_extended_hour_service_en
            )
        if provide_extended_hour_service_tc is not UNSET:
            field_dict["provide_extended_hour_service_tc"] = (
                provide_extended_hour_service_tc
            )
        if other_approved_fees_application_fee_en is not UNSET:
            field_dict["other_approved_fees_application_fee_en"] = (
                other_approved_fees_application_fee_en
            )
        if other_approved_fees_application_fee_tc is not UNSET:
            field_dict["other_approved_fees_application_fee_tc"] = (
                other_approved_fees_application_fee_tc
            )
        if other_approved_fees_registration_fee_hd is not UNSET:
            field_dict["other_approved_fees_registration_fee_hd"] = (
                other_approved_fees_registration_fee_hd
            )
        if no_hd_session_remarks_en is not UNSET:
            field_dict["no_hd_session_remarks_en"] = no_hd_session_remarks_en
        if no_hd_session_remarks_tc is not UNSET:
            field_dict["no_hd_session_remarks_tc"] = no_hd_session_remarks_tc
        if other_approved_fees_registration_fee_wd is not UNSET:
            field_dict["other_approved_fees_registration_fee_wd"] = (
                other_approved_fees_registration_fee_wd
            )
        if no_wd_session_remarks_en is not UNSET:
            field_dict["no_wd_session_remarks_en"] = no_wd_session_remarks_en
        if no_wd_session_remarks_tc is not UNSET:
            field_dict["no_wd_session_remarks_tc"] = no_wd_session_remarks_tc
        if northing is not UNSET:
            field_dict["northing"] = northing
        if easting is not UNSET:
            field_dict["easting"] = easting
        if geometry_longitude is not UNSET:
            field_dict["GeometryLongitude"] = geometry_longitude
        if geometry_latitude is not UNSET:
            field_dict["GeometryLatitude"] = geometry_latitude
        if fid is not UNSET:
            field_dict["fid"] = fid
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_school_no(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        school_no = _parse_school_no(d.pop("school_no", UNSET))

        def _parse_location_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_no = _parse_location_no(d.pop("location_no", UNSET))

        def _parse_school_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_name_en = _parse_school_name_en(d.pop("school_name_en", UNSET))

        def _parse_school_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_name_tc = _parse_school_name_tc(d.pop("school_name_tc", UNSET))

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("district_en", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("district_tc", UNSET))

        def _parse_joining_kg_edu_scheme_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        joining_kg_edu_scheme_en = _parse_joining_kg_edu_scheme_en(
            d.pop("joining_kg_edu_scheme_en", UNSET)
        )

        def _parse_joining_kg_edu_scheme_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        joining_kg_edu_scheme_tc = _parse_joining_kg_edu_scheme_tc(
            d.pop("joining_kg_edu_scheme_tc", UNSET)
        )

        def _parse_received_grant_for_support_to_ncs_students(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        received_grant_for_support_to_ncs_students = (
            _parse_received_grant_for_support_to_ncs_students(
                d.pop("received_grant_for_support_to_ncs_students", UNSET)
            )
        )

        def _parse_application_date_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_date_from = _parse_application_date_from(
            d.pop("application_date_from", UNSET)
        )

        def _parse_application_date_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_date_to = _parse_application_date_to(
            d.pop("application_date_to", UNSET)
        )

        def _parse_application_form_type_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_form_type_en = _parse_application_form_type_en(
            d.pop("application_form_type_en", UNSET)
        )

        def _parse_application_form_type_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_form_type_tc = _parse_application_form_type_tc(
            d.pop("application_form_type_tc", UNSET)
        )

        def _parse_application_period_type_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_period_type_en = _parse_application_period_type_en(
            d.pop("application_period_type_en", UNSET)
        )

        def _parse_application_period_type_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_period_type_tc = _parse_application_period_type_tc(
            d.pop("application_period_type_tc", UNSET)
        )

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("address_en", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("address_tc", UNSET))

        def _parse_school_category_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_category_en = _parse_school_category_en(
            d.pop("school_category_en", UNSET)
        )

        def _parse_school_category_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_category_tc = _parse_school_category_tc(
            d.pop("school_category_tc", UNSET)
        )

        def _parse_student_category_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        student_category_en = _parse_student_category_en(
            d.pop("student_category_en", UNSET)
        )

        def _parse_student_category_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        student_category_tc = _parse_student_category_tc(
            d.pop("student_category_tc", UNSET)
        )

        def _parse_tel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tel = _parse_tel(d.pop("tel", UNSET))

        def _parse_fax(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax = _parse_fax(d.pop("fax", UNSET))

        def _parse_name_of_school_supervisor_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_school_supervisor_en = _parse_name_of_school_supervisor_en(
            d.pop("name_of_school_supervisor_en", UNSET)
        )

        def _parse_name_of_school_supervisor_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_school_supervisor_tc = _parse_name_of_school_supervisor_tc(
            d.pop("name_of_school_supervisor_tc", UNSET)
        )

        def _parse_title_of_school_supervisor_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_of_school_supervisor_en = _parse_title_of_school_supervisor_en(
            d.pop("title_of_school_supervisor_en", UNSET)
        )

        def _parse_title_of_school_supervisor_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_of_school_supervisor_tc = _parse_title_of_school_supervisor_tc(
            d.pop("title_of_school_supervisor_tc", UNSET)
        )

        def _parse_name_of_school_principal_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_school_principal_en = _parse_name_of_school_principal_en(
            d.pop("name_of_school_principal_en", UNSET)
        )

        def _parse_name_of_school_principal_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_school_principal_tc = _parse_name_of_school_principal_tc(
            d.pop("name_of_school_principal_tc", UNSET)
        )

        def _parse_title_of_school_principal_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_of_school_principal_en = _parse_title_of_school_principal_en(
            d.pop("title_of_school_principal_en", UNSET)
        )

        def _parse_title_of_school_principal_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_of_school_principal_tc = _parse_title_of_school_principal_tc(
            d.pop("title_of_school_principal_tc", UNSET)
        )

        def _parse_no_of_registered_classrooms_tc(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        no_of_registered_classrooms_tc = _parse_no_of_registered_classrooms_tc(
            d.pop("no_of_registered_classrooms_tc", UNSET)
        )

        def _parse_no_of_registered_classrooms_remarks_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_registered_classrooms_remarks_en = (
            _parse_no_of_registered_classrooms_remarks_en(
                d.pop("no_of_registered_classrooms_remarks_en", UNSET)
            )
        )

        def _parse_no_of_registered_classrooms_remarks_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_registered_classrooms_remarks_tc = (
            _parse_no_of_registered_classrooms_remarks_tc(
                d.pop("no_of_registered_classrooms_remarks_tc", UNSET)
            )
        )

        def _parse_outdoor_playground_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outdoor_playground_en = _parse_outdoor_playground_en(
            d.pop("outdoor_playground_en", UNSET)
        )

        def _parse_outdoor_playground_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outdoor_playground_tc = _parse_outdoor_playground_tc(
            d.pop("outdoor_playground_tc", UNSET)
        )

        def _parse_indoor_playground_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        indoor_playground_en = _parse_indoor_playground_en(
            d.pop("indoor_playground_en", UNSET)
        )

        def _parse_indoor_playground_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        indoor_playground_tc = _parse_indoor_playground_tc(
            d.pop("indoor_playground_tc", UNSET)
        )

        def _parse_music_room_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        music_room_en = _parse_music_room_en(d.pop("music_room_en", UNSET))

        def _parse_music_room_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        music_room_tc = _parse_music_room_tc(d.pop("music_room_tc", UNSET))

        def _parse_other_special_rooms_or_areas_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_special_rooms_or_areas_en = _parse_other_special_rooms_or_areas_en(
            d.pop("other_special_rooms_or_areas_en", UNSET)
        )

        def _parse_other_special_rooms_or_areas_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_special_rooms_or_areas_tc = _parse_other_special_rooms_or_areas_tc(
            d.pop("other_special_rooms_or_areas_tc", UNSET)
        )

        def _parse_school_founding_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        school_founding_year = _parse_school_founding_year(
            d.pop("school_founding_year", UNSET)
        )

        def _parse_school_founding_year_remarks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_founding_year_remarks_en = _parse_school_founding_year_remarks_en(
            d.pop("school_founding_year_remarks_en", UNSET)
        )

        def _parse_school_founding_year_remarks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_founding_year_remarks_tc = _parse_school_founding_year_remarks_tc(
            d.pop("school_founding_year_remarks_tc", UNSET)
        )

        def _parse_school_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_website = _parse_school_website(d.pop("school_website", UNSET))

        def _parse_working_hd_30000_or_below(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        working_hd_30000_or_below = _parse_working_hd_30000_or_below(
            d.pop("working_hd_30000_or_below", UNSET)
        )

        def _parse_working_hd_30001_to_40000(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        working_hd_30001_to_40000 = _parse_working_hd_30001_to_40000(
            d.pop("working_hd_30001_to_40000", UNSET)
        )

        def _parse_working_hd_40000_above(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        working_hd_40000_above = _parse_working_hd_40000_above(
            d.pop("working_hd_40000_above", UNSET)
        )

        def _parse_working_hd_remarks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        working_hd_remarks_en = _parse_working_hd_remarks_en(
            d.pop("working_hd_remarks_en", UNSET)
        )

        def _parse_working_hd_remarks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        working_hd_remarks_tc = _parse_working_hd_remarks_tc(
            d.pop("working_hd_remarks_tc", UNSET)
        )

        def _parse_working_wd_30000_or_below(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        working_wd_30000_or_below = _parse_working_wd_30000_or_below(
            d.pop("working_wd_30000_or_below", UNSET)
        )

        def _parse_working_wd_30001_to_40000(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        working_wd_30001_to_40000 = _parse_working_wd_30001_to_40000(
            d.pop("working_wd_30001_to_40000", UNSET)
        )

        def _parse_working_wd_40000_above(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        working_wd_40000_above = _parse_working_wd_40000_above(
            d.pop("working_wd_40000_above", UNSET)
        )

        def _parse_working_wd_remarks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        working_wd_remarks_en = _parse_working_wd_remarks_en(
            d.pop("working_wd_remarks_en", UNSET)
        )

        def _parse_working_wd_remarks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        working_wd_remarks_tc = _parse_working_wd_remarks_tc(
            d.pop("working_wd_remarks_tc", UNSET)
        )

        def _parse_working_exp_of_principal_and_teaching_staff_below_4_yrs(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        working_exp_of_principal_and_teaching_staff_below_4_yrs = (
            _parse_working_exp_of_principal_and_teaching_staff_below_4_yrs(
                d.pop("working_exp_of_principal_and_teaching_staff_below_4_yrs", UNSET)
            )
        )

        def _parse_principal_and_teaching_staff_working_exp_fm_4_to_7_yrs(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        principal_and_teaching_staff_working_exp_fm_4_to_7_yrs = (
            _parse_principal_and_teaching_staff_working_exp_fm_4_to_7_yrs(
                d.pop("principal_and_teaching_staff_working_exp_fm_4_to_7_yrs", UNSET)
            )
        )

        def _parse_working_exp_of_principal_and_teaching_staff_above_7_yrs(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        working_exp_of_principal_and_teaching_staff_above_7_yrs = (
            _parse_working_exp_of_principal_and_teaching_staff_above_7_yrs(
                d.pop("working_exp_of_principal_and_teaching_staff_above_7_yrs", UNSET)
            )
        )

        def _parse_working_exp_of_principal_and_teaching_staff_remarks_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        working_exp_of_principal_and_teaching_staff_remarks_en = (
            _parse_working_exp_of_principal_and_teaching_staff_remarks_en(
                d.pop("working_exp_of_principal_and_teaching_staff_remarks_en", UNSET)
            )
        )

        def _parse_working_exp_of_principal_and_teaching_staff_remarks_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        working_exp_of_principal_and_teaching_staff_remarks_tc = (
            _parse_working_exp_of_principal_and_teaching_staff_remarks_tc(
                d.pop("working_exp_of_principal_and_teaching_staff_remarks_tc", UNSET)
            )
        )

        def _parse_summer_uniform_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summer_uniform_en = _parse_summer_uniform_en(d.pop("summer_uniform_en", UNSET))

        def _parse_summer_uniform_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summer_uniform_tc = _parse_summer_uniform_tc(d.pop("summer_uniform_tc", UNSET))

        def _parse_winter_uniform_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        winter_uniform_en = _parse_winter_uniform_en(d.pop("winter_uniform_en", UNSET))

        def _parse_winter_uniform_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        winter_uniform_tc = _parse_winter_uniform_tc(d.pop("winter_uniform_tc", UNSET))

        def _parse_school_bag_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_bag_en = _parse_school_bag_en(d.pop("school_bag_en", UNSET))

        def _parse_school_bag_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_bag_tc = _parse_school_bag_tc(d.pop("school_bag_tc", UNSET))

        def _parse_tea_and_snacks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tea_and_snacks_en = _parse_tea_and_snacks_en(d.pop("tea_and_snacks_en", UNSET))

        def _parse_tea_and_snacks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tea_and_snacks_tc = _parse_tea_and_snacks_tc(d.pop("tea_and_snacks_tc", UNSET))

        def _parse_textbooks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        textbooks_en = _parse_textbooks_en(d.pop("textbooks_en", UNSET))

        def _parse_textbooks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        textbooks_tc = _parse_textbooks_tc(d.pop("textbooks_tc", UNSET))

        def _parse_exercise_books_or_workbooks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exercise_books_or_workbooks_en = _parse_exercise_books_or_workbooks_en(
            d.pop("exercise_books_or_workbooks_en", UNSET)
        )

        def _parse_exercise_books_or_workbooks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exercise_books_or_workbooks_tc = _parse_exercise_books_or_workbooks_tc(
            d.pop("exercise_books_or_workbooks_tc", UNSET)
        )

        def _parse_stationery_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stationery_en = _parse_stationery_en(d.pop("stationery_en", UNSET))

        def _parse_stationery_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stationery_tc = _parse_stationery_tc(d.pop("stationery_tc", UNSET))

        def _parse_bedding_items_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bedding_items_en = _parse_bedding_items_en(d.pop("bedding_items_en", UNSET))

        def _parse_bedding_items_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bedding_items_tc = _parse_bedding_items_tc(d.pop("bedding_items_tc", UNSET))

        def _parse_salary_of_principal_and_teaching_staff(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        salary_of_principal_and_teaching_staff = (
            _parse_salary_of_principal_and_teaching_staff(
                d.pop("salary_of_principal_and_teaching_staff", UNSET)
            )
        )

        def _parse_non_teaching_staff_salary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        non_teaching_staff_salary = _parse_non_teaching_staff_salary(
            d.pop("non_teaching_staff_salary", UNSET)
        )

        def _parse_rent_management_fees_rates_and_government_rent(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rent_management_fees_rates_and_government_rent = (
            _parse_rent_management_fees_rates_and_government_rent(
                d.pop("rent_management_fees_rates_and_government_rent", UNSET)
            )
        )

        def _parse_teaching_resources(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        teaching_resources = _parse_teaching_resources(
            d.pop("teaching_resources", UNSET)
        )

        def _parse_staff_training_and_professional_development(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        staff_training_and_professional_development = (
            _parse_staff_training_and_professional_development(
                d.pop("staff_training_and_professional_development", UNSET)
            )
        )

        def _parse_other_expenses(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_expenses = _parse_other_expenses(d.pop("other_expenses", UNSET))

        def _parse_expenditure_information_remarks_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expenditure_information_remarks_en = _parse_expenditure_information_remarks_en(
            d.pop("expenditure_information_remarks_en", UNSET)
        )

        def _parse_expenditure_information_remarks_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expenditure_information_remarks_tc = _parse_expenditure_information_remarks_tc(
            d.pop("expenditure_information_remarks_tc", UNSET)
        )

        def _parse_expenditure_information_based_on_audited_account_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expenditure_information_based_on_audited_account_en = (
            _parse_expenditure_information_based_on_audited_account_en(
                d.pop("expenditure_information_based_on_audited_account_en", UNSET)
            )
        )

        def _parse_expenditure_information_based_on_audited_account_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expenditure_information_based_on_audited_account_tc = (
            _parse_expenditure_information_based_on_audited_account_tc(
                d.pop("expenditure_information_based_on_audited_account_tc", UNSET)
            )
        )

        def _parse_curriculum_type_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        curriculum_type_en = _parse_curriculum_type_en(
            d.pop("curriculum_type_en", UNSET)
        )

        def _parse_curriculum_type_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        curriculum_type_tc = _parse_curriculum_type_tc(
            d.pop("curriculum_type_tc", UNSET)
        )

        def _parse_curriculum_planning_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        curriculum_planning_en = _parse_curriculum_planning_en(
            d.pop("curriculum_planning_en", UNSET)
        )

        def _parse_curriculum_planning_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        curriculum_planning_tc = _parse_curriculum_planning_tc(
            d.pop("curriculum_planning_tc", UNSET)
        )

        def _parse_learning_or_teaching_approach_and_activities_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        learning_or_teaching_approach_and_activities_en = (
            _parse_learning_or_teaching_approach_and_activities_en(
                d.pop("learning_or_teaching_approach_and_activities_en", UNSET)
            )
        )

        def _parse_learning_or_teaching_approach_and_activities_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        learning_or_teaching_approach_and_activities_tc = (
            _parse_learning_or_teaching_approach_and_activities_tc(
                d.pop("learning_or_teaching_approach_and_activities_tc", UNSET)
            )
        )

        def _parse_assessment_of_children_learning_experiences_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assessment_of_children_learning_experiences_en = (
            _parse_assessment_of_children_learning_experiences_en(
                d.pop("assessment_of_children_learning_experiences_en", UNSET)
            )
        )

        def _parse_assessment_of_children_learning_experiences_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assessment_of_children_learning_experiences_tc = (
            _parse_assessment_of_children_learning_experiences_tc(
                d.pop("assessment_of_children_learning_experiences_tc", UNSET)
            )
        )

        def _parse_school_vision_and_mission_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_vision_and_mission_en = _parse_school_vision_and_mission_en(
            d.pop("school_vision_and_mission_en", UNSET)
        )

        def _parse_school_vision_and_mission_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_vision_and_mission_tc = _parse_school_vision_and_mission_tc(
            d.pop("school_vision_and_mission_tc", UNSET)
        )

        def _parse_support_to_students_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_to_students_en = _parse_support_to_students_en(
            d.pop("support_to_students_en", UNSET)
        )

        def _parse_support_to_students_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_to_students_tc = _parse_support_to_students_tc(
            d.pop("support_to_students_tc", UNSET)
        )

        def _parse_parent_teacher_association_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_teacher_association_en = _parse_parent_teacher_association_en(
            d.pop("parent_teacher_association_en", UNSET)
        )

        def _parse_parent_teacher_association_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_teacher_association_tc = _parse_parent_teacher_association_tc(
            d.pop("parent_teacher_association_tc", UNSET)
        )

        def _parse_other_activities_or_communication_with_parents_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_activities_or_communication_with_parents_en = (
            _parse_other_activities_or_communication_with_parents_en(
                d.pop("other_activities_or_communication_with_parents_en", UNSET)
            )
        )

        def _parse_other_activities_or_communication_with_parents_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_activities_or_communication_with_parents_tc = (
            _parse_other_activities_or_communication_with_parents_tc(
                d.pop("other_activities_or_communication_with_parents_tc", UNSET)
            )
        )

        def _parse_support_to_non_chinese_speaking_ncs_students_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_to_non_chinese_speaking_ncs_students_en = (
            _parse_support_to_non_chinese_speaking_ncs_students_en(
                d.pop("support_to_non_chinese_speaking_ncs_students_en", UNSET)
            )
        )

        def _parse_support_to_non_chinese_speaking_ncs_students_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_to_non_chinese_speaking_ncs_students_tc = (
            _parse_support_to_non_chinese_speaking_ncs_students_tc(
                d.pop("support_to_non_chinese_speaking_ncs_students_tc", UNSET)
            )
        )

        def _parse_support_to_students_with_special_needs_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_to_students_with_special_needs_en = (
            _parse_support_to_students_with_special_needs_en(
                d.pop("support_to_students_with_special_needs_en", UNSET)
            )
        )

        def _parse_support_to_students_with_special_needs_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_to_students_with_special_needs_tc = (
            _parse_support_to_students_with_special_needs_tc(
                d.pop("support_to_students_with_special_needs_tc", UNSET)
            )
        )

        def _parse_nursery_classes_not_writing(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nursery_classes_not_writing = _parse_nursery_classes_not_writing(
            d.pop("nursery_classes_not_writing", UNSET)
        )

        def _parse_total_no_of_permitted_accommodation_of_class_rm_in_use(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_no_of_permitted_accommodation_of_class_rm_in_use = (
            _parse_total_no_of_permitted_accommodation_of_class_rm_in_use(
                d.pop("total_no_of_permitted_accommodation_of_class_rm_in_use", UNSET)
            )
        )

        def _parse_no_of_students_in_nursery_am(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_students_in_nursery_am = _parse_no_of_students_in_nursery_am(
            d.pop("no_of_students_in_nursery_am", UNSET)
        )

        def _parse_no_of_students_in_lkg_am(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_students_in_lkg_am = _parse_no_of_students_in_lkg_am(
            d.pop("no_of_students_in_lkg_am", UNSET)
        )

        def _parse_no_of_students_ukg_am(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_students_ukg_am = _parse_no_of_students_ukg_am(
            d.pop("no_of_students_ukg_am", UNSET)
        )

        def _parse_no_of_students_in_nursery_pm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_students_in_nursery_pm = _parse_no_of_students_in_nursery_pm(
            d.pop("no_of_students_in_nursery_pm", UNSET)
        )

        def _parse_no_of_students_in_lkg_pm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_students_in_lkg_pm = _parse_no_of_students_in_lkg_pm(
            d.pop("no_of_students_in_lkg_pm", UNSET)
        )

        def _parse_no_of_students_ukg_pm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_students_ukg_pm = _parse_no_of_students_ukg_pm(
            d.pop("no_of_students_ukg_pm", UNSET)
        )

        def _parse_no_of_students_in_nursery_wd(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_students_in_nursery_wd = _parse_no_of_students_in_nursery_wd(
            d.pop("no_of_students_in_nursery_wd", UNSET)
        )

        def _parse_no_of_students_in_lkg_wd(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_students_in_lkg_wd = _parse_no_of_students_in_lkg_wd(
            d.pop("no_of_students_in_lkg_wd", UNSET)
        )

        def _parse_no_of_students_in_ukg_wd(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_students_in_ukg_wd = _parse_no_of_students_in_ukg_wd(
            d.pop("no_of_students_in_ukg_wd", UNSET)
        )

        def _parse_teacher_to_pupil_ratio_in_morning_session(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        teacher_to_pupil_ratio_in_morning_session = (
            _parse_teacher_to_pupil_ratio_in_morning_session(
                d.pop("teacher_to_pupil_ratio_in_morning_session", UNSET)
            )
        )

        def _parse_teacher_to_pupil_ratio_in_afternoon_session(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        teacher_to_pupil_ratio_in_afternoon_session = (
            _parse_teacher_to_pupil_ratio_in_afternoon_session(
                d.pop("teacher_to_pupil_ratio_in_afternoon_session", UNSET)
            )
        )

        def _parse_teacher_to_pupil_ratio_remarks_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        teacher_to_pupil_ratio_remarks_en = _parse_teacher_to_pupil_ratio_remarks_en(
            d.pop("teacher_to_pupil_ratio_remarks_en", UNSET)
        )

        def _parse_teacher_to_pupil_ratio_remarks_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        teacher_to_pupil_ratio_remarks_tc = _parse_teacher_to_pupil_ratio_remarks_tc(
            d.pop("teacher_to_pupil_ratio_remarks_tc", UNSET)
        )

        def _parse_no_of_principal_and_teaching_staff_with_degree(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_principal_and_teaching_staff_with_degree = (
            _parse_no_of_principal_and_teaching_staff_with_degree(
                d.pop("no_of_principal_and_teaching_staff_with_degree", UNSET)
            )
        )

        def _parse_no_of_principal_and_teaching_staff_w_non_degree(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_principal_and_teaching_staff_w_non_degree = (
            _parse_no_of_principal_and_teaching_staff_w_non_degree(
                d.pop("no_of_principal_and_teaching_staff_w_non_degree", UNSET)
            )
        )

        def _parse_no_of_prin_n_teaching_staff_w_c_ece_or_above(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_prin_n_teaching_staff_w_c_ece_or_above = (
            _parse_no_of_prin_n_teaching_staff_w_c_ece_or_above(
                d.pop("no_of_prin_n_teaching_staff_w_c_ece_or_above", UNSET)
            )
        )

        def _parse_no_of_principal_and_teaching_staff_w_qkt(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_principal_and_teaching_staff_w_qkt = (
            _parse_no_of_principal_and_teaching_staff_w_qkt(
                d.pop("no_of_principal_and_teaching_staff_w_qkt", UNSET)
            )
        )

        def _parse_no_of_prin_n_teaching_staff_w_other_t_training(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_prin_n_teaching_staff_w_other_t_training = (
            _parse_no_of_prin_n_teaching_staff_w_other_t_training(
                d.pop("no_of_prin_n_teaching_staff_w_other_t_training", UNSET)
            )
        )

        def _parse_no_of_principal_and_teaching_staff_w_qakt(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_principal_and_teaching_staff_w_qakt = (
            _parse_no_of_principal_and_teaching_staff_w_qakt(
                d.pop("no_of_principal_and_teaching_staff_w_qakt", UNSET)
            )
        )

        def _parse_no_of_principal_and_teaching_staff_others(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_principal_and_teaching_staff_others = (
            _parse_no_of_principal_and_teaching_staff_others(
                d.pop("no_of_principal_and_teaching_staff_others", UNSET)
            )
        )

        def _parse_total_no_of_principal_and_teaching_staff(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_no_of_principal_and_teaching_staff = (
            _parse_total_no_of_principal_and_teaching_staff(
                d.pop("total_no_of_principal_and_teaching_staff", UNSET)
            )
        )

        def _parse_fees_certificate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fees_certificate = _parse_fees_certificate(d.pop("fees_certificate", UNSET))

        def _parse_quality_review_result_and_report_chi_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quality_review_result_and_report_chi_en = (
            _parse_quality_review_result_and_report_chi_en(
                d.pop("quality_review_result_and_report_chi_en", UNSET)
            )
        )

        def _parse_quality_review_result_and_report_chi_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quality_review_result_and_report_chi_tc = (
            _parse_quality_review_result_and_report_chi_tc(
                d.pop("quality_review_result_and_report_chi_tc", UNSET)
            )
        )

        def _parse_quality_review_result_and_report_eng_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quality_review_result_and_report_eng_en = (
            _parse_quality_review_result_and_report_eng_en(
                d.pop("quality_review_result_and_report_eng_en", UNSET)
            )
        )

        def _parse_quality_review_result_and_report_eng_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quality_review_result_and_report_eng_tc = (
            _parse_quality_review_result_and_report_eng_tc(
                d.pop("quality_review_result_and_report_eng_tc", UNSET)
            )
        )

        def _parse_child_care_service_for_aged_under_2_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        child_care_service_for_aged_under_2_tc = (
            _parse_child_care_service_for_aged_under_2_tc(
                d.pop("child_care_service_for_aged_under_2_tc", UNSET)
            )
        )

        def _parse_child_care_service_for_aged_under_2_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        child_care_service_for_aged_under_2_en = (
            _parse_child_care_service_for_aged_under_2_en(
                d.pop("child_care_service_for_aged_under_2_en", UNSET)
            )
        )

        def _parse_child_care_service_for_aged_2_to_3_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        child_care_service_for_aged_2_to_3_tc = (
            _parse_child_care_service_for_aged_2_to_3_tc(
                d.pop("child_care_service_for_aged_2_to_3_tc", UNSET)
            )
        )

        def _parse_child_care_service_for_aged_2_to_3_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        child_care_service_for_aged_2_to_3_en = (
            _parse_child_care_service_for_aged_2_to_3_en(
                d.pop("child_care_service_for_aged_2_to_3_en", UNSET)
            )
        )

        def _parse_no_for_enrolment_aged_2_to_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_for_enrolment_aged_2_to_3 = _parse_no_for_enrolment_aged_2_to_3(
            d.pop("no_for_enrolment_aged_2_to_3", UNSET)
        )

        def _parse_cc_service_fee_level_annum_hd(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cc_service_fee_level_annum_hd = _parse_cc_service_fee_level_annum_hd(
            d.pop("cc_service_fee_level_annum_hd", UNSET)
        )

        def _parse_cc_service_fee_level_annum_wd(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cc_service_fee_level_annum_wd = _parse_cc_service_fee_level_annum_wd(
            d.pop("cc_service_fee_level_annum_wd", UNSET)
        )

        def _parse_join_ccc_subsidy_scheme_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        join_ccc_subsidy_scheme_en = _parse_join_ccc_subsidy_scheme_en(
            d.pop("join_ccc_subsidy_scheme_en", UNSET)
        )

        def _parse_join_ccc_subsidy_scheme_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        join_ccc_subsidy_scheme_tc = _parse_join_ccc_subsidy_scheme_tc(
            d.pop("join_ccc_subsidy_scheme_tc", UNSET)
        )

        def _parse_provide_occasional_cc_service_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provide_occasional_cc_service_en = _parse_provide_occasional_cc_service_en(
            d.pop("provide_occasional_cc_service_en", UNSET)
        )

        def _parse_provide_occasional_cc_service_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provide_occasional_cc_service_tc = _parse_provide_occasional_cc_service_tc(
            d.pop("provide_occasional_cc_service_tc", UNSET)
        )

        def _parse_provide_extended_hour_service_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provide_extended_hour_service_en = _parse_provide_extended_hour_service_en(
            d.pop("provide_extended_hour_service_en", UNSET)
        )

        def _parse_provide_extended_hour_service_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provide_extended_hour_service_tc = _parse_provide_extended_hour_service_tc(
            d.pop("provide_extended_hour_service_tc", UNSET)
        )

        def _parse_other_approved_fees_application_fee_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_approved_fees_application_fee_en = (
            _parse_other_approved_fees_application_fee_en(
                d.pop("other_approved_fees_application_fee_en", UNSET)
            )
        )

        def _parse_other_approved_fees_application_fee_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_approved_fees_application_fee_tc = (
            _parse_other_approved_fees_application_fee_tc(
                d.pop("other_approved_fees_application_fee_tc", UNSET)
            )
        )

        def _parse_other_approved_fees_registration_fee_hd(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_approved_fees_registration_fee_hd = (
            _parse_other_approved_fees_registration_fee_hd(
                d.pop("other_approved_fees_registration_fee_hd", UNSET)
            )
        )

        def _parse_no_hd_session_remarks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_hd_session_remarks_en = _parse_no_hd_session_remarks_en(
            d.pop("no_hd_session_remarks_en", UNSET)
        )

        def _parse_no_hd_session_remarks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_hd_session_remarks_tc = _parse_no_hd_session_remarks_tc(
            d.pop("no_hd_session_remarks_tc", UNSET)
        )

        def _parse_other_approved_fees_registration_fee_wd(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_approved_fees_registration_fee_wd = (
            _parse_other_approved_fees_registration_fee_wd(
                d.pop("other_approved_fees_registration_fee_wd", UNSET)
            )
        )

        def _parse_no_wd_session_remarks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_wd_session_remarks_en = _parse_no_wd_session_remarks_en(
            d.pop("no_wd_session_remarks_en", UNSET)
        )

        def _parse_no_wd_session_remarks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_wd_session_remarks_tc = _parse_no_wd_session_remarks_tc(
            d.pop("no_wd_session_remarks_tc", UNSET)
        )

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("northing", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("easting", UNSET))

        def _parse_geometry_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        geometry_longitude = _parse_geometry_longitude(
            d.pop("GeometryLongitude", UNSET)
        )

        def _parse_geometry_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        geometry_latitude = _parse_geometry_latitude(d.pop("GeometryLatitude", UNSET))

        def _parse_fid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fid = _parse_fid(d.pop("fid", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            school_no=school_no,
            location_no=location_no,
            school_name_en=school_name_en,
            school_name_tc=school_name_tc,
            district_en=district_en,
            district_tc=district_tc,
            joining_kg_edu_scheme_en=joining_kg_edu_scheme_en,
            joining_kg_edu_scheme_tc=joining_kg_edu_scheme_tc,
            received_grant_for_support_to_ncs_students=received_grant_for_support_to_ncs_students,
            application_date_from=application_date_from,
            application_date_to=application_date_to,
            application_form_type_en=application_form_type_en,
            application_form_type_tc=application_form_type_tc,
            application_period_type_en=application_period_type_en,
            application_period_type_tc=application_period_type_tc,
            address_en=address_en,
            address_tc=address_tc,
            school_category_en=school_category_en,
            school_category_tc=school_category_tc,
            student_category_en=student_category_en,
            student_category_tc=student_category_tc,
            tel=tel,
            fax=fax,
            name_of_school_supervisor_en=name_of_school_supervisor_en,
            name_of_school_supervisor_tc=name_of_school_supervisor_tc,
            title_of_school_supervisor_en=title_of_school_supervisor_en,
            title_of_school_supervisor_tc=title_of_school_supervisor_tc,
            name_of_school_principal_en=name_of_school_principal_en,
            name_of_school_principal_tc=name_of_school_principal_tc,
            title_of_school_principal_en=title_of_school_principal_en,
            title_of_school_principal_tc=title_of_school_principal_tc,
            no_of_registered_classrooms_tc=no_of_registered_classrooms_tc,
            no_of_registered_classrooms_remarks_en=no_of_registered_classrooms_remarks_en,
            no_of_registered_classrooms_remarks_tc=no_of_registered_classrooms_remarks_tc,
            outdoor_playground_en=outdoor_playground_en,
            outdoor_playground_tc=outdoor_playground_tc,
            indoor_playground_en=indoor_playground_en,
            indoor_playground_tc=indoor_playground_tc,
            music_room_en=music_room_en,
            music_room_tc=music_room_tc,
            other_special_rooms_or_areas_en=other_special_rooms_or_areas_en,
            other_special_rooms_or_areas_tc=other_special_rooms_or_areas_tc,
            school_founding_year=school_founding_year,
            school_founding_year_remarks_en=school_founding_year_remarks_en,
            school_founding_year_remarks_tc=school_founding_year_remarks_tc,
            school_website=school_website,
            working_hd_30000_or_below=working_hd_30000_or_below,
            working_hd_30001_to_40000=working_hd_30001_to_40000,
            working_hd_40000_above=working_hd_40000_above,
            working_hd_remarks_en=working_hd_remarks_en,
            working_hd_remarks_tc=working_hd_remarks_tc,
            working_wd_30000_or_below=working_wd_30000_or_below,
            working_wd_30001_to_40000=working_wd_30001_to_40000,
            working_wd_40000_above=working_wd_40000_above,
            working_wd_remarks_en=working_wd_remarks_en,
            working_wd_remarks_tc=working_wd_remarks_tc,
            working_exp_of_principal_and_teaching_staff_below_4_yrs=working_exp_of_principal_and_teaching_staff_below_4_yrs,
            principal_and_teaching_staff_working_exp_fm_4_to_7_yrs=principal_and_teaching_staff_working_exp_fm_4_to_7_yrs,
            working_exp_of_principal_and_teaching_staff_above_7_yrs=working_exp_of_principal_and_teaching_staff_above_7_yrs,
            working_exp_of_principal_and_teaching_staff_remarks_en=working_exp_of_principal_and_teaching_staff_remarks_en,
            working_exp_of_principal_and_teaching_staff_remarks_tc=working_exp_of_principal_and_teaching_staff_remarks_tc,
            summer_uniform_en=summer_uniform_en,
            summer_uniform_tc=summer_uniform_tc,
            winter_uniform_en=winter_uniform_en,
            winter_uniform_tc=winter_uniform_tc,
            school_bag_en=school_bag_en,
            school_bag_tc=school_bag_tc,
            tea_and_snacks_en=tea_and_snacks_en,
            tea_and_snacks_tc=tea_and_snacks_tc,
            textbooks_en=textbooks_en,
            textbooks_tc=textbooks_tc,
            exercise_books_or_workbooks_en=exercise_books_or_workbooks_en,
            exercise_books_or_workbooks_tc=exercise_books_or_workbooks_tc,
            stationery_en=stationery_en,
            stationery_tc=stationery_tc,
            bedding_items_en=bedding_items_en,
            bedding_items_tc=bedding_items_tc,
            salary_of_principal_and_teaching_staff=salary_of_principal_and_teaching_staff,
            non_teaching_staff_salary=non_teaching_staff_salary,
            rent_management_fees_rates_and_government_rent=rent_management_fees_rates_and_government_rent,
            teaching_resources=teaching_resources,
            staff_training_and_professional_development=staff_training_and_professional_development,
            other_expenses=other_expenses,
            expenditure_information_remarks_en=expenditure_information_remarks_en,
            expenditure_information_remarks_tc=expenditure_information_remarks_tc,
            expenditure_information_based_on_audited_account_en=expenditure_information_based_on_audited_account_en,
            expenditure_information_based_on_audited_account_tc=expenditure_information_based_on_audited_account_tc,
            curriculum_type_en=curriculum_type_en,
            curriculum_type_tc=curriculum_type_tc,
            curriculum_planning_en=curriculum_planning_en,
            curriculum_planning_tc=curriculum_planning_tc,
            learning_or_teaching_approach_and_activities_en=learning_or_teaching_approach_and_activities_en,
            learning_or_teaching_approach_and_activities_tc=learning_or_teaching_approach_and_activities_tc,
            assessment_of_children_learning_experiences_en=assessment_of_children_learning_experiences_en,
            assessment_of_children_learning_experiences_tc=assessment_of_children_learning_experiences_tc,
            school_vision_and_mission_en=school_vision_and_mission_en,
            school_vision_and_mission_tc=school_vision_and_mission_tc,
            support_to_students_en=support_to_students_en,
            support_to_students_tc=support_to_students_tc,
            parent_teacher_association_en=parent_teacher_association_en,
            parent_teacher_association_tc=parent_teacher_association_tc,
            other_activities_or_communication_with_parents_en=other_activities_or_communication_with_parents_en,
            other_activities_or_communication_with_parents_tc=other_activities_or_communication_with_parents_tc,
            support_to_non_chinese_speaking_ncs_students_en=support_to_non_chinese_speaking_ncs_students_en,
            support_to_non_chinese_speaking_ncs_students_tc=support_to_non_chinese_speaking_ncs_students_tc,
            support_to_students_with_special_needs_en=support_to_students_with_special_needs_en,
            support_to_students_with_special_needs_tc=support_to_students_with_special_needs_tc,
            nursery_classes_not_writing=nursery_classes_not_writing,
            total_no_of_permitted_accommodation_of_class_rm_in_use=total_no_of_permitted_accommodation_of_class_rm_in_use,
            no_of_students_in_nursery_am=no_of_students_in_nursery_am,
            no_of_students_in_lkg_am=no_of_students_in_lkg_am,
            no_of_students_ukg_am=no_of_students_ukg_am,
            no_of_students_in_nursery_pm=no_of_students_in_nursery_pm,
            no_of_students_in_lkg_pm=no_of_students_in_lkg_pm,
            no_of_students_ukg_pm=no_of_students_ukg_pm,
            no_of_students_in_nursery_wd=no_of_students_in_nursery_wd,
            no_of_students_in_lkg_wd=no_of_students_in_lkg_wd,
            no_of_students_in_ukg_wd=no_of_students_in_ukg_wd,
            teacher_to_pupil_ratio_in_morning_session=teacher_to_pupil_ratio_in_morning_session,
            teacher_to_pupil_ratio_in_afternoon_session=teacher_to_pupil_ratio_in_afternoon_session,
            teacher_to_pupil_ratio_remarks_en=teacher_to_pupil_ratio_remarks_en,
            teacher_to_pupil_ratio_remarks_tc=teacher_to_pupil_ratio_remarks_tc,
            no_of_principal_and_teaching_staff_with_degree=no_of_principal_and_teaching_staff_with_degree,
            no_of_principal_and_teaching_staff_w_non_degree=no_of_principal_and_teaching_staff_w_non_degree,
            no_of_prin_n_teaching_staff_w_c_ece_or_above=no_of_prin_n_teaching_staff_w_c_ece_or_above,
            no_of_principal_and_teaching_staff_w_qkt=no_of_principal_and_teaching_staff_w_qkt,
            no_of_prin_n_teaching_staff_w_other_t_training=no_of_prin_n_teaching_staff_w_other_t_training,
            no_of_principal_and_teaching_staff_w_qakt=no_of_principal_and_teaching_staff_w_qakt,
            no_of_principal_and_teaching_staff_others=no_of_principal_and_teaching_staff_others,
            total_no_of_principal_and_teaching_staff=total_no_of_principal_and_teaching_staff,
            fees_certificate=fees_certificate,
            quality_review_result_and_report_chi_en=quality_review_result_and_report_chi_en,
            quality_review_result_and_report_chi_tc=quality_review_result_and_report_chi_tc,
            quality_review_result_and_report_eng_en=quality_review_result_and_report_eng_en,
            quality_review_result_and_report_eng_tc=quality_review_result_and_report_eng_tc,
            child_care_service_for_aged_under_2_tc=child_care_service_for_aged_under_2_tc,
            child_care_service_for_aged_under_2_en=child_care_service_for_aged_under_2_en,
            child_care_service_for_aged_2_to_3_tc=child_care_service_for_aged_2_to_3_tc,
            child_care_service_for_aged_2_to_3_en=child_care_service_for_aged_2_to_3_en,
            no_for_enrolment_aged_2_to_3=no_for_enrolment_aged_2_to_3,
            cc_service_fee_level_annum_hd=cc_service_fee_level_annum_hd,
            cc_service_fee_level_annum_wd=cc_service_fee_level_annum_wd,
            join_ccc_subsidy_scheme_en=join_ccc_subsidy_scheme_en,
            join_ccc_subsidy_scheme_tc=join_ccc_subsidy_scheme_tc,
            provide_occasional_cc_service_en=provide_occasional_cc_service_en,
            provide_occasional_cc_service_tc=provide_occasional_cc_service_tc,
            provide_extended_hour_service_en=provide_extended_hour_service_en,
            provide_extended_hour_service_tc=provide_extended_hour_service_tc,
            other_approved_fees_application_fee_en=other_approved_fees_application_fee_en,
            other_approved_fees_application_fee_tc=other_approved_fees_application_fee_tc,
            other_approved_fees_registration_fee_hd=other_approved_fees_registration_fee_hd,
            no_hd_session_remarks_en=no_hd_session_remarks_en,
            no_hd_session_remarks_tc=no_hd_session_remarks_tc,
            other_approved_fees_registration_fee_wd=other_approved_fees_registration_fee_wd,
            no_wd_session_remarks_en=no_wd_session_remarks_en,
            no_wd_session_remarks_tc=no_wd_session_remarks_tc,
            northing=northing,
            easting=easting,
            geometry_longitude=geometry_longitude,
            geometry_latitude=geometry_latitude,
            fid=fid,
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
