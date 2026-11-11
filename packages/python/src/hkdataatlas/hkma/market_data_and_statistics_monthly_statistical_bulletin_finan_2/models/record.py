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
        no_of_ais (float | Unset):
        total_assets (float | Unset):
        total_ext_claims (float | Unset):
        total_ext_liab (float | Unset):
        cust_deposites_hkd (float | Unset):
        cust_deposits_fc (float | Unset):
        cust_deposits_total (float | Unset):
        loans_in_hk (float | Unset):
        loans_outside_hk (float | Unset):
        loans_total (float | Unset):
        loans_resid_mort_lending (float | Unset):
        classif_loans (float | Unset):
        deli_ratio_resid_mort_lend (float | Unset):
        chroff_ratio_of_crcard_rece (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    no_of_ais: float | Unset = UNSET
    total_assets: float | Unset = UNSET
    total_ext_claims: float | Unset = UNSET
    total_ext_liab: float | Unset = UNSET
    cust_deposites_hkd: float | Unset = UNSET
    cust_deposits_fc: float | Unset = UNSET
    cust_deposits_total: float | Unset = UNSET
    loans_in_hk: float | Unset = UNSET
    loans_outside_hk: float | Unset = UNSET
    loans_total: float | Unset = UNSET
    loans_resid_mort_lending: float | Unset = UNSET
    classif_loans: float | Unset = UNSET
    deli_ratio_resid_mort_lend: float | Unset = UNSET
    chroff_ratio_of_crcard_rece: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        no_of_ais = self.no_of_ais

        total_assets = self.total_assets

        total_ext_claims = self.total_ext_claims

        total_ext_liab = self.total_ext_liab

        cust_deposites_hkd = self.cust_deposites_hkd

        cust_deposits_fc = self.cust_deposits_fc

        cust_deposits_total = self.cust_deposits_total

        loans_in_hk = self.loans_in_hk

        loans_outside_hk = self.loans_outside_hk

        loans_total = self.loans_total

        loans_resid_mort_lending = self.loans_resid_mort_lending

        classif_loans = self.classif_loans

        deli_ratio_resid_mort_lend = self.deli_ratio_resid_mort_lend

        chroff_ratio_of_crcard_rece = self.chroff_ratio_of_crcard_rece

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if no_of_ais is not UNSET:
            field_dict["no_of_ais"] = no_of_ais
        if total_assets is not UNSET:
            field_dict["total_assets"] = total_assets
        if total_ext_claims is not UNSET:
            field_dict["total_ext_claims"] = total_ext_claims
        if total_ext_liab is not UNSET:
            field_dict["total_ext_liab"] = total_ext_liab
        if cust_deposites_hkd is not UNSET:
            field_dict["cust_deposites_hkd"] = cust_deposites_hkd
        if cust_deposits_fc is not UNSET:
            field_dict["cust_deposits_fc"] = cust_deposits_fc
        if cust_deposits_total is not UNSET:
            field_dict["cust_deposits_total"] = cust_deposits_total
        if loans_in_hk is not UNSET:
            field_dict["loans_in_hk"] = loans_in_hk
        if loans_outside_hk is not UNSET:
            field_dict["loans_outside_hk"] = loans_outside_hk
        if loans_total is not UNSET:
            field_dict["loans_total"] = loans_total
        if loans_resid_mort_lending is not UNSET:
            field_dict["loans_resid_mort_lending"] = loans_resid_mort_lending
        if classif_loans is not UNSET:
            field_dict["classif_loans"] = classif_loans
        if deli_ratio_resid_mort_lend is not UNSET:
            field_dict["deli_ratio_resid_mort_lend"] = deli_ratio_resid_mort_lend
        if chroff_ratio_of_crcard_rece is not UNSET:
            field_dict["chroff_ratio_of_crcard_rece"] = chroff_ratio_of_crcard_rece

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

        no_of_ais = d.pop("no_of_ais", UNSET)

        total_assets = d.pop("total_assets", UNSET)

        total_ext_claims = d.pop("total_ext_claims", UNSET)

        total_ext_liab = d.pop("total_ext_liab", UNSET)

        cust_deposites_hkd = d.pop("cust_deposites_hkd", UNSET)

        cust_deposits_fc = d.pop("cust_deposits_fc", UNSET)

        cust_deposits_total = d.pop("cust_deposits_total", UNSET)

        loans_in_hk = d.pop("loans_in_hk", UNSET)

        loans_outside_hk = d.pop("loans_outside_hk", UNSET)

        loans_total = d.pop("loans_total", UNSET)

        loans_resid_mort_lending = d.pop("loans_resid_mort_lending", UNSET)

        classif_loans = d.pop("classif_loans", UNSET)

        deli_ratio_resid_mort_lend = d.pop("deli_ratio_resid_mort_lend", UNSET)

        chroff_ratio_of_crcard_rece = d.pop("chroff_ratio_of_crcard_rece", UNSET)

        record = cls(
            end_of_month=end_of_month,
            no_of_ais=no_of_ais,
            total_assets=total_assets,
            total_ext_claims=total_ext_claims,
            total_ext_liab=total_ext_liab,
            cust_deposites_hkd=cust_deposites_hkd,
            cust_deposits_fc=cust_deposits_fc,
            cust_deposits_total=cust_deposits_total,
            loans_in_hk=loans_in_hk,
            loans_outside_hk=loans_outside_hk,
            loans_total=loans_total,
            loans_resid_mort_lending=loans_resid_mort_lending,
            classif_loans=classif_loans,
            deli_ratio_resid_mort_lend=deli_ratio_resid_mort_lend,
            chroff_ratio_of_crcard_rece=chroff_ratio_of_crcard_rece,
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
