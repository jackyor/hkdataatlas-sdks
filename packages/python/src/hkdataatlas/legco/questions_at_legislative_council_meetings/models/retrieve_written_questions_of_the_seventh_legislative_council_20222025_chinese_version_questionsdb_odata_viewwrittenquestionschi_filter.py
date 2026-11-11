from typing import Literal

RetrieveWrittenQuestionsOfTheSeventhLegislativeCouncil20222025ChineseVersionQuestionsdbOdataViewwrittenquestionschiFilter = Literal[
    "MeetingDate ge datetime'2022-01-01' and MeetingDate lt datetime'2026-01-01'"
]

RETRIEVE_WRITTEN_QUESTIONS_OF_THE_SEVENTH_LEGISLATIVE_COUNCIL_20222025_CHINESE_VERSION_QUESTIONSDB_ODATA_VIEWWRITTENQUESTIONSCHI_FILTER_VALUES: set[
    RetrieveWrittenQuestionsOfTheSeventhLegislativeCouncil20222025ChineseVersionQuestionsdbOdataViewwrittenquestionschiFilter
] = {
    "MeetingDate ge datetime'2022-01-01' and MeetingDate lt datetime'2026-01-01'",
}


def check_retrieve_written_questions_of_the_seventh_legislative_council_20222025_chinese_version_questionsdb_odata_viewwrittenquestionschi_filter(
    value: str,
) -> RetrieveWrittenQuestionsOfTheSeventhLegislativeCouncil20222025ChineseVersionQuestionsdbOdataViewwrittenquestionschiFilter:
    if (
        value
        in RETRIEVE_WRITTEN_QUESTIONS_OF_THE_SEVENTH_LEGISLATIVE_COUNCIL_20222025_CHINESE_VERSION_QUESTIONSDB_ODATA_VIEWWRITTENQUESTIONSCHI_FILTER_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETRIEVE_WRITTEN_QUESTIONS_OF_THE_SEVENTH_LEGISLATIVE_COUNCIL_20222025_CHINESE_VERSION_QUESTIONSDB_ODATA_VIEWWRITTENQUESTIONSCHI_FILTER_VALUES!r}"
    )
