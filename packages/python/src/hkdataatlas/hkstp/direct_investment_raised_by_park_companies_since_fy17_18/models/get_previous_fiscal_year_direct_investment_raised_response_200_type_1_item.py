from typing import Literal

GetPreviousFiscalYearDirectInvestmentRaisedResponse200Type1Item = Literal[""]

GET_PREVIOUS_FISCAL_YEAR_DIRECT_INVESTMENT_RAISED_RESPONSE_200_TYPE_1_ITEM_VALUES: set[
    GetPreviousFiscalYearDirectInvestmentRaisedResponse200Type1Item
] = {
    "",
}


def check_get_previous_fiscal_year_direct_investment_raised_response_200_type_1_item(
    value: str,
) -> GetPreviousFiscalYearDirectInvestmentRaisedResponse200Type1Item:
    if (
        value
        in GET_PREVIOUS_FISCAL_YEAR_DIRECT_INVESTMENT_RAISED_RESPONSE_200_TYPE_1_ITEM_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_PREVIOUS_FISCAL_YEAR_DIRECT_INVESTMENT_RAISED_RESPONSE_200_TYPE_1_ITEM_VALUES!r}"
    )
