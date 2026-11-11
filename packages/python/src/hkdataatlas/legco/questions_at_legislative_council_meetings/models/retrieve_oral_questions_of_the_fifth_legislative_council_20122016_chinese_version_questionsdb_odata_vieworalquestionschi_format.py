from typing import Literal

RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsdbOdataVieworalquestionschiFormat = Literal[
    "xml"
]

RETRIEVE_ORAL_QUESTIONS_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_CHINESE_VERSION_QUESTIONSDB_ODATA_VIEWORALQUESTIONSCHI_FORMAT_VALUES: set[
    RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsdbOdataVieworalquestionschiFormat
] = {
    "xml",
}


def check_retrieve_oral_questions_of_the_fifth_legislative_council_20122016_chinese_version_questionsdb_odata_vieworalquestionschi_format(
    value: str,
) -> RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsdbOdataVieworalquestionschiFormat:
    if (
        value
        in RETRIEVE_ORAL_QUESTIONS_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_CHINESE_VERSION_QUESTIONSDB_ODATA_VIEWORALQUESTIONSCHI_FORMAT_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETRIEVE_ORAL_QUESTIONS_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_CHINESE_VERSION_QUESTIONSDB_ODATA_VIEWORALQUESTIONSCHI_FORMAT_VALUES!r}"
    )
