from typing import Literal

RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016EnglishVersionQuestionsdbOdataVieworalquestionsengFormat = Literal[
    "xml"
]

RETRIEVE_ORAL_QUESTIONS_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_ENGLISH_VERSION_QUESTIONSDB_ODATA_VIEWORALQUESTIONSENG_FORMAT_VALUES: set[
    RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016EnglishVersionQuestionsdbOdataVieworalquestionsengFormat
] = {
    "xml",
}


def check_retrieve_oral_questions_of_the_fifth_legislative_council_20122016_english_version_questionsdb_odata_vieworalquestionseng_format(
    value: str,
) -> RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016EnglishVersionQuestionsdbOdataVieworalquestionsengFormat:
    if (
        value
        in RETRIEVE_ORAL_QUESTIONS_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_ENGLISH_VERSION_QUESTIONSDB_ODATA_VIEWORALQUESTIONSENG_FORMAT_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETRIEVE_ORAL_QUESTIONS_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_ENGLISH_VERSION_QUESTIONSDB_ODATA_VIEWORALQUESTIONSENG_FORMAT_VALUES!r}"
    )
