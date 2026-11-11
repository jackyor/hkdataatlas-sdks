from typing import Literal

RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsdbOdataVieworalquestionschiFilter = Literal[
    "MeetingDate ge datetime'2012-10-01' and MeetingDate lt datetime'2016-10-01'"
]

RETRIEVE_ORAL_QUESTIONS_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_CHINESE_VERSION_QUESTIONSDB_ODATA_VIEWORALQUESTIONSCHI_FILTER_VALUES: set[
    RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsdbOdataVieworalquestionschiFilter
] = {
    "MeetingDate ge datetime'2012-10-01' and MeetingDate lt datetime'2016-10-01'",
}


def check_retrieve_oral_questions_of_the_fifth_legislative_council_20122016_chinese_version_questionsdb_odata_vieworalquestionschi_filter(
    value: str,
) -> RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsdbOdataVieworalquestionschiFilter:
    if (
        value
        in RETRIEVE_ORAL_QUESTIONS_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_CHINESE_VERSION_QUESTIONSDB_ODATA_VIEWORALQUESTIONSCHI_FILTER_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETRIEVE_ORAL_QUESTIONS_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_CHINESE_VERSION_QUESTIONSDB_ODATA_VIEWORALQUESTIONSCHI_FILTER_VALUES!r}"
    )
