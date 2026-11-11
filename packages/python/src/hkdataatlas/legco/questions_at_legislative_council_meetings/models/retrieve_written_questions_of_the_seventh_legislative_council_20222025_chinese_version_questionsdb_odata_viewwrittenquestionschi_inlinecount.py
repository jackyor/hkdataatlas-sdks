from typing import Literal

RetrieveWrittenQuestionsOfTheSeventhLegislativeCouncil20222025ChineseVersionQuestionsdbOdataViewwrittenquestionschiInlinecount = Literal[
    "allpages"
]

RETRIEVE_WRITTEN_QUESTIONS_OF_THE_SEVENTH_LEGISLATIVE_COUNCIL_20222025_CHINESE_VERSION_QUESTIONSDB_ODATA_VIEWWRITTENQUESTIONSCHI_INLINECOUNT_VALUES: set[
    RetrieveWrittenQuestionsOfTheSeventhLegislativeCouncil20222025ChineseVersionQuestionsdbOdataViewwrittenquestionschiInlinecount
] = {
    "allpages",
}


def check_retrieve_written_questions_of_the_seventh_legislative_council_20222025_chinese_version_questionsdb_odata_viewwrittenquestionschi_inlinecount(
    value: str,
) -> RetrieveWrittenQuestionsOfTheSeventhLegislativeCouncil20222025ChineseVersionQuestionsdbOdataViewwrittenquestionschiInlinecount:
    if (
        value
        in RETRIEVE_WRITTEN_QUESTIONS_OF_THE_SEVENTH_LEGISLATIVE_COUNCIL_20222025_CHINESE_VERSION_QUESTIONSDB_ODATA_VIEWWRITTENQUESTIONSCHI_INLINECOUNT_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETRIEVE_WRITTEN_QUESTIONS_OF_THE_SEVENTH_LEGISLATIVE_COUNCIL_20222025_CHINESE_VERSION_QUESTIONSDB_ODATA_VIEWWRITTENQUESTIONSCHI_INLINECOUNT_VALUES!r}"
    )
