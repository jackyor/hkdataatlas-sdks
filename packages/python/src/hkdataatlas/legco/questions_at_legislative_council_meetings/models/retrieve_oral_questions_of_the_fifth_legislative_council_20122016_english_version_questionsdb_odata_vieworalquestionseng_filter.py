from typing import Literal

RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016EnglishVersionQuestionsdbOdataVieworalquestionsengFilter = Literal[
    "MeetingDate ge datetime'2012-10-01' and MeetingDate lt datetime'2016-10-01'"
]

RETRIEVE_ORAL_QUESTIONS_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_ENGLISH_VERSION_QUESTIONSDB_ODATA_VIEWORALQUESTIONSENG_FILTER_VALUES: set[
    RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016EnglishVersionQuestionsdbOdataVieworalquestionsengFilter
] = {
    "MeetingDate ge datetime'2012-10-01' and MeetingDate lt datetime'2016-10-01'",
}


def check_retrieve_oral_questions_of_the_fifth_legislative_council_20122016_english_version_questionsdb_odata_vieworalquestionseng_filter(
    value: str,
) -> RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016EnglishVersionQuestionsdbOdataVieworalquestionsengFilter:
    if (
        value
        in RETRIEVE_ORAL_QUESTIONS_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_ENGLISH_VERSION_QUESTIONSDB_ODATA_VIEWORALQUESTIONSENG_FILTER_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETRIEVE_ORAL_QUESTIONS_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_ENGLISH_VERSION_QUESTIONSDB_ODATA_VIEWORALQUESTIONSENG_FILTER_VALUES!r}"
    )
