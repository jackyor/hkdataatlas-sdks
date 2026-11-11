from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        e_case_no (None | str | Unset): Publisher field type: esriFieldTypeString
        plan_no (None | str | Unset): Publisher field type: esriFieldTypeString
        en_ndate (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        en_nexpiry (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        en_sch2_use (None | str | Unset): Publisher field type: esriFieldTypeString
        en_sch2_usec (None | str | Unset): Publisher field type: esriFieldTypeString
        cnen_ndate (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        rn_ndate (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        rn_nexpiry (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        rn_sch2_use (None | str | Unset): Publisher field type: esriFieldTypeString
        rn_sch2_usec (None | str | Unset): Publisher field type: esriFieldTypeString
        cnrn_ndate (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        cann_ndate (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        sent_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        decision (None | str | Unset): Publisher field type: esriFieldTypeString
        grtotal (int | None | Unset): Publisher field type: esriFieldTypeInteger
    """

    objectid: int | Unset = UNSET
    e_case_no: None | str | Unset = UNSET
    plan_no: None | str | Unset = UNSET
    en_ndate: Any | Unset = UNSET
    en_nexpiry: Any | Unset = UNSET
    en_sch2_use: None | str | Unset = UNSET
    en_sch2_usec: None | str | Unset = UNSET
    cnen_ndate: Any | Unset = UNSET
    rn_ndate: Any | Unset = UNSET
    rn_nexpiry: Any | Unset = UNSET
    rn_sch2_use: None | str | Unset = UNSET
    rn_sch2_usec: None | str | Unset = UNSET
    cnrn_ndate: Any | Unset = UNSET
    cann_ndate: Any | Unset = UNSET
    sent_date: Any | Unset = UNSET
    decision: None | str | Unset = UNSET
    grtotal: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        e_case_no: None | str | Unset
        if isinstance(self.e_case_no, Unset):
            e_case_no = UNSET
        else:
            e_case_no = self.e_case_no

        plan_no: None | str | Unset
        if isinstance(self.plan_no, Unset):
            plan_no = UNSET
        else:
            plan_no = self.plan_no

        en_ndate = self.en_ndate

        en_nexpiry = self.en_nexpiry

        en_sch2_use: None | str | Unset
        if isinstance(self.en_sch2_use, Unset):
            en_sch2_use = UNSET
        else:
            en_sch2_use = self.en_sch2_use

        en_sch2_usec: None | str | Unset
        if isinstance(self.en_sch2_usec, Unset):
            en_sch2_usec = UNSET
        else:
            en_sch2_usec = self.en_sch2_usec

        cnen_ndate = self.cnen_ndate

        rn_ndate = self.rn_ndate

        rn_nexpiry = self.rn_nexpiry

        rn_sch2_use: None | str | Unset
        if isinstance(self.rn_sch2_use, Unset):
            rn_sch2_use = UNSET
        else:
            rn_sch2_use = self.rn_sch2_use

        rn_sch2_usec: None | str | Unset
        if isinstance(self.rn_sch2_usec, Unset):
            rn_sch2_usec = UNSET
        else:
            rn_sch2_usec = self.rn_sch2_usec

        cnrn_ndate = self.cnrn_ndate

        cann_ndate = self.cann_ndate

        sent_date = self.sent_date

        decision: None | str | Unset
        if isinstance(self.decision, Unset):
            decision = UNSET
        else:
            decision = self.decision

        grtotal: int | None | Unset
        if isinstance(self.grtotal, Unset):
            grtotal = UNSET
        else:
            grtotal = self.grtotal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if e_case_no is not UNSET:
            field_dict["E_CASE_NO"] = e_case_no
        if plan_no is not UNSET:
            field_dict["PLAN_NO"] = plan_no
        if en_ndate is not UNSET:
            field_dict["EN_NDATE"] = en_ndate
        if en_nexpiry is not UNSET:
            field_dict["EN_NEXPIRY"] = en_nexpiry
        if en_sch2_use is not UNSET:
            field_dict["EN_SCH2_USE"] = en_sch2_use
        if en_sch2_usec is not UNSET:
            field_dict["EN_SCH2_USEC"] = en_sch2_usec
        if cnen_ndate is not UNSET:
            field_dict["CNEN_NDATE"] = cnen_ndate
        if rn_ndate is not UNSET:
            field_dict["RN_NDATE"] = rn_ndate
        if rn_nexpiry is not UNSET:
            field_dict["RN_NEXPIRY"] = rn_nexpiry
        if rn_sch2_use is not UNSET:
            field_dict["RN_SCH2_USE"] = rn_sch2_use
        if rn_sch2_usec is not UNSET:
            field_dict["RN_SCH2_USEC"] = rn_sch2_usec
        if cnrn_ndate is not UNSET:
            field_dict["CNRN_NDATE"] = cnrn_ndate
        if cann_ndate is not UNSET:
            field_dict["CANN_NDATE"] = cann_ndate
        if sent_date is not UNSET:
            field_dict["SENT_DATE"] = sent_date
        if decision is not UNSET:
            field_dict["DECISION"] = decision
        if grtotal is not UNSET:
            field_dict["GRTOTAL"] = grtotal

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_e_case_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        e_case_no = _parse_e_case_no(d.pop("E_CASE_NO", UNSET))

        def _parse_plan_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan_no = _parse_plan_no(d.pop("PLAN_NO", UNSET))

        en_ndate = d.pop("EN_NDATE", UNSET)

        en_nexpiry = d.pop("EN_NEXPIRY", UNSET)

        def _parse_en_sch2_use(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_sch2_use = _parse_en_sch2_use(d.pop("EN_SCH2_USE", UNSET))

        def _parse_en_sch2_usec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_sch2_usec = _parse_en_sch2_usec(d.pop("EN_SCH2_USEC", UNSET))

        cnen_ndate = d.pop("CNEN_NDATE", UNSET)

        rn_ndate = d.pop("RN_NDATE", UNSET)

        rn_nexpiry = d.pop("RN_NEXPIRY", UNSET)

        def _parse_rn_sch2_use(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rn_sch2_use = _parse_rn_sch2_use(d.pop("RN_SCH2_USE", UNSET))

        def _parse_rn_sch2_usec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rn_sch2_usec = _parse_rn_sch2_usec(d.pop("RN_SCH2_USEC", UNSET))

        cnrn_ndate = d.pop("CNRN_NDATE", UNSET)

        cann_ndate = d.pop("CANN_NDATE", UNSET)

        sent_date = d.pop("SENT_DATE", UNSET)

        def _parse_decision(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        decision = _parse_decision(d.pop("DECISION", UNSET))

        def _parse_grtotal(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        grtotal = _parse_grtotal(d.pop("GRTOTAL", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            e_case_no=e_case_no,
            plan_no=plan_no,
            en_ndate=en_ndate,
            en_nexpiry=en_nexpiry,
            en_sch2_use=en_sch2_use,
            en_sch2_usec=en_sch2_usec,
            cnen_ndate=cnen_ndate,
            rn_ndate=rn_ndate,
            rn_nexpiry=rn_nexpiry,
            rn_sch2_use=rn_sch2_use,
            rn_sch2_usec=rn_sch2_usec,
            cnrn_ndate=cnrn_ndate,
            cann_ndate=cann_ndate,
            sent_date=sent_date,
            decision=decision,
            grtotal=grtotal,
        )

        arcgis_feature_server_arcgis_layer_0_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_0_attributes

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
