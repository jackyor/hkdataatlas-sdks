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
        fid (None | str | Unset): Publisher field type: esriFieldTypeString
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        school_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        school_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        school_address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        school_address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        school_tel (None | str | Unset): Publisher field type: esriFieldTypeString
        school_fax (None | str | Unset): Publisher field type: esriFieldTypeString
        school_email (None | str | Unset): Publisher field type: esriFieldTypeString
        school_website (None | str | Unset): Publisher field type: esriFieldTypeString
        school_mission_en (None | str | Unset): Publisher field type: esriFieldTypeString
        school_mission_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_supervisor_chairman_of_mc_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_supervisor_chairman_of_mc_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        title_supervisor_chairman_of_mc_en (None | str | Unset): Publisher field type: esriFieldTypeString
        title_supervisor_chairman_of_mc_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_principal_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_principal_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        title_of_principal_en (None | str | Unset): Publisher field type: esriFieldTypeString
        title_of_principal_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        principal_qualifications_experiences_en (None | str | Unset): Publisher field type: esriFieldTypeString
        principal_qualifications_experiences_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        school_type_en (None | str | Unset): Publisher field type: esriFieldTypeString
        school_type_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        student_gender_en (None | str | Unset): Publisher field type: esriFieldTypeString
        student_gender_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        imc_en (None | str | Unset): Publisher field type: esriFieldTypeString
        imc_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        training_compliance_rate_supervisor_managers_smc_chair_members (None | str | Unset): Publisher field type:
            esriFieldTypeString
        school_size (None | str | Unset): Publisher field type: esriFieldTypeString
        sponsoring_body_en (None | str | Unset): Publisher field type: esriFieldTypeString
        sponsoring_body_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        religion_en (None | str | Unset): Publisher field type: esriFieldTypeString
        religion_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        other_religion_en (None | str | Unset): Publisher field type: esriFieldTypeString
        other_religion_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        commencement_of_operation_year (None | str | Unset): Publisher field type: esriFieldTypeString
        school_motto_en (None | str | Unset): Publisher field type: esriFieldTypeString
        school_motto_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        parent_teacher_association_en (None | str | Unset): Publisher field type: esriFieldTypeString
        parent_teacher_association_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        student_union_association_en (None | str | Unset): Publisher field type: esriFieldTypeString
        student_union_association_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        school_alumni_association_en (None | str | Unset): Publisher field type: esriFieldTypeString
        school_alumni_association_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        tsi_no_of_approved_teaching_posts (None | str | Unset): Publisher field type: esriFieldTypeString
        tsi_total_no_of_teachers (None | str | Unset): Publisher field type: esriFieldTypeString
        tsi_percent_of_received_teacher_training (None | str | Unset): Publisher field type: esriFieldTypeString
        tsi_percent_of_bachelor (None | str | Unset): Publisher field type: esriFieldTypeString
        tsi_percent_of_master_doctorate_or_above (None | str | Unset): Publisher field type: esriFieldTypeString
        tsi_percent_of_special_edu_training (None | str | Unset): Publisher field type: esriFieldTypeString
        tsi_percent_of_exp_0_4 (None | str | Unset): Publisher field type: esriFieldTypeString
        tsi_percent_of_exp_5_9 (None | str | Unset): Publisher field type: esriFieldTypeString
        tsi_percent_of_exp_10_or_above (None | str | Unset): Publisher field type: esriFieldTypeString
        current_year_subject_offered_by_chinese_s1_to_s3_en (None | str | Unset): Publisher field type:
            esriFieldTypeString
        current_year_subject_offered_by_chinese_s1_to_s3_tc (None | str | Unset): Publisher field type:
            esriFieldTypeString
        current_year_subject_offered_by_english_s1_to_s3_en (None | str | Unset): Publisher field type:
            esriFieldTypeString
        current_year_subject_offered_by_english_s1_to_s3_tc (None | str | Unset): Publisher field type:
            esriFieldTypeString
        current_year_subject_offered_others_s1_to_s3_en (None | str | Unset): Publisher field type: esriFieldTypeString
        current_year_subject_offered_others_s1_to_s3_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        current_year_subject_offered_by_chinese_s4_to_s6_en (None | str | Unset): Publisher field type:
            esriFieldTypeString
        current_year_subject_offered_by_chinese_s4_to_s6_tc (None | str | Unset): Publisher field type:
            esriFieldTypeString
        current_year_subject_offered_by_english_s4_to_s6_en (None | str | Unset): Publisher field type:
            esriFieldTypeString
        current_year_subject_offered_by_english_s4_to_s6_tc (None | str | Unset): Publisher field type:
            esriFieldTypeString
        current_year_subject_offered_others_s4_to_s6_en (None | str | Unset): Publisher field type: esriFieldTypeString
        current_year_subject_offered_others_s4_to_s6_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        next_year_subject_offered_by_chinese_s1_to_s3_en (None | str | Unset): Publisher field type: esriFieldTypeString
        next_year_subject_offered_by_chinese_s1_to_s3_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        next_year_subject_offered_by_english_s1_to_s3_en (None | str | Unset): Publisher field type: esriFieldTypeString
        next_year_subject_offered_by_english_s1_to_s3_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        next_year_subject_offered_others_s1_to_s3_en (None | str | Unset): Publisher field type: esriFieldTypeString
        next_year_subject_offered_others_s1_to_s3_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        next_year_subject_offered_by_chinese_s4_to_s6_en (None | str | Unset): Publisher field type: esriFieldTypeString
        next_year_subject_offered_by_chinese_s4_to_s6_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        next_year_subject_offered_by_english_s4_to_s6_en (None | str | Unset): Publisher field type: esriFieldTypeString
        next_year_subject_offered_by_english_s4_to_s6_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        next_year_subject_offered_others_s4_to_s6_en (None | str | Unset): Publisher field type: esriFieldTypeString
        next_year_subject_offered_others_s4_to_s6_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        current_year_no_of_class_s1 (None | str | Unset): Publisher field type: esriFieldTypeString
        current_year_no_of_class_s2 (None | str | Unset): Publisher field type: esriFieldTypeString
        current_year_no_of_class_s3 (None | str | Unset): Publisher field type: esriFieldTypeString
        current_year_no_of_class_s4 (None | str | Unset): Publisher field type: esriFieldTypeString
        current_year_no_of_class_s5 (None | str | Unset): Publisher field type: esriFieldTypeString
        current_year_no_of_class_s6 (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_school_fee_s1 (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_school_fee_s2 (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_school_fee_s3 (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_school_fee_s4 (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_school_fee_s5 (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_school_fee_s6 (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_tong_fai_s1 (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_tong_fai_s2 (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_tong_fai_s3 (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_tong_fai_s4 (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_tong_fai_s5 (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_tong_fai_s6 (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_pta_fee_en (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_pta_fee_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_student_union_association_fee_en (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_student_union_association_fee_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_charges_for_non_standard_items_en (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_charges_for_non_standard_items_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_others_en (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_others_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_remarks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_remarks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        oa_s1_admission_en (None | str | Unset): Publisher field type: esriFieldTypeString
        oa_s1_admission_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        oa_orientation_activities_n_healthy_life_en (None | str | Unset): Publisher field type: esriFieldTypeString
        oa_orientation_activities_n_healthy_life_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        school_management_url (None | str | Unset): Publisher field type: esriFieldTypeString
        school_major_concerns_url (None | str | Unset): Publisher field type: esriFieldTypeString
        school_major_concerns_en (None | str | Unset): Publisher field type: esriFieldTypeString
        school_major_concerns_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        school_organisation_en (None | str | Unset): Publisher field type: esriFieldTypeString
        school_organisation_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        imc_smc_mc_en (None | str | Unset): Publisher field type: esriFieldTypeString
        imc_smc_mc_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        school_green_policy_en (None | str | Unset): Publisher field type: esriFieldTypeString
        school_green_policy_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        learning_and_teaching_plan_url (None | str | Unset): Publisher field type: esriFieldTypeString
        language_policy_en (None | str | Unset): Publisher field type: esriFieldTypeString
        language_policy_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        learning_and_teaching_strategies_en (None | str | Unset): Publisher field type: esriFieldTypeString
        learning_and_teaching_strategies_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        school_based_curriculum_en (None | str | Unset): Publisher field type: esriFieldTypeString
        school_based_curriculum_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        major_renewed_emphases_in_the_school_curriculum_en (None | str | Unset): Publisher field type:
            esriFieldTypeString
        major_renewed_emphases_in_the_school_curriculum_tc (None | str | Unset): Publisher field type:
            esriFieldTypeString
        life_planning_education_en (None | str | Unset): Publisher field type: esriFieldTypeString
        life_planning_education_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        student_support_url (None | str | Unset): Publisher field type: esriFieldTypeString
        whole_school_approach_cater_for_learner_diversity_en (None | str | Unset): Publisher field type:
            esriFieldTypeString
        whole_school_approach_cater_for_learner_diversity_tc (None | str | Unset): Publisher field type:
            esriFieldTypeString
        whole_school_approach_integrated_education_en (None | str | Unset): Publisher field type: esriFieldTypeString
        whole_school_approach_integrated_education_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        support_for_non_chinese_students_en (None | str | Unset): Publisher field type: esriFieldTypeString
        support_for_non_chinese_students_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        adaptation_for_learning_and_assessment_en (None | str | Unset): Publisher field type: esriFieldTypeString
        adaptation_for_learning_and_assessment_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        fee_remission_en (None | str | Unset): Publisher field type: esriFieldTypeString
        fee_remission_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        home_school_co_operation_url (None | str | Unset): Publisher field type: esriFieldTypeString
        home_school_co_operation_en (None | str | Unset): Publisher field type: esriFieldTypeString
        home_school_co_operation_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        school_ethos_en (None | str | Unset): Publisher field type: esriFieldTypeString
        school_ethos_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        future_development_url (None | str | Unset): Publisher field type: esriFieldTypeString
        school_dev_plan_en (None | str | Unset): Publisher field type: esriFieldTypeString
        school_dev_plan_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        teacher_pro_training_and_dev_en (None | str | Unset): Publisher field type: esriFieldTypeString
        teacher_pro_training_and_dev_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        life_wide_learning_en (None | str | Unset): Publisher field type: esriFieldTypeString
        life_wide_learning_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        fac_no_of_classroom (None | str | Unset): Publisher field type: esriFieldTypeString
        fac_school_facilities_en (None | str | Unset): Publisher field type: esriFieldTypeString
        fac_school_facilities_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        fac_facility_for_special_educational_needs_en (None | str | Unset): Publisher field type: esriFieldTypeString
        fac_facility_for_special_educational_needs_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        others_en (None | str | Unset): Publisher field type: esriFieldTypeString
        others_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        direct_public_transportation_to_school_en (None | str | Unset): Publisher field type: esriFieldTypeString
        direct_public_transportation_to_school_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        other_districts_en (None | str | Unset): Publisher field type: esriFieldTypeString
        other_districts_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (None | str | Unset): Publisher field type: esriFieldTypeString
        easting (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    id: None | str | Unset = UNSET
    fid: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    school_name_en: None | str | Unset = UNSET
    school_name_tc: None | str | Unset = UNSET
    school_address_en: None | str | Unset = UNSET
    school_address_tc: None | str | Unset = UNSET
    school_tel: None | str | Unset = UNSET
    school_fax: None | str | Unset = UNSET
    school_email: None | str | Unset = UNSET
    school_website: None | str | Unset = UNSET
    school_mission_en: None | str | Unset = UNSET
    school_mission_tc: None | str | Unset = UNSET
    name_supervisor_chairman_of_mc_en: None | str | Unset = UNSET
    name_supervisor_chairman_of_mc_tc: None | str | Unset = UNSET
    title_supervisor_chairman_of_mc_en: None | str | Unset = UNSET
    title_supervisor_chairman_of_mc_tc: None | str | Unset = UNSET
    name_of_principal_en: None | str | Unset = UNSET
    name_of_principal_tc: None | str | Unset = UNSET
    title_of_principal_en: None | str | Unset = UNSET
    title_of_principal_tc: None | str | Unset = UNSET
    principal_qualifications_experiences_en: None | str | Unset = UNSET
    principal_qualifications_experiences_tc: None | str | Unset = UNSET
    school_type_en: None | str | Unset = UNSET
    school_type_tc: None | str | Unset = UNSET
    student_gender_en: None | str | Unset = UNSET
    student_gender_tc: None | str | Unset = UNSET
    imc_en: None | str | Unset = UNSET
    imc_tc: None | str | Unset = UNSET
    training_compliance_rate_supervisor_managers_smc_chair_members: (
        None | str | Unset
    ) = UNSET
    school_size: None | str | Unset = UNSET
    sponsoring_body_en: None | str | Unset = UNSET
    sponsoring_body_tc: None | str | Unset = UNSET
    religion_en: None | str | Unset = UNSET
    religion_tc: None | str | Unset = UNSET
    other_religion_en: None | str | Unset = UNSET
    other_religion_tc: None | str | Unset = UNSET
    commencement_of_operation_year: None | str | Unset = UNSET
    school_motto_en: None | str | Unset = UNSET
    school_motto_tc: None | str | Unset = UNSET
    parent_teacher_association_en: None | str | Unset = UNSET
    parent_teacher_association_tc: None | str | Unset = UNSET
    student_union_association_en: None | str | Unset = UNSET
    student_union_association_tc: None | str | Unset = UNSET
    school_alumni_association_en: None | str | Unset = UNSET
    school_alumni_association_tc: None | str | Unset = UNSET
    tsi_no_of_approved_teaching_posts: None | str | Unset = UNSET
    tsi_total_no_of_teachers: None | str | Unset = UNSET
    tsi_percent_of_received_teacher_training: None | str | Unset = UNSET
    tsi_percent_of_bachelor: None | str | Unset = UNSET
    tsi_percent_of_master_doctorate_or_above: None | str | Unset = UNSET
    tsi_percent_of_special_edu_training: None | str | Unset = UNSET
    tsi_percent_of_exp_0_4: None | str | Unset = UNSET
    tsi_percent_of_exp_5_9: None | str | Unset = UNSET
    tsi_percent_of_exp_10_or_above: None | str | Unset = UNSET
    current_year_subject_offered_by_chinese_s1_to_s3_en: None | str | Unset = UNSET
    current_year_subject_offered_by_chinese_s1_to_s3_tc: None | str | Unset = UNSET
    current_year_subject_offered_by_english_s1_to_s3_en: None | str | Unset = UNSET
    current_year_subject_offered_by_english_s1_to_s3_tc: None | str | Unset = UNSET
    current_year_subject_offered_others_s1_to_s3_en: None | str | Unset = UNSET
    current_year_subject_offered_others_s1_to_s3_tc: None | str | Unset = UNSET
    current_year_subject_offered_by_chinese_s4_to_s6_en: None | str | Unset = UNSET
    current_year_subject_offered_by_chinese_s4_to_s6_tc: None | str | Unset = UNSET
    current_year_subject_offered_by_english_s4_to_s6_en: None | str | Unset = UNSET
    current_year_subject_offered_by_english_s4_to_s6_tc: None | str | Unset = UNSET
    current_year_subject_offered_others_s4_to_s6_en: None | str | Unset = UNSET
    current_year_subject_offered_others_s4_to_s6_tc: None | str | Unset = UNSET
    next_year_subject_offered_by_chinese_s1_to_s3_en: None | str | Unset = UNSET
    next_year_subject_offered_by_chinese_s1_to_s3_tc: None | str | Unset = UNSET
    next_year_subject_offered_by_english_s1_to_s3_en: None | str | Unset = UNSET
    next_year_subject_offered_by_english_s1_to_s3_tc: None | str | Unset = UNSET
    next_year_subject_offered_others_s1_to_s3_en: None | str | Unset = UNSET
    next_year_subject_offered_others_s1_to_s3_tc: None | str | Unset = UNSET
    next_year_subject_offered_by_chinese_s4_to_s6_en: None | str | Unset = UNSET
    next_year_subject_offered_by_chinese_s4_to_s6_tc: None | str | Unset = UNSET
    next_year_subject_offered_by_english_s4_to_s6_en: None | str | Unset = UNSET
    next_year_subject_offered_by_english_s4_to_s6_tc: None | str | Unset = UNSET
    next_year_subject_offered_others_s4_to_s6_en: None | str | Unset = UNSET
    next_year_subject_offered_others_s4_to_s6_tc: None | str | Unset = UNSET
    current_year_no_of_class_s1: None | str | Unset = UNSET
    current_year_no_of_class_s2: None | str | Unset = UNSET
    current_year_no_of_class_s3: None | str | Unset = UNSET
    current_year_no_of_class_s4: None | str | Unset = UNSET
    current_year_no_of_class_s5: None | str | Unset = UNSET
    current_year_no_of_class_s6: None | str | Unset = UNSET
    sc_school_fee_s1: None | str | Unset = UNSET
    sc_school_fee_s2: None | str | Unset = UNSET
    sc_school_fee_s3: None | str | Unset = UNSET
    sc_school_fee_s4: None | str | Unset = UNSET
    sc_school_fee_s5: None | str | Unset = UNSET
    sc_school_fee_s6: None | str | Unset = UNSET
    sc_tong_fai_s1: None | str | Unset = UNSET
    sc_tong_fai_s2: None | str | Unset = UNSET
    sc_tong_fai_s3: None | str | Unset = UNSET
    sc_tong_fai_s4: None | str | Unset = UNSET
    sc_tong_fai_s5: None | str | Unset = UNSET
    sc_tong_fai_s6: None | str | Unset = UNSET
    sc_pta_fee_en: None | str | Unset = UNSET
    sc_pta_fee_tc: None | str | Unset = UNSET
    sc_student_union_association_fee_en: None | str | Unset = UNSET
    sc_student_union_association_fee_tc: None | str | Unset = UNSET
    sc_charges_for_non_standard_items_en: None | str | Unset = UNSET
    sc_charges_for_non_standard_items_tc: None | str | Unset = UNSET
    sc_others_en: None | str | Unset = UNSET
    sc_others_tc: None | str | Unset = UNSET
    sc_remarks_en: None | str | Unset = UNSET
    sc_remarks_tc: None | str | Unset = UNSET
    oa_s1_admission_en: None | str | Unset = UNSET
    oa_s1_admission_tc: None | str | Unset = UNSET
    oa_orientation_activities_n_healthy_life_en: None | str | Unset = UNSET
    oa_orientation_activities_n_healthy_life_tc: None | str | Unset = UNSET
    school_management_url: None | str | Unset = UNSET
    school_major_concerns_url: None | str | Unset = UNSET
    school_major_concerns_en: None | str | Unset = UNSET
    school_major_concerns_tc: None | str | Unset = UNSET
    school_organisation_en: None | str | Unset = UNSET
    school_organisation_tc: None | str | Unset = UNSET
    imc_smc_mc_en: None | str | Unset = UNSET
    imc_smc_mc_tc: None | str | Unset = UNSET
    school_green_policy_en: None | str | Unset = UNSET
    school_green_policy_tc: None | str | Unset = UNSET
    learning_and_teaching_plan_url: None | str | Unset = UNSET
    language_policy_en: None | str | Unset = UNSET
    language_policy_tc: None | str | Unset = UNSET
    learning_and_teaching_strategies_en: None | str | Unset = UNSET
    learning_and_teaching_strategies_tc: None | str | Unset = UNSET
    school_based_curriculum_en: None | str | Unset = UNSET
    school_based_curriculum_tc: None | str | Unset = UNSET
    major_renewed_emphases_in_the_school_curriculum_en: None | str | Unset = UNSET
    major_renewed_emphases_in_the_school_curriculum_tc: None | str | Unset = UNSET
    life_planning_education_en: None | str | Unset = UNSET
    life_planning_education_tc: None | str | Unset = UNSET
    student_support_url: None | str | Unset = UNSET
    whole_school_approach_cater_for_learner_diversity_en: None | str | Unset = UNSET
    whole_school_approach_cater_for_learner_diversity_tc: None | str | Unset = UNSET
    whole_school_approach_integrated_education_en: None | str | Unset = UNSET
    whole_school_approach_integrated_education_tc: None | str | Unset = UNSET
    support_for_non_chinese_students_en: None | str | Unset = UNSET
    support_for_non_chinese_students_tc: None | str | Unset = UNSET
    adaptation_for_learning_and_assessment_en: None | str | Unset = UNSET
    adaptation_for_learning_and_assessment_tc: None | str | Unset = UNSET
    fee_remission_en: None | str | Unset = UNSET
    fee_remission_tc: None | str | Unset = UNSET
    home_school_co_operation_url: None | str | Unset = UNSET
    home_school_co_operation_en: None | str | Unset = UNSET
    home_school_co_operation_tc: None | str | Unset = UNSET
    school_ethos_en: None | str | Unset = UNSET
    school_ethos_tc: None | str | Unset = UNSET
    future_development_url: None | str | Unset = UNSET
    school_dev_plan_en: None | str | Unset = UNSET
    school_dev_plan_tc: None | str | Unset = UNSET
    teacher_pro_training_and_dev_en: None | str | Unset = UNSET
    teacher_pro_training_and_dev_tc: None | str | Unset = UNSET
    life_wide_learning_en: None | str | Unset = UNSET
    life_wide_learning_tc: None | str | Unset = UNSET
    fac_no_of_classroom: None | str | Unset = UNSET
    fac_school_facilities_en: None | str | Unset = UNSET
    fac_school_facilities_tc: None | str | Unset = UNSET
    fac_facility_for_special_educational_needs_en: None | str | Unset = UNSET
    fac_facility_for_special_educational_needs_tc: None | str | Unset = UNSET
    others_en: None | str | Unset = UNSET
    others_tc: None | str | Unset = UNSET
    direct_public_transportation_to_school_en: None | str | Unset = UNSET
    direct_public_transportation_to_school_tc: None | str | Unset = UNSET
    other_districts_en: None | str | Unset = UNSET
    other_districts_tc: None | str | Unset = UNSET
    northing: None | str | Unset = UNSET
    easting: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        fid: None | str | Unset
        if isinstance(self.fid, Unset):
            fid = UNSET
        else:
            fid = self.fid

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

        name_of_principal_en: None | str | Unset
        if isinstance(self.name_of_principal_en, Unset):
            name_of_principal_en = UNSET
        else:
            name_of_principal_en = self.name_of_principal_en

        name_of_principal_tc: None | str | Unset
        if isinstance(self.name_of_principal_tc, Unset):
            name_of_principal_tc = UNSET
        else:
            name_of_principal_tc = self.name_of_principal_tc

        title_of_principal_en: None | str | Unset
        if isinstance(self.title_of_principal_en, Unset):
            title_of_principal_en = UNSET
        else:
            title_of_principal_en = self.title_of_principal_en

        title_of_principal_tc: None | str | Unset
        if isinstance(self.title_of_principal_tc, Unset):
            title_of_principal_tc = UNSET
        else:
            title_of_principal_tc = self.title_of_principal_tc

        principal_qualifications_experiences_en: None | str | Unset
        if isinstance(self.principal_qualifications_experiences_en, Unset):
            principal_qualifications_experiences_en = UNSET
        else:
            principal_qualifications_experiences_en = (
                self.principal_qualifications_experiences_en
            )

        principal_qualifications_experiences_tc: None | str | Unset
        if isinstance(self.principal_qualifications_experiences_tc, Unset):
            principal_qualifications_experiences_tc = UNSET
        else:
            principal_qualifications_experiences_tc = (
                self.principal_qualifications_experiences_tc
            )

        school_type_en: None | str | Unset
        if isinstance(self.school_type_en, Unset):
            school_type_en = UNSET
        else:
            school_type_en = self.school_type_en

        school_type_tc: None | str | Unset
        if isinstance(self.school_type_tc, Unset):
            school_type_tc = UNSET
        else:
            school_type_tc = self.school_type_tc

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

        school_size: None | str | Unset
        if isinstance(self.school_size, Unset):
            school_size = UNSET
        else:
            school_size = self.school_size

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

        commencement_of_operation_year: None | str | Unset
        if isinstance(self.commencement_of_operation_year, Unset):
            commencement_of_operation_year = UNSET
        else:
            commencement_of_operation_year = self.commencement_of_operation_year

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

        student_union_association_en: None | str | Unset
        if isinstance(self.student_union_association_en, Unset):
            student_union_association_en = UNSET
        else:
            student_union_association_en = self.student_union_association_en

        student_union_association_tc: None | str | Unset
        if isinstance(self.student_union_association_tc, Unset):
            student_union_association_tc = UNSET
        else:
            student_union_association_tc = self.student_union_association_tc

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

        tsi_no_of_approved_teaching_posts: None | str | Unset
        if isinstance(self.tsi_no_of_approved_teaching_posts, Unset):
            tsi_no_of_approved_teaching_posts = UNSET
        else:
            tsi_no_of_approved_teaching_posts = self.tsi_no_of_approved_teaching_posts

        tsi_total_no_of_teachers: None | str | Unset
        if isinstance(self.tsi_total_no_of_teachers, Unset):
            tsi_total_no_of_teachers = UNSET
        else:
            tsi_total_no_of_teachers = self.tsi_total_no_of_teachers

        tsi_percent_of_received_teacher_training: None | str | Unset
        if isinstance(self.tsi_percent_of_received_teacher_training, Unset):
            tsi_percent_of_received_teacher_training = UNSET
        else:
            tsi_percent_of_received_teacher_training = (
                self.tsi_percent_of_received_teacher_training
            )

        tsi_percent_of_bachelor: None | str | Unset
        if isinstance(self.tsi_percent_of_bachelor, Unset):
            tsi_percent_of_bachelor = UNSET
        else:
            tsi_percent_of_bachelor = self.tsi_percent_of_bachelor

        tsi_percent_of_master_doctorate_or_above: None | str | Unset
        if isinstance(self.tsi_percent_of_master_doctorate_or_above, Unset):
            tsi_percent_of_master_doctorate_or_above = UNSET
        else:
            tsi_percent_of_master_doctorate_or_above = (
                self.tsi_percent_of_master_doctorate_or_above
            )

        tsi_percent_of_special_edu_training: None | str | Unset
        if isinstance(self.tsi_percent_of_special_edu_training, Unset):
            tsi_percent_of_special_edu_training = UNSET
        else:
            tsi_percent_of_special_edu_training = (
                self.tsi_percent_of_special_edu_training
            )

        tsi_percent_of_exp_0_4: None | str | Unset
        if isinstance(self.tsi_percent_of_exp_0_4, Unset):
            tsi_percent_of_exp_0_4 = UNSET
        else:
            tsi_percent_of_exp_0_4 = self.tsi_percent_of_exp_0_4

        tsi_percent_of_exp_5_9: None | str | Unset
        if isinstance(self.tsi_percent_of_exp_5_9, Unset):
            tsi_percent_of_exp_5_9 = UNSET
        else:
            tsi_percent_of_exp_5_9 = self.tsi_percent_of_exp_5_9

        tsi_percent_of_exp_10_or_above: None | str | Unset
        if isinstance(self.tsi_percent_of_exp_10_or_above, Unset):
            tsi_percent_of_exp_10_or_above = UNSET
        else:
            tsi_percent_of_exp_10_or_above = self.tsi_percent_of_exp_10_or_above

        current_year_subject_offered_by_chinese_s1_to_s3_en: None | str | Unset
        if isinstance(self.current_year_subject_offered_by_chinese_s1_to_s3_en, Unset):
            current_year_subject_offered_by_chinese_s1_to_s3_en = UNSET
        else:
            current_year_subject_offered_by_chinese_s1_to_s3_en = (
                self.current_year_subject_offered_by_chinese_s1_to_s3_en
            )

        current_year_subject_offered_by_chinese_s1_to_s3_tc: None | str | Unset
        if isinstance(self.current_year_subject_offered_by_chinese_s1_to_s3_tc, Unset):
            current_year_subject_offered_by_chinese_s1_to_s3_tc = UNSET
        else:
            current_year_subject_offered_by_chinese_s1_to_s3_tc = (
                self.current_year_subject_offered_by_chinese_s1_to_s3_tc
            )

        current_year_subject_offered_by_english_s1_to_s3_en: None | str | Unset
        if isinstance(self.current_year_subject_offered_by_english_s1_to_s3_en, Unset):
            current_year_subject_offered_by_english_s1_to_s3_en = UNSET
        else:
            current_year_subject_offered_by_english_s1_to_s3_en = (
                self.current_year_subject_offered_by_english_s1_to_s3_en
            )

        current_year_subject_offered_by_english_s1_to_s3_tc: None | str | Unset
        if isinstance(self.current_year_subject_offered_by_english_s1_to_s3_tc, Unset):
            current_year_subject_offered_by_english_s1_to_s3_tc = UNSET
        else:
            current_year_subject_offered_by_english_s1_to_s3_tc = (
                self.current_year_subject_offered_by_english_s1_to_s3_tc
            )

        current_year_subject_offered_others_s1_to_s3_en: None | str | Unset
        if isinstance(self.current_year_subject_offered_others_s1_to_s3_en, Unset):
            current_year_subject_offered_others_s1_to_s3_en = UNSET
        else:
            current_year_subject_offered_others_s1_to_s3_en = (
                self.current_year_subject_offered_others_s1_to_s3_en
            )

        current_year_subject_offered_others_s1_to_s3_tc: None | str | Unset
        if isinstance(self.current_year_subject_offered_others_s1_to_s3_tc, Unset):
            current_year_subject_offered_others_s1_to_s3_tc = UNSET
        else:
            current_year_subject_offered_others_s1_to_s3_tc = (
                self.current_year_subject_offered_others_s1_to_s3_tc
            )

        current_year_subject_offered_by_chinese_s4_to_s6_en: None | str | Unset
        if isinstance(self.current_year_subject_offered_by_chinese_s4_to_s6_en, Unset):
            current_year_subject_offered_by_chinese_s4_to_s6_en = UNSET
        else:
            current_year_subject_offered_by_chinese_s4_to_s6_en = (
                self.current_year_subject_offered_by_chinese_s4_to_s6_en
            )

        current_year_subject_offered_by_chinese_s4_to_s6_tc: None | str | Unset
        if isinstance(self.current_year_subject_offered_by_chinese_s4_to_s6_tc, Unset):
            current_year_subject_offered_by_chinese_s4_to_s6_tc = UNSET
        else:
            current_year_subject_offered_by_chinese_s4_to_s6_tc = (
                self.current_year_subject_offered_by_chinese_s4_to_s6_tc
            )

        current_year_subject_offered_by_english_s4_to_s6_en: None | str | Unset
        if isinstance(self.current_year_subject_offered_by_english_s4_to_s6_en, Unset):
            current_year_subject_offered_by_english_s4_to_s6_en = UNSET
        else:
            current_year_subject_offered_by_english_s4_to_s6_en = (
                self.current_year_subject_offered_by_english_s4_to_s6_en
            )

        current_year_subject_offered_by_english_s4_to_s6_tc: None | str | Unset
        if isinstance(self.current_year_subject_offered_by_english_s4_to_s6_tc, Unset):
            current_year_subject_offered_by_english_s4_to_s6_tc = UNSET
        else:
            current_year_subject_offered_by_english_s4_to_s6_tc = (
                self.current_year_subject_offered_by_english_s4_to_s6_tc
            )

        current_year_subject_offered_others_s4_to_s6_en: None | str | Unset
        if isinstance(self.current_year_subject_offered_others_s4_to_s6_en, Unset):
            current_year_subject_offered_others_s4_to_s6_en = UNSET
        else:
            current_year_subject_offered_others_s4_to_s6_en = (
                self.current_year_subject_offered_others_s4_to_s6_en
            )

        current_year_subject_offered_others_s4_to_s6_tc: None | str | Unset
        if isinstance(self.current_year_subject_offered_others_s4_to_s6_tc, Unset):
            current_year_subject_offered_others_s4_to_s6_tc = UNSET
        else:
            current_year_subject_offered_others_s4_to_s6_tc = (
                self.current_year_subject_offered_others_s4_to_s6_tc
            )

        next_year_subject_offered_by_chinese_s1_to_s3_en: None | str | Unset
        if isinstance(self.next_year_subject_offered_by_chinese_s1_to_s3_en, Unset):
            next_year_subject_offered_by_chinese_s1_to_s3_en = UNSET
        else:
            next_year_subject_offered_by_chinese_s1_to_s3_en = (
                self.next_year_subject_offered_by_chinese_s1_to_s3_en
            )

        next_year_subject_offered_by_chinese_s1_to_s3_tc: None | str | Unset
        if isinstance(self.next_year_subject_offered_by_chinese_s1_to_s3_tc, Unset):
            next_year_subject_offered_by_chinese_s1_to_s3_tc = UNSET
        else:
            next_year_subject_offered_by_chinese_s1_to_s3_tc = (
                self.next_year_subject_offered_by_chinese_s1_to_s3_tc
            )

        next_year_subject_offered_by_english_s1_to_s3_en: None | str | Unset
        if isinstance(self.next_year_subject_offered_by_english_s1_to_s3_en, Unset):
            next_year_subject_offered_by_english_s1_to_s3_en = UNSET
        else:
            next_year_subject_offered_by_english_s1_to_s3_en = (
                self.next_year_subject_offered_by_english_s1_to_s3_en
            )

        next_year_subject_offered_by_english_s1_to_s3_tc: None | str | Unset
        if isinstance(self.next_year_subject_offered_by_english_s1_to_s3_tc, Unset):
            next_year_subject_offered_by_english_s1_to_s3_tc = UNSET
        else:
            next_year_subject_offered_by_english_s1_to_s3_tc = (
                self.next_year_subject_offered_by_english_s1_to_s3_tc
            )

        next_year_subject_offered_others_s1_to_s3_en: None | str | Unset
        if isinstance(self.next_year_subject_offered_others_s1_to_s3_en, Unset):
            next_year_subject_offered_others_s1_to_s3_en = UNSET
        else:
            next_year_subject_offered_others_s1_to_s3_en = (
                self.next_year_subject_offered_others_s1_to_s3_en
            )

        next_year_subject_offered_others_s1_to_s3_tc: None | str | Unset
        if isinstance(self.next_year_subject_offered_others_s1_to_s3_tc, Unset):
            next_year_subject_offered_others_s1_to_s3_tc = UNSET
        else:
            next_year_subject_offered_others_s1_to_s3_tc = (
                self.next_year_subject_offered_others_s1_to_s3_tc
            )

        next_year_subject_offered_by_chinese_s4_to_s6_en: None | str | Unset
        if isinstance(self.next_year_subject_offered_by_chinese_s4_to_s6_en, Unset):
            next_year_subject_offered_by_chinese_s4_to_s6_en = UNSET
        else:
            next_year_subject_offered_by_chinese_s4_to_s6_en = (
                self.next_year_subject_offered_by_chinese_s4_to_s6_en
            )

        next_year_subject_offered_by_chinese_s4_to_s6_tc: None | str | Unset
        if isinstance(self.next_year_subject_offered_by_chinese_s4_to_s6_tc, Unset):
            next_year_subject_offered_by_chinese_s4_to_s6_tc = UNSET
        else:
            next_year_subject_offered_by_chinese_s4_to_s6_tc = (
                self.next_year_subject_offered_by_chinese_s4_to_s6_tc
            )

        next_year_subject_offered_by_english_s4_to_s6_en: None | str | Unset
        if isinstance(self.next_year_subject_offered_by_english_s4_to_s6_en, Unset):
            next_year_subject_offered_by_english_s4_to_s6_en = UNSET
        else:
            next_year_subject_offered_by_english_s4_to_s6_en = (
                self.next_year_subject_offered_by_english_s4_to_s6_en
            )

        next_year_subject_offered_by_english_s4_to_s6_tc: None | str | Unset
        if isinstance(self.next_year_subject_offered_by_english_s4_to_s6_tc, Unset):
            next_year_subject_offered_by_english_s4_to_s6_tc = UNSET
        else:
            next_year_subject_offered_by_english_s4_to_s6_tc = (
                self.next_year_subject_offered_by_english_s4_to_s6_tc
            )

        next_year_subject_offered_others_s4_to_s6_en: None | str | Unset
        if isinstance(self.next_year_subject_offered_others_s4_to_s6_en, Unset):
            next_year_subject_offered_others_s4_to_s6_en = UNSET
        else:
            next_year_subject_offered_others_s4_to_s6_en = (
                self.next_year_subject_offered_others_s4_to_s6_en
            )

        next_year_subject_offered_others_s4_to_s6_tc: None | str | Unset
        if isinstance(self.next_year_subject_offered_others_s4_to_s6_tc, Unset):
            next_year_subject_offered_others_s4_to_s6_tc = UNSET
        else:
            next_year_subject_offered_others_s4_to_s6_tc = (
                self.next_year_subject_offered_others_s4_to_s6_tc
            )

        current_year_no_of_class_s1: None | str | Unset
        if isinstance(self.current_year_no_of_class_s1, Unset):
            current_year_no_of_class_s1 = UNSET
        else:
            current_year_no_of_class_s1 = self.current_year_no_of_class_s1

        current_year_no_of_class_s2: None | str | Unset
        if isinstance(self.current_year_no_of_class_s2, Unset):
            current_year_no_of_class_s2 = UNSET
        else:
            current_year_no_of_class_s2 = self.current_year_no_of_class_s2

        current_year_no_of_class_s3: None | str | Unset
        if isinstance(self.current_year_no_of_class_s3, Unset):
            current_year_no_of_class_s3 = UNSET
        else:
            current_year_no_of_class_s3 = self.current_year_no_of_class_s3

        current_year_no_of_class_s4: None | str | Unset
        if isinstance(self.current_year_no_of_class_s4, Unset):
            current_year_no_of_class_s4 = UNSET
        else:
            current_year_no_of_class_s4 = self.current_year_no_of_class_s4

        current_year_no_of_class_s5: None | str | Unset
        if isinstance(self.current_year_no_of_class_s5, Unset):
            current_year_no_of_class_s5 = UNSET
        else:
            current_year_no_of_class_s5 = self.current_year_no_of_class_s5

        current_year_no_of_class_s6: None | str | Unset
        if isinstance(self.current_year_no_of_class_s6, Unset):
            current_year_no_of_class_s6 = UNSET
        else:
            current_year_no_of_class_s6 = self.current_year_no_of_class_s6

        sc_school_fee_s1: None | str | Unset
        if isinstance(self.sc_school_fee_s1, Unset):
            sc_school_fee_s1 = UNSET
        else:
            sc_school_fee_s1 = self.sc_school_fee_s1

        sc_school_fee_s2: None | str | Unset
        if isinstance(self.sc_school_fee_s2, Unset):
            sc_school_fee_s2 = UNSET
        else:
            sc_school_fee_s2 = self.sc_school_fee_s2

        sc_school_fee_s3: None | str | Unset
        if isinstance(self.sc_school_fee_s3, Unset):
            sc_school_fee_s3 = UNSET
        else:
            sc_school_fee_s3 = self.sc_school_fee_s3

        sc_school_fee_s4: None | str | Unset
        if isinstance(self.sc_school_fee_s4, Unset):
            sc_school_fee_s4 = UNSET
        else:
            sc_school_fee_s4 = self.sc_school_fee_s4

        sc_school_fee_s5: None | str | Unset
        if isinstance(self.sc_school_fee_s5, Unset):
            sc_school_fee_s5 = UNSET
        else:
            sc_school_fee_s5 = self.sc_school_fee_s5

        sc_school_fee_s6: None | str | Unset
        if isinstance(self.sc_school_fee_s6, Unset):
            sc_school_fee_s6 = UNSET
        else:
            sc_school_fee_s6 = self.sc_school_fee_s6

        sc_tong_fai_s1: None | str | Unset
        if isinstance(self.sc_tong_fai_s1, Unset):
            sc_tong_fai_s1 = UNSET
        else:
            sc_tong_fai_s1 = self.sc_tong_fai_s1

        sc_tong_fai_s2: None | str | Unset
        if isinstance(self.sc_tong_fai_s2, Unset):
            sc_tong_fai_s2 = UNSET
        else:
            sc_tong_fai_s2 = self.sc_tong_fai_s2

        sc_tong_fai_s3: None | str | Unset
        if isinstance(self.sc_tong_fai_s3, Unset):
            sc_tong_fai_s3 = UNSET
        else:
            sc_tong_fai_s3 = self.sc_tong_fai_s3

        sc_tong_fai_s4: None | str | Unset
        if isinstance(self.sc_tong_fai_s4, Unset):
            sc_tong_fai_s4 = UNSET
        else:
            sc_tong_fai_s4 = self.sc_tong_fai_s4

        sc_tong_fai_s5: None | str | Unset
        if isinstance(self.sc_tong_fai_s5, Unset):
            sc_tong_fai_s5 = UNSET
        else:
            sc_tong_fai_s5 = self.sc_tong_fai_s5

        sc_tong_fai_s6: None | str | Unset
        if isinstance(self.sc_tong_fai_s6, Unset):
            sc_tong_fai_s6 = UNSET
        else:
            sc_tong_fai_s6 = self.sc_tong_fai_s6

        sc_pta_fee_en: None | str | Unset
        if isinstance(self.sc_pta_fee_en, Unset):
            sc_pta_fee_en = UNSET
        else:
            sc_pta_fee_en = self.sc_pta_fee_en

        sc_pta_fee_tc: None | str | Unset
        if isinstance(self.sc_pta_fee_tc, Unset):
            sc_pta_fee_tc = UNSET
        else:
            sc_pta_fee_tc = self.sc_pta_fee_tc

        sc_student_union_association_fee_en: None | str | Unset
        if isinstance(self.sc_student_union_association_fee_en, Unset):
            sc_student_union_association_fee_en = UNSET
        else:
            sc_student_union_association_fee_en = (
                self.sc_student_union_association_fee_en
            )

        sc_student_union_association_fee_tc: None | str | Unset
        if isinstance(self.sc_student_union_association_fee_tc, Unset):
            sc_student_union_association_fee_tc = UNSET
        else:
            sc_student_union_association_fee_tc = (
                self.sc_student_union_association_fee_tc
            )

        sc_charges_for_non_standard_items_en: None | str | Unset
        if isinstance(self.sc_charges_for_non_standard_items_en, Unset):
            sc_charges_for_non_standard_items_en = UNSET
        else:
            sc_charges_for_non_standard_items_en = (
                self.sc_charges_for_non_standard_items_en
            )

        sc_charges_for_non_standard_items_tc: None | str | Unset
        if isinstance(self.sc_charges_for_non_standard_items_tc, Unset):
            sc_charges_for_non_standard_items_tc = UNSET
        else:
            sc_charges_for_non_standard_items_tc = (
                self.sc_charges_for_non_standard_items_tc
            )

        sc_others_en: None | str | Unset
        if isinstance(self.sc_others_en, Unset):
            sc_others_en = UNSET
        else:
            sc_others_en = self.sc_others_en

        sc_others_tc: None | str | Unset
        if isinstance(self.sc_others_tc, Unset):
            sc_others_tc = UNSET
        else:
            sc_others_tc = self.sc_others_tc

        sc_remarks_en: None | str | Unset
        if isinstance(self.sc_remarks_en, Unset):
            sc_remarks_en = UNSET
        else:
            sc_remarks_en = self.sc_remarks_en

        sc_remarks_tc: None | str | Unset
        if isinstance(self.sc_remarks_tc, Unset):
            sc_remarks_tc = UNSET
        else:
            sc_remarks_tc = self.sc_remarks_tc

        oa_s1_admission_en: None | str | Unset
        if isinstance(self.oa_s1_admission_en, Unset):
            oa_s1_admission_en = UNSET
        else:
            oa_s1_admission_en = self.oa_s1_admission_en

        oa_s1_admission_tc: None | str | Unset
        if isinstance(self.oa_s1_admission_tc, Unset):
            oa_s1_admission_tc = UNSET
        else:
            oa_s1_admission_tc = self.oa_s1_admission_tc

        oa_orientation_activities_n_healthy_life_en: None | str | Unset
        if isinstance(self.oa_orientation_activities_n_healthy_life_en, Unset):
            oa_orientation_activities_n_healthy_life_en = UNSET
        else:
            oa_orientation_activities_n_healthy_life_en = (
                self.oa_orientation_activities_n_healthy_life_en
            )

        oa_orientation_activities_n_healthy_life_tc: None | str | Unset
        if isinstance(self.oa_orientation_activities_n_healthy_life_tc, Unset):
            oa_orientation_activities_n_healthy_life_tc = UNSET
        else:
            oa_orientation_activities_n_healthy_life_tc = (
                self.oa_orientation_activities_n_healthy_life_tc
            )

        school_management_url: None | str | Unset
        if isinstance(self.school_management_url, Unset):
            school_management_url = UNSET
        else:
            school_management_url = self.school_management_url

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

        learning_and_teaching_plan_url: None | str | Unset
        if isinstance(self.learning_and_teaching_plan_url, Unset):
            learning_and_teaching_plan_url = UNSET
        else:
            learning_and_teaching_plan_url = self.learning_and_teaching_plan_url

        language_policy_en: None | str | Unset
        if isinstance(self.language_policy_en, Unset):
            language_policy_en = UNSET
        else:
            language_policy_en = self.language_policy_en

        language_policy_tc: None | str | Unset
        if isinstance(self.language_policy_tc, Unset):
            language_policy_tc = UNSET
        else:
            language_policy_tc = self.language_policy_tc

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

        school_based_curriculum_en: None | str | Unset
        if isinstance(self.school_based_curriculum_en, Unset):
            school_based_curriculum_en = UNSET
        else:
            school_based_curriculum_en = self.school_based_curriculum_en

        school_based_curriculum_tc: None | str | Unset
        if isinstance(self.school_based_curriculum_tc, Unset):
            school_based_curriculum_tc = UNSET
        else:
            school_based_curriculum_tc = self.school_based_curriculum_tc

        major_renewed_emphases_in_the_school_curriculum_en: None | str | Unset
        if isinstance(self.major_renewed_emphases_in_the_school_curriculum_en, Unset):
            major_renewed_emphases_in_the_school_curriculum_en = UNSET
        else:
            major_renewed_emphases_in_the_school_curriculum_en = (
                self.major_renewed_emphases_in_the_school_curriculum_en
            )

        major_renewed_emphases_in_the_school_curriculum_tc: None | str | Unset
        if isinstance(self.major_renewed_emphases_in_the_school_curriculum_tc, Unset):
            major_renewed_emphases_in_the_school_curriculum_tc = UNSET
        else:
            major_renewed_emphases_in_the_school_curriculum_tc = (
                self.major_renewed_emphases_in_the_school_curriculum_tc
            )

        life_planning_education_en: None | str | Unset
        if isinstance(self.life_planning_education_en, Unset):
            life_planning_education_en = UNSET
        else:
            life_planning_education_en = self.life_planning_education_en

        life_planning_education_tc: None | str | Unset
        if isinstance(self.life_planning_education_tc, Unset):
            life_planning_education_tc = UNSET
        else:
            life_planning_education_tc = self.life_planning_education_tc

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

        adaptation_for_learning_and_assessment_en: None | str | Unset
        if isinstance(self.adaptation_for_learning_and_assessment_en, Unset):
            adaptation_for_learning_and_assessment_en = UNSET
        else:
            adaptation_for_learning_and_assessment_en = (
                self.adaptation_for_learning_and_assessment_en
            )

        adaptation_for_learning_and_assessment_tc: None | str | Unset
        if isinstance(self.adaptation_for_learning_and_assessment_tc, Unset):
            adaptation_for_learning_and_assessment_tc = UNSET
        else:
            adaptation_for_learning_and_assessment_tc = (
                self.adaptation_for_learning_and_assessment_tc
            )

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

        home_school_co_operation_url: None | str | Unset
        if isinstance(self.home_school_co_operation_url, Unset):
            home_school_co_operation_url = UNSET
        else:
            home_school_co_operation_url = self.home_school_co_operation_url

        home_school_co_operation_en: None | str | Unset
        if isinstance(self.home_school_co_operation_en, Unset):
            home_school_co_operation_en = UNSET
        else:
            home_school_co_operation_en = self.home_school_co_operation_en

        home_school_co_operation_tc: None | str | Unset
        if isinstance(self.home_school_co_operation_tc, Unset):
            home_school_co_operation_tc = UNSET
        else:
            home_school_co_operation_tc = self.home_school_co_operation_tc

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

        future_development_url: None | str | Unset
        if isinstance(self.future_development_url, Unset):
            future_development_url = UNSET
        else:
            future_development_url = self.future_development_url

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

        fac_no_of_classroom: None | str | Unset
        if isinstance(self.fac_no_of_classroom, Unset):
            fac_no_of_classroom = UNSET
        else:
            fac_no_of_classroom = self.fac_no_of_classroom

        fac_school_facilities_en: None | str | Unset
        if isinstance(self.fac_school_facilities_en, Unset):
            fac_school_facilities_en = UNSET
        else:
            fac_school_facilities_en = self.fac_school_facilities_en

        fac_school_facilities_tc: None | str | Unset
        if isinstance(self.fac_school_facilities_tc, Unset):
            fac_school_facilities_tc = UNSET
        else:
            fac_school_facilities_tc = self.fac_school_facilities_tc

        fac_facility_for_special_educational_needs_en: None | str | Unset
        if isinstance(self.fac_facility_for_special_educational_needs_en, Unset):
            fac_facility_for_special_educational_needs_en = UNSET
        else:
            fac_facility_for_special_educational_needs_en = (
                self.fac_facility_for_special_educational_needs_en
            )

        fac_facility_for_special_educational_needs_tc: None | str | Unset
        if isinstance(self.fac_facility_for_special_educational_needs_tc, Unset):
            fac_facility_for_special_educational_needs_tc = UNSET
        else:
            fac_facility_for_special_educational_needs_tc = (
                self.fac_facility_for_special_educational_needs_tc
            )

        others_en: None | str | Unset
        if isinstance(self.others_en, Unset):
            others_en = UNSET
        else:
            others_en = self.others_en

        others_tc: None | str | Unset
        if isinstance(self.others_tc, Unset):
            others_tc = UNSET
        else:
            others_tc = self.others_tc

        direct_public_transportation_to_school_en: None | str | Unset
        if isinstance(self.direct_public_transportation_to_school_en, Unset):
            direct_public_transportation_to_school_en = UNSET
        else:
            direct_public_transportation_to_school_en = (
                self.direct_public_transportation_to_school_en
            )

        direct_public_transportation_to_school_tc: None | str | Unset
        if isinstance(self.direct_public_transportation_to_school_tc, Unset):
            direct_public_transportation_to_school_tc = UNSET
        else:
            direct_public_transportation_to_school_tc = (
                self.direct_public_transportation_to_school_tc
            )

        other_districts_en: None | str | Unset
        if isinstance(self.other_districts_en, Unset):
            other_districts_en = UNSET
        else:
            other_districts_en = self.other_districts_en

        other_districts_tc: None | str | Unset
        if isinstance(self.other_districts_tc, Unset):
            other_districts_tc = UNSET
        else:
            other_districts_tc = self.other_districts_tc

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if fid is not UNSET:
            field_dict["fid"] = fid
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
        if school_tel is not UNSET:
            field_dict["school_tel"] = school_tel
        if school_fax is not UNSET:
            field_dict["school_fax"] = school_fax
        if school_email is not UNSET:
            field_dict["school_email"] = school_email
        if school_website is not UNSET:
            field_dict["school_website"] = school_website
        if school_mission_en is not UNSET:
            field_dict["school_mission_en"] = school_mission_en
        if school_mission_tc is not UNSET:
            field_dict["school_mission_tc"] = school_mission_tc
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
        if name_of_principal_en is not UNSET:
            field_dict["name_of_principal_en"] = name_of_principal_en
        if name_of_principal_tc is not UNSET:
            field_dict["name_of_principal_tc"] = name_of_principal_tc
        if title_of_principal_en is not UNSET:
            field_dict["title_of_principal_en"] = title_of_principal_en
        if title_of_principal_tc is not UNSET:
            field_dict["title_of_principal_tc"] = title_of_principal_tc
        if principal_qualifications_experiences_en is not UNSET:
            field_dict["principal_qualifications_experiences_en"] = (
                principal_qualifications_experiences_en
            )
        if principal_qualifications_experiences_tc is not UNSET:
            field_dict["principal_qualifications_experiences_tc"] = (
                principal_qualifications_experiences_tc
            )
        if school_type_en is not UNSET:
            field_dict["school_type_en"] = school_type_en
        if school_type_tc is not UNSET:
            field_dict["school_type_tc"] = school_type_tc
        if student_gender_en is not UNSET:
            field_dict["student_gender_en"] = student_gender_en
        if student_gender_tc is not UNSET:
            field_dict["student_gender_tc"] = student_gender_tc
        if imc_en is not UNSET:
            field_dict["imc_en"] = imc_en
        if imc_tc is not UNSET:
            field_dict["imc_tc"] = imc_tc
        if training_compliance_rate_supervisor_managers_smc_chair_members is not UNSET:
            field_dict[
                "training_compliance_rate_supervisor_managers_smc_chair_members"
            ] = training_compliance_rate_supervisor_managers_smc_chair_members
        if school_size is not UNSET:
            field_dict["school_size"] = school_size
        if sponsoring_body_en is not UNSET:
            field_dict["sponsoring_body_en"] = sponsoring_body_en
        if sponsoring_body_tc is not UNSET:
            field_dict["sponsoring_body_tc"] = sponsoring_body_tc
        if religion_en is not UNSET:
            field_dict["religion_en"] = religion_en
        if religion_tc is not UNSET:
            field_dict["religion_tc"] = religion_tc
        if other_religion_en is not UNSET:
            field_dict["other_religion_en"] = other_religion_en
        if other_religion_tc is not UNSET:
            field_dict["other_religion_tc"] = other_religion_tc
        if commencement_of_operation_year is not UNSET:
            field_dict["commencement_of_operation_year"] = (
                commencement_of_operation_year
            )
        if school_motto_en is not UNSET:
            field_dict["school_motto_en"] = school_motto_en
        if school_motto_tc is not UNSET:
            field_dict["school_motto_tc"] = school_motto_tc
        if parent_teacher_association_en is not UNSET:
            field_dict["parent_teacher_association_en"] = parent_teacher_association_en
        if parent_teacher_association_tc is not UNSET:
            field_dict["parent_teacher_association_tc"] = parent_teacher_association_tc
        if student_union_association_en is not UNSET:
            field_dict["student_union_association_en"] = student_union_association_en
        if student_union_association_tc is not UNSET:
            field_dict["student_union_association_tc"] = student_union_association_tc
        if school_alumni_association_en is not UNSET:
            field_dict["school_alumni_association_en"] = school_alumni_association_en
        if school_alumni_association_tc is not UNSET:
            field_dict["school_alumni_association_tc"] = school_alumni_association_tc
        if tsi_no_of_approved_teaching_posts is not UNSET:
            field_dict["tsi_no_of_approved_teaching_posts"] = (
                tsi_no_of_approved_teaching_posts
            )
        if tsi_total_no_of_teachers is not UNSET:
            field_dict["tsi_total_no_of_teachers"] = tsi_total_no_of_teachers
        if tsi_percent_of_received_teacher_training is not UNSET:
            field_dict["tsi_percent_of_received_teacher_training"] = (
                tsi_percent_of_received_teacher_training
            )
        if tsi_percent_of_bachelor is not UNSET:
            field_dict["tsi_percent_of_bachelor"] = tsi_percent_of_bachelor
        if tsi_percent_of_master_doctorate_or_above is not UNSET:
            field_dict["tsi_percent_of_master_doctorate_or_above"] = (
                tsi_percent_of_master_doctorate_or_above
            )
        if tsi_percent_of_special_edu_training is not UNSET:
            field_dict["tsi_percent_of_special_edu_training"] = (
                tsi_percent_of_special_edu_training
            )
        if tsi_percent_of_exp_0_4 is not UNSET:
            field_dict["tsi_percent_of_exp_0_4"] = tsi_percent_of_exp_0_4
        if tsi_percent_of_exp_5_9 is not UNSET:
            field_dict["tsi_percent_of_exp_5_9"] = tsi_percent_of_exp_5_9
        if tsi_percent_of_exp_10_or_above is not UNSET:
            field_dict["tsi_percent_of_exp_10_or_above"] = (
                tsi_percent_of_exp_10_or_above
            )
        if current_year_subject_offered_by_chinese_s1_to_s3_en is not UNSET:
            field_dict["current_year_subject_offered_by_chinese_s1_to_s3_en"] = (
                current_year_subject_offered_by_chinese_s1_to_s3_en
            )
        if current_year_subject_offered_by_chinese_s1_to_s3_tc is not UNSET:
            field_dict["current_year_subject_offered_by_chinese_s1_to_s3_tc"] = (
                current_year_subject_offered_by_chinese_s1_to_s3_tc
            )
        if current_year_subject_offered_by_english_s1_to_s3_en is not UNSET:
            field_dict["current_year_subject_offered_by_english_s1_to_s3_en"] = (
                current_year_subject_offered_by_english_s1_to_s3_en
            )
        if current_year_subject_offered_by_english_s1_to_s3_tc is not UNSET:
            field_dict["current_year_subject_offered_by_english_s1_to_s3_tc"] = (
                current_year_subject_offered_by_english_s1_to_s3_tc
            )
        if current_year_subject_offered_others_s1_to_s3_en is not UNSET:
            field_dict["current_year_subject_offered_others_s1_to_s3_en"] = (
                current_year_subject_offered_others_s1_to_s3_en
            )
        if current_year_subject_offered_others_s1_to_s3_tc is not UNSET:
            field_dict["current_year_subject_offered_others_s1_to_s3_tc"] = (
                current_year_subject_offered_others_s1_to_s3_tc
            )
        if current_year_subject_offered_by_chinese_s4_to_s6_en is not UNSET:
            field_dict["current_year_subject_offered_by_chinese_s4_to_s6_en"] = (
                current_year_subject_offered_by_chinese_s4_to_s6_en
            )
        if current_year_subject_offered_by_chinese_s4_to_s6_tc is not UNSET:
            field_dict["current_year_subject_offered_by_chinese_s4_to_s6_tc"] = (
                current_year_subject_offered_by_chinese_s4_to_s6_tc
            )
        if current_year_subject_offered_by_english_s4_to_s6_en is not UNSET:
            field_dict["current_year_subject_offered_by_english_s4_to_s6_en"] = (
                current_year_subject_offered_by_english_s4_to_s6_en
            )
        if current_year_subject_offered_by_english_s4_to_s6_tc is not UNSET:
            field_dict["current_year_subject_offered_by_english_s4_to_s6_tc"] = (
                current_year_subject_offered_by_english_s4_to_s6_tc
            )
        if current_year_subject_offered_others_s4_to_s6_en is not UNSET:
            field_dict["current_year_subject_offered_others_s4_to_s6_en"] = (
                current_year_subject_offered_others_s4_to_s6_en
            )
        if current_year_subject_offered_others_s4_to_s6_tc is not UNSET:
            field_dict["current_year_subject_offered_others_s4_to_s6_tc"] = (
                current_year_subject_offered_others_s4_to_s6_tc
            )
        if next_year_subject_offered_by_chinese_s1_to_s3_en is not UNSET:
            field_dict["next_year_subject_offered_by_chinese_s1_to_s3_en"] = (
                next_year_subject_offered_by_chinese_s1_to_s3_en
            )
        if next_year_subject_offered_by_chinese_s1_to_s3_tc is not UNSET:
            field_dict["next_year_subject_offered_by_chinese_s1_to_s3_tc"] = (
                next_year_subject_offered_by_chinese_s1_to_s3_tc
            )
        if next_year_subject_offered_by_english_s1_to_s3_en is not UNSET:
            field_dict["next_year_subject_offered_by_english_s1_to_s3_en"] = (
                next_year_subject_offered_by_english_s1_to_s3_en
            )
        if next_year_subject_offered_by_english_s1_to_s3_tc is not UNSET:
            field_dict["next_year_subject_offered_by_english_s1_to_s3_tc"] = (
                next_year_subject_offered_by_english_s1_to_s3_tc
            )
        if next_year_subject_offered_others_s1_to_s3_en is not UNSET:
            field_dict["next_year_subject_offered_others_s1_to_s3_en"] = (
                next_year_subject_offered_others_s1_to_s3_en
            )
        if next_year_subject_offered_others_s1_to_s3_tc is not UNSET:
            field_dict["next_year_subject_offered_others_s1_to_s3_tc"] = (
                next_year_subject_offered_others_s1_to_s3_tc
            )
        if next_year_subject_offered_by_chinese_s4_to_s6_en is not UNSET:
            field_dict["next_year_subject_offered_by_chinese_s4_to_s6_en"] = (
                next_year_subject_offered_by_chinese_s4_to_s6_en
            )
        if next_year_subject_offered_by_chinese_s4_to_s6_tc is not UNSET:
            field_dict["next_year_subject_offered_by_chinese_s4_to_s6_tc"] = (
                next_year_subject_offered_by_chinese_s4_to_s6_tc
            )
        if next_year_subject_offered_by_english_s4_to_s6_en is not UNSET:
            field_dict["next_year_subject_offered_by_english_s4_to_s6_en"] = (
                next_year_subject_offered_by_english_s4_to_s6_en
            )
        if next_year_subject_offered_by_english_s4_to_s6_tc is not UNSET:
            field_dict["next_year_subject_offered_by_english_s4_to_s6_tc"] = (
                next_year_subject_offered_by_english_s4_to_s6_tc
            )
        if next_year_subject_offered_others_s4_to_s6_en is not UNSET:
            field_dict["next_year_subject_offered_others_s4_to_s6_en"] = (
                next_year_subject_offered_others_s4_to_s6_en
            )
        if next_year_subject_offered_others_s4_to_s6_tc is not UNSET:
            field_dict["next_year_subject_offered_others_s4_to_s6_tc"] = (
                next_year_subject_offered_others_s4_to_s6_tc
            )
        if current_year_no_of_class_s1 is not UNSET:
            field_dict["current_year_no_of_class_s1"] = current_year_no_of_class_s1
        if current_year_no_of_class_s2 is not UNSET:
            field_dict["current_year_no_of_class_s2"] = current_year_no_of_class_s2
        if current_year_no_of_class_s3 is not UNSET:
            field_dict["current_year_no_of_class_s3"] = current_year_no_of_class_s3
        if current_year_no_of_class_s4 is not UNSET:
            field_dict["current_year_no_of_class_s4"] = current_year_no_of_class_s4
        if current_year_no_of_class_s5 is not UNSET:
            field_dict["current_year_no_of_class_s5"] = current_year_no_of_class_s5
        if current_year_no_of_class_s6 is not UNSET:
            field_dict["current_year_no_of_class_s6"] = current_year_no_of_class_s6
        if sc_school_fee_s1 is not UNSET:
            field_dict["sc_school_fee_s1"] = sc_school_fee_s1
        if sc_school_fee_s2 is not UNSET:
            field_dict["sc_school_fee_s2"] = sc_school_fee_s2
        if sc_school_fee_s3 is not UNSET:
            field_dict["sc_school_fee_s3"] = sc_school_fee_s3
        if sc_school_fee_s4 is not UNSET:
            field_dict["sc_school_fee_s4"] = sc_school_fee_s4
        if sc_school_fee_s5 is not UNSET:
            field_dict["sc_school_fee_s5"] = sc_school_fee_s5
        if sc_school_fee_s6 is not UNSET:
            field_dict["sc_school_fee_s6"] = sc_school_fee_s6
        if sc_tong_fai_s1 is not UNSET:
            field_dict["sc_tong_fai_s1"] = sc_tong_fai_s1
        if sc_tong_fai_s2 is not UNSET:
            field_dict["sc_tong_fai_s2"] = sc_tong_fai_s2
        if sc_tong_fai_s3 is not UNSET:
            field_dict["sc_tong_fai_s3"] = sc_tong_fai_s3
        if sc_tong_fai_s4 is not UNSET:
            field_dict["sc_tong_fai_s4"] = sc_tong_fai_s4
        if sc_tong_fai_s5 is not UNSET:
            field_dict["sc_tong_fai_s5"] = sc_tong_fai_s5
        if sc_tong_fai_s6 is not UNSET:
            field_dict["sc_tong_fai_s6"] = sc_tong_fai_s6
        if sc_pta_fee_en is not UNSET:
            field_dict["sc_pta_fee_en"] = sc_pta_fee_en
        if sc_pta_fee_tc is not UNSET:
            field_dict["sc_pta_fee_tc"] = sc_pta_fee_tc
        if sc_student_union_association_fee_en is not UNSET:
            field_dict["sc_student_union_association_fee_en"] = (
                sc_student_union_association_fee_en
            )
        if sc_student_union_association_fee_tc is not UNSET:
            field_dict["sc_student_union_association_fee_tc"] = (
                sc_student_union_association_fee_tc
            )
        if sc_charges_for_non_standard_items_en is not UNSET:
            field_dict["sc_charges_for_non_standard_items_en"] = (
                sc_charges_for_non_standard_items_en
            )
        if sc_charges_for_non_standard_items_tc is not UNSET:
            field_dict["sc_charges_for_non_standard_items_tc"] = (
                sc_charges_for_non_standard_items_tc
            )
        if sc_others_en is not UNSET:
            field_dict["sc_others_en"] = sc_others_en
        if sc_others_tc is not UNSET:
            field_dict["sc_others_tc"] = sc_others_tc
        if sc_remarks_en is not UNSET:
            field_dict["sc_remarks_en"] = sc_remarks_en
        if sc_remarks_tc is not UNSET:
            field_dict["sc_remarks_tc"] = sc_remarks_tc
        if oa_s1_admission_en is not UNSET:
            field_dict["oa_s1_admission_en"] = oa_s1_admission_en
        if oa_s1_admission_tc is not UNSET:
            field_dict["oa_s1_admission_tc"] = oa_s1_admission_tc
        if oa_orientation_activities_n_healthy_life_en is not UNSET:
            field_dict["oa_orientation_activities_n_healthy_life_en"] = (
                oa_orientation_activities_n_healthy_life_en
            )
        if oa_orientation_activities_n_healthy_life_tc is not UNSET:
            field_dict["oa_orientation_activities_n_healthy_life_tc"] = (
                oa_orientation_activities_n_healthy_life_tc
            )
        if school_management_url is not UNSET:
            field_dict["school_management_url"] = school_management_url
        if school_major_concerns_url is not UNSET:
            field_dict["school_major_concerns_url"] = school_major_concerns_url
        if school_major_concerns_en is not UNSET:
            field_dict["school_major_concerns_en"] = school_major_concerns_en
        if school_major_concerns_tc is not UNSET:
            field_dict["school_major_concerns_tc"] = school_major_concerns_tc
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
        if learning_and_teaching_plan_url is not UNSET:
            field_dict["learning_and_teaching_plan_url"] = (
                learning_and_teaching_plan_url
            )
        if language_policy_en is not UNSET:
            field_dict["language_policy_en"] = language_policy_en
        if language_policy_tc is not UNSET:
            field_dict["language_policy_tc"] = language_policy_tc
        if learning_and_teaching_strategies_en is not UNSET:
            field_dict["learning_and_teaching_strategies_en"] = (
                learning_and_teaching_strategies_en
            )
        if learning_and_teaching_strategies_tc is not UNSET:
            field_dict["learning_and_teaching_strategies_tc"] = (
                learning_and_teaching_strategies_tc
            )
        if school_based_curriculum_en is not UNSET:
            field_dict["school_based_curriculum_en"] = school_based_curriculum_en
        if school_based_curriculum_tc is not UNSET:
            field_dict["school_based_curriculum_tc"] = school_based_curriculum_tc
        if major_renewed_emphases_in_the_school_curriculum_en is not UNSET:
            field_dict["major_renewed_emphases_in_the_school_curriculum_en"] = (
                major_renewed_emphases_in_the_school_curriculum_en
            )
        if major_renewed_emphases_in_the_school_curriculum_tc is not UNSET:
            field_dict["major_renewed_emphases_in_the_school_curriculum_tc"] = (
                major_renewed_emphases_in_the_school_curriculum_tc
            )
        if life_planning_education_en is not UNSET:
            field_dict["life_planning_education_en"] = life_planning_education_en
        if life_planning_education_tc is not UNSET:
            field_dict["life_planning_education_tc"] = life_planning_education_tc
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
        if adaptation_for_learning_and_assessment_en is not UNSET:
            field_dict["adaptation_for_learning_and_assessment_en"] = (
                adaptation_for_learning_and_assessment_en
            )
        if adaptation_for_learning_and_assessment_tc is not UNSET:
            field_dict["adaptation_for_learning_and_assessment_tc"] = (
                adaptation_for_learning_and_assessment_tc
            )
        if fee_remission_en is not UNSET:
            field_dict["fee_remission_en"] = fee_remission_en
        if fee_remission_tc is not UNSET:
            field_dict["fee_remission_tc"] = fee_remission_tc
        if home_school_co_operation_url is not UNSET:
            field_dict["home_school_co_operation_url"] = home_school_co_operation_url
        if home_school_co_operation_en is not UNSET:
            field_dict["home_school_co_operation_en"] = home_school_co_operation_en
        if home_school_co_operation_tc is not UNSET:
            field_dict["home_school_co_operation_tc"] = home_school_co_operation_tc
        if school_ethos_en is not UNSET:
            field_dict["school_ethos_en"] = school_ethos_en
        if school_ethos_tc is not UNSET:
            field_dict["school_ethos_tc"] = school_ethos_tc
        if future_development_url is not UNSET:
            field_dict["future_development_url"] = future_development_url
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
        if life_wide_learning_en is not UNSET:
            field_dict["life_wide_learning_en"] = life_wide_learning_en
        if life_wide_learning_tc is not UNSET:
            field_dict["life_wide_learning_tc"] = life_wide_learning_tc
        if fac_no_of_classroom is not UNSET:
            field_dict["fac_no_of_classroom"] = fac_no_of_classroom
        if fac_school_facilities_en is not UNSET:
            field_dict["fac_school_facilities_en"] = fac_school_facilities_en
        if fac_school_facilities_tc is not UNSET:
            field_dict["fac_school_facilities_tc"] = fac_school_facilities_tc
        if fac_facility_for_special_educational_needs_en is not UNSET:
            field_dict["fac_facility_for_special_educational_needs_en"] = (
                fac_facility_for_special_educational_needs_en
            )
        if fac_facility_for_special_educational_needs_tc is not UNSET:
            field_dict["fac_facility_for_special_educational_needs_tc"] = (
                fac_facility_for_special_educational_needs_tc
            )
        if others_en is not UNSET:
            field_dict["others_en"] = others_en
        if others_tc is not UNSET:
            field_dict["others_tc"] = others_tc
        if direct_public_transportation_to_school_en is not UNSET:
            field_dict["direct_public_transportation_to_school_en"] = (
                direct_public_transportation_to_school_en
            )
        if direct_public_transportation_to_school_tc is not UNSET:
            field_dict["direct_public_transportation_to_school_tc"] = (
                direct_public_transportation_to_school_tc
            )
        if other_districts_en is not UNSET:
            field_dict["other_districts_en"] = other_districts_en
        if other_districts_tc is not UNSET:
            field_dict["other_districts_tc"] = other_districts_tc
        if northing is not UNSET:
            field_dict["northing"] = northing
        if easting is not UNSET:
            field_dict["easting"] = easting
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

        id = _parse_id(d.pop("id", UNSET))

        def _parse_fid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fid = _parse_fid(d.pop("fid", UNSET))

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

        def _parse_name_of_principal_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_principal_en = _parse_name_of_principal_en(
            d.pop("name_of_principal_en", UNSET)
        )

        def _parse_name_of_principal_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_principal_tc = _parse_name_of_principal_tc(
            d.pop("name_of_principal_tc", UNSET)
        )

        def _parse_title_of_principal_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_of_principal_en = _parse_title_of_principal_en(
            d.pop("title_of_principal_en", UNSET)
        )

        def _parse_title_of_principal_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_of_principal_tc = _parse_title_of_principal_tc(
            d.pop("title_of_principal_tc", UNSET)
        )

        def _parse_principal_qualifications_experiences_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        principal_qualifications_experiences_en = (
            _parse_principal_qualifications_experiences_en(
                d.pop("principal_qualifications_experiences_en", UNSET)
            )
        )

        def _parse_principal_qualifications_experiences_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        principal_qualifications_experiences_tc = (
            _parse_principal_qualifications_experiences_tc(
                d.pop("principal_qualifications_experiences_tc", UNSET)
            )
        )

        def _parse_school_type_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_type_en = _parse_school_type_en(d.pop("school_type_en", UNSET))

        def _parse_school_type_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_type_tc = _parse_school_type_tc(d.pop("school_type_tc", UNSET))

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

        def _parse_school_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_size = _parse_school_size(d.pop("school_size", UNSET))

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

        def _parse_commencement_of_operation_year(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commencement_of_operation_year = _parse_commencement_of_operation_year(
            d.pop("commencement_of_operation_year", UNSET)
        )

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

        def _parse_student_union_association_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        student_union_association_en = _parse_student_union_association_en(
            d.pop("student_union_association_en", UNSET)
        )

        def _parse_student_union_association_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        student_union_association_tc = _parse_student_union_association_tc(
            d.pop("student_union_association_tc", UNSET)
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

        def _parse_tsi_no_of_approved_teaching_posts(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tsi_no_of_approved_teaching_posts = _parse_tsi_no_of_approved_teaching_posts(
            d.pop("tsi_no_of_approved_teaching_posts", UNSET)
        )

        def _parse_tsi_total_no_of_teachers(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tsi_total_no_of_teachers = _parse_tsi_total_no_of_teachers(
            d.pop("tsi_total_no_of_teachers", UNSET)
        )

        def _parse_tsi_percent_of_received_teacher_training(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tsi_percent_of_received_teacher_training = (
            _parse_tsi_percent_of_received_teacher_training(
                d.pop("tsi_percent_of_received_teacher_training", UNSET)
            )
        )

        def _parse_tsi_percent_of_bachelor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tsi_percent_of_bachelor = _parse_tsi_percent_of_bachelor(
            d.pop("tsi_percent_of_bachelor", UNSET)
        )

        def _parse_tsi_percent_of_master_doctorate_or_above(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tsi_percent_of_master_doctorate_or_above = (
            _parse_tsi_percent_of_master_doctorate_or_above(
                d.pop("tsi_percent_of_master_doctorate_or_above", UNSET)
            )
        )

        def _parse_tsi_percent_of_special_edu_training(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tsi_percent_of_special_edu_training = (
            _parse_tsi_percent_of_special_edu_training(
                d.pop("tsi_percent_of_special_edu_training", UNSET)
            )
        )

        def _parse_tsi_percent_of_exp_0_4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tsi_percent_of_exp_0_4 = _parse_tsi_percent_of_exp_0_4(
            d.pop("tsi_percent_of_exp_0_4", UNSET)
        )

        def _parse_tsi_percent_of_exp_5_9(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tsi_percent_of_exp_5_9 = _parse_tsi_percent_of_exp_5_9(
            d.pop("tsi_percent_of_exp_5_9", UNSET)
        )

        def _parse_tsi_percent_of_exp_10_or_above(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tsi_percent_of_exp_10_or_above = _parse_tsi_percent_of_exp_10_or_above(
            d.pop("tsi_percent_of_exp_10_or_above", UNSET)
        )

        def _parse_current_year_subject_offered_by_chinese_s1_to_s3_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_subject_offered_by_chinese_s1_to_s3_en = (
            _parse_current_year_subject_offered_by_chinese_s1_to_s3_en(
                d.pop("current_year_subject_offered_by_chinese_s1_to_s3_en", UNSET)
            )
        )

        def _parse_current_year_subject_offered_by_chinese_s1_to_s3_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_subject_offered_by_chinese_s1_to_s3_tc = (
            _parse_current_year_subject_offered_by_chinese_s1_to_s3_tc(
                d.pop("current_year_subject_offered_by_chinese_s1_to_s3_tc", UNSET)
            )
        )

        def _parse_current_year_subject_offered_by_english_s1_to_s3_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_subject_offered_by_english_s1_to_s3_en = (
            _parse_current_year_subject_offered_by_english_s1_to_s3_en(
                d.pop("current_year_subject_offered_by_english_s1_to_s3_en", UNSET)
            )
        )

        def _parse_current_year_subject_offered_by_english_s1_to_s3_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_subject_offered_by_english_s1_to_s3_tc = (
            _parse_current_year_subject_offered_by_english_s1_to_s3_tc(
                d.pop("current_year_subject_offered_by_english_s1_to_s3_tc", UNSET)
            )
        )

        def _parse_current_year_subject_offered_others_s1_to_s3_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_subject_offered_others_s1_to_s3_en = (
            _parse_current_year_subject_offered_others_s1_to_s3_en(
                d.pop("current_year_subject_offered_others_s1_to_s3_en", UNSET)
            )
        )

        def _parse_current_year_subject_offered_others_s1_to_s3_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_subject_offered_others_s1_to_s3_tc = (
            _parse_current_year_subject_offered_others_s1_to_s3_tc(
                d.pop("current_year_subject_offered_others_s1_to_s3_tc", UNSET)
            )
        )

        def _parse_current_year_subject_offered_by_chinese_s4_to_s6_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_subject_offered_by_chinese_s4_to_s6_en = (
            _parse_current_year_subject_offered_by_chinese_s4_to_s6_en(
                d.pop("current_year_subject_offered_by_chinese_s4_to_s6_en", UNSET)
            )
        )

        def _parse_current_year_subject_offered_by_chinese_s4_to_s6_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_subject_offered_by_chinese_s4_to_s6_tc = (
            _parse_current_year_subject_offered_by_chinese_s4_to_s6_tc(
                d.pop("current_year_subject_offered_by_chinese_s4_to_s6_tc", UNSET)
            )
        )

        def _parse_current_year_subject_offered_by_english_s4_to_s6_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_subject_offered_by_english_s4_to_s6_en = (
            _parse_current_year_subject_offered_by_english_s4_to_s6_en(
                d.pop("current_year_subject_offered_by_english_s4_to_s6_en", UNSET)
            )
        )

        def _parse_current_year_subject_offered_by_english_s4_to_s6_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_subject_offered_by_english_s4_to_s6_tc = (
            _parse_current_year_subject_offered_by_english_s4_to_s6_tc(
                d.pop("current_year_subject_offered_by_english_s4_to_s6_tc", UNSET)
            )
        )

        def _parse_current_year_subject_offered_others_s4_to_s6_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_subject_offered_others_s4_to_s6_en = (
            _parse_current_year_subject_offered_others_s4_to_s6_en(
                d.pop("current_year_subject_offered_others_s4_to_s6_en", UNSET)
            )
        )

        def _parse_current_year_subject_offered_others_s4_to_s6_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_subject_offered_others_s4_to_s6_tc = (
            _parse_current_year_subject_offered_others_s4_to_s6_tc(
                d.pop("current_year_subject_offered_others_s4_to_s6_tc", UNSET)
            )
        )

        def _parse_next_year_subject_offered_by_chinese_s1_to_s3_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_year_subject_offered_by_chinese_s1_to_s3_en = (
            _parse_next_year_subject_offered_by_chinese_s1_to_s3_en(
                d.pop("next_year_subject_offered_by_chinese_s1_to_s3_en", UNSET)
            )
        )

        def _parse_next_year_subject_offered_by_chinese_s1_to_s3_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_year_subject_offered_by_chinese_s1_to_s3_tc = (
            _parse_next_year_subject_offered_by_chinese_s1_to_s3_tc(
                d.pop("next_year_subject_offered_by_chinese_s1_to_s3_tc", UNSET)
            )
        )

        def _parse_next_year_subject_offered_by_english_s1_to_s3_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_year_subject_offered_by_english_s1_to_s3_en = (
            _parse_next_year_subject_offered_by_english_s1_to_s3_en(
                d.pop("next_year_subject_offered_by_english_s1_to_s3_en", UNSET)
            )
        )

        def _parse_next_year_subject_offered_by_english_s1_to_s3_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_year_subject_offered_by_english_s1_to_s3_tc = (
            _parse_next_year_subject_offered_by_english_s1_to_s3_tc(
                d.pop("next_year_subject_offered_by_english_s1_to_s3_tc", UNSET)
            )
        )

        def _parse_next_year_subject_offered_others_s1_to_s3_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_year_subject_offered_others_s1_to_s3_en = (
            _parse_next_year_subject_offered_others_s1_to_s3_en(
                d.pop("next_year_subject_offered_others_s1_to_s3_en", UNSET)
            )
        )

        def _parse_next_year_subject_offered_others_s1_to_s3_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_year_subject_offered_others_s1_to_s3_tc = (
            _parse_next_year_subject_offered_others_s1_to_s3_tc(
                d.pop("next_year_subject_offered_others_s1_to_s3_tc", UNSET)
            )
        )

        def _parse_next_year_subject_offered_by_chinese_s4_to_s6_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_year_subject_offered_by_chinese_s4_to_s6_en = (
            _parse_next_year_subject_offered_by_chinese_s4_to_s6_en(
                d.pop("next_year_subject_offered_by_chinese_s4_to_s6_en", UNSET)
            )
        )

        def _parse_next_year_subject_offered_by_chinese_s4_to_s6_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_year_subject_offered_by_chinese_s4_to_s6_tc = (
            _parse_next_year_subject_offered_by_chinese_s4_to_s6_tc(
                d.pop("next_year_subject_offered_by_chinese_s4_to_s6_tc", UNSET)
            )
        )

        def _parse_next_year_subject_offered_by_english_s4_to_s6_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_year_subject_offered_by_english_s4_to_s6_en = (
            _parse_next_year_subject_offered_by_english_s4_to_s6_en(
                d.pop("next_year_subject_offered_by_english_s4_to_s6_en", UNSET)
            )
        )

        def _parse_next_year_subject_offered_by_english_s4_to_s6_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_year_subject_offered_by_english_s4_to_s6_tc = (
            _parse_next_year_subject_offered_by_english_s4_to_s6_tc(
                d.pop("next_year_subject_offered_by_english_s4_to_s6_tc", UNSET)
            )
        )

        def _parse_next_year_subject_offered_others_s4_to_s6_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_year_subject_offered_others_s4_to_s6_en = (
            _parse_next_year_subject_offered_others_s4_to_s6_en(
                d.pop("next_year_subject_offered_others_s4_to_s6_en", UNSET)
            )
        )

        def _parse_next_year_subject_offered_others_s4_to_s6_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_year_subject_offered_others_s4_to_s6_tc = (
            _parse_next_year_subject_offered_others_s4_to_s6_tc(
                d.pop("next_year_subject_offered_others_s4_to_s6_tc", UNSET)
            )
        )

        def _parse_current_year_no_of_class_s1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_no_of_class_s1 = _parse_current_year_no_of_class_s1(
            d.pop("current_year_no_of_class_s1", UNSET)
        )

        def _parse_current_year_no_of_class_s2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_no_of_class_s2 = _parse_current_year_no_of_class_s2(
            d.pop("current_year_no_of_class_s2", UNSET)
        )

        def _parse_current_year_no_of_class_s3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_no_of_class_s3 = _parse_current_year_no_of_class_s3(
            d.pop("current_year_no_of_class_s3", UNSET)
        )

        def _parse_current_year_no_of_class_s4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_no_of_class_s4 = _parse_current_year_no_of_class_s4(
            d.pop("current_year_no_of_class_s4", UNSET)
        )

        def _parse_current_year_no_of_class_s5(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_no_of_class_s5 = _parse_current_year_no_of_class_s5(
            d.pop("current_year_no_of_class_s5", UNSET)
        )

        def _parse_current_year_no_of_class_s6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_year_no_of_class_s6 = _parse_current_year_no_of_class_s6(
            d.pop("current_year_no_of_class_s6", UNSET)
        )

        def _parse_sc_school_fee_s1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_school_fee_s1 = _parse_sc_school_fee_s1(d.pop("sc_school_fee_s1", UNSET))

        def _parse_sc_school_fee_s2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_school_fee_s2 = _parse_sc_school_fee_s2(d.pop("sc_school_fee_s2", UNSET))

        def _parse_sc_school_fee_s3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_school_fee_s3 = _parse_sc_school_fee_s3(d.pop("sc_school_fee_s3", UNSET))

        def _parse_sc_school_fee_s4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_school_fee_s4 = _parse_sc_school_fee_s4(d.pop("sc_school_fee_s4", UNSET))

        def _parse_sc_school_fee_s5(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_school_fee_s5 = _parse_sc_school_fee_s5(d.pop("sc_school_fee_s5", UNSET))

        def _parse_sc_school_fee_s6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_school_fee_s6 = _parse_sc_school_fee_s6(d.pop("sc_school_fee_s6", UNSET))

        def _parse_sc_tong_fai_s1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_tong_fai_s1 = _parse_sc_tong_fai_s1(d.pop("sc_tong_fai_s1", UNSET))

        def _parse_sc_tong_fai_s2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_tong_fai_s2 = _parse_sc_tong_fai_s2(d.pop("sc_tong_fai_s2", UNSET))

        def _parse_sc_tong_fai_s3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_tong_fai_s3 = _parse_sc_tong_fai_s3(d.pop("sc_tong_fai_s3", UNSET))

        def _parse_sc_tong_fai_s4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_tong_fai_s4 = _parse_sc_tong_fai_s4(d.pop("sc_tong_fai_s4", UNSET))

        def _parse_sc_tong_fai_s5(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_tong_fai_s5 = _parse_sc_tong_fai_s5(d.pop("sc_tong_fai_s5", UNSET))

        def _parse_sc_tong_fai_s6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_tong_fai_s6 = _parse_sc_tong_fai_s6(d.pop("sc_tong_fai_s6", UNSET))

        def _parse_sc_pta_fee_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_pta_fee_en = _parse_sc_pta_fee_en(d.pop("sc_pta_fee_en", UNSET))

        def _parse_sc_pta_fee_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_pta_fee_tc = _parse_sc_pta_fee_tc(d.pop("sc_pta_fee_tc", UNSET))

        def _parse_sc_student_union_association_fee_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_student_union_association_fee_en = (
            _parse_sc_student_union_association_fee_en(
                d.pop("sc_student_union_association_fee_en", UNSET)
            )
        )

        def _parse_sc_student_union_association_fee_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_student_union_association_fee_tc = (
            _parse_sc_student_union_association_fee_tc(
                d.pop("sc_student_union_association_fee_tc", UNSET)
            )
        )

        def _parse_sc_charges_for_non_standard_items_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_charges_for_non_standard_items_en = (
            _parse_sc_charges_for_non_standard_items_en(
                d.pop("sc_charges_for_non_standard_items_en", UNSET)
            )
        )

        def _parse_sc_charges_for_non_standard_items_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_charges_for_non_standard_items_tc = (
            _parse_sc_charges_for_non_standard_items_tc(
                d.pop("sc_charges_for_non_standard_items_tc", UNSET)
            )
        )

        def _parse_sc_others_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_others_en = _parse_sc_others_en(d.pop("sc_others_en", UNSET))

        def _parse_sc_others_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_others_tc = _parse_sc_others_tc(d.pop("sc_others_tc", UNSET))

        def _parse_sc_remarks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_remarks_en = _parse_sc_remarks_en(d.pop("sc_remarks_en", UNSET))

        def _parse_sc_remarks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_remarks_tc = _parse_sc_remarks_tc(d.pop("sc_remarks_tc", UNSET))

        def _parse_oa_s1_admission_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        oa_s1_admission_en = _parse_oa_s1_admission_en(
            d.pop("oa_s1_admission_en", UNSET)
        )

        def _parse_oa_s1_admission_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        oa_s1_admission_tc = _parse_oa_s1_admission_tc(
            d.pop("oa_s1_admission_tc", UNSET)
        )

        def _parse_oa_orientation_activities_n_healthy_life_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        oa_orientation_activities_n_healthy_life_en = (
            _parse_oa_orientation_activities_n_healthy_life_en(
                d.pop("oa_orientation_activities_n_healthy_life_en", UNSET)
            )
        )

        def _parse_oa_orientation_activities_n_healthy_life_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        oa_orientation_activities_n_healthy_life_tc = (
            _parse_oa_orientation_activities_n_healthy_life_tc(
                d.pop("oa_orientation_activities_n_healthy_life_tc", UNSET)
            )
        )

        def _parse_school_management_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_management_url = _parse_school_management_url(
            d.pop("school_management_url", UNSET)
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

        def _parse_learning_and_teaching_plan_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        learning_and_teaching_plan_url = _parse_learning_and_teaching_plan_url(
            d.pop("learning_and_teaching_plan_url", UNSET)
        )

        def _parse_language_policy_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language_policy_en = _parse_language_policy_en(
            d.pop("language_policy_en", UNSET)
        )

        def _parse_language_policy_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language_policy_tc = _parse_language_policy_tc(
            d.pop("language_policy_tc", UNSET)
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

        def _parse_school_based_curriculum_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_based_curriculum_en = _parse_school_based_curriculum_en(
            d.pop("school_based_curriculum_en", UNSET)
        )

        def _parse_school_based_curriculum_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_based_curriculum_tc = _parse_school_based_curriculum_tc(
            d.pop("school_based_curriculum_tc", UNSET)
        )

        def _parse_major_renewed_emphases_in_the_school_curriculum_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        major_renewed_emphases_in_the_school_curriculum_en = (
            _parse_major_renewed_emphases_in_the_school_curriculum_en(
                d.pop("major_renewed_emphases_in_the_school_curriculum_en", UNSET)
            )
        )

        def _parse_major_renewed_emphases_in_the_school_curriculum_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        major_renewed_emphases_in_the_school_curriculum_tc = (
            _parse_major_renewed_emphases_in_the_school_curriculum_tc(
                d.pop("major_renewed_emphases_in_the_school_curriculum_tc", UNSET)
            )
        )

        def _parse_life_planning_education_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        life_planning_education_en = _parse_life_planning_education_en(
            d.pop("life_planning_education_en", UNSET)
        )

        def _parse_life_planning_education_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        life_planning_education_tc = _parse_life_planning_education_tc(
            d.pop("life_planning_education_tc", UNSET)
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

        def _parse_adaptation_for_learning_and_assessment_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        adaptation_for_learning_and_assessment_en = (
            _parse_adaptation_for_learning_and_assessment_en(
                d.pop("adaptation_for_learning_and_assessment_en", UNSET)
            )
        )

        def _parse_adaptation_for_learning_and_assessment_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        adaptation_for_learning_and_assessment_tc = (
            _parse_adaptation_for_learning_and_assessment_tc(
                d.pop("adaptation_for_learning_and_assessment_tc", UNSET)
            )
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

        def _parse_home_school_co_operation_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        home_school_co_operation_url = _parse_home_school_co_operation_url(
            d.pop("home_school_co_operation_url", UNSET)
        )

        def _parse_home_school_co_operation_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        home_school_co_operation_en = _parse_home_school_co_operation_en(
            d.pop("home_school_co_operation_en", UNSET)
        )

        def _parse_home_school_co_operation_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        home_school_co_operation_tc = _parse_home_school_co_operation_tc(
            d.pop("home_school_co_operation_tc", UNSET)
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

        def _parse_future_development_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        future_development_url = _parse_future_development_url(
            d.pop("future_development_url", UNSET)
        )

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

        def _parse_fac_no_of_classroom(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_no_of_classroom = _parse_fac_no_of_classroom(
            d.pop("fac_no_of_classroom", UNSET)
        )

        def _parse_fac_school_facilities_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_school_facilities_en = _parse_fac_school_facilities_en(
            d.pop("fac_school_facilities_en", UNSET)
        )

        def _parse_fac_school_facilities_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_school_facilities_tc = _parse_fac_school_facilities_tc(
            d.pop("fac_school_facilities_tc", UNSET)
        )

        def _parse_fac_facility_for_special_educational_needs_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_facility_for_special_educational_needs_en = (
            _parse_fac_facility_for_special_educational_needs_en(
                d.pop("fac_facility_for_special_educational_needs_en", UNSET)
            )
        )

        def _parse_fac_facility_for_special_educational_needs_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_facility_for_special_educational_needs_tc = (
            _parse_fac_facility_for_special_educational_needs_tc(
                d.pop("fac_facility_for_special_educational_needs_tc", UNSET)
            )
        )

        def _parse_others_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        others_en = _parse_others_en(d.pop("others_en", UNSET))

        def _parse_others_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        others_tc = _parse_others_tc(d.pop("others_tc", UNSET))

        def _parse_direct_public_transportation_to_school_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        direct_public_transportation_to_school_en = (
            _parse_direct_public_transportation_to_school_en(
                d.pop("direct_public_transportation_to_school_en", UNSET)
            )
        )

        def _parse_direct_public_transportation_to_school_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        direct_public_transportation_to_school_tc = (
            _parse_direct_public_transportation_to_school_tc(
                d.pop("direct_public_transportation_to_school_tc", UNSET)
            )
        )

        def _parse_other_districts_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_districts_en = _parse_other_districts_en(
            d.pop("other_districts_en", UNSET)
        )

        def _parse_other_districts_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_districts_tc = _parse_other_districts_tc(
            d.pop("other_districts_tc", UNSET)
        )

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

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            id=id,
            fid=fid,
            district_en=district_en,
            district_tc=district_tc,
            school_name_en=school_name_en,
            school_name_tc=school_name_tc,
            school_address_en=school_address_en,
            school_address_tc=school_address_tc,
            school_tel=school_tel,
            school_fax=school_fax,
            school_email=school_email,
            school_website=school_website,
            school_mission_en=school_mission_en,
            school_mission_tc=school_mission_tc,
            name_supervisor_chairman_of_mc_en=name_supervisor_chairman_of_mc_en,
            name_supervisor_chairman_of_mc_tc=name_supervisor_chairman_of_mc_tc,
            title_supervisor_chairman_of_mc_en=title_supervisor_chairman_of_mc_en,
            title_supervisor_chairman_of_mc_tc=title_supervisor_chairman_of_mc_tc,
            name_of_principal_en=name_of_principal_en,
            name_of_principal_tc=name_of_principal_tc,
            title_of_principal_en=title_of_principal_en,
            title_of_principal_tc=title_of_principal_tc,
            principal_qualifications_experiences_en=principal_qualifications_experiences_en,
            principal_qualifications_experiences_tc=principal_qualifications_experiences_tc,
            school_type_en=school_type_en,
            school_type_tc=school_type_tc,
            student_gender_en=student_gender_en,
            student_gender_tc=student_gender_tc,
            imc_en=imc_en,
            imc_tc=imc_tc,
            training_compliance_rate_supervisor_managers_smc_chair_members=training_compliance_rate_supervisor_managers_smc_chair_members,
            school_size=school_size,
            sponsoring_body_en=sponsoring_body_en,
            sponsoring_body_tc=sponsoring_body_tc,
            religion_en=religion_en,
            religion_tc=religion_tc,
            other_religion_en=other_religion_en,
            other_religion_tc=other_religion_tc,
            commencement_of_operation_year=commencement_of_operation_year,
            school_motto_en=school_motto_en,
            school_motto_tc=school_motto_tc,
            parent_teacher_association_en=parent_teacher_association_en,
            parent_teacher_association_tc=parent_teacher_association_tc,
            student_union_association_en=student_union_association_en,
            student_union_association_tc=student_union_association_tc,
            school_alumni_association_en=school_alumni_association_en,
            school_alumni_association_tc=school_alumni_association_tc,
            tsi_no_of_approved_teaching_posts=tsi_no_of_approved_teaching_posts,
            tsi_total_no_of_teachers=tsi_total_no_of_teachers,
            tsi_percent_of_received_teacher_training=tsi_percent_of_received_teacher_training,
            tsi_percent_of_bachelor=tsi_percent_of_bachelor,
            tsi_percent_of_master_doctorate_or_above=tsi_percent_of_master_doctorate_or_above,
            tsi_percent_of_special_edu_training=tsi_percent_of_special_edu_training,
            tsi_percent_of_exp_0_4=tsi_percent_of_exp_0_4,
            tsi_percent_of_exp_5_9=tsi_percent_of_exp_5_9,
            tsi_percent_of_exp_10_or_above=tsi_percent_of_exp_10_or_above,
            current_year_subject_offered_by_chinese_s1_to_s3_en=current_year_subject_offered_by_chinese_s1_to_s3_en,
            current_year_subject_offered_by_chinese_s1_to_s3_tc=current_year_subject_offered_by_chinese_s1_to_s3_tc,
            current_year_subject_offered_by_english_s1_to_s3_en=current_year_subject_offered_by_english_s1_to_s3_en,
            current_year_subject_offered_by_english_s1_to_s3_tc=current_year_subject_offered_by_english_s1_to_s3_tc,
            current_year_subject_offered_others_s1_to_s3_en=current_year_subject_offered_others_s1_to_s3_en,
            current_year_subject_offered_others_s1_to_s3_tc=current_year_subject_offered_others_s1_to_s3_tc,
            current_year_subject_offered_by_chinese_s4_to_s6_en=current_year_subject_offered_by_chinese_s4_to_s6_en,
            current_year_subject_offered_by_chinese_s4_to_s6_tc=current_year_subject_offered_by_chinese_s4_to_s6_tc,
            current_year_subject_offered_by_english_s4_to_s6_en=current_year_subject_offered_by_english_s4_to_s6_en,
            current_year_subject_offered_by_english_s4_to_s6_tc=current_year_subject_offered_by_english_s4_to_s6_tc,
            current_year_subject_offered_others_s4_to_s6_en=current_year_subject_offered_others_s4_to_s6_en,
            current_year_subject_offered_others_s4_to_s6_tc=current_year_subject_offered_others_s4_to_s6_tc,
            next_year_subject_offered_by_chinese_s1_to_s3_en=next_year_subject_offered_by_chinese_s1_to_s3_en,
            next_year_subject_offered_by_chinese_s1_to_s3_tc=next_year_subject_offered_by_chinese_s1_to_s3_tc,
            next_year_subject_offered_by_english_s1_to_s3_en=next_year_subject_offered_by_english_s1_to_s3_en,
            next_year_subject_offered_by_english_s1_to_s3_tc=next_year_subject_offered_by_english_s1_to_s3_tc,
            next_year_subject_offered_others_s1_to_s3_en=next_year_subject_offered_others_s1_to_s3_en,
            next_year_subject_offered_others_s1_to_s3_tc=next_year_subject_offered_others_s1_to_s3_tc,
            next_year_subject_offered_by_chinese_s4_to_s6_en=next_year_subject_offered_by_chinese_s4_to_s6_en,
            next_year_subject_offered_by_chinese_s4_to_s6_tc=next_year_subject_offered_by_chinese_s4_to_s6_tc,
            next_year_subject_offered_by_english_s4_to_s6_en=next_year_subject_offered_by_english_s4_to_s6_en,
            next_year_subject_offered_by_english_s4_to_s6_tc=next_year_subject_offered_by_english_s4_to_s6_tc,
            next_year_subject_offered_others_s4_to_s6_en=next_year_subject_offered_others_s4_to_s6_en,
            next_year_subject_offered_others_s4_to_s6_tc=next_year_subject_offered_others_s4_to_s6_tc,
            current_year_no_of_class_s1=current_year_no_of_class_s1,
            current_year_no_of_class_s2=current_year_no_of_class_s2,
            current_year_no_of_class_s3=current_year_no_of_class_s3,
            current_year_no_of_class_s4=current_year_no_of_class_s4,
            current_year_no_of_class_s5=current_year_no_of_class_s5,
            current_year_no_of_class_s6=current_year_no_of_class_s6,
            sc_school_fee_s1=sc_school_fee_s1,
            sc_school_fee_s2=sc_school_fee_s2,
            sc_school_fee_s3=sc_school_fee_s3,
            sc_school_fee_s4=sc_school_fee_s4,
            sc_school_fee_s5=sc_school_fee_s5,
            sc_school_fee_s6=sc_school_fee_s6,
            sc_tong_fai_s1=sc_tong_fai_s1,
            sc_tong_fai_s2=sc_tong_fai_s2,
            sc_tong_fai_s3=sc_tong_fai_s3,
            sc_tong_fai_s4=sc_tong_fai_s4,
            sc_tong_fai_s5=sc_tong_fai_s5,
            sc_tong_fai_s6=sc_tong_fai_s6,
            sc_pta_fee_en=sc_pta_fee_en,
            sc_pta_fee_tc=sc_pta_fee_tc,
            sc_student_union_association_fee_en=sc_student_union_association_fee_en,
            sc_student_union_association_fee_tc=sc_student_union_association_fee_tc,
            sc_charges_for_non_standard_items_en=sc_charges_for_non_standard_items_en,
            sc_charges_for_non_standard_items_tc=sc_charges_for_non_standard_items_tc,
            sc_others_en=sc_others_en,
            sc_others_tc=sc_others_tc,
            sc_remarks_en=sc_remarks_en,
            sc_remarks_tc=sc_remarks_tc,
            oa_s1_admission_en=oa_s1_admission_en,
            oa_s1_admission_tc=oa_s1_admission_tc,
            oa_orientation_activities_n_healthy_life_en=oa_orientation_activities_n_healthy_life_en,
            oa_orientation_activities_n_healthy_life_tc=oa_orientation_activities_n_healthy_life_tc,
            school_management_url=school_management_url,
            school_major_concerns_url=school_major_concerns_url,
            school_major_concerns_en=school_major_concerns_en,
            school_major_concerns_tc=school_major_concerns_tc,
            school_organisation_en=school_organisation_en,
            school_organisation_tc=school_organisation_tc,
            imc_smc_mc_en=imc_smc_mc_en,
            imc_smc_mc_tc=imc_smc_mc_tc,
            school_green_policy_en=school_green_policy_en,
            school_green_policy_tc=school_green_policy_tc,
            learning_and_teaching_plan_url=learning_and_teaching_plan_url,
            language_policy_en=language_policy_en,
            language_policy_tc=language_policy_tc,
            learning_and_teaching_strategies_en=learning_and_teaching_strategies_en,
            learning_and_teaching_strategies_tc=learning_and_teaching_strategies_tc,
            school_based_curriculum_en=school_based_curriculum_en,
            school_based_curriculum_tc=school_based_curriculum_tc,
            major_renewed_emphases_in_the_school_curriculum_en=major_renewed_emphases_in_the_school_curriculum_en,
            major_renewed_emphases_in_the_school_curriculum_tc=major_renewed_emphases_in_the_school_curriculum_tc,
            life_planning_education_en=life_planning_education_en,
            life_planning_education_tc=life_planning_education_tc,
            student_support_url=student_support_url,
            whole_school_approach_cater_for_learner_diversity_en=whole_school_approach_cater_for_learner_diversity_en,
            whole_school_approach_cater_for_learner_diversity_tc=whole_school_approach_cater_for_learner_diversity_tc,
            whole_school_approach_integrated_education_en=whole_school_approach_integrated_education_en,
            whole_school_approach_integrated_education_tc=whole_school_approach_integrated_education_tc,
            support_for_non_chinese_students_en=support_for_non_chinese_students_en,
            support_for_non_chinese_students_tc=support_for_non_chinese_students_tc,
            adaptation_for_learning_and_assessment_en=adaptation_for_learning_and_assessment_en,
            adaptation_for_learning_and_assessment_tc=adaptation_for_learning_and_assessment_tc,
            fee_remission_en=fee_remission_en,
            fee_remission_tc=fee_remission_tc,
            home_school_co_operation_url=home_school_co_operation_url,
            home_school_co_operation_en=home_school_co_operation_en,
            home_school_co_operation_tc=home_school_co_operation_tc,
            school_ethos_en=school_ethos_en,
            school_ethos_tc=school_ethos_tc,
            future_development_url=future_development_url,
            school_dev_plan_en=school_dev_plan_en,
            school_dev_plan_tc=school_dev_plan_tc,
            teacher_pro_training_and_dev_en=teacher_pro_training_and_dev_en,
            teacher_pro_training_and_dev_tc=teacher_pro_training_and_dev_tc,
            life_wide_learning_en=life_wide_learning_en,
            life_wide_learning_tc=life_wide_learning_tc,
            fac_no_of_classroom=fac_no_of_classroom,
            fac_school_facilities_en=fac_school_facilities_en,
            fac_school_facilities_tc=fac_school_facilities_tc,
            fac_facility_for_special_educational_needs_en=fac_facility_for_special_educational_needs_en,
            fac_facility_for_special_educational_needs_tc=fac_facility_for_special_educational_needs_tc,
            others_en=others_en,
            others_tc=others_tc,
            direct_public_transportation_to_school_en=direct_public_transportation_to_school_en,
            direct_public_transportation_to_school_tc=direct_public_transportation_to_school_tc,
            other_districts_en=other_districts_en,
            other_districts_tc=other_districts_tc,
            northing=northing,
            easting=easting,
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
