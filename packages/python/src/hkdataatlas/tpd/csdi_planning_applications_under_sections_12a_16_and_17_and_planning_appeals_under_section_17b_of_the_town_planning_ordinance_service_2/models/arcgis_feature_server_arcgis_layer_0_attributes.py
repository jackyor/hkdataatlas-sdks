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
        case_no (None | str | Unset): Publisher field type: esriFieldTypeString
        fi_no (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        dpo (None | str | Unset): Publisher field type: esriFieldTypeString
        schm_code (None | str | Unset): Publisher field type: esriFieldTypeString
        ozp_pln_no (None | str | Unset): Publisher field type: esriFieldTypeString
        status (None | str | Unset): Publisher field type: esriFieldTypeString
        prop_amend (None | str | Unset): Publisher field type: esriFieldTypeString
        locat_addr (None | str | Unset): Publisher field type: esriFieldTypeString
        s12a_deci (None | str | Unset): Publisher field type: esriFieldTypeString
        s12a_d_date (None | str | Unset): Publisher field type: esriFieldTypeString
        lst_upload (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    case_no: None | str | Unset = UNSET
    fi_no: int | None | Unset = UNSET
    dpo: None | str | Unset = UNSET
    schm_code: None | str | Unset = UNSET
    ozp_pln_no: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    prop_amend: None | str | Unset = UNSET
    locat_addr: None | str | Unset = UNSET
    s12a_deci: None | str | Unset = UNSET
    s12a_d_date: None | str | Unset = UNSET
    lst_upload: Any | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        case_no: None | str | Unset
        if isinstance(self.case_no, Unset):
            case_no = UNSET
        else:
            case_no = self.case_no

        fi_no: int | None | Unset
        if isinstance(self.fi_no, Unset):
            fi_no = UNSET
        else:
            fi_no = self.fi_no

        dpo: None | str | Unset
        if isinstance(self.dpo, Unset):
            dpo = UNSET
        else:
            dpo = self.dpo

        schm_code: None | str | Unset
        if isinstance(self.schm_code, Unset):
            schm_code = UNSET
        else:
            schm_code = self.schm_code

        ozp_pln_no: None | str | Unset
        if isinstance(self.ozp_pln_no, Unset):
            ozp_pln_no = UNSET
        else:
            ozp_pln_no = self.ozp_pln_no

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        prop_amend: None | str | Unset
        if isinstance(self.prop_amend, Unset):
            prop_amend = UNSET
        else:
            prop_amend = self.prop_amend

        locat_addr: None | str | Unset
        if isinstance(self.locat_addr, Unset):
            locat_addr = UNSET
        else:
            locat_addr = self.locat_addr

        s12a_deci: None | str | Unset
        if isinstance(self.s12a_deci, Unset):
            s12a_deci = UNSET
        else:
            s12a_deci = self.s12a_deci

        s12a_d_date: None | str | Unset
        if isinstance(self.s12a_d_date, Unset):
            s12a_d_date = UNSET
        else:
            s12a_d_date = self.s12a_d_date

        lst_upload = self.lst_upload

        shape_area: float | None | Unset
        if isinstance(self.shape_area, Unset):
            shape_area = UNSET
        else:
            shape_area = self.shape_area

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if case_no is not UNSET:
            field_dict["CASE_NO"] = case_no
        if fi_no is not UNSET:
            field_dict["FI_NO"] = fi_no
        if dpo is not UNSET:
            field_dict["DPO"] = dpo
        if schm_code is not UNSET:
            field_dict["SCHM_CODE"] = schm_code
        if ozp_pln_no is not UNSET:
            field_dict["OZP_PLN_NO"] = ozp_pln_no
        if status is not UNSET:
            field_dict["STATUS"] = status
        if prop_amend is not UNSET:
            field_dict["PROP_AMEND"] = prop_amend
        if locat_addr is not UNSET:
            field_dict["LOCAT_ADDR"] = locat_addr
        if s12a_deci is not UNSET:
            field_dict["S12A_DECI"] = s12a_deci
        if s12a_d_date is not UNSET:
            field_dict["S12A_D_DATE"] = s12a_d_date
        if lst_upload is not UNSET:
            field_dict["LST_UPLOAD"] = lst_upload
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_case_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        case_no = _parse_case_no(d.pop("CASE_NO", UNSET))

        def _parse_fi_no(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fi_no = _parse_fi_no(d.pop("FI_NO", UNSET))

        def _parse_dpo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dpo = _parse_dpo(d.pop("DPO", UNSET))

        def _parse_schm_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schm_code = _parse_schm_code(d.pop("SCHM_CODE", UNSET))

        def _parse_ozp_pln_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ozp_pln_no = _parse_ozp_pln_no(d.pop("OZP_PLN_NO", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("STATUS", UNSET))

        def _parse_prop_amend(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prop_amend = _parse_prop_amend(d.pop("PROP_AMEND", UNSET))

        def _parse_locat_addr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locat_addr = _parse_locat_addr(d.pop("LOCAT_ADDR", UNSET))

        def _parse_s12a_deci(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s12a_deci = _parse_s12a_deci(d.pop("S12A_DECI", UNSET))

        def _parse_s12a_d_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s12a_d_date = _parse_s12a_d_date(d.pop("S12A_D_DATE", UNSET))

        lst_upload = d.pop("LST_UPLOAD", UNSET)

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape__Area", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            case_no=case_no,
            fi_no=fi_no,
            dpo=dpo,
            schm_code=schm_code,
            ozp_pln_no=ozp_pln_no,
            status=status,
            prop_amend=prop_amend,
            locat_addr=locat_addr,
            s12a_deci=s12a_deci,
            s12a_d_date=s12a_d_date,
            lst_upload=lst_upload,
            shape_area=shape_area,
            shape_length=shape_length,
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
