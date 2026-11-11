from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsAPPCRTAttributes")


@_attrs_define
class WfsMapServerWfsAPPCRTAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        case_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        type_code (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        fi_no (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML occurrence into
            all JSON queries.
        dpo (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        schm_code (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        ozp_pln_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        status (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        aply_use (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        locat_addr (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        appeal_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        s16_deci (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        s16_d_date (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        s17_deci (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        s17_d_date (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        apl_deci (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        apl_d_date (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        lst_upload (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML occurrence
            into all JSON queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        shape_st_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_st_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    objectid: int | Unset = UNSET
    case_no: None | str | Unset = UNSET
    type_code: None | str | Unset = UNSET
    fi_no: int | None | Unset = UNSET
    dpo: None | str | Unset = UNSET
    schm_code: None | str | Unset = UNSET
    ozp_pln_no: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    aply_use: None | str | Unset = UNSET
    locat_addr: None | str | Unset = UNSET
    appeal_no: None | str | Unset = UNSET
    s16_deci: None | str | Unset = UNSET
    s16_d_date: None | str | Unset = UNSET
    s17_deci: None | str | Unset = UNSET
    s17_d_date: None | str | Unset = UNSET
    apl_deci: None | str | Unset = UNSET
    apl_d_date: None | str | Unset = UNSET
    lst_upload: None | str | Unset = UNSET
    shape: Any | Unset = UNSET
    shape_st_area: float | None | Unset = UNSET
    shape_st_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        case_no: None | str | Unset
        if isinstance(self.case_no, Unset):
            case_no = UNSET
        else:
            case_no = self.case_no

        type_code: None | str | Unset
        if isinstance(self.type_code, Unset):
            type_code = UNSET
        else:
            type_code = self.type_code

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

        aply_use: None | str | Unset
        if isinstance(self.aply_use, Unset):
            aply_use = UNSET
        else:
            aply_use = self.aply_use

        locat_addr: None | str | Unset
        if isinstance(self.locat_addr, Unset):
            locat_addr = UNSET
        else:
            locat_addr = self.locat_addr

        appeal_no: None | str | Unset
        if isinstance(self.appeal_no, Unset):
            appeal_no = UNSET
        else:
            appeal_no = self.appeal_no

        s16_deci: None | str | Unset
        if isinstance(self.s16_deci, Unset):
            s16_deci = UNSET
        else:
            s16_deci = self.s16_deci

        s16_d_date: None | str | Unset
        if isinstance(self.s16_d_date, Unset):
            s16_d_date = UNSET
        else:
            s16_d_date = self.s16_d_date

        s17_deci: None | str | Unset
        if isinstance(self.s17_deci, Unset):
            s17_deci = UNSET
        else:
            s17_deci = self.s17_deci

        s17_d_date: None | str | Unset
        if isinstance(self.s17_d_date, Unset):
            s17_d_date = UNSET
        else:
            s17_d_date = self.s17_d_date

        apl_deci: None | str | Unset
        if isinstance(self.apl_deci, Unset):
            apl_deci = UNSET
        else:
            apl_deci = self.apl_deci

        apl_d_date: None | str | Unset
        if isinstance(self.apl_d_date, Unset):
            apl_d_date = UNSET
        else:
            apl_d_date = self.apl_d_date

        lst_upload: None | str | Unset
        if isinstance(self.lst_upload, Unset):
            lst_upload = UNSET
        else:
            lst_upload = self.lst_upload

        shape = self.shape

        shape_st_area: float | None | Unset
        if isinstance(self.shape_st_area, Unset):
            shape_st_area = UNSET
        else:
            shape_st_area = self.shape_st_area

        shape_st_length: float | None | Unset
        if isinstance(self.shape_st_length, Unset):
            shape_st_length = UNSET
        else:
            shape_st_length = self.shape_st_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if case_no is not UNSET:
            field_dict["CASE_NO"] = case_no
        if type_code is not UNSET:
            field_dict["TYPE_CODE"] = type_code
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
        if aply_use is not UNSET:
            field_dict["APLY_USE"] = aply_use
        if locat_addr is not UNSET:
            field_dict["LOCAT_ADDR"] = locat_addr
        if appeal_no is not UNSET:
            field_dict["APPEAL_NO"] = appeal_no
        if s16_deci is not UNSET:
            field_dict["S16_DECI"] = s16_deci
        if s16_d_date is not UNSET:
            field_dict["S16_D_DATE"] = s16_d_date
        if s17_deci is not UNSET:
            field_dict["S17_DECI"] = s17_deci
        if s17_d_date is not UNSET:
            field_dict["S17_D_DATE"] = s17_d_date
        if apl_deci is not UNSET:
            field_dict["APL_DECI"] = apl_deci
        if apl_d_date is not UNSET:
            field_dict["APL_D_DATE"] = apl_d_date
        if lst_upload is not UNSET:
            field_dict["LST_UPLOAD"] = lst_upload
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if shape_st_area is not UNSET:
            field_dict["Shape.STArea__"] = shape_st_area
        if shape_st_length is not UNSET:
            field_dict["Shape.STLength__"] = shape_st_length

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

        def _parse_type_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_code = _parse_type_code(d.pop("TYPE_CODE", UNSET))

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

        def _parse_aply_use(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aply_use = _parse_aply_use(d.pop("APLY_USE", UNSET))

        def _parse_locat_addr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locat_addr = _parse_locat_addr(d.pop("LOCAT_ADDR", UNSET))

        def _parse_appeal_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        appeal_no = _parse_appeal_no(d.pop("APPEAL_NO", UNSET))

        def _parse_s16_deci(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s16_deci = _parse_s16_deci(d.pop("S16_DECI", UNSET))

        def _parse_s16_d_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s16_d_date = _parse_s16_d_date(d.pop("S16_D_DATE", UNSET))

        def _parse_s17_deci(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s17_deci = _parse_s17_deci(d.pop("S17_DECI", UNSET))

        def _parse_s17_d_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s17_d_date = _parse_s17_d_date(d.pop("S17_D_DATE", UNSET))

        def _parse_apl_deci(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        apl_deci = _parse_apl_deci(d.pop("APL_DECI", UNSET))

        def _parse_apl_d_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        apl_d_date = _parse_apl_d_date(d.pop("APL_D_DATE", UNSET))

        def _parse_lst_upload(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lst_upload = _parse_lst_upload(d.pop("LST_UPLOAD", UNSET))

        shape = d.pop("Shape", UNSET)

        def _parse_shape_st_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_st_area = _parse_shape_st_area(d.pop("Shape.STArea__", UNSET))

        def _parse_shape_st_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_st_length = _parse_shape_st_length(d.pop("Shape.STLength__", UNSET))

        wfs_map_server_wfs_appcrt_attributes = cls(
            objectid=objectid,
            case_no=case_no,
            type_code=type_code,
            fi_no=fi_no,
            dpo=dpo,
            schm_code=schm_code,
            ozp_pln_no=ozp_pln_no,
            status=status,
            aply_use=aply_use,
            locat_addr=locat_addr,
            appeal_no=appeal_no,
            s16_deci=s16_deci,
            s16_d_date=s16_d_date,
            s17_deci=s17_deci,
            s17_d_date=s17_d_date,
            apl_deci=apl_deci,
            apl_d_date=apl_d_date,
            lst_upload=lst_upload,
            shape=shape,
            shape_st_area=shape_st_area,
            shape_st_length=shape_st_length,
        )

        wfs_map_server_wfs_appcrt_attributes.additional_properties = d
        return wfs_map_server_wfs_appcrt_attributes

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
