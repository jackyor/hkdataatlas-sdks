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
        end_of_month (datetime.date | Unset):
        pass_loans (float | Unset):
        sp_ment_loans (float | Unset):
        cl_gross_substandard (float | Unset):
        cl_gross_doubtful (float | Unset):
        cl_gross_loss (float | Unset):
        cl_gross_total (float | Unset):
        cl_net (float | Unset):
        loans_od3m (float | Unset):
        loans_resch (float | Unset):
        loans_od3m_resch_total (float | Unset):
        nonperform_loans (float | Unset):
        cl_gross_mainland_lend (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    pass_loans: float | Unset = UNSET
    sp_ment_loans: float | Unset = UNSET
    cl_gross_substandard: float | Unset = UNSET
    cl_gross_doubtful: float | Unset = UNSET
    cl_gross_loss: float | Unset = UNSET
    cl_gross_total: float | Unset = UNSET
    cl_net: float | Unset = UNSET
    loans_od3m: float | Unset = UNSET
    loans_resch: float | Unset = UNSET
    loans_od3m_resch_total: float | Unset = UNSET
    nonperform_loans: float | Unset = UNSET
    cl_gross_mainland_lend: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        pass_loans = self.pass_loans

        sp_ment_loans = self.sp_ment_loans

        cl_gross_substandard = self.cl_gross_substandard

        cl_gross_doubtful = self.cl_gross_doubtful

        cl_gross_loss = self.cl_gross_loss

        cl_gross_total = self.cl_gross_total

        cl_net = self.cl_net

        loans_od3m = self.loans_od3m

        loans_resch = self.loans_resch

        loans_od3m_resch_total = self.loans_od3m_resch_total

        nonperform_loans = self.nonperform_loans

        cl_gross_mainland_lend = self.cl_gross_mainland_lend

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if pass_loans is not UNSET:
            field_dict["pass_loans"] = pass_loans
        if sp_ment_loans is not UNSET:
            field_dict["sp_ment_loans"] = sp_ment_loans
        if cl_gross_substandard is not UNSET:
            field_dict["cl_gross_substandard"] = cl_gross_substandard
        if cl_gross_doubtful is not UNSET:
            field_dict["cl_gross_doubtful"] = cl_gross_doubtful
        if cl_gross_loss is not UNSET:
            field_dict["cl_gross_loss"] = cl_gross_loss
        if cl_gross_total is not UNSET:
            field_dict["cl_gross_total"] = cl_gross_total
        if cl_net is not UNSET:
            field_dict["cl_net"] = cl_net
        if loans_od3m is not UNSET:
            field_dict["loans_od3m"] = loans_od3m
        if loans_resch is not UNSET:
            field_dict["loans_resch"] = loans_resch
        if loans_od3m_resch_total is not UNSET:
            field_dict["loans_od3m_resch_total"] = loans_od3m_resch_total
        if nonperform_loans is not UNSET:
            field_dict["nonperform_loans"] = nonperform_loans
        if cl_gross_mainland_lend is not UNSET:
            field_dict["cl_gross_mainland_lend"] = cl_gross_mainland_lend

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _end_of_month = d.pop("end_of_month", UNSET)
        end_of_month: datetime.date | Unset
        if isinstance(_end_of_month, Unset):
            end_of_month = UNSET
        else:
            end_of_month = datetime.date.fromisoformat(_end_of_month)

        pass_loans = d.pop("pass_loans", UNSET)

        sp_ment_loans = d.pop("sp_ment_loans", UNSET)

        cl_gross_substandard = d.pop("cl_gross_substandard", UNSET)

        cl_gross_doubtful = d.pop("cl_gross_doubtful", UNSET)

        cl_gross_loss = d.pop("cl_gross_loss", UNSET)

        cl_gross_total = d.pop("cl_gross_total", UNSET)

        cl_net = d.pop("cl_net", UNSET)

        loans_od3m = d.pop("loans_od3m", UNSET)

        loans_resch = d.pop("loans_resch", UNSET)

        loans_od3m_resch_total = d.pop("loans_od3m_resch_total", UNSET)

        nonperform_loans = d.pop("nonperform_loans", UNSET)

        cl_gross_mainland_lend = d.pop("cl_gross_mainland_lend", UNSET)

        record = cls(
            end_of_month=end_of_month,
            pass_loans=pass_loans,
            sp_ment_loans=sp_ment_loans,
            cl_gross_substandard=cl_gross_substandard,
            cl_gross_doubtful=cl_gross_doubtful,
            cl_gross_loss=cl_gross_loss,
            cl_gross_total=cl_gross_total,
            cl_net=cl_net,
            loans_od3m=loans_od3m,
            loans_resch=loans_resch,
            loans_od3m_resch_total=loans_od3m_resch_total,
            nonperform_loans=nonperform_loans,
            cl_gross_mainland_lend=cl_gross_mainland_lend,
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
