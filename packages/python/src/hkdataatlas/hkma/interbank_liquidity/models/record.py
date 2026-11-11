from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Record")


@_attrs_define
class Record:
    """
    Attributes:
        end_of_date (datetime.date | Unset):
        cu_weakside (float | Unset):
        cu_strongside (float | Unset):
        disc_win_base_rate (float | Unset):
        hibor_overnight (float | Unset):
        hibor_fixing_1m (float | Unset):
        twi (float | Unset):
        opening_balance (float | Unset):
        closing_balance (float | Unset):
        market_activities (str | Unset):
        interest_payment (str | Unset):
        discount_window_reversal (str | Unset):
        discount_window_activities (str | Unset):
        intraday_movements_of_aggregate_balance_at_0930 (float | Unset):
        intraday_movements_of_aggregate_balance_at_1000 (float | Unset):
        intraday_movements_of_aggregate_balance_at_1100 (float | Unset):
        intraday_movements_of_aggregate_balance_at_1200 (float | Unset):
        intraday_movements_of_aggregate_balance_at_1500 (float | Unset):
        intraday_movements_of_aggregate_balance_at_1600 (float | Unset):
        forex_trans_t1 (str | Unset):
        other_market_activities_t1 (str | Unset):
        reversal_of_discount_window_t1 (str | Unset):
        interest_payment_issuance_efbn_t1 (str | Unset):
        forecast_aggregate_bal_t1 (float | Unset):
        forex_trans_t2 (str | Unset):
        other_market_activities_t2 (str | Unset):
        reversal_of_discount_window_t2 (str | Unset):
        interest_payment_issuance_efbn_t2 (str | Unset):
        forecast_aggregate_bal_t2 (float | Unset):
        forex_trans_t3 (str | Unset):
        other_market_activities_t3 (str | Unset):
        reversal_of_discount_window_t3 (str | Unset):
        interest_payment_issuance_efbn_t3 (str | Unset):
        forecast_aggregate_bal_t3 (float | Unset):
        forex_trans_t4 (str | Unset):
        other_market_activities_t4 (str | Unset):
        reversal_of_discount_window_t4 (str | Unset):
        interest_payment_issuance_efbn_t4 (str | Unset):
        forecast_aggregate_bal_t4 (float | Unset):
        forex_trans_u (str | Unset):
        other_market_activities_u (str | Unset):
        reversal_of_discount_window_u (str | Unset):
        interest_payment_issuance_efbn_u (str | Unset):
        forecast_aggregate_bal_u (float | Unset):
    """

    end_of_date: datetime.date | Unset = UNSET
    cu_weakside: float | Unset = UNSET
    cu_strongside: float | Unset = UNSET
    disc_win_base_rate: float | Unset = UNSET
    hibor_overnight: float | Unset = UNSET
    hibor_fixing_1m: float | Unset = UNSET
    twi: float | Unset = UNSET
    opening_balance: float | Unset = UNSET
    closing_balance: float | Unset = UNSET
    market_activities: str | Unset = UNSET
    interest_payment: str | Unset = UNSET
    discount_window_reversal: str | Unset = UNSET
    discount_window_activities: str | Unset = UNSET
    intraday_movements_of_aggregate_balance_at_0930: float | Unset = UNSET
    intraday_movements_of_aggregate_balance_at_1000: float | Unset = UNSET
    intraday_movements_of_aggregate_balance_at_1100: float | Unset = UNSET
    intraday_movements_of_aggregate_balance_at_1200: float | Unset = UNSET
    intraday_movements_of_aggregate_balance_at_1500: float | Unset = UNSET
    intraday_movements_of_aggregate_balance_at_1600: float | Unset = UNSET
    forex_trans_t1: str | Unset = UNSET
    other_market_activities_t1: str | Unset = UNSET
    reversal_of_discount_window_t1: str | Unset = UNSET
    interest_payment_issuance_efbn_t1: str | Unset = UNSET
    forecast_aggregate_bal_t1: float | Unset = UNSET
    forex_trans_t2: str | Unset = UNSET
    other_market_activities_t2: str | Unset = UNSET
    reversal_of_discount_window_t2: str | Unset = UNSET
    interest_payment_issuance_efbn_t2: str | Unset = UNSET
    forecast_aggregate_bal_t2: float | Unset = UNSET
    forex_trans_t3: str | Unset = UNSET
    other_market_activities_t3: str | Unset = UNSET
    reversal_of_discount_window_t3: str | Unset = UNSET
    interest_payment_issuance_efbn_t3: str | Unset = UNSET
    forecast_aggregate_bal_t3: float | Unset = UNSET
    forex_trans_t4: str | Unset = UNSET
    other_market_activities_t4: str | Unset = UNSET
    reversal_of_discount_window_t4: str | Unset = UNSET
    interest_payment_issuance_efbn_t4: str | Unset = UNSET
    forecast_aggregate_bal_t4: float | Unset = UNSET
    forex_trans_u: str | Unset = UNSET
    other_market_activities_u: str | Unset = UNSET
    reversal_of_discount_window_u: str | Unset = UNSET
    interest_payment_issuance_efbn_u: str | Unset = UNSET
    forecast_aggregate_bal_u: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_date: str | Unset = UNSET
        if not isinstance(self.end_of_date, Unset):
            end_of_date = self.end_of_date.isoformat()

        cu_weakside = self.cu_weakside

        cu_strongside = self.cu_strongside

        disc_win_base_rate = self.disc_win_base_rate

        hibor_overnight = self.hibor_overnight

        hibor_fixing_1m = self.hibor_fixing_1m

        twi = self.twi

        opening_balance = self.opening_balance

        closing_balance = self.closing_balance

        market_activities = self.market_activities

        interest_payment = self.interest_payment

        discount_window_reversal = self.discount_window_reversal

        discount_window_activities = self.discount_window_activities

        intraday_movements_of_aggregate_balance_at_0930 = (
            self.intraday_movements_of_aggregate_balance_at_0930
        )

        intraday_movements_of_aggregate_balance_at_1000 = (
            self.intraday_movements_of_aggregate_balance_at_1000
        )

        intraday_movements_of_aggregate_balance_at_1100 = (
            self.intraday_movements_of_aggregate_balance_at_1100
        )

        intraday_movements_of_aggregate_balance_at_1200 = (
            self.intraday_movements_of_aggregate_balance_at_1200
        )

        intraday_movements_of_aggregate_balance_at_1500 = (
            self.intraday_movements_of_aggregate_balance_at_1500
        )

        intraday_movements_of_aggregate_balance_at_1600 = (
            self.intraday_movements_of_aggregate_balance_at_1600
        )

        forex_trans_t1 = self.forex_trans_t1

        other_market_activities_t1 = self.other_market_activities_t1

        reversal_of_discount_window_t1 = self.reversal_of_discount_window_t1

        interest_payment_issuance_efbn_t1 = self.interest_payment_issuance_efbn_t1

        forecast_aggregate_bal_t1 = self.forecast_aggregate_bal_t1

        forex_trans_t2 = self.forex_trans_t2

        other_market_activities_t2 = self.other_market_activities_t2

        reversal_of_discount_window_t2 = self.reversal_of_discount_window_t2

        interest_payment_issuance_efbn_t2 = self.interest_payment_issuance_efbn_t2

        forecast_aggregate_bal_t2 = self.forecast_aggregate_bal_t2

        forex_trans_t3 = self.forex_trans_t3

        other_market_activities_t3 = self.other_market_activities_t3

        reversal_of_discount_window_t3 = self.reversal_of_discount_window_t3

        interest_payment_issuance_efbn_t3 = self.interest_payment_issuance_efbn_t3

        forecast_aggregate_bal_t3 = self.forecast_aggregate_bal_t3

        forex_trans_t4 = self.forex_trans_t4

        other_market_activities_t4 = self.other_market_activities_t4

        reversal_of_discount_window_t4 = self.reversal_of_discount_window_t4

        interest_payment_issuance_efbn_t4 = self.interest_payment_issuance_efbn_t4

        forecast_aggregate_bal_t4 = self.forecast_aggregate_bal_t4

        forex_trans_u = self.forex_trans_u

        other_market_activities_u = self.other_market_activities_u

        reversal_of_discount_window_u = self.reversal_of_discount_window_u

        interest_payment_issuance_efbn_u = self.interest_payment_issuance_efbn_u

        forecast_aggregate_bal_u = self.forecast_aggregate_bal_u

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_date is not UNSET:
            field_dict["end_of_date"] = end_of_date
        if cu_weakside is not UNSET:
            field_dict["cu_weakside"] = cu_weakside
        if cu_strongside is not UNSET:
            field_dict["cu_strongside"] = cu_strongside
        if disc_win_base_rate is not UNSET:
            field_dict["disc_win_base_rate"] = disc_win_base_rate
        if hibor_overnight is not UNSET:
            field_dict["hibor_overnight"] = hibor_overnight
        if hibor_fixing_1m is not UNSET:
            field_dict["hibor_fixing_1m"] = hibor_fixing_1m
        if twi is not UNSET:
            field_dict["twi"] = twi
        if opening_balance is not UNSET:
            field_dict["opening_balance"] = opening_balance
        if closing_balance is not UNSET:
            field_dict["closing_balance"] = closing_balance
        if market_activities is not UNSET:
            field_dict["market_activities"] = market_activities
        if interest_payment is not UNSET:
            field_dict["interest_payment"] = interest_payment
        if discount_window_reversal is not UNSET:
            field_dict["discount_window_reversal"] = discount_window_reversal
        if discount_window_activities is not UNSET:
            field_dict["discount_window_activities"] = discount_window_activities
        if intraday_movements_of_aggregate_balance_at_0930 is not UNSET:
            field_dict["intraday_movements_of_aggregate_balance_at_0930"] = (
                intraday_movements_of_aggregate_balance_at_0930
            )
        if intraday_movements_of_aggregate_balance_at_1000 is not UNSET:
            field_dict["intraday_movements_of_aggregate_balance_at_1000"] = (
                intraday_movements_of_aggregate_balance_at_1000
            )
        if intraday_movements_of_aggregate_balance_at_1100 is not UNSET:
            field_dict["intraday_movements_of_aggregate_balance_at_1100"] = (
                intraday_movements_of_aggregate_balance_at_1100
            )
        if intraday_movements_of_aggregate_balance_at_1200 is not UNSET:
            field_dict["intraday_movements_of_aggregate_balance_at_1200"] = (
                intraday_movements_of_aggregate_balance_at_1200
            )
        if intraday_movements_of_aggregate_balance_at_1500 is not UNSET:
            field_dict["intraday_movements_of_aggregate_balance_at_1500"] = (
                intraday_movements_of_aggregate_balance_at_1500
            )
        if intraday_movements_of_aggregate_balance_at_1600 is not UNSET:
            field_dict["intraday_movements_of_aggregate_balance_at_1600"] = (
                intraday_movements_of_aggregate_balance_at_1600
            )
        if forex_trans_t1 is not UNSET:
            field_dict["forex_trans_t1"] = forex_trans_t1
        if other_market_activities_t1 is not UNSET:
            field_dict["other_market_activities_t1"] = other_market_activities_t1
        if reversal_of_discount_window_t1 is not UNSET:
            field_dict["reversal_of_discount_window_t1"] = (
                reversal_of_discount_window_t1
            )
        if interest_payment_issuance_efbn_t1 is not UNSET:
            field_dict["interest_payment_issuance_efbn_t1"] = (
                interest_payment_issuance_efbn_t1
            )
        if forecast_aggregate_bal_t1 is not UNSET:
            field_dict["forecast_aggregate_bal_t1"] = forecast_aggregate_bal_t1
        if forex_trans_t2 is not UNSET:
            field_dict["forex_trans_t2"] = forex_trans_t2
        if other_market_activities_t2 is not UNSET:
            field_dict["other_market_activities_t2"] = other_market_activities_t2
        if reversal_of_discount_window_t2 is not UNSET:
            field_dict["reversal_of_discount_window_t2"] = (
                reversal_of_discount_window_t2
            )
        if interest_payment_issuance_efbn_t2 is not UNSET:
            field_dict["interest_payment_issuance_efbn_t2"] = (
                interest_payment_issuance_efbn_t2
            )
        if forecast_aggregate_bal_t2 is not UNSET:
            field_dict["forecast_aggregate_bal_t2"] = forecast_aggregate_bal_t2
        if forex_trans_t3 is not UNSET:
            field_dict["forex_trans_t3"] = forex_trans_t3
        if other_market_activities_t3 is not UNSET:
            field_dict["other_market_activities_t3"] = other_market_activities_t3
        if reversal_of_discount_window_t3 is not UNSET:
            field_dict["reversal_of_discount_window_t3"] = (
                reversal_of_discount_window_t3
            )
        if interest_payment_issuance_efbn_t3 is not UNSET:
            field_dict["interest_payment_issuance_efbn_t3"] = (
                interest_payment_issuance_efbn_t3
            )
        if forecast_aggregate_bal_t3 is not UNSET:
            field_dict["forecast_aggregate_bal_t3"] = forecast_aggregate_bal_t3
        if forex_trans_t4 is not UNSET:
            field_dict["forex_trans_t4"] = forex_trans_t4
        if other_market_activities_t4 is not UNSET:
            field_dict["other_market_activities_t4"] = other_market_activities_t4
        if reversal_of_discount_window_t4 is not UNSET:
            field_dict["reversal_of_discount_window_t4"] = (
                reversal_of_discount_window_t4
            )
        if interest_payment_issuance_efbn_t4 is not UNSET:
            field_dict["interest_payment_issuance_efbn_t4"] = (
                interest_payment_issuance_efbn_t4
            )
        if forecast_aggregate_bal_t4 is not UNSET:
            field_dict["forecast_aggregate_bal_t4"] = forecast_aggregate_bal_t4
        if forex_trans_u is not UNSET:
            field_dict["forex_trans_u"] = forex_trans_u
        if other_market_activities_u is not UNSET:
            field_dict["other_market_activities_u"] = other_market_activities_u
        if reversal_of_discount_window_u is not UNSET:
            field_dict["reversal_of_discount_window_u"] = reversal_of_discount_window_u
        if interest_payment_issuance_efbn_u is not UNSET:
            field_dict["interest_payment_issuance_efbn_u"] = (
                interest_payment_issuance_efbn_u
            )
        if forecast_aggregate_bal_u is not UNSET:
            field_dict["forecast_aggregate_bal_u"] = forecast_aggregate_bal_u

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _end_of_date = d.pop("end_of_date", UNSET)
        end_of_date: datetime.date | Unset
        if isinstance(_end_of_date, Unset):
            end_of_date = UNSET
        else:
            end_of_date = datetime.date.fromisoformat(_end_of_date)

        cu_weakside = d.pop("cu_weakside", UNSET)

        cu_strongside = d.pop("cu_strongside", UNSET)

        disc_win_base_rate = d.pop("disc_win_base_rate", UNSET)

        hibor_overnight = d.pop("hibor_overnight", UNSET)

        hibor_fixing_1m = d.pop("hibor_fixing_1m", UNSET)

        twi = d.pop("twi", UNSET)

        opening_balance = d.pop("opening_balance", UNSET)

        closing_balance = d.pop("closing_balance", UNSET)

        market_activities = d.pop("market_activities", UNSET)

        interest_payment = d.pop("interest_payment", UNSET)

        discount_window_reversal = d.pop("discount_window_reversal", UNSET)

        discount_window_activities = d.pop("discount_window_activities", UNSET)

        intraday_movements_of_aggregate_balance_at_0930 = d.pop(
            "intraday_movements_of_aggregate_balance_at_0930", UNSET
        )

        intraday_movements_of_aggregate_balance_at_1000 = d.pop(
            "intraday_movements_of_aggregate_balance_at_1000", UNSET
        )

        intraday_movements_of_aggregate_balance_at_1100 = d.pop(
            "intraday_movements_of_aggregate_balance_at_1100", UNSET
        )

        intraday_movements_of_aggregate_balance_at_1200 = d.pop(
            "intraday_movements_of_aggregate_balance_at_1200", UNSET
        )

        intraday_movements_of_aggregate_balance_at_1500 = d.pop(
            "intraday_movements_of_aggregate_balance_at_1500", UNSET
        )

        intraday_movements_of_aggregate_balance_at_1600 = d.pop(
            "intraday_movements_of_aggregate_balance_at_1600", UNSET
        )

        forex_trans_t1 = d.pop("forex_trans_t1", UNSET)

        other_market_activities_t1 = d.pop("other_market_activities_t1", UNSET)

        reversal_of_discount_window_t1 = d.pop("reversal_of_discount_window_t1", UNSET)

        interest_payment_issuance_efbn_t1 = d.pop(
            "interest_payment_issuance_efbn_t1", UNSET
        )

        forecast_aggregate_bal_t1 = d.pop("forecast_aggregate_bal_t1", UNSET)

        forex_trans_t2 = d.pop("forex_trans_t2", UNSET)

        other_market_activities_t2 = d.pop("other_market_activities_t2", UNSET)

        reversal_of_discount_window_t2 = d.pop("reversal_of_discount_window_t2", UNSET)

        interest_payment_issuance_efbn_t2 = d.pop(
            "interest_payment_issuance_efbn_t2", UNSET
        )

        forecast_aggregate_bal_t2 = d.pop("forecast_aggregate_bal_t2", UNSET)

        forex_trans_t3 = d.pop("forex_trans_t3", UNSET)

        other_market_activities_t3 = d.pop("other_market_activities_t3", UNSET)

        reversal_of_discount_window_t3 = d.pop("reversal_of_discount_window_t3", UNSET)

        interest_payment_issuance_efbn_t3 = d.pop(
            "interest_payment_issuance_efbn_t3", UNSET
        )

        forecast_aggregate_bal_t3 = d.pop("forecast_aggregate_bal_t3", UNSET)

        forex_trans_t4 = d.pop("forex_trans_t4", UNSET)

        other_market_activities_t4 = d.pop("other_market_activities_t4", UNSET)

        reversal_of_discount_window_t4 = d.pop("reversal_of_discount_window_t4", UNSET)

        interest_payment_issuance_efbn_t4 = d.pop(
            "interest_payment_issuance_efbn_t4", UNSET
        )

        forecast_aggregate_bal_t4 = d.pop("forecast_aggregate_bal_t4", UNSET)

        forex_trans_u = d.pop("forex_trans_u", UNSET)

        other_market_activities_u = d.pop("other_market_activities_u", UNSET)

        reversal_of_discount_window_u = d.pop("reversal_of_discount_window_u", UNSET)

        interest_payment_issuance_efbn_u = d.pop(
            "interest_payment_issuance_efbn_u", UNSET
        )

        forecast_aggregate_bal_u = d.pop("forecast_aggregate_bal_u", UNSET)

        record = cls(
            end_of_date=end_of_date,
            cu_weakside=cu_weakside,
            cu_strongside=cu_strongside,
            disc_win_base_rate=disc_win_base_rate,
            hibor_overnight=hibor_overnight,
            hibor_fixing_1m=hibor_fixing_1m,
            twi=twi,
            opening_balance=opening_balance,
            closing_balance=closing_balance,
            market_activities=market_activities,
            interest_payment=interest_payment,
            discount_window_reversal=discount_window_reversal,
            discount_window_activities=discount_window_activities,
            intraday_movements_of_aggregate_balance_at_0930=intraday_movements_of_aggregate_balance_at_0930,
            intraday_movements_of_aggregate_balance_at_1000=intraday_movements_of_aggregate_balance_at_1000,
            intraday_movements_of_aggregate_balance_at_1100=intraday_movements_of_aggregate_balance_at_1100,
            intraday_movements_of_aggregate_balance_at_1200=intraday_movements_of_aggregate_balance_at_1200,
            intraday_movements_of_aggregate_balance_at_1500=intraday_movements_of_aggregate_balance_at_1500,
            intraday_movements_of_aggregate_balance_at_1600=intraday_movements_of_aggregate_balance_at_1600,
            forex_trans_t1=forex_trans_t1,
            other_market_activities_t1=other_market_activities_t1,
            reversal_of_discount_window_t1=reversal_of_discount_window_t1,
            interest_payment_issuance_efbn_t1=interest_payment_issuance_efbn_t1,
            forecast_aggregate_bal_t1=forecast_aggregate_bal_t1,
            forex_trans_t2=forex_trans_t2,
            other_market_activities_t2=other_market_activities_t2,
            reversal_of_discount_window_t2=reversal_of_discount_window_t2,
            interest_payment_issuance_efbn_t2=interest_payment_issuance_efbn_t2,
            forecast_aggregate_bal_t2=forecast_aggregate_bal_t2,
            forex_trans_t3=forex_trans_t3,
            other_market_activities_t3=other_market_activities_t3,
            reversal_of_discount_window_t3=reversal_of_discount_window_t3,
            interest_payment_issuance_efbn_t3=interest_payment_issuance_efbn_t3,
            forecast_aggregate_bal_t3=forecast_aggregate_bal_t3,
            forex_trans_t4=forex_trans_t4,
            other_market_activities_t4=other_market_activities_t4,
            reversal_of_discount_window_t4=reversal_of_discount_window_t4,
            interest_payment_issuance_efbn_t4=interest_payment_issuance_efbn_t4,
            forecast_aggregate_bal_t4=forecast_aggregate_bal_t4,
            forex_trans_u=forex_trans_u,
            other_market_activities_u=other_market_activities_u,
            reversal_of_discount_window_u=reversal_of_discount_window_u,
            interest_payment_issuance_efbn_u=interest_payment_issuance_efbn_u,
            forecast_aggregate_bal_u=forecast_aggregate_bal_u,
        )

        record.additional_properties = d
        return record

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
