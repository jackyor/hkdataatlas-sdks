from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsPSchoolProfilesAttributes")


@_attrs_define
class WfsMapServerWfsPSchoolProfilesAttributes:
    """
    Attributes:
        feature_member_owns (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML
            occurrence into all JSON queries.
        fid (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        id (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        district_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        school_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        school_name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        school_address_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        school_address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        poa_school_net (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        school_tel (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        school_fax (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        school_email (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        school_website (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        school_type_1_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        school_type_1_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        school_type_2_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        school_type_2_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        imc_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        imc_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        training_compliance_rate_supervisor_managers_smc_chair_members (None | str | Unset): Native XSD type .
            Requiredness is not projected from XML occurrence into all JSON queries.
        name_supervisor_chairman_of_mc_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        name_supervisor_chairman_of_mc_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        title_supervisor_chairman_of_mc_en (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        title_supervisor_chairman_of_mc_tc (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        name_of_school_head_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        name_of_school_head_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        title_of_school_head_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        title_of_school_head_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        student_gender_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        student_gender_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        sponsoring_body_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        sponsoring_body_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        commencement_of_operation_year (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        religion_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        religion_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        other_religion_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        other_religion_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        school_motto_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        school_motto_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        school_size (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        medium_of_instruction_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        medium_of_instruction_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        through_train_sec_school_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        through_train_sec_school_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        feeder_sec_school_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        feeder_sec_school_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        nominated_sec_school_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        nominated_sec_school_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        school_bus_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        school_bus_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        nanny_van_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        nanny_van_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        parent_teacher_association_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        parent_teacher_association_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        school_alumni_association_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        school_alumni_association_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        four_rs_mental_health_charter (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        whole_school_health_programme (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        asc_school_fee_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        asc_school_fee_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        asc_tong_fai (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        asc_pta_fee_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        asc_pta_fee_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        asc_charges_for_non_standard_items_en (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        asc_charges_for_non_standard_items_tc (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        asc_others_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        asc_others_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        fac_no_of_classroom (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        fac_no_of_school_hall (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        fac_no_of_playground (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        fac_no_of_library (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        fac_special_rooms_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        fac_special_rooms_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        fac_others_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        fac_others_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        fac_support_for_specialedu_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        fac_support_for_specialedu_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        previous_year_tsi_no_of_approved_teaching_posts (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        previous_year_tsi_total_no_of_teachers (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        previous_year_tsi_percent_of_received_teacher_training (None | str | Unset): Native XSD type . Requiredness is
            not projected from XML occurrence into all JSON queries.
        previous_year_tsi_percent_of_bacherlor (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        previous_year_tsi_percent_of_master_doctorate_or_above (None | str | Unset): Native XSD type . Requiredness is
            not projected from XML occurrence into all JSON queries.
        previous_year_tsi_percent_of_special_edu_training (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        previous_year_tsi_percent_of_exp_0_4 (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        previous_year_tsi_percent_of_exp_5_9 (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        previous_year_tsi_percent_of_exp_10_or_above (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        previous_year_no_of_class_p1 (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        previous_year_no_of_class_p2 (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        previous_year_no_of_class_p3 (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        previous_year_no_of_class_p4 (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        previous_year_no_of_class_p5 (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        previous_year_no_of_class_p6 (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        previous_year_no_of_class_total (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        current_year_no_of_class_p1 (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        current_year_no_of_class_p2 (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        current_year_no_of_class_p3 (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        current_year_no_of_class_p4 (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        current_year_no_of_class_p5 (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        current_year_no_of_class_p6 (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        current_year_no_of_class_total (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        cs_mode_of_teaching_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        cs_mode_of_teaching_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        cs_remarks_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        cs_remarks_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        no_of_test_per_year_p1 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        no_of_exam_per_year_p1 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        replace_test_exam_p1_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        replace_test_exam_p1_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        no_of_test_per_year_p2_p6 (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        no_of_exam_p2_p6 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_en (None | str | Unset): Native XSD type .
            Requiredness is not projected from XML occurrence into all JSON queries.
        fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_tc (None | str | Unset): Native XSD type .
            Requiredness is not projected from XML occurrence into all JSON queries.
        upload_school_assessment_policy_to_school_web_en (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        upload_school_assessment_policy_to_school_web_tc (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        upload_school_assignment_policy_to_school_web_en (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        upload_school_assignment_policy_to_school_web_tc (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        diversified_assessment_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        diversified_assessment_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        avoid_test_exam_after_long_holidays_en (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        avoid_test_exam_after_long_holidays_tc (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        arrange_timetable_flexibly_tutorial_session_in_afternoon_en (None | str | Unset): Native XSD type . Requiredness
            is not projected from XML occurrence into all JSON queries.
        arrange_timetable_flexibly_tutorial_session_in_afternoon_tc (None | str | Unset): Native XSD type . Requiredness
            is not projected from XML occurrence into all JSON queries.
        streaming_arrangement_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        streaming_arrangement_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        no_of_school_days_per_week (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        no_of_periods_per_day (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        duration_of_each_period (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        school_starts_at (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        school_starts_at_ampm_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        school_starts_at_ampm_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        school_ends_at (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        school_ends_at_ampm_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        school_ends_at_ampm_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        lunch_start_time (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        lunch_end_time (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        lunch_arrangement_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        lunch_arrangement_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        healthy_school_life_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        healthy_school_life_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        school_life_remarks_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        school_life_remarks_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        life_wide_learning_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        life_wide_learning_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        school_mission_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        school_mission_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        school_management_url (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        school_organisation_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        school_organisation_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        imc_smc_mc_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        imc_smc_mc_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        school_green_policy_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        school_green_policy_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        school_major_concerns_url (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        school_major_concerns_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        school_major_concerns_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        learning_and_teaching_plan_url (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        learning_and_teaching_strategies_en (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        learning_and_teaching_strategies_tc (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        major_renewed_emphases_pri_edu_curriculum_en (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        major_renewed_emphases_pri_edu_curriculum_tc (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        dev_of_generic_skills_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        dev_of_generic_skills_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        cultivation_of_proper_values_attitudes_and_behaviours_en (None | str | Unset): Native XSD type . Requiredness is
            not projected from XML occurrence into all JSON queries.
        cultivation_of_proper_values_attitudes_and_behaviours_tc (None | str | Unset): Native XSD type . Requiredness is
            not projected from XML occurrence into all JSON queries.
        student_support_url (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        whole_school_approach_cater_for_learner_diversity_en (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        whole_school_approach_cater_for_learner_diversity_tc (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        whole_school_approach_integrated_education_en (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        whole_school_approach_integrated_education_tc (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        support_for_non_chinese_students_en (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        support_for_non_chinese_students_tc (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        curriculum_tailoring_and_adaptation_en (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        curriculum_tailoring_and_adaptation_tc (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        home_school_cooperation_url (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        home_school_cooperation_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        home_school_cooperation_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        school_ethos_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        school_ethos_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        future_dev_url (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        school_dev_plan_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        school_dev_plan_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        teacher_pro_training_and_dev_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        teacher_pro_training_and_dev_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        school_character_others_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        school_character_others_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        fee_remission_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        fee_remission_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        northing (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        easting (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    feature_member_owns: int | None | Unset = UNSET
    fid: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    school_name_en: None | str | Unset = UNSET
    school_name_tc: None | str | Unset = UNSET
    school_address_en: None | str | Unset = UNSET
    school_address_tc: None | str | Unset = UNSET
    poa_school_net: None | str | Unset = UNSET
    school_tel: None | str | Unset = UNSET
    school_fax: None | str | Unset = UNSET
    school_email: None | str | Unset = UNSET
    school_website: None | str | Unset = UNSET
    school_type_1_en: None | str | Unset = UNSET
    school_type_1_tc: None | str | Unset = UNSET
    school_type_2_en: None | str | Unset = UNSET
    school_type_2_tc: None | str | Unset = UNSET
    imc_en: None | str | Unset = UNSET
    imc_tc: None | str | Unset = UNSET
    training_compliance_rate_supervisor_managers_smc_chair_members: (
        None | str | Unset
    ) = UNSET
    name_supervisor_chairman_of_mc_en: None | str | Unset = UNSET
    name_supervisor_chairman_of_mc_tc: None | str | Unset = UNSET
    title_supervisor_chairman_of_mc_en: None | str | Unset = UNSET
    title_supervisor_chairman_of_mc_tc: None | str | Unset = UNSET
    name_of_school_head_en: None | str | Unset = UNSET
    name_of_school_head_tc: None | str | Unset = UNSET
    title_of_school_head_en: None | str | Unset = UNSET
    title_of_school_head_tc: None | str | Unset = UNSET
    student_gender_en: None | str | Unset = UNSET
    student_gender_tc: None | str | Unset = UNSET
    sponsoring_body_en: None | str | Unset = UNSET
    sponsoring_body_tc: None | str | Unset = UNSET
    commencement_of_operation_year: None | str | Unset = UNSET
    religion_en: None | str | Unset = UNSET
    religion_tc: None | str | Unset = UNSET
    other_religion_en: None | str | Unset = UNSET
    other_religion_tc: None | str | Unset = UNSET
    school_motto_en: None | str | Unset = UNSET
    school_motto_tc: None | str | Unset = UNSET
    school_size: None | str | Unset = UNSET
    medium_of_instruction_en: None | str | Unset = UNSET
    medium_of_instruction_tc: None | str | Unset = UNSET
    through_train_sec_school_en: None | str | Unset = UNSET
    through_train_sec_school_tc: None | str | Unset = UNSET
    feeder_sec_school_en: None | str | Unset = UNSET
    feeder_sec_school_tc: None | str | Unset = UNSET
    nominated_sec_school_en: None | str | Unset = UNSET
    nominated_sec_school_tc: None | str | Unset = UNSET
    school_bus_en: None | str | Unset = UNSET
    school_bus_tc: None | str | Unset = UNSET
    nanny_van_en: None | str | Unset = UNSET
    nanny_van_tc: None | str | Unset = UNSET
    parent_teacher_association_en: None | str | Unset = UNSET
    parent_teacher_association_tc: None | str | Unset = UNSET
    school_alumni_association_en: None | str | Unset = UNSET
    school_alumni_association_tc: None | str | Unset = UNSET
    four_rs_mental_health_charter: None | str | Unset = UNSET
    whole_school_health_programme: None | str | Unset = UNSET
    asc_school_fee_en: None | str | Unset = UNSET
    asc_school_fee_tc: None | str | Unset = UNSET
    asc_tong_fai: None | str | Unset = UNSET
    asc_pta_fee_en: None | str | Unset = UNSET
    asc_pta_fee_tc: None | str | Unset = UNSET
    asc_charges_for_non_standard_items_en: None | str | Unset = UNSET
    asc_charges_for_non_standard_items_tc: None | str | Unset = UNSET
    asc_others_en: None | str | Unset = UNSET
    asc_others_tc: None | str | Unset = UNSET
    fac_no_of_classroom: None | str | Unset = UNSET
    fac_no_of_school_hall: None | str | Unset = UNSET
    fac_no_of_playground: None | str | Unset = UNSET
    fac_no_of_library: None | str | Unset = UNSET
    fac_special_rooms_en: None | str | Unset = UNSET
    fac_special_rooms_tc: None | str | Unset = UNSET
    fac_others_en: None | str | Unset = UNSET
    fac_others_tc: None | str | Unset = UNSET
    fac_support_for_specialedu_en: None | str | Unset = UNSET
    fac_support_for_specialedu_tc: None | str | Unset = UNSET
    previous_year_tsi_no_of_approved_teaching_posts: None | str | Unset = UNSET
    previous_year_tsi_total_no_of_teachers: None | str | Unset = UNSET
    previous_year_tsi_percent_of_received_teacher_training: None | str | Unset = UNSET
    previous_year_tsi_percent_of_bacherlor: None | str | Unset = UNSET
    previous_year_tsi_percent_of_master_doctorate_or_above: None | str | Unset = UNSET
    previous_year_tsi_percent_of_special_edu_training: None | str | Unset = UNSET
    previous_year_tsi_percent_of_exp_0_4: None | str | Unset = UNSET
    previous_year_tsi_percent_of_exp_5_9: None | str | Unset = UNSET
    previous_year_tsi_percent_of_exp_10_or_above: None | str | Unset = UNSET
    previous_year_no_of_class_p1: None | str | Unset = UNSET
    previous_year_no_of_class_p2: None | str | Unset = UNSET
    previous_year_no_of_class_p3: None | str | Unset = UNSET
    previous_year_no_of_class_p4: None | str | Unset = UNSET
    previous_year_no_of_class_p5: None | str | Unset = UNSET
    previous_year_no_of_class_p6: None | str | Unset = UNSET
    previous_year_no_of_class_total: None | str | Unset = UNSET
    current_year_no_of_class_p1: None | str | Unset = UNSET
    current_year_no_of_class_p2: None | str | Unset = UNSET
    current_year_no_of_class_p3: None | str | Unset = UNSET
    current_year_no_of_class_p4: None | str | Unset = UNSET
    current_year_no_of_class_p5: None | str | Unset = UNSET
    current_year_no_of_class_p6: None | str | Unset = UNSET
    current_year_no_of_class_total: None | str | Unset = UNSET
    cs_mode_of_teaching_en: None | str | Unset = UNSET
    cs_mode_of_teaching_tc: None | str | Unset = UNSET
    cs_remarks_en: None | str | Unset = UNSET
    cs_remarks_tc: None | str | Unset = UNSET
    no_of_test_per_year_p1: None | str | Unset = UNSET
    no_of_exam_per_year_p1: None | str | Unset = UNSET
    replace_test_exam_p1_en: None | str | Unset = UNSET
    replace_test_exam_p1_tc: None | str | Unset = UNSET
    no_of_test_per_year_p2_p6: None | str | Unset = UNSET
    no_of_exam_p2_p6: None | str | Unset = UNSET
    fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_en: (
        None | str | Unset
    ) = UNSET
    fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_tc: (
        None | str | Unset
    ) = UNSET
    upload_school_assessment_policy_to_school_web_en: None | str | Unset = UNSET
    upload_school_assessment_policy_to_school_web_tc: None | str | Unset = UNSET
    upload_school_assignment_policy_to_school_web_en: None | str | Unset = UNSET
    upload_school_assignment_policy_to_school_web_tc: None | str | Unset = UNSET
    diversified_assessment_en: None | str | Unset = UNSET
    diversified_assessment_tc: None | str | Unset = UNSET
    avoid_test_exam_after_long_holidays_en: None | str | Unset = UNSET
    avoid_test_exam_after_long_holidays_tc: None | str | Unset = UNSET
    arrange_timetable_flexibly_tutorial_session_in_afternoon_en: None | str | Unset = (
        UNSET
    )
    arrange_timetable_flexibly_tutorial_session_in_afternoon_tc: None | str | Unset = (
        UNSET
    )
    streaming_arrangement_en: None | str | Unset = UNSET
    streaming_arrangement_tc: None | str | Unset = UNSET
    no_of_school_days_per_week: None | str | Unset = UNSET
    no_of_periods_per_day: None | str | Unset = UNSET
    duration_of_each_period: None | str | Unset = UNSET
    school_starts_at: None | str | Unset = UNSET
    school_starts_at_ampm_en: None | str | Unset = UNSET
    school_starts_at_ampm_tc: None | str | Unset = UNSET
    school_ends_at: None | str | Unset = UNSET
    school_ends_at_ampm_en: None | str | Unset = UNSET
    school_ends_at_ampm_tc: None | str | Unset = UNSET
    lunch_start_time: None | str | Unset = UNSET
    lunch_end_time: None | str | Unset = UNSET
    lunch_arrangement_en: None | str | Unset = UNSET
    lunch_arrangement_tc: None | str | Unset = UNSET
    healthy_school_life_en: None | str | Unset = UNSET
    healthy_school_life_tc: None | str | Unset = UNSET
    school_life_remarks_en: None | str | Unset = UNSET
    school_life_remarks_tc: None | str | Unset = UNSET
    life_wide_learning_en: None | str | Unset = UNSET
    life_wide_learning_tc: None | str | Unset = UNSET
    school_mission_en: None | str | Unset = UNSET
    school_mission_tc: None | str | Unset = UNSET
    school_management_url: None | str | Unset = UNSET
    school_organisation_en: None | str | Unset = UNSET
    school_organisation_tc: None | str | Unset = UNSET
    imc_smc_mc_en: None | str | Unset = UNSET
    imc_smc_mc_tc: None | str | Unset = UNSET
    school_green_policy_en: None | str | Unset = UNSET
    school_green_policy_tc: None | str | Unset = UNSET
    school_major_concerns_url: None | str | Unset = UNSET
    school_major_concerns_en: None | str | Unset = UNSET
    school_major_concerns_tc: None | str | Unset = UNSET
    learning_and_teaching_plan_url: None | str | Unset = UNSET
    learning_and_teaching_strategies_en: None | str | Unset = UNSET
    learning_and_teaching_strategies_tc: None | str | Unset = UNSET
    major_renewed_emphases_pri_edu_curriculum_en: None | str | Unset = UNSET
    major_renewed_emphases_pri_edu_curriculum_tc: None | str | Unset = UNSET
    dev_of_generic_skills_en: None | str | Unset = UNSET
    dev_of_generic_skills_tc: None | str | Unset = UNSET
    cultivation_of_proper_values_attitudes_and_behaviours_en: None | str | Unset = UNSET
    cultivation_of_proper_values_attitudes_and_behaviours_tc: None | str | Unset = UNSET
    student_support_url: None | str | Unset = UNSET
    whole_school_approach_cater_for_learner_diversity_en: None | str | Unset = UNSET
    whole_school_approach_cater_for_learner_diversity_tc: None | str | Unset = UNSET
    whole_school_approach_integrated_education_en: None | str | Unset = UNSET
    whole_school_approach_integrated_education_tc: None | str | Unset = UNSET
    support_for_non_chinese_students_en: None | str | Unset = UNSET
    support_for_non_chinese_students_tc: None | str | Unset = UNSET
    curriculum_tailoring_and_adaptation_en: None | str | Unset = UNSET
    curriculum_tailoring_and_adaptation_tc: None | str | Unset = UNSET
    home_school_cooperation_url: None | str | Unset = UNSET
    home_school_cooperation_en: None | str | Unset = UNSET
    home_school_cooperation_tc: None | str | Unset = UNSET
    school_ethos_en: None | str | Unset = UNSET
    school_ethos_tc: None | str | Unset = UNSET
    future_dev_url: None | str | Unset = UNSET
    school_dev_plan_en: None | str | Unset = UNSET
    school_dev_plan_tc: None | str | Unset = UNSET
    teacher_pro_training_and_dev_en: None | str | Unset = UNSET
    teacher_pro_training_and_dev_tc: None | str | Unset = UNSET
    school_character_others_en: None | str | Unset = UNSET
    school_character_others_tc: None | str | Unset = UNSET
    fee_remission_en: None | str | Unset = UNSET
    fee_remission_tc: None | str | Unset = UNSET
    northing: None | str | Unset = UNSET
    easting: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature_member_owns: int | None | Unset
        if isinstance(self.feature_member_owns, Unset):
            feature_member_owns = UNSET
        else:
            feature_member_owns = self.feature_member_owns

        fid: None | str | Unset
        if isinstance(self.fid, Unset):
            fid = UNSET
        else:
            fid = self.fid

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

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

        school_address_en: None | str | Unset
        if isinstance(self.school_address_en, Unset):
            school_address_en = UNSET
        else:
            school_address_en = self.school_address_en

        school_address_tc: None | str | Unset
        if isinstance(self.school_address_tc, Unset):
            school_address_tc = UNSET
        else:
            school_address_tc = self.school_address_tc

        poa_school_net: None | str | Unset
        if isinstance(self.poa_school_net, Unset):
            poa_school_net = UNSET
        else:
            poa_school_net = self.poa_school_net

        school_tel: None | str | Unset
        if isinstance(self.school_tel, Unset):
            school_tel = UNSET
        else:
            school_tel = self.school_tel

        school_fax: None | str | Unset
        if isinstance(self.school_fax, Unset):
            school_fax = UNSET
        else:
            school_fax = self.school_fax

        school_email: None | str | Unset
        if isinstance(self.school_email, Unset):
            school_email = UNSET
        else:
            school_email = self.school_email

        school_website: None | str | Unset
        if isinstance(self.school_website, Unset):
            school_website = UNSET
        else:
            school_website = self.school_website

        school_type_1_en: None | str | Unset
        if isinstance(self.school_type_1_en, Unset):
            school_type_1_en = UNSET
        else:
            school_type_1_en = self.school_type_1_en

        school_type_1_tc: None | str | Unset
        if isinstance(self.school_type_1_tc, Unset):
            school_type_1_tc = UNSET
        else:
            school_type_1_tc = self.school_type_1_tc

        school_type_2_en: None | str | Unset
        if isinstance(self.school_type_2_en, Unset):
            school_type_2_en = UNSET
        else:
            school_type_2_en = self.school_type_2_en

        school_type_2_tc: None | str | Unset
        if isinstance(self.school_type_2_tc, Unset):
            school_type_2_tc = UNSET
        else:
            school_type_2_tc = self.school_type_2_tc

        imc_en: None | str | Unset
        if isinstance(self.imc_en, Unset):
            imc_en = UNSET
        else:
            imc_en = self.imc_en

        imc_tc: None | str | Unset
        if isinstance(self.imc_tc, Unset):
            imc_tc = UNSET
        else:
            imc_tc = self.imc_tc

        training_compliance_rate_supervisor_managers_smc_chair_members: (
            None | str | Unset
        )
        if isinstance(
            self.training_compliance_rate_supervisor_managers_smc_chair_members, Unset
        ):
            training_compliance_rate_supervisor_managers_smc_chair_members = UNSET
        else:
            training_compliance_rate_supervisor_managers_smc_chair_members = (
                self.training_compliance_rate_supervisor_managers_smc_chair_members
            )

        name_supervisor_chairman_of_mc_en: None | str | Unset
        if isinstance(self.name_supervisor_chairman_of_mc_en, Unset):
            name_supervisor_chairman_of_mc_en = UNSET
        else:
            name_supervisor_chairman_of_mc_en = self.name_supervisor_chairman_of_mc_en

        name_supervisor_chairman_of_mc_tc: None | str | Unset
        if isinstance(self.name_supervisor_chairman_of_mc_tc, Unset):
            name_supervisor_chairman_of_mc_tc = UNSET
        else:
            name_supervisor_chairman_of_mc_tc = self.name_supervisor_chairman_of_mc_tc

        title_supervisor_chairman_of_mc_en: None | str | Unset
        if isinstance(self.title_supervisor_chairman_of_mc_en, Unset):
            title_supervisor_chairman_of_mc_en = UNSET
        else:
            title_supervisor_chairman_of_mc_en = self.title_supervisor_chairman_of_mc_en

        title_supervisor_chairman_of_mc_tc: None | str | Unset
        if isinstance(self.title_supervisor_chairman_of_mc_tc, Unset):
            title_supervisor_chairman_of_mc_tc = UNSET
        else:
            title_supervisor_chairman_of_mc_tc = self.title_supervisor_chairman_of_mc_tc

        name_of_school_head_en: None | str | Unset
        if isinstance(self.name_of_school_head_en, Unset):
            name_of_school_head_en = UNSET
        else:
            name_of_school_head_en = self.name_of_school_head_en

        name_of_school_head_tc: None | str | Unset
        if isinstance(self.name_of_school_head_tc, Unset):
            name_of_school_head_tc = UNSET
        else:
            name_of_school_head_tc = self.name_of_school_head_tc

        title_of_school_head_en: None | str | Unset
        if isinstance(self.title_of_school_head_en, Unset):
            title_of_school_head_en = UNSET
        else:
            title_of_school_head_en = self.title_of_school_head_en

        title_of_school_head_tc: None | str | Unset
        if isinstance(self.title_of_school_head_tc, Unset):
            title_of_school_head_tc = UNSET
        else:
            title_of_school_head_tc = self.title_of_school_head_tc

        student_gender_en: None | str | Unset
        if isinstance(self.student_gender_en, Unset):
            student_gender_en = UNSET
        else:
            student_gender_en = self.student_gender_en

        student_gender_tc: None | str | Unset
        if isinstance(self.student_gender_tc, Unset):
            student_gender_tc = UNSET
        else:
            student_gender_tc = self.student_gender_tc

        sponsoring_body_en: None | str | Unset
        if isinstance(self.sponsoring_body_en, Unset):
            sponsoring_body_en = UNSET
        else:
            sponsoring_body_en = self.sponsoring_body_en

        sponsoring_body_tc: None | str | Unset
        if isinstance(self.sponsoring_body_tc, Unset):
            sponsoring_body_tc = UNSET
        else:
            sponsoring_body_tc = self.sponsoring_body_tc

        commencement_of_operation_year: None | str | Unset
        if isinstance(self.commencement_of_operation_year, Unset):
            commencement_of_operation_year = UNSET
        else:
            commencement_of_operation_year = self.commencement_of_operation_year

        religion_en: None | str | Unset
        if isinstance(self.religion_en, Unset):
            religion_en = UNSET
        else:
            religion_en = self.religion_en

        religion_tc: None | str | Unset
        if isinstance(self.religion_tc, Unset):
            religion_tc = UNSET
        else:
            religion_tc = self.religion_tc

        other_religion_en: None | str | Unset
        if isinstance(self.other_religion_en, Unset):
            other_religion_en = UNSET
        else:
            other_religion_en = self.other_religion_en

        other_religion_tc: None | str | Unset
        if isinstance(self.other_religion_tc, Unset):
            other_religion_tc = UNSET
        else:
            other_religion_tc = self.other_religion_tc

        school_motto_en: None | str | Unset
        if isinstance(self.school_motto_en, Unset):
            school_motto_en = UNSET
        else:
            school_motto_en = self.school_motto_en

        school_motto_tc: None | str | Unset
        if isinstance(self.school_motto_tc, Unset):
            school_motto_tc = UNSET
        else:
            school_motto_tc = self.school_motto_tc

        school_size: None | str | Unset
        if isinstance(self.school_size, Unset):
            school_size = UNSET
        else:
            school_size = self.school_size

        medium_of_instruction_en: None | str | Unset
        if isinstance(self.medium_of_instruction_en, Unset):
            medium_of_instruction_en = UNSET
        else:
            medium_of_instruction_en = self.medium_of_instruction_en

        medium_of_instruction_tc: None | str | Unset
        if isinstance(self.medium_of_instruction_tc, Unset):
            medium_of_instruction_tc = UNSET
        else:
            medium_of_instruction_tc = self.medium_of_instruction_tc

        through_train_sec_school_en: None | str | Unset
        if isinstance(self.through_train_sec_school_en, Unset):
            through_train_sec_school_en = UNSET
        else:
            through_train_sec_school_en = self.through_train_sec_school_en

        through_train_sec_school_tc: None | str | Unset
        if isinstance(self.through_train_sec_school_tc, Unset):
            through_train_sec_school_tc = UNSET
        else:
            through_train_sec_school_tc = self.through_train_sec_school_tc

        feeder_sec_school_en: None | str | Unset
        if isinstance(self.feeder_sec_school_en, Unset):
            feeder_sec_school_en = UNSET
        else:
            feeder_sec_school_en = self.feeder_sec_school_en

        feeder_sec_school_tc: None | str | Unset
        if isinstance(self.feeder_sec_school_tc, Unset):
            feeder_sec_school_tc = UNSET
        else:
            feeder_sec_school_tc = self.feeder_sec_school_tc

        nominated_sec_school_en: None | str | Unset
        if isinstance(self.nominated_sec_school_en, Unset):
            nominated_sec_school_en = UNSET
        else:
            nominated_sec_school_en = self.nominated_sec_school_en

        nominated_sec_school_tc: None | str | Unset
        if isinstance(self.nominated_sec_school_tc, Unset):
            nominated_sec_school_tc = UNSET
        else:
            nominated_sec_school_tc = self.nominated_sec_school_tc

        school_bus_en: None | str | Unset
        if isinstance(self.school_bus_en, Unset):
            school_bus_en = UNSET
        else:
            school_bus_en = self.school_bus_en

        school_bus_tc: None | str | Unset
        if isinstance(self.school_bus_tc, Unset):
            school_bus_tc = UNSET
        else:
            school_bus_tc = self.school_bus_tc

        nanny_van_en: None | str | Unset
        if isinstance(self.nanny_van_en, Unset):
            nanny_van_en = UNSET
        else:
            nanny_van_en = self.nanny_van_en

        nanny_van_tc: None | str | Unset
        if isinstance(self.nanny_van_tc, Unset):
            nanny_van_tc = UNSET
        else:
            nanny_van_tc = self.nanny_van_tc

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

        school_alumni_association_en: None | str | Unset
        if isinstance(self.school_alumni_association_en, Unset):
            school_alumni_association_en = UNSET
        else:
            school_alumni_association_en = self.school_alumni_association_en

        school_alumni_association_tc: None | str | Unset
        if isinstance(self.school_alumni_association_tc, Unset):
            school_alumni_association_tc = UNSET
        else:
            school_alumni_association_tc = self.school_alumni_association_tc

        four_rs_mental_health_charter: None | str | Unset
        if isinstance(self.four_rs_mental_health_charter, Unset):
            four_rs_mental_health_charter = UNSET
        else:
            four_rs_mental_health_charter = self.four_rs_mental_health_charter

        whole_school_health_programme: None | str | Unset
        if isinstance(self.whole_school_health_programme, Unset):
            whole_school_health_programme = UNSET
        else:
            whole_school_health_programme = self.whole_school_health_programme

        asc_school_fee_en: None | str | Unset
        if isinstance(self.asc_school_fee_en, Unset):
            asc_school_fee_en = UNSET
        else:
            asc_school_fee_en = self.asc_school_fee_en

        asc_school_fee_tc: None | str | Unset
        if isinstance(self.asc_school_fee_tc, Unset):
            asc_school_fee_tc = UNSET
        else:
            asc_school_fee_tc = self.asc_school_fee_tc

        asc_tong_fai: None | str | Unset
        if isinstance(self.asc_tong_fai, Unset):
            asc_tong_fai = UNSET
        else:
            asc_tong_fai = self.asc_tong_fai

        asc_pta_fee_en: None | str | Unset
        if isinstance(self.asc_pta_fee_en, Unset):
            asc_pta_fee_en = UNSET
        else:
            asc_pta_fee_en = self.asc_pta_fee_en

        asc_pta_fee_tc: None | str | Unset
        if isinstance(self.asc_pta_fee_tc, Unset):
            asc_pta_fee_tc = UNSET
        else:
            asc_pta_fee_tc = self.asc_pta_fee_tc

        asc_charges_for_non_standard_items_en: None | str | Unset
        if isinstance(self.asc_charges_for_non_standard_items_en, Unset):
            asc_charges_for_non_standard_items_en = UNSET
        else:
            asc_charges_for_non_standard_items_en = (
                self.asc_charges_for_non_standard_items_en
            )

        asc_charges_for_non_standard_items_tc: None | str | Unset
        if isinstance(self.asc_charges_for_non_standard_items_tc, Unset):
            asc_charges_for_non_standard_items_tc = UNSET
        else:
            asc_charges_for_non_standard_items_tc = (
                self.asc_charges_for_non_standard_items_tc
            )

        asc_others_en: None | str | Unset
        if isinstance(self.asc_others_en, Unset):
            asc_others_en = UNSET
        else:
            asc_others_en = self.asc_others_en

        asc_others_tc: None | str | Unset
        if isinstance(self.asc_others_tc, Unset):
            asc_others_tc = UNSET
        else:
            asc_others_tc = self.asc_others_tc

        fac_no_of_classroom: None | str | Unset
        if isinstance(self.fac_no_of_classroom, Unset):
            fac_no_of_classroom = UNSET
        else:
            fac_no_of_classroom = self.fac_no_of_classroom

        fac_no_of_school_hall: None | str | Unset
        if isinstance(self.fac_no_of_school_hall, Unset):
            fac_no_of_school_hall = UNSET
        else:
            fac_no_of_school_hall = self.fac_no_of_school_hall

        fac_no_of_playground: None | str | Unset
        if isinstance(self.fac_no_of_playground, Unset):
            fac_no_of_playground = UNSET
        else:
            fac_no_of_playground = self.fac_no_of_playground

        fac_no_of_library: None | str | Unset
        if isinstance(self.fac_no_of_library, Unset):
            fac_no_of_library = UNSET
        else:
            fac_no_of_library = self.fac_no_of_library

        fac_special_rooms_en: None | str | Unset
        if isinstance(self.fac_special_rooms_en, Unset):
            fac_special_rooms_en = UNSET
        else:
            fac_special_rooms_en = self.fac_special_rooms_en

        fac_special_rooms_tc: None | str | Unset
        if isinstance(self.fac_special_rooms_tc, Unset):
            fac_special_rooms_tc = UNSET
        else:
            fac_special_rooms_tc = self.fac_special_rooms_tc

        fac_others_en: None | str | Unset
        if isinstance(self.fac_others_en, Unset):
            fac_others_en = UNSET
        else:
            fac_others_en = self.fac_others_en

        fac_others_tc: None | str | Unset
        if isinstance(self.fac_others_tc, Unset):
            fac_others_tc = UNSET
        else:
            fac_others_tc = self.fac_others_tc

        fac_support_for_specialedu_en: None | str | Unset
        if isinstance(self.fac_support_for_specialedu_en, Unset):
            fac_support_for_specialedu_en = UNSET
        else:
            fac_support_for_specialedu_en = self.fac_support_for_specialedu_en

        fac_support_for_specialedu_tc: None | str | Unset
        if isinstance(self.fac_support_for_specialedu_tc, Unset):
            fac_support_for_specialedu_tc = UNSET
        else:
            fac_support_for_specialedu_tc = self.fac_support_for_specialedu_tc

        previous_year_tsi_no_of_approved_teaching_posts: None | str | Unset
        if isinstance(self.previous_year_tsi_no_of_approved_teaching_posts, Unset):
            previous_year_tsi_no_of_approved_teaching_posts = UNSET
        else:
            previous_year_tsi_no_of_approved_teaching_posts = (
                self.previous_year_tsi_no_of_approved_teaching_posts
            )

        previous_year_tsi_total_no_of_teachers: None | str | Unset
        if isinstance(self.previous_year_tsi_total_no_of_teachers, Unset):
            previous_year_tsi_total_no_of_teachers = UNSET
        else:
            previous_year_tsi_total_no_of_teachers = (
                self.previous_year_tsi_total_no_of_teachers
            )

        previous_year_tsi_percent_of_received_teacher_training: None | str | Unset
        if isinstance(
            self.previous_year_tsi_percent_of_received_teacher_training, Unset
        ):
            previous_year_tsi_percent_of_received_teacher_training = UNSET
        else:
            previous_year_tsi_percent_of_received_teacher_training = (
                self.previous_year_tsi_percent_of_received_teacher_training
            )

        previous_year_tsi_percent_of_bacherlor: None | str | Unset
        if isinstance(self.previous_year_tsi_percent_of_bacherlor, Unset):
            previous_year_tsi_percent_of_bacherlor = UNSET
        else:
            previous_year_tsi_percent_of_bacherlor = (
                self.previous_year_tsi_percent_of_bacherlor
            )

        previous_year_tsi_percent_of_master_doctorate_or_above: None | str | Unset
        if isinstance(
            self.previous_year_tsi_percent_of_master_doctorate_or_above, Unset
        ):
            previous_year_tsi_percent_of_master_doctorate_or_above = UNSET
        else:
            previous_year_tsi_percent_of_master_doctorate_or_above = (
                self.previous_year_tsi_percent_of_master_doctorate_or_above
            )

        previous_year_tsi_percent_of_special_edu_training: None | str | Unset
        if isinstance(self.previous_year_tsi_percent_of_special_edu_training, Unset):
            previous_year_tsi_percent_of_special_edu_training = UNSET
        else:
            previous_year_tsi_percent_of_special_edu_training = (
                self.previous_year_tsi_percent_of_special_edu_training
            )

        previous_year_tsi_percent_of_exp_0_4: None | str | Unset
        if isinstance(self.previous_year_tsi_percent_of_exp_0_4, Unset):
            previous_year_tsi_percent_of_exp_0_4 = UNSET
        else:
            previous_year_tsi_percent_of_exp_0_4 = (
                self.previous_year_tsi_percent_of_exp_0_4
            )

        previous_year_tsi_percent_of_exp_5_9: None | str | Unset
        if isinstance(self.previous_year_tsi_percent_of_exp_5_9, Unset):
            previous_year_tsi_percent_of_exp_5_9 = UNSET
        else:
            previous_year_tsi_percent_of_exp_5_9 = (
                self.previous_year_tsi_percent_of_exp_5_9
            )

        previous_year_tsi_percent_of_exp_10_or_above: None | str | Unset
        if isinstance(self.previous_year_tsi_percent_of_exp_10_or_above, Unset):
            previous_year_tsi_percent_of_exp_10_or_above = UNSET
        else:
            previous_year_tsi_percent_of_exp_10_or_above = (
                self.previous_year_tsi_percent_of_exp_10_or_above
            )

        previous_year_no_of_class_p1: None | str | Unset
        if isinstance(self.previous_year_no_of_class_p1, Unset):
            previous_year_no_of_class_p1 = UNSET
        else:
            previous_year_no_of_class_p1 = self.previous_year_no_of_class_p1

        previous_year_no_of_class_p2: None | str | Unset
        if isinstance(self.previous_year_no_of_class_p2, Unset):
            previous_year_no_of_class_p2 = UNSET
        else:
            previous_year_no_of_class_p2 = self.previous_year_no_of_class_p2

        previous_year_no_of_class_p3: None | str | Unset
        if isinstance(self.previous_year_no_of_class_p3, Unset):
            previous_year_no_of_class_p3 = UNSET
        else:
            previous_year_no_of_class_p3 = self.previous_year_no_of_class_p3

        previous_year_no_of_class_p4: None | str | Unset
        if isinstance(self.previous_year_no_of_class_p4, Unset):
            previous_year_no_of_class_p4 = UNSET
        else:
            previous_year_no_of_class_p4 = self.previous_year_no_of_class_p4

        previous_year_no_of_class_p5: None | str | Unset
        if isinstance(self.previous_year_no_of_class_p5, Unset):
            previous_year_no_of_class_p5 = UNSET
        else:
            previous_year_no_of_class_p5 = self.previous_year_no_of_class_p5

        previous_year_no_of_class_p6: None | str | Unset
        if isinstance(self.previous_year_no_of_class_p6, Unset):
            previous_year_no_of_class_p6 = UNSET
        else:
            previous_year_no_of_class_p6 = self.previous_year_no_of_class_p6

        previous_year_no_of_class_total: None | str | Unset
        if isinstance(self.previous_year_no_of_class_total, Unset):
            previous_year_no_of_class_total = UNSET
        else:
            previous_year_no_of_class_total = self.previous_year_no_of_class_total

        current_year_no_of_class_p1: None | str | Unset
        if isinstance(self.current_year_no_of_class_p1, Unset):
            current_year_no_of_class_p1 = UNSET
        else:
            current_year_no_of_class_p1 = self.current_year_no_of_class_p1

        current_year_no_of_class_p2: None | str | Unset
        if isinstance(self.current_year_no_of_class_p2, Unset):
            current_year_no_of_class_p2 = UNSET
        else:
            current_year_no_of_class_p2 = self.current_year_no_of_class_p2

        current_year_no_of_class_p3: None | str | Unset
        if isinstance(self.current_year_no_of_class_p3, Unset):
            current_year_no_of_class_p3 = UNSET
        else:
            current_year_no_of_class_p3 = self.current_year_no_of_class_p3

        current_year_no_of_class_p4: None | str | Unset
        if isinstance(self.current_year_no_of_class_p4, Unset):
            current_year_no_of_class_p4 = UNSET
        else:
            current_year_no_of_class_p4 = self.current_year_no_of_class_p4

        current_year_no_of_class_p5: None | str | Unset
        if isinstance(self.current_year_no_of_class_p5, Unset):
            current_year_no_of_class_p5 = UNSET
        else:
            current_year_no_of_class_p5 = self.current_year_no_of_class_p5

        current_year_no_of_class_p6: None | str | Unset
        if isinstance(self.current_year_no_of_class_p6, Unset):
            current_year_no_of_class_p6 = UNSET
        else:
            current_year_no_of_class_p6 = self.current_year_no_of_class_p6

        current_year_no_of_class_total: None | str | Unset
        if isinstance(self.current_year_no_of_class_total, Unset):
            current_year_no_of_class_total = UNSET
        else:
            current_year_no_of_class_total = self.current_year_no_of_class_total

        cs_mode_of_teaching_en: None | str | Unset
        if isinstance(self.cs_mode_of_teaching_en, Unset):
            cs_mode_of_teaching_en = UNSET
        else:
            cs_mode_of_teaching_en = self.cs_mode_of_teaching_en

        cs_mode_of_teaching_tc: None | str | Unset
        if isinstance(self.cs_mode_of_teaching_tc, Unset):
            cs_mode_of_teaching_tc = UNSET
        else:
            cs_mode_of_teaching_tc = self.cs_mode_of_teaching_tc

        cs_remarks_en: None | str | Unset
        if isinstance(self.cs_remarks_en, Unset):
            cs_remarks_en = UNSET
        else:
            cs_remarks_en = self.cs_remarks_en

        cs_remarks_tc: None | str | Unset
        if isinstance(self.cs_remarks_tc, Unset):
            cs_remarks_tc = UNSET
        else:
            cs_remarks_tc = self.cs_remarks_tc

        no_of_test_per_year_p1: None | str | Unset
        if isinstance(self.no_of_test_per_year_p1, Unset):
            no_of_test_per_year_p1 = UNSET
        else:
            no_of_test_per_year_p1 = self.no_of_test_per_year_p1

        no_of_exam_per_year_p1: None | str | Unset
        if isinstance(self.no_of_exam_per_year_p1, Unset):
            no_of_exam_per_year_p1 = UNSET
        else:
            no_of_exam_per_year_p1 = self.no_of_exam_per_year_p1

        replace_test_exam_p1_en: None | str | Unset
        if isinstance(self.replace_test_exam_p1_en, Unset):
            replace_test_exam_p1_en = UNSET
        else:
            replace_test_exam_p1_en = self.replace_test_exam_p1_en

        replace_test_exam_p1_tc: None | str | Unset
        if isinstance(self.replace_test_exam_p1_tc, Unset):
            replace_test_exam_p1_tc = UNSET
        else:
            replace_test_exam_p1_tc = self.replace_test_exam_p1_tc

        no_of_test_per_year_p2_p6: None | str | Unset
        if isinstance(self.no_of_test_per_year_p2_p6, Unset):
            no_of_test_per_year_p2_p6 = UNSET
        else:
            no_of_test_per_year_p2_p6 = self.no_of_test_per_year_p2_p6

        no_of_exam_p2_p6: None | str | Unset
        if isinstance(self.no_of_exam_p2_p6, Unset):
            no_of_exam_p2_p6 = UNSET
        else:
            no_of_exam_p2_p6 = self.no_of_exam_p2_p6

        fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_en: (
            None | str | Unset
        )
        if isinstance(
            self.fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_en, Unset
        ):
            fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_en = UNSET
        else:
            fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_en = (
                self.fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_en
            )

        fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_tc: (
            None | str | Unset
        )
        if isinstance(
            self.fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_tc, Unset
        ):
            fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_tc = UNSET
        else:
            fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_tc = (
                self.fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_tc
            )

        upload_school_assessment_policy_to_school_web_en: None | str | Unset
        if isinstance(self.upload_school_assessment_policy_to_school_web_en, Unset):
            upload_school_assessment_policy_to_school_web_en = UNSET
        else:
            upload_school_assessment_policy_to_school_web_en = (
                self.upload_school_assessment_policy_to_school_web_en
            )

        upload_school_assessment_policy_to_school_web_tc: None | str | Unset
        if isinstance(self.upload_school_assessment_policy_to_school_web_tc, Unset):
            upload_school_assessment_policy_to_school_web_tc = UNSET
        else:
            upload_school_assessment_policy_to_school_web_tc = (
                self.upload_school_assessment_policy_to_school_web_tc
            )

        upload_school_assignment_policy_to_school_web_en: None | str | Unset
        if isinstance(self.upload_school_assignment_policy_to_school_web_en, Unset):
            upload_school_assignment_policy_to_school_web_en = UNSET
        else:
            upload_school_assignment_policy_to_school_web_en = (
                self.upload_school_assignment_policy_to_school_web_en
            )

        upload_school_assignment_policy_to_school_web_tc: None | str | Unset
        if isinstance(self.upload_school_assignment_policy_to_school_web_tc, Unset):
            upload_school_assignment_policy_to_school_web_tc = UNSET
        else:
            upload_school_assignment_policy_to_school_web_tc = (
                self.upload_school_assignment_policy_to_school_web_tc
            )

        diversified_assessment_en: None | str | Unset
        if isinstance(self.diversified_assessment_en, Unset):
            diversified_assessment_en = UNSET
        else:
            diversified_assessment_en = self.diversified_assessment_en

        diversified_assessment_tc: None | str | Unset
        if isinstance(self.diversified_assessment_tc, Unset):
            diversified_assessment_tc = UNSET
        else:
            diversified_assessment_tc = self.diversified_assessment_tc

        avoid_test_exam_after_long_holidays_en: None | str | Unset
        if isinstance(self.avoid_test_exam_after_long_holidays_en, Unset):
            avoid_test_exam_after_long_holidays_en = UNSET
        else:
            avoid_test_exam_after_long_holidays_en = (
                self.avoid_test_exam_after_long_holidays_en
            )

        avoid_test_exam_after_long_holidays_tc: None | str | Unset
        if isinstance(self.avoid_test_exam_after_long_holidays_tc, Unset):
            avoid_test_exam_after_long_holidays_tc = UNSET
        else:
            avoid_test_exam_after_long_holidays_tc = (
                self.avoid_test_exam_after_long_holidays_tc
            )

        arrange_timetable_flexibly_tutorial_session_in_afternoon_en: None | str | Unset
        if isinstance(
            self.arrange_timetable_flexibly_tutorial_session_in_afternoon_en, Unset
        ):
            arrange_timetable_flexibly_tutorial_session_in_afternoon_en = UNSET
        else:
            arrange_timetable_flexibly_tutorial_session_in_afternoon_en = (
                self.arrange_timetable_flexibly_tutorial_session_in_afternoon_en
            )

        arrange_timetable_flexibly_tutorial_session_in_afternoon_tc: None | str | Unset
        if isinstance(
            self.arrange_timetable_flexibly_tutorial_session_in_afternoon_tc, Unset
        ):
            arrange_timetable_flexibly_tutorial_session_in_afternoon_tc = UNSET
        else:
            arrange_timetable_flexibly_tutorial_session_in_afternoon_tc = (
                self.arrange_timetable_flexibly_tutorial_session_in_afternoon_tc
            )

        streaming_arrangement_en: None | str | Unset
        if isinstance(self.streaming_arrangement_en, Unset):
            streaming_arrangement_en = UNSET
        else:
            streaming_arrangement_en = self.streaming_arrangement_en

        streaming_arrangement_tc: None | str | Unset
        if isinstance(self.streaming_arrangement_tc, Unset):
            streaming_arrangement_tc = UNSET
        else:
            streaming_arrangement_tc = self.streaming_arrangement_tc

        no_of_school_days_per_week: None | str | Unset
        if isinstance(self.no_of_school_days_per_week, Unset):
            no_of_school_days_per_week = UNSET
        else:
            no_of_school_days_per_week = self.no_of_school_days_per_week

        no_of_periods_per_day: None | str | Unset
        if isinstance(self.no_of_periods_per_day, Unset):
            no_of_periods_per_day = UNSET
        else:
            no_of_periods_per_day = self.no_of_periods_per_day

        duration_of_each_period: None | str | Unset
        if isinstance(self.duration_of_each_period, Unset):
            duration_of_each_period = UNSET
        else:
            duration_of_each_period = self.duration_of_each_period

        school_starts_at: None | str | Unset
        if isinstance(self.school_starts_at, Unset):
            school_starts_at = UNSET
        else:
            school_starts_at = self.school_starts_at

        school_starts_at_ampm_en: None | str | Unset
        if isinstance(self.school_starts_at_ampm_en, Unset):
            school_starts_at_ampm_en = UNSET
        else:
            school_starts_at_ampm_en = self.school_starts_at_ampm_en

        school_starts_at_ampm_tc: None | str | Unset
        if isinstance(self.school_starts_at_ampm_tc, Unset):
            school_starts_at_ampm_tc = UNSET
        else:
            school_starts_at_ampm_tc = self.school_starts_at_ampm_tc

        school_ends_at: None | str | Unset
        if isinstance(self.school_ends_at, Unset):
            school_ends_at = UNSET
        else:
            school_ends_at = self.school_ends_at

        school_ends_at_ampm_en: None | str | Unset
        if isinstance(self.school_ends_at_ampm_en, Unset):
            school_ends_at_ampm_en = UNSET
        else:
            school_ends_at_ampm_en = self.school_ends_at_ampm_en

        school_ends_at_ampm_tc: None | str | Unset
        if isinstance(self.school_ends_at_ampm_tc, Unset):
            school_ends_at_ampm_tc = UNSET
        else:
            school_ends_at_ampm_tc = self.school_ends_at_ampm_tc

        lunch_start_time: None | str | Unset
        if isinstance(self.lunch_start_time, Unset):
            lunch_start_time = UNSET
        else:
            lunch_start_time = self.lunch_start_time

        lunch_end_time: None | str | Unset
        if isinstance(self.lunch_end_time, Unset):
            lunch_end_time = UNSET
        else:
            lunch_end_time = self.lunch_end_time

        lunch_arrangement_en: None | str | Unset
        if isinstance(self.lunch_arrangement_en, Unset):
            lunch_arrangement_en = UNSET
        else:
            lunch_arrangement_en = self.lunch_arrangement_en

        lunch_arrangement_tc: None | str | Unset
        if isinstance(self.lunch_arrangement_tc, Unset):
            lunch_arrangement_tc = UNSET
        else:
            lunch_arrangement_tc = self.lunch_arrangement_tc

        healthy_school_life_en: None | str | Unset
        if isinstance(self.healthy_school_life_en, Unset):
            healthy_school_life_en = UNSET
        else:
            healthy_school_life_en = self.healthy_school_life_en

        healthy_school_life_tc: None | str | Unset
        if isinstance(self.healthy_school_life_tc, Unset):
            healthy_school_life_tc = UNSET
        else:
            healthy_school_life_tc = self.healthy_school_life_tc

        school_life_remarks_en: None | str | Unset
        if isinstance(self.school_life_remarks_en, Unset):
            school_life_remarks_en = UNSET
        else:
            school_life_remarks_en = self.school_life_remarks_en

        school_life_remarks_tc: None | str | Unset
        if isinstance(self.school_life_remarks_tc, Unset):
            school_life_remarks_tc = UNSET
        else:
            school_life_remarks_tc = self.school_life_remarks_tc

        life_wide_learning_en: None | str | Unset
        if isinstance(self.life_wide_learning_en, Unset):
            life_wide_learning_en = UNSET
        else:
            life_wide_learning_en = self.life_wide_learning_en

        life_wide_learning_tc: None | str | Unset
        if isinstance(self.life_wide_learning_tc, Unset):
            life_wide_learning_tc = UNSET
        else:
            life_wide_learning_tc = self.life_wide_learning_tc

        school_mission_en: None | str | Unset
        if isinstance(self.school_mission_en, Unset):
            school_mission_en = UNSET
        else:
            school_mission_en = self.school_mission_en

        school_mission_tc: None | str | Unset
        if isinstance(self.school_mission_tc, Unset):
            school_mission_tc = UNSET
        else:
            school_mission_tc = self.school_mission_tc

        school_management_url: None | str | Unset
        if isinstance(self.school_management_url, Unset):
            school_management_url = UNSET
        else:
            school_management_url = self.school_management_url

        school_organisation_en: None | str | Unset
        if isinstance(self.school_organisation_en, Unset):
            school_organisation_en = UNSET
        else:
            school_organisation_en = self.school_organisation_en

        school_organisation_tc: None | str | Unset
        if isinstance(self.school_organisation_tc, Unset):
            school_organisation_tc = UNSET
        else:
            school_organisation_tc = self.school_organisation_tc

        imc_smc_mc_en: None | str | Unset
        if isinstance(self.imc_smc_mc_en, Unset):
            imc_smc_mc_en = UNSET
        else:
            imc_smc_mc_en = self.imc_smc_mc_en

        imc_smc_mc_tc: None | str | Unset
        if isinstance(self.imc_smc_mc_tc, Unset):
            imc_smc_mc_tc = UNSET
        else:
            imc_smc_mc_tc = self.imc_smc_mc_tc

        school_green_policy_en: None | str | Unset
        if isinstance(self.school_green_policy_en, Unset):
            school_green_policy_en = UNSET
        else:
            school_green_policy_en = self.school_green_policy_en

        school_green_policy_tc: None | str | Unset
        if isinstance(self.school_green_policy_tc, Unset):
            school_green_policy_tc = UNSET
        else:
            school_green_policy_tc = self.school_green_policy_tc

        school_major_concerns_url: None | str | Unset
        if isinstance(self.school_major_concerns_url, Unset):
            school_major_concerns_url = UNSET
        else:
            school_major_concerns_url = self.school_major_concerns_url

        school_major_concerns_en: None | str | Unset
        if isinstance(self.school_major_concerns_en, Unset):
            school_major_concerns_en = UNSET
        else:
            school_major_concerns_en = self.school_major_concerns_en

        school_major_concerns_tc: None | str | Unset
        if isinstance(self.school_major_concerns_tc, Unset):
            school_major_concerns_tc = UNSET
        else:
            school_major_concerns_tc = self.school_major_concerns_tc

        learning_and_teaching_plan_url: None | str | Unset
        if isinstance(self.learning_and_teaching_plan_url, Unset):
            learning_and_teaching_plan_url = UNSET
        else:
            learning_and_teaching_plan_url = self.learning_and_teaching_plan_url

        learning_and_teaching_strategies_en: None | str | Unset
        if isinstance(self.learning_and_teaching_strategies_en, Unset):
            learning_and_teaching_strategies_en = UNSET
        else:
            learning_and_teaching_strategies_en = (
                self.learning_and_teaching_strategies_en
            )

        learning_and_teaching_strategies_tc: None | str | Unset
        if isinstance(self.learning_and_teaching_strategies_tc, Unset):
            learning_and_teaching_strategies_tc = UNSET
        else:
            learning_and_teaching_strategies_tc = (
                self.learning_and_teaching_strategies_tc
            )

        major_renewed_emphases_pri_edu_curriculum_en: None | str | Unset
        if isinstance(self.major_renewed_emphases_pri_edu_curriculum_en, Unset):
            major_renewed_emphases_pri_edu_curriculum_en = UNSET
        else:
            major_renewed_emphases_pri_edu_curriculum_en = (
                self.major_renewed_emphases_pri_edu_curriculum_en
            )

        major_renewed_emphases_pri_edu_curriculum_tc: None | str | Unset
        if isinstance(self.major_renewed_emphases_pri_edu_curriculum_tc, Unset):
            major_renewed_emphases_pri_edu_curriculum_tc = UNSET
        else:
            major_renewed_emphases_pri_edu_curriculum_tc = (
                self.major_renewed_emphases_pri_edu_curriculum_tc
            )

        dev_of_generic_skills_en: None | str | Unset
        if isinstance(self.dev_of_generic_skills_en, Unset):
            dev_of_generic_skills_en = UNSET
        else:
            dev_of_generic_skills_en = self.dev_of_generic_skills_en

        dev_of_generic_skills_tc: None | str | Unset
        if isinstance(self.dev_of_generic_skills_tc, Unset):
            dev_of_generic_skills_tc = UNSET
        else:
            dev_of_generic_skills_tc = self.dev_of_generic_skills_tc

        cultivation_of_proper_values_attitudes_and_behaviours_en: None | str | Unset
        if isinstance(
            self.cultivation_of_proper_values_attitudes_and_behaviours_en, Unset
        ):
            cultivation_of_proper_values_attitudes_and_behaviours_en = UNSET
        else:
            cultivation_of_proper_values_attitudes_and_behaviours_en = (
                self.cultivation_of_proper_values_attitudes_and_behaviours_en
            )

        cultivation_of_proper_values_attitudes_and_behaviours_tc: None | str | Unset
        if isinstance(
            self.cultivation_of_proper_values_attitudes_and_behaviours_tc, Unset
        ):
            cultivation_of_proper_values_attitudes_and_behaviours_tc = UNSET
        else:
            cultivation_of_proper_values_attitudes_and_behaviours_tc = (
                self.cultivation_of_proper_values_attitudes_and_behaviours_tc
            )

        student_support_url: None | str | Unset
        if isinstance(self.student_support_url, Unset):
            student_support_url = UNSET
        else:
            student_support_url = self.student_support_url

        whole_school_approach_cater_for_learner_diversity_en: None | str | Unset
        if isinstance(self.whole_school_approach_cater_for_learner_diversity_en, Unset):
            whole_school_approach_cater_for_learner_diversity_en = UNSET
        else:
            whole_school_approach_cater_for_learner_diversity_en = (
                self.whole_school_approach_cater_for_learner_diversity_en
            )

        whole_school_approach_cater_for_learner_diversity_tc: None | str | Unset
        if isinstance(self.whole_school_approach_cater_for_learner_diversity_tc, Unset):
            whole_school_approach_cater_for_learner_diversity_tc = UNSET
        else:
            whole_school_approach_cater_for_learner_diversity_tc = (
                self.whole_school_approach_cater_for_learner_diversity_tc
            )

        whole_school_approach_integrated_education_en: None | str | Unset
        if isinstance(self.whole_school_approach_integrated_education_en, Unset):
            whole_school_approach_integrated_education_en = UNSET
        else:
            whole_school_approach_integrated_education_en = (
                self.whole_school_approach_integrated_education_en
            )

        whole_school_approach_integrated_education_tc: None | str | Unset
        if isinstance(self.whole_school_approach_integrated_education_tc, Unset):
            whole_school_approach_integrated_education_tc = UNSET
        else:
            whole_school_approach_integrated_education_tc = (
                self.whole_school_approach_integrated_education_tc
            )

        support_for_non_chinese_students_en: None | str | Unset
        if isinstance(self.support_for_non_chinese_students_en, Unset):
            support_for_non_chinese_students_en = UNSET
        else:
            support_for_non_chinese_students_en = (
                self.support_for_non_chinese_students_en
            )

        support_for_non_chinese_students_tc: None | str | Unset
        if isinstance(self.support_for_non_chinese_students_tc, Unset):
            support_for_non_chinese_students_tc = UNSET
        else:
            support_for_non_chinese_students_tc = (
                self.support_for_non_chinese_students_tc
            )

        curriculum_tailoring_and_adaptation_en: None | str | Unset
        if isinstance(self.curriculum_tailoring_and_adaptation_en, Unset):
            curriculum_tailoring_and_adaptation_en = UNSET
        else:
            curriculum_tailoring_and_adaptation_en = (
                self.curriculum_tailoring_and_adaptation_en
            )

        curriculum_tailoring_and_adaptation_tc: None | str | Unset
        if isinstance(self.curriculum_tailoring_and_adaptation_tc, Unset):
            curriculum_tailoring_and_adaptation_tc = UNSET
        else:
            curriculum_tailoring_and_adaptation_tc = (
                self.curriculum_tailoring_and_adaptation_tc
            )

        home_school_cooperation_url: None | str | Unset
        if isinstance(self.home_school_cooperation_url, Unset):
            home_school_cooperation_url = UNSET
        else:
            home_school_cooperation_url = self.home_school_cooperation_url

        home_school_cooperation_en: None | str | Unset
        if isinstance(self.home_school_cooperation_en, Unset):
            home_school_cooperation_en = UNSET
        else:
            home_school_cooperation_en = self.home_school_cooperation_en

        home_school_cooperation_tc: None | str | Unset
        if isinstance(self.home_school_cooperation_tc, Unset):
            home_school_cooperation_tc = UNSET
        else:
            home_school_cooperation_tc = self.home_school_cooperation_tc

        school_ethos_en: None | str | Unset
        if isinstance(self.school_ethos_en, Unset):
            school_ethos_en = UNSET
        else:
            school_ethos_en = self.school_ethos_en

        school_ethos_tc: None | str | Unset
        if isinstance(self.school_ethos_tc, Unset):
            school_ethos_tc = UNSET
        else:
            school_ethos_tc = self.school_ethos_tc

        future_dev_url: None | str | Unset
        if isinstance(self.future_dev_url, Unset):
            future_dev_url = UNSET
        else:
            future_dev_url = self.future_dev_url

        school_dev_plan_en: None | str | Unset
        if isinstance(self.school_dev_plan_en, Unset):
            school_dev_plan_en = UNSET
        else:
            school_dev_plan_en = self.school_dev_plan_en

        school_dev_plan_tc: None | str | Unset
        if isinstance(self.school_dev_plan_tc, Unset):
            school_dev_plan_tc = UNSET
        else:
            school_dev_plan_tc = self.school_dev_plan_tc

        teacher_pro_training_and_dev_en: None | str | Unset
        if isinstance(self.teacher_pro_training_and_dev_en, Unset):
            teacher_pro_training_and_dev_en = UNSET
        else:
            teacher_pro_training_and_dev_en = self.teacher_pro_training_and_dev_en

        teacher_pro_training_and_dev_tc: None | str | Unset
        if isinstance(self.teacher_pro_training_and_dev_tc, Unset):
            teacher_pro_training_and_dev_tc = UNSET
        else:
            teacher_pro_training_and_dev_tc = self.teacher_pro_training_and_dev_tc

        school_character_others_en: None | str | Unset
        if isinstance(self.school_character_others_en, Unset):
            school_character_others_en = UNSET
        else:
            school_character_others_en = self.school_character_others_en

        school_character_others_tc: None | str | Unset
        if isinstance(self.school_character_others_tc, Unset):
            school_character_others_tc = UNSET
        else:
            school_character_others_tc = self.school_character_others_tc

        fee_remission_en: None | str | Unset
        if isinstance(self.fee_remission_en, Unset):
            fee_remission_en = UNSET
        else:
            fee_remission_en = self.fee_remission_en

        fee_remission_tc: None | str | Unset
        if isinstance(self.fee_remission_tc, Unset):
            fee_remission_tc = UNSET
        else:
            fee_remission_tc = self.fee_remission_tc

        northing: None | str | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        easting: None | str | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if feature_member_owns is not UNSET:
            field_dict["featureMember___owns"] = feature_member_owns
        if fid is not UNSET:
            field_dict["fid"] = fid
        if id is not UNSET:
            field_dict["id"] = id
        if district_en is not UNSET:
            field_dict["district_en"] = district_en
        if district_tc is not UNSET:
            field_dict["district_tc"] = district_tc
        if school_name_en is not UNSET:
            field_dict["school_name_en"] = school_name_en
        if school_name_tc is not UNSET:
            field_dict["school_name_tc"] = school_name_tc
        if school_address_en is not UNSET:
            field_dict["school_address_en"] = school_address_en
        if school_address_tc is not UNSET:
            field_dict["school_address_tc"] = school_address_tc
        if poa_school_net is not UNSET:
            field_dict["poa_school_net"] = poa_school_net
        if school_tel is not UNSET:
            field_dict["school_tel"] = school_tel
        if school_fax is not UNSET:
            field_dict["school_fax"] = school_fax
        if school_email is not UNSET:
            field_dict["school_email"] = school_email
        if school_website is not UNSET:
            field_dict["school_website"] = school_website
        if school_type_1_en is not UNSET:
            field_dict["school_type_1_en"] = school_type_1_en
        if school_type_1_tc is not UNSET:
            field_dict["school_type_1_tc"] = school_type_1_tc
        if school_type_2_en is not UNSET:
            field_dict["school_type_2_en"] = school_type_2_en
        if school_type_2_tc is not UNSET:
            field_dict["school_type_2_tc"] = school_type_2_tc
        if imc_en is not UNSET:
            field_dict["imc_en"] = imc_en
        if imc_tc is not UNSET:
            field_dict["imc_tc"] = imc_tc
        if training_compliance_rate_supervisor_managers_smc_chair_members is not UNSET:
            field_dict[
                "training_compliance_rate_supervisor_managers_smc_chair_members"
            ] = training_compliance_rate_supervisor_managers_smc_chair_members
        if name_supervisor_chairman_of_mc_en is not UNSET:
            field_dict["name_supervisor_chairman_of_mc_en"] = (
                name_supervisor_chairman_of_mc_en
            )
        if name_supervisor_chairman_of_mc_tc is not UNSET:
            field_dict["name_supervisor_chairman_of_mc_tc"] = (
                name_supervisor_chairman_of_mc_tc
            )
        if title_supervisor_chairman_of_mc_en is not UNSET:
            field_dict["title_supervisor_chairman_of_mc_en"] = (
                title_supervisor_chairman_of_mc_en
            )
        if title_supervisor_chairman_of_mc_tc is not UNSET:
            field_dict["title_supervisor_chairman_of_mc_tc"] = (
                title_supervisor_chairman_of_mc_tc
            )
        if name_of_school_head_en is not UNSET:
            field_dict["name_of_school_head_en"] = name_of_school_head_en
        if name_of_school_head_tc is not UNSET:
            field_dict["name_of_school_head_tc"] = name_of_school_head_tc
        if title_of_school_head_en is not UNSET:
            field_dict["title_of_school_head_en"] = title_of_school_head_en
        if title_of_school_head_tc is not UNSET:
            field_dict["title_of_school_head_tc"] = title_of_school_head_tc
        if student_gender_en is not UNSET:
            field_dict["student_gender_en"] = student_gender_en
        if student_gender_tc is not UNSET:
            field_dict["student_gender_tc"] = student_gender_tc
        if sponsoring_body_en is not UNSET:
            field_dict["sponsoring_body_en"] = sponsoring_body_en
        if sponsoring_body_tc is not UNSET:
            field_dict["sponsoring_body_tc"] = sponsoring_body_tc
        if commencement_of_operation_year is not UNSET:
            field_dict["commencement_of_operation_year"] = (
                commencement_of_operation_year
            )
        if religion_en is not UNSET:
            field_dict["religion_en"] = religion_en
        if religion_tc is not UNSET:
            field_dict["religion_tc"] = religion_tc
        if other_religion_en is not UNSET:
            field_dict["other_religion_en"] = other_religion_en
        if other_religion_tc is not UNSET:
            field_dict["other_religion_tc"] = other_religion_tc
        if school_motto_en is not UNSET:
            field_dict["school_motto_en"] = school_motto_en
        if school_motto_tc is not UNSET:
            field_dict["school_motto_tc"] = school_motto_tc
        if school_size is not UNSET:
            field_dict["school_size"] = school_size
        if medium_of_instruction_en is not UNSET:
            field_dict["medium_of_instruction_en"] = medium_of_instruction_en
        if medium_of_instruction_tc is not UNSET:
            field_dict["medium_of_instruction_tc"] = medium_of_instruction_tc
        if through_train_sec_school_en is not UNSET:
            field_dict["through_train_sec_school_en"] = through_train_sec_school_en
        if through_train_sec_school_tc is not UNSET:
            field_dict["through_train_sec_school_tc"] = through_train_sec_school_tc
        if feeder_sec_school_en is not UNSET:
            field_dict["feeder_sec_school_en"] = feeder_sec_school_en
        if feeder_sec_school_tc is not UNSET:
            field_dict["feeder_sec_school_tc"] = feeder_sec_school_tc
        if nominated_sec_school_en is not UNSET:
            field_dict["nominated_sec_school_en"] = nominated_sec_school_en
        if nominated_sec_school_tc is not UNSET:
            field_dict["nominated_sec_school_tc"] = nominated_sec_school_tc
        if school_bus_en is not UNSET:
            field_dict["school_bus_en"] = school_bus_en
        if school_bus_tc is not UNSET:
            field_dict["school_bus_tc"] = school_bus_tc
        if nanny_van_en is not UNSET:
            field_dict["nanny_van_en"] = nanny_van_en
        if nanny_van_tc is not UNSET:
            field_dict["nanny_van_tc"] = nanny_van_tc
        if parent_teacher_association_en is not UNSET:
            field_dict["parent_teacher_association_en"] = parent_teacher_association_en
        if parent_teacher_association_tc is not UNSET:
            field_dict["parent_teacher_association_tc"] = parent_teacher_association_tc
        if school_alumni_association_en is not UNSET:
            field_dict["school_alumni_association_en"] = school_alumni_association_en
        if school_alumni_association_tc is not UNSET:
            field_dict["school_alumni_association_tc"] = school_alumni_association_tc
        if four_rs_mental_health_charter is not UNSET:
            field_dict["four_rs_mental_health_charter"] = four_rs_mental_health_charter
        if whole_school_health_programme is not UNSET:
            field_dict["whole_school_health_programme"] = whole_school_health_programme
        if asc_school_fee_en is not UNSET:
            field_dict["asc_school_fee_en"] = asc_school_fee_en
        if asc_school_fee_tc is not UNSET:
            field_dict["asc_school_fee_tc"] = asc_school_fee_tc
        if asc_tong_fai is not UNSET:
            field_dict["asc_tong_fai"] = asc_tong_fai
        if asc_pta_fee_en is not UNSET:
            field_dict["asc_pta_fee_en"] = asc_pta_fee_en
        if asc_pta_fee_tc is not UNSET:
            field_dict["asc_pta_fee_tc"] = asc_pta_fee_tc
        if asc_charges_for_non_standard_items_en is not UNSET:
            field_dict["asc_charges_for_non_standard_items_en"] = (
                asc_charges_for_non_standard_items_en
            )
        if asc_charges_for_non_standard_items_tc is not UNSET:
            field_dict["asc_charges_for_non_standard_items_tc"] = (
                asc_charges_for_non_standard_items_tc
            )
        if asc_others_en is not UNSET:
            field_dict["asc_others_en"] = asc_others_en
        if asc_others_tc is not UNSET:
            field_dict["asc_others_tc"] = asc_others_tc
        if fac_no_of_classroom is not UNSET:
            field_dict["fac_no_of_classroom"] = fac_no_of_classroom
        if fac_no_of_school_hall is not UNSET:
            field_dict["fac_no_of_school_hall"] = fac_no_of_school_hall
        if fac_no_of_playground is not UNSET:
            field_dict["fac_no_of_playground"] = fac_no_of_playground
        if fac_no_of_library is not UNSET:
            field_dict["fac_no_of_library"] = fac_no_of_library
        if fac_special_rooms_en is not UNSET:
            field_dict["fac_special_rooms_en"] = fac_special_rooms_en
        if fac_special_rooms_tc is not UNSET:
            field_dict["fac_special_rooms_tc"] = fac_special_rooms_tc
        if fac_others_en is not UNSET:
            field_dict["fac_others_en"] = fac_others_en
        if fac_others_tc is not UNSET:
            field_dict["fac_others_tc"] = fac_others_tc
        if fac_support_for_specialedu_en is not UNSET:
            field_dict["fac_support_for_specialedu_en"] = fac_support_for_specialedu_en
        if fac_support_for_specialedu_tc is not UNSET:
            field_dict["fac_support_for_specialedu_tc"] = fac_support_for_specialedu_tc
        if previous_year_tsi_no_of_approved_teaching_posts is not UNSET:
            field_dict["previous_year_tsi_no_of_approved_teaching_posts"] = (
                previous_year_tsi_no_of_approved_teaching_posts
            )
        if previous_year_tsi_total_no_of_teachers is not UNSET:
            field_dict["previous_year_tsi_total_no_of_teachers"] = (
                previous_year_tsi_total_no_of_teachers
            )
        if previous_year_tsi_percent_of_received_teacher_training is not UNSET:
            field_dict["previous_year_tsi_percent_of_received_teacher_training"] = (
                previous_year_tsi_percent_of_received_teacher_training
            )
        if previous_year_tsi_percent_of_bacherlor is not UNSET:
            field_dict["previous_year_tsi_percent_of_bacherlor"] = (
                previous_year_tsi_percent_of_bacherlor
            )
        if previous_year_tsi_percent_of_master_doctorate_or_above is not UNSET:
            field_dict["previous_year_tsi_percent_of_master_doctorate_or_above"] = (
                previous_year_tsi_percent_of_master_doctorate_or_above
            )
        if previous_year_tsi_percent_of_special_edu_training is not UNSET:
            field_dict["previous_year_tsi_percent_of_special_edu_training"] = (
                previous_year_tsi_percent_of_special_edu_training
            )
        if previous_year_tsi_percent_of_exp_0_4 is not UNSET:
            field_dict["previous_year_tsi_percent_of_exp_0_4"] = (
                previous_year_tsi_percent_of_exp_0_4
            )
        if previous_year_tsi_percent_of_exp_5_9 is not UNSET:
            field_dict["previous_year_tsi_percent_of_exp_5_9"] = (
                previous_year_tsi_percent_of_exp_5_9
            )
        if previous_year_tsi_percent_of_exp_10_or_above is not UNSET:
            field_dict["previous_year_tsi_percent_of_exp_10_or_above"] = (
                previous_year_tsi_percent_of_exp_10_or_above
            )
        if previous_year_no_of_class_p1 is not UNSET:
            field_dict["previous_year_no_of_class_p1"] = previous_year_no_of_class_p1
        if previous_year_no_of_class_p2 is not UNSET:
            field_dict["previous_year_no_of_class_p2"] = previous_year_no_of_class_p2
        if previous_year_no_of_class_p3 is not UNSET:
            field_dict["previous_year_no_of_class_p3"] = previous_year_no_of_class_p3
        if previous_year_no_of_class_p4 is not UNSET:
            field_dict["previous_year_no_of_class_p4"] = previous_year_no_of_class_p4
        if previous_year_no_of_class_p5 is not UNSET:
            field_dict["previous_year_no_of_class_p5"] = previous_year_no_of_class_p5
        if previous_year_no_of_class_p6 is not UNSET:
            field_dict["previous_year_no_of_class_p6"] = previous_year_no_of_class_p6
        if previous_year_no_of_class_total is not UNSET:
            field_dict["previous_year_no_of_class_total"] = (
                previous_year_no_of_class_total
            )
        if current_year_no_of_class_p1 is not UNSET:
            field_dict["current_year_no_of_class_p1"] = current_year_no_of_class_p1
        if current_year_no_of_class_p2 is not UNSET:
            field_dict["current_year_no_of_class_p2"] = current_year_no_of_class_p2
        if current_year_no_of_class_p3 is not UNSET:
            field_dict["current_year_no_of_class_p3"] = current_year_no_of_class_p3
        if current_year_no_of_class_p4 is not UNSET:
            field_dict["current_year_no_of_class_p4"] = current_year_no_of_class_p4
        if current_year_no_of_class_p5 is not UNSET:
            field_dict["current_year_no_of_class_p5"] = current_year_no_of_class_p5
        if current_year_no_of_class_p6 is not UNSET:
            field_dict["current_year_no_of_class_p6"] = current_year_no_of_class_p6
        if current_year_no_of_class_total is not UNSET:
            field_dict["current_year_no_of_class_total"] = (
                current_year_no_of_class_total
            )
        if cs_mode_of_teaching_en is not UNSET:
            field_dict["cs_mode_of_teaching_en"] = cs_mode_of_teaching_en
        if cs_mode_of_teaching_tc is not UNSET:
            field_dict["cs_mode_of_teaching_tc"] = cs_mode_of_teaching_tc
        if cs_remarks_en is not UNSET:
            field_dict["cs_remarks_en"] = cs_remarks_en
        if cs_remarks_tc is not UNSET:
            field_dict["cs_remarks_tc"] = cs_remarks_tc
        if no_of_test_per_year_p1 is not UNSET:
            field_dict["no_of_test_per_year_P1"] = no_of_test_per_year_p1
        if no_of_exam_per_year_p1 is not UNSET:
            field_dict["no_of_exam_per_year_P1"] = no_of_exam_per_year_p1
        if replace_test_exam_p1_en is not UNSET:
            field_dict["replace_test_exam_P1_en"] = replace_test_exam_p1_en
        if replace_test_exam_p1_tc is not UNSET:
            field_dict["replace_test_exam_P1_tc"] = replace_test_exam_p1_tc
        if no_of_test_per_year_p2_p6 is not UNSET:
            field_dict["no_of_test_per_year_P2_P6"] = no_of_test_per_year_p2_p6
        if no_of_exam_p2_p6 is not UNSET:
            field_dict["no_of_exam_P2_P6"] = no_of_exam_p2_p6
        if fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_en is not UNSET:
            field_dict[
                "fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_en"
            ] = fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_en
        if fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_tc is not UNSET:
            field_dict[
                "fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_tc"
            ] = fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_tc
        if upload_school_assessment_policy_to_school_web_en is not UNSET:
            field_dict["upload_school_assessment_policy_to_school_web_en"] = (
                upload_school_assessment_policy_to_school_web_en
            )
        if upload_school_assessment_policy_to_school_web_tc is not UNSET:
            field_dict["upload_school_assessment_policy_to_school_web_tc"] = (
                upload_school_assessment_policy_to_school_web_tc
            )
        if upload_school_assignment_policy_to_school_web_en is not UNSET:
            field_dict["upload_school_assignment_policy_to_school_web_en"] = (
                upload_school_assignment_policy_to_school_web_en
            )
        if upload_school_assignment_policy_to_school_web_tc is not UNSET:
            field_dict["upload_school_assignment_policy_to_school_web_tc"] = (
                upload_school_assignment_policy_to_school_web_tc
            )
        if diversified_assessment_en is not UNSET:
            field_dict["diversified_assessment_en"] = diversified_assessment_en
        if diversified_assessment_tc is not UNSET:
            field_dict["diversified_assessment_tc"] = diversified_assessment_tc
        if avoid_test_exam_after_long_holidays_en is not UNSET:
            field_dict["avoid_test_exam_after_long_holidays_en"] = (
                avoid_test_exam_after_long_holidays_en
            )
        if avoid_test_exam_after_long_holidays_tc is not UNSET:
            field_dict["avoid_test_exam_after_long_holidays_tc"] = (
                avoid_test_exam_after_long_holidays_tc
            )
        if arrange_timetable_flexibly_tutorial_session_in_afternoon_en is not UNSET:
            field_dict[
                "arrange_timetable_flexibly_tutorial_session_in_afternoon_en"
            ] = arrange_timetable_flexibly_tutorial_session_in_afternoon_en
        if arrange_timetable_flexibly_tutorial_session_in_afternoon_tc is not UNSET:
            field_dict[
                "arrange_timetable_flexibly_tutorial_session_in_afternoon_tc"
            ] = arrange_timetable_flexibly_tutorial_session_in_afternoon_tc
        if streaming_arrangement_en is not UNSET:
            field_dict["streaming_arrangement_en"] = streaming_arrangement_en
        if streaming_arrangement_tc is not UNSET:
            field_dict["streaming_arrangement_tc"] = streaming_arrangement_tc
        if no_of_school_days_per_week is not UNSET:
            field_dict["no_of_school_days_per_week"] = no_of_school_days_per_week
        if no_of_periods_per_day is not UNSET:
            field_dict["no_of_periods_per_day"] = no_of_periods_per_day
        if duration_of_each_period is not UNSET:
            field_dict["duration_of_each_period"] = duration_of_each_period
        if school_starts_at is not UNSET:
            field_dict["school_starts_at"] = school_starts_at
        if school_starts_at_ampm_en is not UNSET:
            field_dict["school_starts_at_AMPM_en"] = school_starts_at_ampm_en
        if school_starts_at_ampm_tc is not UNSET:
            field_dict["school_starts_at_AMPM_tc"] = school_starts_at_ampm_tc
        if school_ends_at is not UNSET:
            field_dict["school_ends_at"] = school_ends_at
        if school_ends_at_ampm_en is not UNSET:
            field_dict["school_ends_at_AMPM_en"] = school_ends_at_ampm_en
        if school_ends_at_ampm_tc is not UNSET:
            field_dict["school_ends_at_AMPM_tc"] = school_ends_at_ampm_tc
        if lunch_start_time is not UNSET:
            field_dict["lunch_start_time"] = lunch_start_time
        if lunch_end_time is not UNSET:
            field_dict["lunch_end_time"] = lunch_end_time
        if lunch_arrangement_en is not UNSET:
            field_dict["lunch_arrangement_en"] = lunch_arrangement_en
        if lunch_arrangement_tc is not UNSET:
            field_dict["lunch_arrangement_tc"] = lunch_arrangement_tc
        if healthy_school_life_en is not UNSET:
            field_dict["healthy_school_life_en"] = healthy_school_life_en
        if healthy_school_life_tc is not UNSET:
            field_dict["healthy_school_life_tc"] = healthy_school_life_tc
        if school_life_remarks_en is not UNSET:
            field_dict["school_life_remarks_en"] = school_life_remarks_en
        if school_life_remarks_tc is not UNSET:
            field_dict["school_life_remarks_tc"] = school_life_remarks_tc
        if life_wide_learning_en is not UNSET:
            field_dict["life_wide_learning_en"] = life_wide_learning_en
        if life_wide_learning_tc is not UNSET:
            field_dict["life_wide_learning_tc"] = life_wide_learning_tc
        if school_mission_en is not UNSET:
            field_dict["school_mission_en"] = school_mission_en
        if school_mission_tc is not UNSET:
            field_dict["school_mission_tc"] = school_mission_tc
        if school_management_url is not UNSET:
            field_dict["school_management_url"] = school_management_url
        if school_organisation_en is not UNSET:
            field_dict["school_organisation_en"] = school_organisation_en
        if school_organisation_tc is not UNSET:
            field_dict["school_organisation_tc"] = school_organisation_tc
        if imc_smc_mc_en is not UNSET:
            field_dict["imc_smc_mc_en"] = imc_smc_mc_en
        if imc_smc_mc_tc is not UNSET:
            field_dict["imc_smc_mc_tc"] = imc_smc_mc_tc
        if school_green_policy_en is not UNSET:
            field_dict["school_green_policy_en"] = school_green_policy_en
        if school_green_policy_tc is not UNSET:
            field_dict["school_green_policy_tc"] = school_green_policy_tc
        if school_major_concerns_url is not UNSET:
            field_dict["school_major_concerns_url"] = school_major_concerns_url
        if school_major_concerns_en is not UNSET:
            field_dict["school_major_concerns_en"] = school_major_concerns_en
        if school_major_concerns_tc is not UNSET:
            field_dict["school_major_concerns_tc"] = school_major_concerns_tc
        if learning_and_teaching_plan_url is not UNSET:
            field_dict["learning_and_teaching_plan_url"] = (
                learning_and_teaching_plan_url
            )
        if learning_and_teaching_strategies_en is not UNSET:
            field_dict["learning_and_teaching_strategies_en"] = (
                learning_and_teaching_strategies_en
            )
        if learning_and_teaching_strategies_tc is not UNSET:
            field_dict["learning_and_teaching_strategies_tc"] = (
                learning_and_teaching_strategies_tc
            )
        if major_renewed_emphases_pri_edu_curriculum_en is not UNSET:
            field_dict["major_renewed_emphases_pri_edu_curriculum_en"] = (
                major_renewed_emphases_pri_edu_curriculum_en
            )
        if major_renewed_emphases_pri_edu_curriculum_tc is not UNSET:
            field_dict["major_renewed_emphases_pri_edu_curriculum_tc"] = (
                major_renewed_emphases_pri_edu_curriculum_tc
            )
        if dev_of_generic_skills_en is not UNSET:
            field_dict["dev_of_generic_skills_en"] = dev_of_generic_skills_en
        if dev_of_generic_skills_tc is not UNSET:
            field_dict["dev_of_generic_skills_tc"] = dev_of_generic_skills_tc
        if cultivation_of_proper_values_attitudes_and_behaviours_en is not UNSET:
            field_dict["cultivation_of_proper_values_attitudes_and_behaviours_en"] = (
                cultivation_of_proper_values_attitudes_and_behaviours_en
            )
        if cultivation_of_proper_values_attitudes_and_behaviours_tc is not UNSET:
            field_dict["cultivation_of_proper_values_attitudes_and_behaviours_tc"] = (
                cultivation_of_proper_values_attitudes_and_behaviours_tc
            )
        if student_support_url is not UNSET:
            field_dict["student_support_url"] = student_support_url
        if whole_school_approach_cater_for_learner_diversity_en is not UNSET:
            field_dict["whole_school_approach_cater_for_learner_diversity_en"] = (
                whole_school_approach_cater_for_learner_diversity_en
            )
        if whole_school_approach_cater_for_learner_diversity_tc is not UNSET:
            field_dict["whole_school_approach_cater_for_learner_diversity_tc"] = (
                whole_school_approach_cater_for_learner_diversity_tc
            )
        if whole_school_approach_integrated_education_en is not UNSET:
            field_dict["whole_school_approach_integrated_education_en"] = (
                whole_school_approach_integrated_education_en
            )
        if whole_school_approach_integrated_education_tc is not UNSET:
            field_dict["whole_school_approach_integrated_education_tc"] = (
                whole_school_approach_integrated_education_tc
            )
        if support_for_non_chinese_students_en is not UNSET:
            field_dict["support_for_non_chinese_students_en"] = (
                support_for_non_chinese_students_en
            )
        if support_for_non_chinese_students_tc is not UNSET:
            field_dict["support_for_non_chinese_students_tc"] = (
                support_for_non_chinese_students_tc
            )
        if curriculum_tailoring_and_adaptation_en is not UNSET:
            field_dict["curriculum_tailoring_and_adaptation_en"] = (
                curriculum_tailoring_and_adaptation_en
            )
        if curriculum_tailoring_and_adaptation_tc is not UNSET:
            field_dict["curriculum_tailoring_and_adaptation_tc"] = (
                curriculum_tailoring_and_adaptation_tc
            )
        if home_school_cooperation_url is not UNSET:
            field_dict["home_school_cooperation_url"] = home_school_cooperation_url
        if home_school_cooperation_en is not UNSET:
            field_dict["home_school_cooperation_en"] = home_school_cooperation_en
        if home_school_cooperation_tc is not UNSET:
            field_dict["home_school_cooperation_tc"] = home_school_cooperation_tc
        if school_ethos_en is not UNSET:
            field_dict["school_ethos_en"] = school_ethos_en
        if school_ethos_tc is not UNSET:
            field_dict["school_ethos_tc"] = school_ethos_tc
        if future_dev_url is not UNSET:
            field_dict["future_dev_url"] = future_dev_url
        if school_dev_plan_en is not UNSET:
            field_dict["school_dev_plan_en"] = school_dev_plan_en
        if school_dev_plan_tc is not UNSET:
            field_dict["school_dev_plan_tc"] = school_dev_plan_tc
        if teacher_pro_training_and_dev_en is not UNSET:
            field_dict["teacher_pro_training_and_dev_en"] = (
                teacher_pro_training_and_dev_en
            )
        if teacher_pro_training_and_dev_tc is not UNSET:
            field_dict["teacher_pro_training_and_dev_tc"] = (
                teacher_pro_training_and_dev_tc
            )
        if school_character_others_en is not UNSET:
            field_dict["school_character_others_en"] = school_character_others_en
        if school_character_others_tc is not UNSET:
            field_dict["school_character_others_tc"] = school_character_others_tc
        if fee_remission_en is not UNSET:
            field_dict["fee_remission_en"] = fee_remission_en
        if fee_remission_tc is not UNSET:
            field_dict["fee_remission_tc"] = fee_remission_tc
        if northing is not UNSET:
            field_dict["northing"] = northing
        if easting is not UNSET:
            field_dict["easting"] = easting
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_feature_member_owns(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        feature_member_owns = _parse_feature_member_owns(
            d.pop("featureMember___owns", UNSET)
        )

        def _parse_fid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fid = _parse_fid(d.pop("fid", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

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

        def _parse_school_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_address_en = _parse_school_address_en(d.pop("school_address_en", UNSET))

        def _parse_school_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_address_tc = _parse_school_address_tc(d.pop("school_address_tc", UNSET))

        def _parse_poa_school_net(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        poa_school_net = _parse_poa_school_net(d.pop("poa_school_net", UNSET))

        def _parse_school_tel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_tel = _parse_school_tel(d.pop("school_tel", UNSET))

        def _parse_school_fax(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_fax = _parse_school_fax(d.pop("school_fax", UNSET))

        def _parse_school_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_email = _parse_school_email(d.pop("school_email", UNSET))

        def _parse_school_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_website = _parse_school_website(d.pop("school_website", UNSET))

        def _parse_school_type_1_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_type_1_en = _parse_school_type_1_en(d.pop("school_type_1_en", UNSET))

        def _parse_school_type_1_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_type_1_tc = _parse_school_type_1_tc(d.pop("school_type_1_tc", UNSET))

        def _parse_school_type_2_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_type_2_en = _parse_school_type_2_en(d.pop("school_type_2_en", UNSET))

        def _parse_school_type_2_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_type_2_tc = _parse_school_type_2_tc(d.pop("school_type_2_tc", UNSET))

        def _parse_imc_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        imc_en = _parse_imc_en(d.pop("imc_en", UNSET))

        def _parse_imc_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        imc_tc = _parse_imc_tc(d.pop("imc_tc", UNSET))

        def _parse_training_compliance_rate_supervisor_managers_smc_chair_members(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        training_compliance_rate_supervisor_managers_smc_chair_members = (
            _parse_training_compliance_rate_supervisor_managers_smc_chair_members(
                d.pop(
                    "training_compliance_rate_supervisor_managers_smc_chair_members",
                    UNSET,
                )
            )
        )

        def _parse_name_supervisor_chairman_of_mc_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_supervisor_chairman_of_mc_en = _parse_name_supervisor_chairman_of_mc_en(
            d.pop("name_supervisor_chairman_of_mc_en", UNSET)
        )

        def _parse_name_supervisor_chairman_of_mc_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_supervisor_chairman_of_mc_tc = _parse_name_supervisor_chairman_of_mc_tc(
            d.pop("name_supervisor_chairman_of_mc_tc", UNSET)
        )

        def _parse_title_supervisor_chairman_of_mc_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_supervisor_chairman_of_mc_en = _parse_title_supervisor_chairman_of_mc_en(
            d.pop("title_supervisor_chairman_of_mc_en", UNSET)
        )

        def _parse_title_supervisor_chairman_of_mc_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_supervisor_chairman_of_mc_tc = _parse_title_supervisor_chairman_of_mc_tc(
            d.pop("title_supervisor_chairman_of_mc_tc", UNSET)
        )

        def _parse_name_of_school_head_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_school_head_en = _parse_name_of_school_head_en(
            d.pop("name_of_school_head_en", UNSET)
        )

        def _parse_name_of_school_head_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_school_head_tc = _parse_name_of_school_head_tc(
            d.pop("name_of_school_head_tc", UNSET)
        )

        def _parse_title_of_school_head_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_of_school_head_en = _parse_title_of_school_head_en(
            d.pop("title_of_school_head_en", UNSET)
        )

        def _parse_title_of_school_head_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_of_school_head_tc = _parse_title_of_school_head_tc(
            d.pop("title_of_school_head_tc", UNSET)
        )

        def _parse_student_gender_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        student_gender_en = _parse_student_gender_en(d.pop("student_gender_en", UNSET))

        def _parse_student_gender_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        student_gender_tc = _parse_student_gender_tc(d.pop("student_gender_tc", UNSET))

        def _parse_sponsoring_body_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sponsoring_body_en = _parse_sponsoring_body_en(
            d.pop("sponsoring_body_en", UNSET)
        )

        def _parse_sponsoring_body_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sponsoring_body_tc = _parse_sponsoring_body_tc(
            d.pop("sponsoring_body_tc", UNSET)
        )

        def _parse_commencement_of_operation_year(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commencement_of_operation_year = _parse_commencement_of_operation_year(
            d.pop("commencement_of_operation_year", UNSET)
        )

        def _parse_religion_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        religion_en = _parse_religion_en(d.pop("religion_en", UNSET))

        def _parse_religion_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        religion_tc = _parse_religion_tc(d.pop("religion_tc", UNSET))

        def _parse_other_religion_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_religion_en = _parse_other_religion_en(d.pop("other_religion_en", UNSET))

        def _parse_other_religion_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_religion_tc = _parse_other_religion_tc(d.pop("other_religion_tc", UNSET))

        def _parse_school_motto_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_motto_en = _parse_school_motto_en(d.pop("school_motto_en", UNSET))

        def _parse_school_motto_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_motto_tc = _parse_school_motto_tc(d.pop("school_motto_tc", UNSET))

        def _parse_school_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_size = _parse_school_size(d.pop("school_size", UNSET))

        def _parse_medium_of_instruction_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        medium_of_instruction_en = _parse_medium_of_instruction_en(
            d.pop("medium_of_instruction_en", UNSET)
        )

        def _parse_medium_of_instruction_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        medium_of_instruction_tc = _parse_medium_of_instruction_tc(
            d.pop("medium_of_instruction_tc", UNSET)
        )

        def _parse_through_train_sec_school_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        through_train_sec_school_en = _parse_through_train_sec_school_en(
            d.pop("through_train_sec_school_en", UNSET)
        )

        def _parse_through_train_sec_school_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        through_train_sec_school_tc = _parse_through_train_sec_school_tc(
            d.pop("through_train_sec_school_tc", UNSET)
        )

        def _parse_feeder_sec_school_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feeder_sec_school_en = _parse_feeder_sec_school_en(
            d.pop("feeder_sec_school_en", UNSET)
        )

        def _parse_feeder_sec_school_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feeder_sec_school_tc = _parse_feeder_sec_school_tc(
            d.pop("feeder_sec_school_tc", UNSET)
        )

        def _parse_nominated_sec_school_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nominated_sec_school_en = _parse_nominated_sec_school_en(
            d.pop("nominated_sec_school_en", UNSET)
        )

        def _parse_nominated_sec_school_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nominated_sec_school_tc = _parse_nominated_sec_school_tc(
            d.pop("nominated_sec_school_tc", UNSET)
        )

        def _parse_school_bus_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_bus_en = _parse_school_bus_en(d.pop("school_bus_en", UNSET))

        def _parse_school_bus_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_bus_tc = _parse_school_bus_tc(d.pop("school_bus_tc", UNSET))

        def _parse_nanny_van_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nanny_van_en = _parse_nanny_van_en(d.pop("nanny_van_en", UNSET))

        def _parse_nanny_van_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nanny_van_tc = _parse_nanny_van_tc(d.pop("nanny_van_tc", UNSET))

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

        def _parse_school_alumni_association_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_alumni_association_en = _parse_school_alumni_association_en(
            d.pop("school_alumni_association_en", UNSET)
        )

        def _parse_school_alumni_association_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_alumni_association_tc = _parse_school_alumni_association_tc(
            d.pop("school_alumni_association_tc", UNSET)
        )

        def _parse_four_rs_mental_health_charter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        four_rs_mental_health_charter = _parse_four_rs_mental_health_charter(
            d.pop("four_rs_mental_health_charter", UNSET)
        )

        def _parse_whole_school_health_programme(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        whole_school_health_programme = _parse_whole_school_health_programme(
            d.pop("whole_school_health_programme", UNSET)
        )

        def _parse_asc_school_fee_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asc_school_fee_en = _parse_asc_school_fee_en(d.pop("asc_school_fee_en", UNSET))

        def _parse_asc_school_fee_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asc_school_fee_tc = _parse_asc_school_fee_tc(d.pop("asc_school_fee_tc", UNSET))

        def _parse_asc_tong_fai(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asc_tong_fai = _parse_asc_tong_fai(d.pop("asc_tong_fai", UNSET))

        def _parse_asc_pta_fee_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asc_pta_fee_en = _parse_asc_pta_fee_en(d.pop("asc_pta_fee_en", UNSET))

        def _parse_asc_pta_fee_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asc_pta_fee_tc = _parse_asc_pta_fee_tc(d.pop("asc_pta_fee_tc", UNSET))

        def _parse_asc_charges_for_non_standard_items_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asc_charges_for_non_standard_items_en = (
            _parse_asc_charges_for_non_standard_items_en(
                d.pop("asc_charges_for_non_standard_items_en", UNSET)
            )
        )

        def _parse_asc_charges_for_non_standard_items_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asc_charges_for_non_standard_items_tc = (
            _parse_asc_charges_for_non_standard_items_tc(
                d.pop("asc_charges_for_non_standard_items_tc", UNSET)
            )
        )

        def _parse_asc_others_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asc_others_en = _parse_asc_others_en(d.pop("asc_others_en", UNSET))

        def _parse_asc_others_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asc_others_tc = _parse_asc_others_tc(d.pop("asc_others_tc", UNSET))

        def _parse_fac_no_of_classroom(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_no_of_classroom = _parse_fac_no_of_classroom(
            d.pop("fac_no_of_classroom", UNSET)
        )

        def _parse_fac_no_of_school_hall(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_no_of_school_hall = _parse_fac_no_of_school_hall(
            d.pop("fac_no_of_school_hall", UNSET)
        )

        def _parse_fac_no_of_playground(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_no_of_playground = _parse_fac_no_of_playground(
            d.pop("fac_no_of_playground", UNSET)
        )

        def _parse_fac_no_of_library(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_no_of_library = _parse_fac_no_of_library(d.pop("fac_no_of_library", UNSET))

        def _parse_fac_special_rooms_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_special_rooms_en = _parse_fac_special_rooms_en(
            d.pop("fac_special_rooms_en", UNSET)
        )

        def _parse_fac_special_rooms_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_special_rooms_tc = _parse_fac_special_rooms_tc(
            d.pop("fac_special_rooms_tc", UNSET)
        )

        def _parse_fac_others_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_others_en = _parse_fac_others_en(d.pop("fac_others_en", UNSET))

        def _parse_fac_others_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_others_tc = _parse_fac_others_tc(d.pop("fac_others_tc", UNSET))

        def _parse_fac_support_for_specialedu_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_support_for_specialedu_en = _parse_fac_support_for_specialedu_en(
            d.pop("fac_support_for_specialedu_en", UNSET)
        )

        def _parse_fac_support_for_specialedu_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_support_for_specialedu_tc = _parse_fac_support_for_specialedu_tc(
            d.pop("fac_support_for_specialedu_tc", UNSET)
        )

        def _parse_previous_year_tsi_no_of_approved_teaching_posts(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_year_tsi_no_of_approved_teaching_posts = (
            _parse_previous_year_tsi_no_of_approved_teaching_posts(
                d.pop("previous_year_tsi_no_of_approved_teaching_posts", UNSET)
            )
        )

        def _parse_previous_year_tsi_total_no_of_teachers(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_year_tsi_total_no_of_teachers = (
            _parse_previous_year_tsi_total_no_of_teachers(
                d.pop("previous_year_tsi_total_no_of_teachers", UNSET)
            )
        )

        def _parse_previous_year_tsi_percent_of_received_teacher_training(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_year_tsi_percent_of_received_teacher_training = (
            _parse_previous_year_tsi_percent_of_received_teacher_training(
                d.pop("previous_year_tsi_percent_of_received_teacher_training", UNSET)
            )
        )

        def _parse_previous_year_tsi_percent_of_bacherlor(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_year_tsi_percent_of_bacherlor = (
            _parse_previous_year_tsi_percent_of_bacherlor(
                d.pop("previous_year_tsi_percent_of_bacherlor", UNSET)
            )
        )

        def _parse_previous_year_tsi_percent_of_master_doctorate_or_above(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_year_tsi_percent_of_master_doctorate_or_above = (
            _parse_previous_year_tsi_percent_of_master_doctorate_or_above(
                d.pop("previous_year_tsi_percent_of_master_doctorate_or_above", UNSET)
            )
        )

        def _parse_previous_year_tsi_percent_of_special_edu_training(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_year_tsi_percent_of_special_edu_training = (
            _parse_previous_year_tsi_percent_of_special_edu_training(
                d.pop("previous_year_tsi_percent_of_special_edu_training", UNSET)
            )
        )

        def _parse_previous_year_tsi_percent_of_exp_0_4(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_year_tsi_percent_of_exp_0_4 = (
            _parse_previous_year_tsi_percent_of_exp_0_4(
                d.pop("previous_year_tsi_percent_of_exp_0_4", UNSET)
            )
        )

        def _parse_previous_year_tsi_percent_of_exp_5_9(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_year_tsi_percent_of_exp_5_9 = (
            _parse_previous_year_tsi_percent_of_exp_5_9(
                d.pop("previous_year_tsi_percent_of_exp_5_9", UNSET)
            )
        )

        def _parse_previous_year_tsi_percent_of_exp_10_or_above(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_year_tsi_percent_of_exp_10_or_above = (
            _parse_previous_year_tsi_percent_of_exp_10_or_above(
                d.pop("previous_year_tsi_percent_of_exp_10_or_above", UNSET)
            )
        )

        def _parse_previous_year_no_of_class_p1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_year_no_of_class_p1 = _parse_previous_year_no_of_class_p1(
            d.pop("previous_year_no_of_class_p1", UNSET)
        )

        def _parse_previous_year_no_of_class_p2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_year_no_of_class_p2 = _parse_previous_year_no_of_class_p2(
            d.pop("previous_year_no_of_class_p2", UNSET)
        )

        def _parse_previous_year_no_of_class_p3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_year_no_of_class_p3 = _parse_previous_year_no_of_class_p3(
            d.pop("previous_year_no_of_class_p3", UNSET)
        )

        def _parse_previous_year_no_of_class_p4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_year_no_of_class_p4 = _parse_previous_year_no_of_class_p4(
            d.pop("previous_year_no_of_class_p4", UNSET)
        )

        def _parse_previous_year_no_of_class_p5(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_year_no_of_class_p5 = _parse_previous_year_no_of_class_p5(
            d.pop("previous_year_no_of_class_p5", UNSET)
        )

        def _parse_previous_year_no_of_class_p6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_year_no_of_class_p6 = _parse_previous_year_no_of_class_p6(
            d.pop("previous_year_no_of_class_p6", UNSET)
        )

        def _parse_previous_year_no_of_class_total(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_year_no_of_class_total = _parse_previous_year_no_of_class_total(
            d.pop("previous_year_no_of_class_total", UNSET)
        )

        def _parse_current_year_no_of_class_p1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_no_of_class_p1 = _parse_current_year_no_of_class_p1(
            d.pop("current_year_no_of_class_p1", UNSET)
        )

        def _parse_current_year_no_of_class_p2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_no_of_class_p2 = _parse_current_year_no_of_class_p2(
            d.pop("current_year_no_of_class_p2", UNSET)
        )

        def _parse_current_year_no_of_class_p3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_no_of_class_p3 = _parse_current_year_no_of_class_p3(
            d.pop("current_year_no_of_class_p3", UNSET)
        )

        def _parse_current_year_no_of_class_p4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_no_of_class_p4 = _parse_current_year_no_of_class_p4(
            d.pop("current_year_no_of_class_p4", UNSET)
        )

        def _parse_current_year_no_of_class_p5(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_no_of_class_p5 = _parse_current_year_no_of_class_p5(
            d.pop("current_year_no_of_class_p5", UNSET)
        )

        def _parse_current_year_no_of_class_p6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_no_of_class_p6 = _parse_current_year_no_of_class_p6(
            d.pop("current_year_no_of_class_p6", UNSET)
        )

        def _parse_current_year_no_of_class_total(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_no_of_class_total = _parse_current_year_no_of_class_total(
            d.pop("current_year_no_of_class_total", UNSET)
        )

        def _parse_cs_mode_of_teaching_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cs_mode_of_teaching_en = _parse_cs_mode_of_teaching_en(
            d.pop("cs_mode_of_teaching_en", UNSET)
        )

        def _parse_cs_mode_of_teaching_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cs_mode_of_teaching_tc = _parse_cs_mode_of_teaching_tc(
            d.pop("cs_mode_of_teaching_tc", UNSET)
        )

        def _parse_cs_remarks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cs_remarks_en = _parse_cs_remarks_en(d.pop("cs_remarks_en", UNSET))

        def _parse_cs_remarks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cs_remarks_tc = _parse_cs_remarks_tc(d.pop("cs_remarks_tc", UNSET))

        def _parse_no_of_test_per_year_p1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_test_per_year_p1 = _parse_no_of_test_per_year_p1(
            d.pop("no_of_test_per_year_P1", UNSET)
        )

        def _parse_no_of_exam_per_year_p1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_exam_per_year_p1 = _parse_no_of_exam_per_year_p1(
            d.pop("no_of_exam_per_year_P1", UNSET)
        )

        def _parse_replace_test_exam_p1_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        replace_test_exam_p1_en = _parse_replace_test_exam_p1_en(
            d.pop("replace_test_exam_P1_en", UNSET)
        )

        def _parse_replace_test_exam_p1_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        replace_test_exam_p1_tc = _parse_replace_test_exam_p1_tc(
            d.pop("replace_test_exam_P1_tc", UNSET)
        )

        def _parse_no_of_test_per_year_p2_p6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_test_per_year_p2_p6 = _parse_no_of_test_per_year_p2_p6(
            d.pop("no_of_test_per_year_P2_P6", UNSET)
        )

        def _parse_no_of_exam_p2_p6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_exam_p2_p6 = _parse_no_of_exam_p2_p6(d.pop("no_of_exam_P2_P6", UNSET))

        def _parse_fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_en = (
            _parse_fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_en(
                d.pop(
                    "fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_en",
                    UNSET,
                )
            )
        )

        def _parse_fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_tc = (
            _parse_fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_tc(
                d.pop(
                    "fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_tc",
                    UNSET,
                )
            )
        )

        def _parse_upload_school_assessment_policy_to_school_web_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_school_assessment_policy_to_school_web_en = (
            _parse_upload_school_assessment_policy_to_school_web_en(
                d.pop("upload_school_assessment_policy_to_school_web_en", UNSET)
            )
        )

        def _parse_upload_school_assessment_policy_to_school_web_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_school_assessment_policy_to_school_web_tc = (
            _parse_upload_school_assessment_policy_to_school_web_tc(
                d.pop("upload_school_assessment_policy_to_school_web_tc", UNSET)
            )
        )

        def _parse_upload_school_assignment_policy_to_school_web_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_school_assignment_policy_to_school_web_en = (
            _parse_upload_school_assignment_policy_to_school_web_en(
                d.pop("upload_school_assignment_policy_to_school_web_en", UNSET)
            )
        )

        def _parse_upload_school_assignment_policy_to_school_web_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_school_assignment_policy_to_school_web_tc = (
            _parse_upload_school_assignment_policy_to_school_web_tc(
                d.pop("upload_school_assignment_policy_to_school_web_tc", UNSET)
            )
        )

        def _parse_diversified_assessment_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        diversified_assessment_en = _parse_diversified_assessment_en(
            d.pop("diversified_assessment_en", UNSET)
        )

        def _parse_diversified_assessment_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        diversified_assessment_tc = _parse_diversified_assessment_tc(
            d.pop("diversified_assessment_tc", UNSET)
        )

        def _parse_avoid_test_exam_after_long_holidays_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avoid_test_exam_after_long_holidays_en = (
            _parse_avoid_test_exam_after_long_holidays_en(
                d.pop("avoid_test_exam_after_long_holidays_en", UNSET)
            )
        )

        def _parse_avoid_test_exam_after_long_holidays_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avoid_test_exam_after_long_holidays_tc = (
            _parse_avoid_test_exam_after_long_holidays_tc(
                d.pop("avoid_test_exam_after_long_holidays_tc", UNSET)
            )
        )

        def _parse_arrange_timetable_flexibly_tutorial_session_in_afternoon_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        arrange_timetable_flexibly_tutorial_session_in_afternoon_en = (
            _parse_arrange_timetable_flexibly_tutorial_session_in_afternoon_en(
                d.pop(
                    "arrange_timetable_flexibly_tutorial_session_in_afternoon_en", UNSET
                )
            )
        )

        def _parse_arrange_timetable_flexibly_tutorial_session_in_afternoon_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        arrange_timetable_flexibly_tutorial_session_in_afternoon_tc = (
            _parse_arrange_timetable_flexibly_tutorial_session_in_afternoon_tc(
                d.pop(
                    "arrange_timetable_flexibly_tutorial_session_in_afternoon_tc", UNSET
                )
            )
        )

        def _parse_streaming_arrangement_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        streaming_arrangement_en = _parse_streaming_arrangement_en(
            d.pop("streaming_arrangement_en", UNSET)
        )

        def _parse_streaming_arrangement_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        streaming_arrangement_tc = _parse_streaming_arrangement_tc(
            d.pop("streaming_arrangement_tc", UNSET)
        )

        def _parse_no_of_school_days_per_week(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_school_days_per_week = _parse_no_of_school_days_per_week(
            d.pop("no_of_school_days_per_week", UNSET)
        )

        def _parse_no_of_periods_per_day(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_periods_per_day = _parse_no_of_periods_per_day(
            d.pop("no_of_periods_per_day", UNSET)
        )

        def _parse_duration_of_each_period(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        duration_of_each_period = _parse_duration_of_each_period(
            d.pop("duration_of_each_period", UNSET)
        )

        def _parse_school_starts_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_starts_at = _parse_school_starts_at(d.pop("school_starts_at", UNSET))

        def _parse_school_starts_at_ampm_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_starts_at_ampm_en = _parse_school_starts_at_ampm_en(
            d.pop("school_starts_at_AMPM_en", UNSET)
        )

        def _parse_school_starts_at_ampm_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_starts_at_ampm_tc = _parse_school_starts_at_ampm_tc(
            d.pop("school_starts_at_AMPM_tc", UNSET)
        )

        def _parse_school_ends_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_ends_at = _parse_school_ends_at(d.pop("school_ends_at", UNSET))

        def _parse_school_ends_at_ampm_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_ends_at_ampm_en = _parse_school_ends_at_ampm_en(
            d.pop("school_ends_at_AMPM_en", UNSET)
        )

        def _parse_school_ends_at_ampm_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_ends_at_ampm_tc = _parse_school_ends_at_ampm_tc(
            d.pop("school_ends_at_AMPM_tc", UNSET)
        )

        def _parse_lunch_start_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lunch_start_time = _parse_lunch_start_time(d.pop("lunch_start_time", UNSET))

        def _parse_lunch_end_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lunch_end_time = _parse_lunch_end_time(d.pop("lunch_end_time", UNSET))

        def _parse_lunch_arrangement_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lunch_arrangement_en = _parse_lunch_arrangement_en(
            d.pop("lunch_arrangement_en", UNSET)
        )

        def _parse_lunch_arrangement_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lunch_arrangement_tc = _parse_lunch_arrangement_tc(
            d.pop("lunch_arrangement_tc", UNSET)
        )

        def _parse_healthy_school_life_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        healthy_school_life_en = _parse_healthy_school_life_en(
            d.pop("healthy_school_life_en", UNSET)
        )

        def _parse_healthy_school_life_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        healthy_school_life_tc = _parse_healthy_school_life_tc(
            d.pop("healthy_school_life_tc", UNSET)
        )

        def _parse_school_life_remarks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_life_remarks_en = _parse_school_life_remarks_en(
            d.pop("school_life_remarks_en", UNSET)
        )

        def _parse_school_life_remarks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_life_remarks_tc = _parse_school_life_remarks_tc(
            d.pop("school_life_remarks_tc", UNSET)
        )

        def _parse_life_wide_learning_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        life_wide_learning_en = _parse_life_wide_learning_en(
            d.pop("life_wide_learning_en", UNSET)
        )

        def _parse_life_wide_learning_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        life_wide_learning_tc = _parse_life_wide_learning_tc(
            d.pop("life_wide_learning_tc", UNSET)
        )

        def _parse_school_mission_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_mission_en = _parse_school_mission_en(d.pop("school_mission_en", UNSET))

        def _parse_school_mission_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_mission_tc = _parse_school_mission_tc(d.pop("school_mission_tc", UNSET))

        def _parse_school_management_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_management_url = _parse_school_management_url(
            d.pop("school_management_url", UNSET)
        )

        def _parse_school_organisation_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_organisation_en = _parse_school_organisation_en(
            d.pop("school_organisation_en", UNSET)
        )

        def _parse_school_organisation_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_organisation_tc = _parse_school_organisation_tc(
            d.pop("school_organisation_tc", UNSET)
        )

        def _parse_imc_smc_mc_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        imc_smc_mc_en = _parse_imc_smc_mc_en(d.pop("imc_smc_mc_en", UNSET))

        def _parse_imc_smc_mc_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        imc_smc_mc_tc = _parse_imc_smc_mc_tc(d.pop("imc_smc_mc_tc", UNSET))

        def _parse_school_green_policy_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_green_policy_en = _parse_school_green_policy_en(
            d.pop("school_green_policy_en", UNSET)
        )

        def _parse_school_green_policy_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_green_policy_tc = _parse_school_green_policy_tc(
            d.pop("school_green_policy_tc", UNSET)
        )

        def _parse_school_major_concerns_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_major_concerns_url = _parse_school_major_concerns_url(
            d.pop("school_major_concerns_url", UNSET)
        )

        def _parse_school_major_concerns_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_major_concerns_en = _parse_school_major_concerns_en(
            d.pop("school_major_concerns_en", UNSET)
        )

        def _parse_school_major_concerns_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_major_concerns_tc = _parse_school_major_concerns_tc(
            d.pop("school_major_concerns_tc", UNSET)
        )

        def _parse_learning_and_teaching_plan_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        learning_and_teaching_plan_url = _parse_learning_and_teaching_plan_url(
            d.pop("learning_and_teaching_plan_url", UNSET)
        )

        def _parse_learning_and_teaching_strategies_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        learning_and_teaching_strategies_en = (
            _parse_learning_and_teaching_strategies_en(
                d.pop("learning_and_teaching_strategies_en", UNSET)
            )
        )

        def _parse_learning_and_teaching_strategies_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        learning_and_teaching_strategies_tc = (
            _parse_learning_and_teaching_strategies_tc(
                d.pop("learning_and_teaching_strategies_tc", UNSET)
            )
        )

        def _parse_major_renewed_emphases_pri_edu_curriculum_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        major_renewed_emphases_pri_edu_curriculum_en = (
            _parse_major_renewed_emphases_pri_edu_curriculum_en(
                d.pop("major_renewed_emphases_pri_edu_curriculum_en", UNSET)
            )
        )

        def _parse_major_renewed_emphases_pri_edu_curriculum_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        major_renewed_emphases_pri_edu_curriculum_tc = (
            _parse_major_renewed_emphases_pri_edu_curriculum_tc(
                d.pop("major_renewed_emphases_pri_edu_curriculum_tc", UNSET)
            )
        )

        def _parse_dev_of_generic_skills_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dev_of_generic_skills_en = _parse_dev_of_generic_skills_en(
            d.pop("dev_of_generic_skills_en", UNSET)
        )

        def _parse_dev_of_generic_skills_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dev_of_generic_skills_tc = _parse_dev_of_generic_skills_tc(
            d.pop("dev_of_generic_skills_tc", UNSET)
        )

        def _parse_cultivation_of_proper_values_attitudes_and_behaviours_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cultivation_of_proper_values_attitudes_and_behaviours_en = (
            _parse_cultivation_of_proper_values_attitudes_and_behaviours_en(
                d.pop("cultivation_of_proper_values_attitudes_and_behaviours_en", UNSET)
            )
        )

        def _parse_cultivation_of_proper_values_attitudes_and_behaviours_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cultivation_of_proper_values_attitudes_and_behaviours_tc = (
            _parse_cultivation_of_proper_values_attitudes_and_behaviours_tc(
                d.pop("cultivation_of_proper_values_attitudes_and_behaviours_tc", UNSET)
            )
        )

        def _parse_student_support_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        student_support_url = _parse_student_support_url(
            d.pop("student_support_url", UNSET)
        )

        def _parse_whole_school_approach_cater_for_learner_diversity_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        whole_school_approach_cater_for_learner_diversity_en = (
            _parse_whole_school_approach_cater_for_learner_diversity_en(
                d.pop("whole_school_approach_cater_for_learner_diversity_en", UNSET)
            )
        )

        def _parse_whole_school_approach_cater_for_learner_diversity_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        whole_school_approach_cater_for_learner_diversity_tc = (
            _parse_whole_school_approach_cater_for_learner_diversity_tc(
                d.pop("whole_school_approach_cater_for_learner_diversity_tc", UNSET)
            )
        )

        def _parse_whole_school_approach_integrated_education_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        whole_school_approach_integrated_education_en = (
            _parse_whole_school_approach_integrated_education_en(
                d.pop("whole_school_approach_integrated_education_en", UNSET)
            )
        )

        def _parse_whole_school_approach_integrated_education_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        whole_school_approach_integrated_education_tc = (
            _parse_whole_school_approach_integrated_education_tc(
                d.pop("whole_school_approach_integrated_education_tc", UNSET)
            )
        )

        def _parse_support_for_non_chinese_students_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_for_non_chinese_students_en = (
            _parse_support_for_non_chinese_students_en(
                d.pop("support_for_non_chinese_students_en", UNSET)
            )
        )

        def _parse_support_for_non_chinese_students_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_for_non_chinese_students_tc = (
            _parse_support_for_non_chinese_students_tc(
                d.pop("support_for_non_chinese_students_tc", UNSET)
            )
        )

        def _parse_curriculum_tailoring_and_adaptation_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        curriculum_tailoring_and_adaptation_en = (
            _parse_curriculum_tailoring_and_adaptation_en(
                d.pop("curriculum_tailoring_and_adaptation_en", UNSET)
            )
        )

        def _parse_curriculum_tailoring_and_adaptation_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        curriculum_tailoring_and_adaptation_tc = (
            _parse_curriculum_tailoring_and_adaptation_tc(
                d.pop("curriculum_tailoring_and_adaptation_tc", UNSET)
            )
        )

        def _parse_home_school_cooperation_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        home_school_cooperation_url = _parse_home_school_cooperation_url(
            d.pop("home_school_cooperation_url", UNSET)
        )

        def _parse_home_school_cooperation_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        home_school_cooperation_en = _parse_home_school_cooperation_en(
            d.pop("home_school_cooperation_en", UNSET)
        )

        def _parse_home_school_cooperation_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        home_school_cooperation_tc = _parse_home_school_cooperation_tc(
            d.pop("home_school_cooperation_tc", UNSET)
        )

        def _parse_school_ethos_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_ethos_en = _parse_school_ethos_en(d.pop("school_ethos_en", UNSET))

        def _parse_school_ethos_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_ethos_tc = _parse_school_ethos_tc(d.pop("school_ethos_tc", UNSET))

        def _parse_future_dev_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        future_dev_url = _parse_future_dev_url(d.pop("future_dev_url", UNSET))

        def _parse_school_dev_plan_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_dev_plan_en = _parse_school_dev_plan_en(
            d.pop("school_dev_plan_en", UNSET)
        )

        def _parse_school_dev_plan_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_dev_plan_tc = _parse_school_dev_plan_tc(
            d.pop("school_dev_plan_tc", UNSET)
        )

        def _parse_teacher_pro_training_and_dev_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        teacher_pro_training_and_dev_en = _parse_teacher_pro_training_and_dev_en(
            d.pop("teacher_pro_training_and_dev_en", UNSET)
        )

        def _parse_teacher_pro_training_and_dev_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        teacher_pro_training_and_dev_tc = _parse_teacher_pro_training_and_dev_tc(
            d.pop("teacher_pro_training_and_dev_tc", UNSET)
        )

        def _parse_school_character_others_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_character_others_en = _parse_school_character_others_en(
            d.pop("school_character_others_en", UNSET)
        )

        def _parse_school_character_others_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_character_others_tc = _parse_school_character_others_tc(
            d.pop("school_character_others_tc", UNSET)
        )

        def _parse_fee_remission_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fee_remission_en = _parse_fee_remission_en(d.pop("fee_remission_en", UNSET))

        def _parse_fee_remission_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fee_remission_tc = _parse_fee_remission_tc(d.pop("fee_remission_tc", UNSET))

        def _parse_northing(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        northing = _parse_northing(d.pop("northing", UNSET))

        def _parse_easting(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        easting = _parse_easting(d.pop("easting", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfs_p_school_profiles_attributes = cls(
            feature_member_owns=feature_member_owns,
            fid=fid,
            id=id,
            district_en=district_en,
            district_tc=district_tc,
            school_name_en=school_name_en,
            school_name_tc=school_name_tc,
            school_address_en=school_address_en,
            school_address_tc=school_address_tc,
            poa_school_net=poa_school_net,
            school_tel=school_tel,
            school_fax=school_fax,
            school_email=school_email,
            school_website=school_website,
            school_type_1_en=school_type_1_en,
            school_type_1_tc=school_type_1_tc,
            school_type_2_en=school_type_2_en,
            school_type_2_tc=school_type_2_tc,
            imc_en=imc_en,
            imc_tc=imc_tc,
            training_compliance_rate_supervisor_managers_smc_chair_members=training_compliance_rate_supervisor_managers_smc_chair_members,
            name_supervisor_chairman_of_mc_en=name_supervisor_chairman_of_mc_en,
            name_supervisor_chairman_of_mc_tc=name_supervisor_chairman_of_mc_tc,
            title_supervisor_chairman_of_mc_en=title_supervisor_chairman_of_mc_en,
            title_supervisor_chairman_of_mc_tc=title_supervisor_chairman_of_mc_tc,
            name_of_school_head_en=name_of_school_head_en,
            name_of_school_head_tc=name_of_school_head_tc,
            title_of_school_head_en=title_of_school_head_en,
            title_of_school_head_tc=title_of_school_head_tc,
            student_gender_en=student_gender_en,
            student_gender_tc=student_gender_tc,
            sponsoring_body_en=sponsoring_body_en,
            sponsoring_body_tc=sponsoring_body_tc,
            commencement_of_operation_year=commencement_of_operation_year,
            religion_en=religion_en,
            religion_tc=religion_tc,
            other_religion_en=other_religion_en,
            other_religion_tc=other_religion_tc,
            school_motto_en=school_motto_en,
            school_motto_tc=school_motto_tc,
            school_size=school_size,
            medium_of_instruction_en=medium_of_instruction_en,
            medium_of_instruction_tc=medium_of_instruction_tc,
            through_train_sec_school_en=through_train_sec_school_en,
            through_train_sec_school_tc=through_train_sec_school_tc,
            feeder_sec_school_en=feeder_sec_school_en,
            feeder_sec_school_tc=feeder_sec_school_tc,
            nominated_sec_school_en=nominated_sec_school_en,
            nominated_sec_school_tc=nominated_sec_school_tc,
            school_bus_en=school_bus_en,
            school_bus_tc=school_bus_tc,
            nanny_van_en=nanny_van_en,
            nanny_van_tc=nanny_van_tc,
            parent_teacher_association_en=parent_teacher_association_en,
            parent_teacher_association_tc=parent_teacher_association_tc,
            school_alumni_association_en=school_alumni_association_en,
            school_alumni_association_tc=school_alumni_association_tc,
            four_rs_mental_health_charter=four_rs_mental_health_charter,
            whole_school_health_programme=whole_school_health_programme,
            asc_school_fee_en=asc_school_fee_en,
            asc_school_fee_tc=asc_school_fee_tc,
            asc_tong_fai=asc_tong_fai,
            asc_pta_fee_en=asc_pta_fee_en,
            asc_pta_fee_tc=asc_pta_fee_tc,
            asc_charges_for_non_standard_items_en=asc_charges_for_non_standard_items_en,
            asc_charges_for_non_standard_items_tc=asc_charges_for_non_standard_items_tc,
            asc_others_en=asc_others_en,
            asc_others_tc=asc_others_tc,
            fac_no_of_classroom=fac_no_of_classroom,
            fac_no_of_school_hall=fac_no_of_school_hall,
            fac_no_of_playground=fac_no_of_playground,
            fac_no_of_library=fac_no_of_library,
            fac_special_rooms_en=fac_special_rooms_en,
            fac_special_rooms_tc=fac_special_rooms_tc,
            fac_others_en=fac_others_en,
            fac_others_tc=fac_others_tc,
            fac_support_for_specialedu_en=fac_support_for_specialedu_en,
            fac_support_for_specialedu_tc=fac_support_for_specialedu_tc,
            previous_year_tsi_no_of_approved_teaching_posts=previous_year_tsi_no_of_approved_teaching_posts,
            previous_year_tsi_total_no_of_teachers=previous_year_tsi_total_no_of_teachers,
            previous_year_tsi_percent_of_received_teacher_training=previous_year_tsi_percent_of_received_teacher_training,
            previous_year_tsi_percent_of_bacherlor=previous_year_tsi_percent_of_bacherlor,
            previous_year_tsi_percent_of_master_doctorate_or_above=previous_year_tsi_percent_of_master_doctorate_or_above,
            previous_year_tsi_percent_of_special_edu_training=previous_year_tsi_percent_of_special_edu_training,
            previous_year_tsi_percent_of_exp_0_4=previous_year_tsi_percent_of_exp_0_4,
            previous_year_tsi_percent_of_exp_5_9=previous_year_tsi_percent_of_exp_5_9,
            previous_year_tsi_percent_of_exp_10_or_above=previous_year_tsi_percent_of_exp_10_or_above,
            previous_year_no_of_class_p1=previous_year_no_of_class_p1,
            previous_year_no_of_class_p2=previous_year_no_of_class_p2,
            previous_year_no_of_class_p3=previous_year_no_of_class_p3,
            previous_year_no_of_class_p4=previous_year_no_of_class_p4,
            previous_year_no_of_class_p5=previous_year_no_of_class_p5,
            previous_year_no_of_class_p6=previous_year_no_of_class_p6,
            previous_year_no_of_class_total=previous_year_no_of_class_total,
            current_year_no_of_class_p1=current_year_no_of_class_p1,
            current_year_no_of_class_p2=current_year_no_of_class_p2,
            current_year_no_of_class_p3=current_year_no_of_class_p3,
            current_year_no_of_class_p4=current_year_no_of_class_p4,
            current_year_no_of_class_p5=current_year_no_of_class_p5,
            current_year_no_of_class_p6=current_year_no_of_class_p6,
            current_year_no_of_class_total=current_year_no_of_class_total,
            cs_mode_of_teaching_en=cs_mode_of_teaching_en,
            cs_mode_of_teaching_tc=cs_mode_of_teaching_tc,
            cs_remarks_en=cs_remarks_en,
            cs_remarks_tc=cs_remarks_tc,
            no_of_test_per_year_p1=no_of_test_per_year_p1,
            no_of_exam_per_year_p1=no_of_exam_per_year_p1,
            replace_test_exam_p1_en=replace_test_exam_p1_en,
            replace_test_exam_p1_tc=replace_test_exam_p1_tc,
            no_of_test_per_year_p2_p6=no_of_test_per_year_p2_p6,
            no_of_exam_p2_p6=no_of_exam_p2_p6,
            fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_en=fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_en,
            fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_tc=fm_apt_sch_based_asmt_asgm_policy_inform_collect_views_rgly_tc,
            upload_school_assessment_policy_to_school_web_en=upload_school_assessment_policy_to_school_web_en,
            upload_school_assessment_policy_to_school_web_tc=upload_school_assessment_policy_to_school_web_tc,
            upload_school_assignment_policy_to_school_web_en=upload_school_assignment_policy_to_school_web_en,
            upload_school_assignment_policy_to_school_web_tc=upload_school_assignment_policy_to_school_web_tc,
            diversified_assessment_en=diversified_assessment_en,
            diversified_assessment_tc=diversified_assessment_tc,
            avoid_test_exam_after_long_holidays_en=avoid_test_exam_after_long_holidays_en,
            avoid_test_exam_after_long_holidays_tc=avoid_test_exam_after_long_holidays_tc,
            arrange_timetable_flexibly_tutorial_session_in_afternoon_en=arrange_timetable_flexibly_tutorial_session_in_afternoon_en,
            arrange_timetable_flexibly_tutorial_session_in_afternoon_tc=arrange_timetable_flexibly_tutorial_session_in_afternoon_tc,
            streaming_arrangement_en=streaming_arrangement_en,
            streaming_arrangement_tc=streaming_arrangement_tc,
            no_of_school_days_per_week=no_of_school_days_per_week,
            no_of_periods_per_day=no_of_periods_per_day,
            duration_of_each_period=duration_of_each_period,
            school_starts_at=school_starts_at,
            school_starts_at_ampm_en=school_starts_at_ampm_en,
            school_starts_at_ampm_tc=school_starts_at_ampm_tc,
            school_ends_at=school_ends_at,
            school_ends_at_ampm_en=school_ends_at_ampm_en,
            school_ends_at_ampm_tc=school_ends_at_ampm_tc,
            lunch_start_time=lunch_start_time,
            lunch_end_time=lunch_end_time,
            lunch_arrangement_en=lunch_arrangement_en,
            lunch_arrangement_tc=lunch_arrangement_tc,
            healthy_school_life_en=healthy_school_life_en,
            healthy_school_life_tc=healthy_school_life_tc,
            school_life_remarks_en=school_life_remarks_en,
            school_life_remarks_tc=school_life_remarks_tc,
            life_wide_learning_en=life_wide_learning_en,
            life_wide_learning_tc=life_wide_learning_tc,
            school_mission_en=school_mission_en,
            school_mission_tc=school_mission_tc,
            school_management_url=school_management_url,
            school_organisation_en=school_organisation_en,
            school_organisation_tc=school_organisation_tc,
            imc_smc_mc_en=imc_smc_mc_en,
            imc_smc_mc_tc=imc_smc_mc_tc,
            school_green_policy_en=school_green_policy_en,
            school_green_policy_tc=school_green_policy_tc,
            school_major_concerns_url=school_major_concerns_url,
            school_major_concerns_en=school_major_concerns_en,
            school_major_concerns_tc=school_major_concerns_tc,
            learning_and_teaching_plan_url=learning_and_teaching_plan_url,
            learning_and_teaching_strategies_en=learning_and_teaching_strategies_en,
            learning_and_teaching_strategies_tc=learning_and_teaching_strategies_tc,
            major_renewed_emphases_pri_edu_curriculum_en=major_renewed_emphases_pri_edu_curriculum_en,
            major_renewed_emphases_pri_edu_curriculum_tc=major_renewed_emphases_pri_edu_curriculum_tc,
            dev_of_generic_skills_en=dev_of_generic_skills_en,
            dev_of_generic_skills_tc=dev_of_generic_skills_tc,
            cultivation_of_proper_values_attitudes_and_behaviours_en=cultivation_of_proper_values_attitudes_and_behaviours_en,
            cultivation_of_proper_values_attitudes_and_behaviours_tc=cultivation_of_proper_values_attitudes_and_behaviours_tc,
            student_support_url=student_support_url,
            whole_school_approach_cater_for_learner_diversity_en=whole_school_approach_cater_for_learner_diversity_en,
            whole_school_approach_cater_for_learner_diversity_tc=whole_school_approach_cater_for_learner_diversity_tc,
            whole_school_approach_integrated_education_en=whole_school_approach_integrated_education_en,
            whole_school_approach_integrated_education_tc=whole_school_approach_integrated_education_tc,
            support_for_non_chinese_students_en=support_for_non_chinese_students_en,
            support_for_non_chinese_students_tc=support_for_non_chinese_students_tc,
            curriculum_tailoring_and_adaptation_en=curriculum_tailoring_and_adaptation_en,
            curriculum_tailoring_and_adaptation_tc=curriculum_tailoring_and_adaptation_tc,
            home_school_cooperation_url=home_school_cooperation_url,
            home_school_cooperation_en=home_school_cooperation_en,
            home_school_cooperation_tc=home_school_cooperation_tc,
            school_ethos_en=school_ethos_en,
            school_ethos_tc=school_ethos_tc,
            future_dev_url=future_dev_url,
            school_dev_plan_en=school_dev_plan_en,
            school_dev_plan_tc=school_dev_plan_tc,
            teacher_pro_training_and_dev_en=teacher_pro_training_and_dev_en,
            teacher_pro_training_and_dev_tc=teacher_pro_training_and_dev_tc,
            school_character_others_en=school_character_others_en,
            school_character_others_tc=school_character_others_tc,
            fee_remission_en=fee_remission_en,
            fee_remission_tc=fee_remission_tc,
            northing=northing,
            easting=easting,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfs_p_school_profiles_attributes.additional_properties = d
        return wfs_map_server_wfs_p_school_profiles_attributes

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
