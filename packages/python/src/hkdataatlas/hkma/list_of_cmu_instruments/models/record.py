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
        issue_number (str | Unset):
        issue_description (str | Unset):
        issuer (str | Unset):
        p_agent_code (str | Unset):
        issue_date (datetime.date | Unset):
        maturity_date (datetime.date | Unset):
        call_put_option_date (datetime.date | Unset):
        coupon_rate (float | Unset):
        last_coupon_date (datetime.date | Unset):
        next_coupon_date (datetime.date | Unset):
        int_pay_freq (float | Unset):
        common_code (str | Unset):
        isin (str | Unset):
        issue_ccy (str | Unset):
        issue_size (float | Unset):
        outstanding_amount (float | Unset):
        tender_allowed (str | Unset):
        income_dist (str | Unset):
        repo_cat_hkd (str | Unset):
        repo_cat_usd (str | Unset):
        repo_cat_eur (str | Unset):
        repo_cat_cny_cb (str | Unset):
        repo_cat_cny_ma (str | Unset):
        bank_repo_cat (str | Unset):
        min_tradable_amount (float | Unset):
        multi_tradable_amount (float | Unset):
        special_action_date (datetime.date | Unset):
        special_action (str | Unset):
        fatca_withholding (str | Unset):
        form (str | Unset):
    """

    issue_number: str | Unset = UNSET
    issue_description: str | Unset = UNSET
    issuer: str | Unset = UNSET
    p_agent_code: str | Unset = UNSET
    issue_date: datetime.date | Unset = UNSET
    maturity_date: datetime.date | Unset = UNSET
    call_put_option_date: datetime.date | Unset = UNSET
    coupon_rate: float | Unset = UNSET
    last_coupon_date: datetime.date | Unset = UNSET
    next_coupon_date: datetime.date | Unset = UNSET
    int_pay_freq: float | Unset = UNSET
    common_code: str | Unset = UNSET
    isin: str | Unset = UNSET
    issue_ccy: str | Unset = UNSET
    issue_size: float | Unset = UNSET
    outstanding_amount: float | Unset = UNSET
    tender_allowed: str | Unset = UNSET
    income_dist: str | Unset = UNSET
    repo_cat_hkd: str | Unset = UNSET
    repo_cat_usd: str | Unset = UNSET
    repo_cat_eur: str | Unset = UNSET
    repo_cat_cny_cb: str | Unset = UNSET
    repo_cat_cny_ma: str | Unset = UNSET
    bank_repo_cat: str | Unset = UNSET
    min_tradable_amount: float | Unset = UNSET
    multi_tradable_amount: float | Unset = UNSET
    special_action_date: datetime.date | Unset = UNSET
    special_action: str | Unset = UNSET
    fatca_withholding: str | Unset = UNSET
    form: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_number = self.issue_number

        issue_description = self.issue_description

        issuer = self.issuer

        p_agent_code = self.p_agent_code

        issue_date: str | Unset = UNSET
        if not isinstance(self.issue_date, Unset):
            issue_date = self.issue_date.isoformat()

        maturity_date: str | Unset = UNSET
        if not isinstance(self.maturity_date, Unset):
            maturity_date = self.maturity_date.isoformat()

        call_put_option_date: str | Unset = UNSET
        if not isinstance(self.call_put_option_date, Unset):
            call_put_option_date = self.call_put_option_date.isoformat()

        coupon_rate = self.coupon_rate

        last_coupon_date: str | Unset = UNSET
        if not isinstance(self.last_coupon_date, Unset):
            last_coupon_date = self.last_coupon_date.isoformat()

        next_coupon_date: str | Unset = UNSET
        if not isinstance(self.next_coupon_date, Unset):
            next_coupon_date = self.next_coupon_date.isoformat()

        int_pay_freq = self.int_pay_freq

        common_code = self.common_code

        isin = self.isin

        issue_ccy = self.issue_ccy

        issue_size = self.issue_size

        outstanding_amount = self.outstanding_amount

        tender_allowed = self.tender_allowed

        income_dist = self.income_dist

        repo_cat_hkd = self.repo_cat_hkd

        repo_cat_usd = self.repo_cat_usd

        repo_cat_eur = self.repo_cat_eur

        repo_cat_cny_cb = self.repo_cat_cny_cb

        repo_cat_cny_ma = self.repo_cat_cny_ma

        bank_repo_cat = self.bank_repo_cat

        min_tradable_amount = self.min_tradable_amount

        multi_tradable_amount = self.multi_tradable_amount

        special_action_date: str | Unset = UNSET
        if not isinstance(self.special_action_date, Unset):
            special_action_date = self.special_action_date.isoformat()

        special_action = self.special_action

        fatca_withholding = self.fatca_withholding

        form = self.form

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issue_number is not UNSET:
            field_dict["issue_number"] = issue_number
        if issue_description is not UNSET:
            field_dict["issue_description"] = issue_description
        if issuer is not UNSET:
            field_dict["Issuer"] = issuer
        if p_agent_code is not UNSET:
            field_dict["p_agent_code"] = p_agent_code
        if issue_date is not UNSET:
            field_dict["issue_date"] = issue_date
        if maturity_date is not UNSET:
            field_dict["maturity_date"] = maturity_date
        if call_put_option_date is not UNSET:
            field_dict["call_put_option_date"] = call_put_option_date
        if coupon_rate is not UNSET:
            field_dict["coupon_rate"] = coupon_rate
        if last_coupon_date is not UNSET:
            field_dict["last_coupon_date"] = last_coupon_date
        if next_coupon_date is not UNSET:
            field_dict["next_coupon_date"] = next_coupon_date
        if int_pay_freq is not UNSET:
            field_dict["int_pay_freq"] = int_pay_freq
        if common_code is not UNSET:
            field_dict["common_code"] = common_code
        if isin is not UNSET:
            field_dict["Isin"] = isin
        if issue_ccy is not UNSET:
            field_dict["issue_ccy"] = issue_ccy
        if issue_size is not UNSET:
            field_dict["issue_size"] = issue_size
        if outstanding_amount is not UNSET:
            field_dict["outstanding_amount"] = outstanding_amount
        if tender_allowed is not UNSET:
            field_dict["tender_allowed"] = tender_allowed
        if income_dist is not UNSET:
            field_dict["income_dist"] = income_dist
        if repo_cat_hkd is not UNSET:
            field_dict["repo_cat_hkd"] = repo_cat_hkd
        if repo_cat_usd is not UNSET:
            field_dict["repo_cat_usd"] = repo_cat_usd
        if repo_cat_eur is not UNSET:
            field_dict["repo_cat_eur"] = repo_cat_eur
        if repo_cat_cny_cb is not UNSET:
            field_dict["repo_cat_cny_cb"] = repo_cat_cny_cb
        if repo_cat_cny_ma is not UNSET:
            field_dict["repo_cat_cny_ma"] = repo_cat_cny_ma
        if bank_repo_cat is not UNSET:
            field_dict["bank_repo_cat"] = bank_repo_cat
        if min_tradable_amount is not UNSET:
            field_dict["min_tradable_amount"] = min_tradable_amount
        if multi_tradable_amount is not UNSET:
            field_dict["multi_tradable_amount"] = multi_tradable_amount
        if special_action_date is not UNSET:
            field_dict["special_action_date"] = special_action_date
        if special_action is not UNSET:
            field_dict["special_action"] = special_action
        if fatca_withholding is not UNSET:
            field_dict["fatca_withholding"] = fatca_withholding
        if form is not UNSET:
            field_dict["form"] = form

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        issue_number = d.pop("issue_number", UNSET)

        issue_description = d.pop("issue_description", UNSET)

        issuer = d.pop("Issuer", UNSET)

        p_agent_code = d.pop("p_agent_code", UNSET)

        _issue_date = d.pop("issue_date", UNSET)
        issue_date: datetime.date | Unset
        if isinstance(_issue_date, Unset):
            issue_date = UNSET
        else:
            issue_date = datetime.date.fromisoformat(_issue_date)

        _maturity_date = d.pop("maturity_date", UNSET)
        maturity_date: datetime.date | Unset
        if isinstance(_maturity_date, Unset):
            maturity_date = UNSET
        else:
            maturity_date = datetime.date.fromisoformat(_maturity_date)

        _call_put_option_date = d.pop("call_put_option_date", UNSET)
        call_put_option_date: datetime.date | Unset
        if isinstance(_call_put_option_date, Unset):
            call_put_option_date = UNSET
        else:
            call_put_option_date = datetime.date.fromisoformat(_call_put_option_date)

        coupon_rate = d.pop("coupon_rate", UNSET)

        _last_coupon_date = d.pop("last_coupon_date", UNSET)
        last_coupon_date: datetime.date | Unset
        if isinstance(_last_coupon_date, Unset):
            last_coupon_date = UNSET
        else:
            last_coupon_date = datetime.date.fromisoformat(_last_coupon_date)

        _next_coupon_date = d.pop("next_coupon_date", UNSET)
        next_coupon_date: datetime.date | Unset
        if isinstance(_next_coupon_date, Unset):
            next_coupon_date = UNSET
        else:
            next_coupon_date = datetime.date.fromisoformat(_next_coupon_date)

        int_pay_freq = d.pop("int_pay_freq", UNSET)

        common_code = d.pop("common_code", UNSET)

        isin = d.pop("Isin", UNSET)

        issue_ccy = d.pop("issue_ccy", UNSET)

        issue_size = d.pop("issue_size", UNSET)

        outstanding_amount = d.pop("outstanding_amount", UNSET)

        tender_allowed = d.pop("tender_allowed", UNSET)

        income_dist = d.pop("income_dist", UNSET)

        repo_cat_hkd = d.pop("repo_cat_hkd", UNSET)

        repo_cat_usd = d.pop("repo_cat_usd", UNSET)

        repo_cat_eur = d.pop("repo_cat_eur", UNSET)

        repo_cat_cny_cb = d.pop("repo_cat_cny_cb", UNSET)

        repo_cat_cny_ma = d.pop("repo_cat_cny_ma", UNSET)

        bank_repo_cat = d.pop("bank_repo_cat", UNSET)

        min_tradable_amount = d.pop("min_tradable_amount", UNSET)

        multi_tradable_amount = d.pop("multi_tradable_amount", UNSET)

        _special_action_date = d.pop("special_action_date", UNSET)
        special_action_date: datetime.date | Unset
        if isinstance(_special_action_date, Unset):
            special_action_date = UNSET
        else:
            special_action_date = datetime.date.fromisoformat(_special_action_date)

        special_action = d.pop("special_action", UNSET)

        fatca_withholding = d.pop("fatca_withholding", UNSET)

        form = d.pop("form", UNSET)

        record = cls(
            issue_number=issue_number,
            issue_description=issue_description,
            issuer=issuer,
            p_agent_code=p_agent_code,
            issue_date=issue_date,
            maturity_date=maturity_date,
            call_put_option_date=call_put_option_date,
            coupon_rate=coupon_rate,
            last_coupon_date=last_coupon_date,
            next_coupon_date=next_coupon_date,
            int_pay_freq=int_pay_freq,
            common_code=common_code,
            isin=isin,
            issue_ccy=issue_ccy,
            issue_size=issue_size,
            outstanding_amount=outstanding_amount,
            tender_allowed=tender_allowed,
            income_dist=income_dist,
            repo_cat_hkd=repo_cat_hkd,
            repo_cat_usd=repo_cat_usd,
            repo_cat_eur=repo_cat_eur,
            repo_cat_cny_cb=repo_cat_cny_cb,
            repo_cat_cny_ma=repo_cat_cny_ma,
            bank_repo_cat=bank_repo_cat,
            min_tradable_amount=min_tradable_amount,
            multi_tradable_amount=multi_tradable_amount,
            special_action_date=special_action_date,
            special_action=special_action,
            fatca_withholding=fatca_withholding,
            form=form,
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
