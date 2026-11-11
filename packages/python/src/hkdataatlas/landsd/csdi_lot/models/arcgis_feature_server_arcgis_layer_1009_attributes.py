from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1009Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1009Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        prn (str | Unset): Publisher field type: esriFieldTypeString
        lot_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lot_area_unit (None | str | Unset): Publisher field type: esriFieldTypeString
        grant_doc_type (None | str | Unset): Publisher field type: esriFieldTypeString
        grant_doc_no (None | str | Unset): Publisher field type: esriFieldTypeString
        commencement_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
        expiry_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        lease_term (None | str | Unset): Publisher field type: esriFieldTypeString
        renewability (None | str | Unset): Publisher field type: esriFieldTypeString
        user_type (None | str | Unset): Publisher field type: esriFieldTypeString
        tree_preservation (str | Unset): Publisher field type: esriFieldTypeString
        type_of_bldg (str | Unset): Publisher field type: esriFieldTypeString
        bc_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        cto_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        max_bldg_ht (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_storeys (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_units_restriction (str | Unset): Publisher field type: esriFieldTypeString
        unit_size_restriction (str | Unset): Publisher field type: esriFieldTypeString
        dd_or_ddh_clause (str | Unset): Publisher field type: esriFieldTypeString
        site_coverage (None | str | Unset): Publisher field type: esriFieldTypeString
        max_gfa (None | str | Unset): Publisher field type: esriFieldTypeString
        min_gfa (None | str | Unset): Publisher field type: esriFieldTypeString
        public_open_space (str | Unset): Publisher field type: esriFieldTypeString
        govt_accom (str | Unset): Publisher field type: esriFieldTypeString
        sc_auth_satisfaction (str | Unset): Publisher field type: esriFieldTypeString
        sc_alienation (str | Unset): Publisher field type: esriFieldTypeString
        sc_non_profit (str | Unset): Publisher field type: esriFieldTypeString
        sc_acc_submission (str | Unset): Publisher field type: esriFieldTypeString
        sc_profit_dist (str | Unset): Publisher field type: esriFieldTypeString
        sc_user_cessation (str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    prn: str | Unset = UNSET
    lot_area: float | None | Unset = UNSET
    lot_area_unit: None | str | Unset = UNSET
    grant_doc_type: None | str | Unset = UNSET
    grant_doc_no: None | str | Unset = UNSET
    commencement_date: Any | Unset = UNSET
    expiry_date: Any | Unset = UNSET
    lease_term: None | str | Unset = UNSET
    renewability: None | str | Unset = UNSET
    user_type: None | str | Unset = UNSET
    tree_preservation: str | Unset = UNSET
    type_of_bldg: str | Unset = UNSET
    bc_date: Any | Unset = UNSET
    cto_date: Any | Unset = UNSET
    max_bldg_ht: None | str | Unset = UNSET
    no_of_storeys: None | str | Unset = UNSET
    no_of_units_restriction: str | Unset = UNSET
    unit_size_restriction: str | Unset = UNSET
    dd_or_ddh_clause: str | Unset = UNSET
    site_coverage: None | str | Unset = UNSET
    max_gfa: None | str | Unset = UNSET
    min_gfa: None | str | Unset = UNSET
    public_open_space: str | Unset = UNSET
    govt_accom: str | Unset = UNSET
    sc_auth_satisfaction: str | Unset = UNSET
    sc_alienation: str | Unset = UNSET
    sc_non_profit: str | Unset = UNSET
    sc_acc_submission: str | Unset = UNSET
    sc_profit_dist: str | Unset = UNSET
    sc_user_cessation: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        prn = self.prn

        lot_area: float | None | Unset
        if isinstance(self.lot_area, Unset):
            lot_area = UNSET
        else:
            lot_area = self.lot_area

        lot_area_unit: None | str | Unset
        if isinstance(self.lot_area_unit, Unset):
            lot_area_unit = UNSET
        else:
            lot_area_unit = self.lot_area_unit

        grant_doc_type: None | str | Unset
        if isinstance(self.grant_doc_type, Unset):
            grant_doc_type = UNSET
        else:
            grant_doc_type = self.grant_doc_type

        grant_doc_no: None | str | Unset
        if isinstance(self.grant_doc_no, Unset):
            grant_doc_no = UNSET
        else:
            grant_doc_no = self.grant_doc_no

        commencement_date = self.commencement_date

        expiry_date = self.expiry_date

        lease_term: None | str | Unset
        if isinstance(self.lease_term, Unset):
            lease_term = UNSET
        else:
            lease_term = self.lease_term

        renewability: None | str | Unset
        if isinstance(self.renewability, Unset):
            renewability = UNSET
        else:
            renewability = self.renewability

        user_type: None | str | Unset
        if isinstance(self.user_type, Unset):
            user_type = UNSET
        else:
            user_type = self.user_type

        tree_preservation = self.tree_preservation

        type_of_bldg = self.type_of_bldg

        bc_date = self.bc_date

        cto_date = self.cto_date

        max_bldg_ht: None | str | Unset
        if isinstance(self.max_bldg_ht, Unset):
            max_bldg_ht = UNSET
        else:
            max_bldg_ht = self.max_bldg_ht

        no_of_storeys: None | str | Unset
        if isinstance(self.no_of_storeys, Unset):
            no_of_storeys = UNSET
        else:
            no_of_storeys = self.no_of_storeys

        no_of_units_restriction = self.no_of_units_restriction

        unit_size_restriction = self.unit_size_restriction

        dd_or_ddh_clause = self.dd_or_ddh_clause

        site_coverage: None | str | Unset
        if isinstance(self.site_coverage, Unset):
            site_coverage = UNSET
        else:
            site_coverage = self.site_coverage

        max_gfa: None | str | Unset
        if isinstance(self.max_gfa, Unset):
            max_gfa = UNSET
        else:
            max_gfa = self.max_gfa

        min_gfa: None | str | Unset
        if isinstance(self.min_gfa, Unset):
            min_gfa = UNSET
        else:
            min_gfa = self.min_gfa

        public_open_space = self.public_open_space

        govt_accom = self.govt_accom

        sc_auth_satisfaction = self.sc_auth_satisfaction

        sc_alienation = self.sc_alienation

        sc_non_profit = self.sc_non_profit

        sc_acc_submission = self.sc_acc_submission

        sc_profit_dist = self.sc_profit_dist

        sc_user_cessation = self.sc_user_cessation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if prn is not UNSET:
            field_dict["PRN"] = prn
        if lot_area is not UNSET:
            field_dict["LotArea"] = lot_area
        if lot_area_unit is not UNSET:
            field_dict["LotAreaUnit"] = lot_area_unit
        if grant_doc_type is not UNSET:
            field_dict["GrantDocType"] = grant_doc_type
        if grant_doc_no is not UNSET:
            field_dict["GrantDocNo"] = grant_doc_no
        if commencement_date is not UNSET:
            field_dict["CommencementDate"] = commencement_date
        if expiry_date is not UNSET:
            field_dict["ExpiryDate"] = expiry_date
        if lease_term is not UNSET:
            field_dict["LeaseTerm"] = lease_term
        if renewability is not UNSET:
            field_dict["Renewability"] = renewability
        if user_type is not UNSET:
            field_dict["UserType"] = user_type
        if tree_preservation is not UNSET:
            field_dict["TreePreservation"] = tree_preservation
        if type_of_bldg is not UNSET:
            field_dict["TypeOfBldg"] = type_of_bldg
        if bc_date is not UNSET:
            field_dict["BCDate"] = bc_date
        if cto_date is not UNSET:
            field_dict["CTODate"] = cto_date
        if max_bldg_ht is not UNSET:
            field_dict["MaxBldgHt"] = max_bldg_ht
        if no_of_storeys is not UNSET:
            field_dict["NoOfStoreys"] = no_of_storeys
        if no_of_units_restriction is not UNSET:
            field_dict["NoOfUnitsRestriction"] = no_of_units_restriction
        if unit_size_restriction is not UNSET:
            field_dict["UnitSizeRestriction"] = unit_size_restriction
        if dd_or_ddh_clause is not UNSET:
            field_dict["DDOrDDHClause"] = dd_or_ddh_clause
        if site_coverage is not UNSET:
            field_dict["SiteCoverage"] = site_coverage
        if max_gfa is not UNSET:
            field_dict["MaxGFA"] = max_gfa
        if min_gfa is not UNSET:
            field_dict["MinGFA"] = min_gfa
        if public_open_space is not UNSET:
            field_dict["PublicOpenSpace"] = public_open_space
        if govt_accom is not UNSET:
            field_dict["GovtAccom"] = govt_accom
        if sc_auth_satisfaction is not UNSET:
            field_dict["SCAuthSatisfaction"] = sc_auth_satisfaction
        if sc_alienation is not UNSET:
            field_dict["SCAlienation"] = sc_alienation
        if sc_non_profit is not UNSET:
            field_dict["SCNonProfit"] = sc_non_profit
        if sc_acc_submission is not UNSET:
            field_dict["SCAccSubmission"] = sc_acc_submission
        if sc_profit_dist is not UNSET:
            field_dict["SCProfitDist"] = sc_profit_dist
        if sc_user_cessation is not UNSET:
            field_dict["SCUserCessation"] = sc_user_cessation

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        prn = d.pop("PRN", UNSET)

        def _parse_lot_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lot_area = _parse_lot_area(d.pop("LotArea", UNSET))

        def _parse_lot_area_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lot_area_unit = _parse_lot_area_unit(d.pop("LotAreaUnit", UNSET))

        def _parse_grant_doc_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grant_doc_type = _parse_grant_doc_type(d.pop("GrantDocType", UNSET))

        def _parse_grant_doc_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grant_doc_no = _parse_grant_doc_no(d.pop("GrantDocNo", UNSET))

        commencement_date = d.pop("CommencementDate", UNSET)

        expiry_date = d.pop("ExpiryDate", UNSET)

        def _parse_lease_term(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lease_term = _parse_lease_term(d.pop("LeaseTerm", UNSET))

        def _parse_renewability(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        renewability = _parse_renewability(d.pop("Renewability", UNSET))

        def _parse_user_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_type = _parse_user_type(d.pop("UserType", UNSET))

        tree_preservation = d.pop("TreePreservation", UNSET)

        type_of_bldg = d.pop("TypeOfBldg", UNSET)

        bc_date = d.pop("BCDate", UNSET)

        cto_date = d.pop("CTODate", UNSET)

        def _parse_max_bldg_ht(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_bldg_ht = _parse_max_bldg_ht(d.pop("MaxBldgHt", UNSET))

        def _parse_no_of_storeys(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_storeys = _parse_no_of_storeys(d.pop("NoOfStoreys", UNSET))

        no_of_units_restriction = d.pop("NoOfUnitsRestriction", UNSET)

        unit_size_restriction = d.pop("UnitSizeRestriction", UNSET)

        dd_or_ddh_clause = d.pop("DDOrDDHClause", UNSET)

        def _parse_site_coverage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_coverage = _parse_site_coverage(d.pop("SiteCoverage", UNSET))

        def _parse_max_gfa(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_gfa = _parse_max_gfa(d.pop("MaxGFA", UNSET))

        def _parse_min_gfa(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        min_gfa = _parse_min_gfa(d.pop("MinGFA", UNSET))

        public_open_space = d.pop("PublicOpenSpace", UNSET)

        govt_accom = d.pop("GovtAccom", UNSET)

        sc_auth_satisfaction = d.pop("SCAuthSatisfaction", UNSET)

        sc_alienation = d.pop("SCAlienation", UNSET)

        sc_non_profit = d.pop("SCNonProfit", UNSET)

        sc_acc_submission = d.pop("SCAccSubmission", UNSET)

        sc_profit_dist = d.pop("SCProfitDist", UNSET)

        sc_user_cessation = d.pop("SCUserCessation", UNSET)

        arcgis_feature_server_arcgis_layer_1009_attributes = cls(
            objectid=objectid,
            prn=prn,
            lot_area=lot_area,
            lot_area_unit=lot_area_unit,
            grant_doc_type=grant_doc_type,
            grant_doc_no=grant_doc_no,
            commencement_date=commencement_date,
            expiry_date=expiry_date,
            lease_term=lease_term,
            renewability=renewability,
            user_type=user_type,
            tree_preservation=tree_preservation,
            type_of_bldg=type_of_bldg,
            bc_date=bc_date,
            cto_date=cto_date,
            max_bldg_ht=max_bldg_ht,
            no_of_storeys=no_of_storeys,
            no_of_units_restriction=no_of_units_restriction,
            unit_size_restriction=unit_size_restriction,
            dd_or_ddh_clause=dd_or_ddh_clause,
            site_coverage=site_coverage,
            max_gfa=max_gfa,
            min_gfa=min_gfa,
            public_open_space=public_open_space,
            govt_accom=govt_accom,
            sc_auth_satisfaction=sc_auth_satisfaction,
            sc_alienation=sc_alienation,
            sc_non_profit=sc_non_profit,
            sc_acc_submission=sc_acc_submission,
            sc_profit_dist=sc_profit_dist,
            sc_user_cessation=sc_user_cessation,
        )

        arcgis_feature_server_arcgis_layer_1009_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1009_attributes

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
