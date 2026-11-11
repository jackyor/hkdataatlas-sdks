from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsVillage2023Attributes")


@_attrs_define
class WfsMapServerWfsVillage2023Attributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        planno (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        rcom_ename (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        rcom_cname (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        vil_ename (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        vil_cname (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        had_district_ename (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        had_district_cname (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        pdf_en_url (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        pdf_cn_url (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        pdf_zh_url (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        had_rcom_cname (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        had_rcom_ename (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        had_vil_cname (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        had_vil_ename (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        had_market_cname (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        had_market_ename (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        file_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    planno: None | str | Unset = UNSET
    rcom_ename: None | str | Unset = UNSET
    rcom_cname: None | str | Unset = UNSET
    vil_ename: None | str | Unset = UNSET
    vil_cname: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    had_district_ename: None | str | Unset = UNSET
    had_district_cname: None | str | Unset = UNSET
    pdf_en_url: None | str | Unset = UNSET
    pdf_cn_url: None | str | Unset = UNSET
    pdf_zh_url: None | str | Unset = UNSET
    had_rcom_cname: None | str | Unset = UNSET
    had_rcom_ename: None | str | Unset = UNSET
    had_vil_cname: None | str | Unset = UNSET
    had_vil_ename: None | str | Unset = UNSET
    had_market_cname: None | str | Unset = UNSET
    had_market_ename: None | str | Unset = UNSET
    file_name: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        planno: None | str | Unset
        if isinstance(self.planno, Unset):
            planno = UNSET
        else:
            planno = self.planno

        rcom_ename: None | str | Unset
        if isinstance(self.rcom_ename, Unset):
            rcom_ename = UNSET
        else:
            rcom_ename = self.rcom_ename

        rcom_cname: None | str | Unset
        if isinstance(self.rcom_cname, Unset):
            rcom_cname = UNSET
        else:
            rcom_cname = self.rcom_cname

        vil_ename: None | str | Unset
        if isinstance(self.vil_ename, Unset):
            vil_ename = UNSET
        else:
            vil_ename = self.vil_ename

        vil_cname: None | str | Unset
        if isinstance(self.vil_cname, Unset):
            vil_cname = UNSET
        else:
            vil_cname = self.vil_cname

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        had_district_ename: None | str | Unset
        if isinstance(self.had_district_ename, Unset):
            had_district_ename = UNSET
        else:
            had_district_ename = self.had_district_ename

        had_district_cname: None | str | Unset
        if isinstance(self.had_district_cname, Unset):
            had_district_cname = UNSET
        else:
            had_district_cname = self.had_district_cname

        pdf_en_url: None | str | Unset
        if isinstance(self.pdf_en_url, Unset):
            pdf_en_url = UNSET
        else:
            pdf_en_url = self.pdf_en_url

        pdf_cn_url: None | str | Unset
        if isinstance(self.pdf_cn_url, Unset):
            pdf_cn_url = UNSET
        else:
            pdf_cn_url = self.pdf_cn_url

        pdf_zh_url: None | str | Unset
        if isinstance(self.pdf_zh_url, Unset):
            pdf_zh_url = UNSET
        else:
            pdf_zh_url = self.pdf_zh_url

        had_rcom_cname: None | str | Unset
        if isinstance(self.had_rcom_cname, Unset):
            had_rcom_cname = UNSET
        else:
            had_rcom_cname = self.had_rcom_cname

        had_rcom_ename: None | str | Unset
        if isinstance(self.had_rcom_ename, Unset):
            had_rcom_ename = UNSET
        else:
            had_rcom_ename = self.had_rcom_ename

        had_vil_cname: None | str | Unset
        if isinstance(self.had_vil_cname, Unset):
            had_vil_cname = UNSET
        else:
            had_vil_cname = self.had_vil_cname

        had_vil_ename: None | str | Unset
        if isinstance(self.had_vil_ename, Unset):
            had_vil_ename = UNSET
        else:
            had_vil_ename = self.had_vil_ename

        had_market_cname: None | str | Unset
        if isinstance(self.had_market_cname, Unset):
            had_market_cname = UNSET
        else:
            had_market_cname = self.had_market_cname

        had_market_ename: None | str | Unset
        if isinstance(self.had_market_ename, Unset):
            had_market_ename = UNSET
        else:
            had_market_ename = self.had_market_ename

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        shape_area: float | None | Unset
        if isinstance(self.shape_area, Unset):
            shape_area = UNSET
        else:
            shape_area = self.shape_area

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if planno is not UNSET:
            field_dict["PLANNO"] = planno
        if rcom_ename is not UNSET:
            field_dict["RCOM_ENAME"] = rcom_ename
        if rcom_cname is not UNSET:
            field_dict["RCOM_CNAME"] = rcom_cname
        if vil_ename is not UNSET:
            field_dict["VIL_ENAME"] = vil_ename
        if vil_cname is not UNSET:
            field_dict["VIL_CNAME"] = vil_cname
        if district is not UNSET:
            field_dict["DISTRICT"] = district
        if had_district_ename is not UNSET:
            field_dict["HAD_DISTRICT_ENAME"] = had_district_ename
        if had_district_cname is not UNSET:
            field_dict["HAD_DISTRICT_CNAME"] = had_district_cname
        if pdf_en_url is not UNSET:
            field_dict["PDF_EN_URL"] = pdf_en_url
        if pdf_cn_url is not UNSET:
            field_dict["PDF_CN_URL"] = pdf_cn_url
        if pdf_zh_url is not UNSET:
            field_dict["PDF_ZH_URL"] = pdf_zh_url
        if had_rcom_cname is not UNSET:
            field_dict["HAD_RCOM_CNAME"] = had_rcom_cname
        if had_rcom_ename is not UNSET:
            field_dict["HAD_RCOM_ENAME"] = had_rcom_ename
        if had_vil_cname is not UNSET:
            field_dict["HAD_VIL_CNAME"] = had_vil_cname
        if had_vil_ename is not UNSET:
            field_dict["HAD_VIL_ENAME"] = had_vil_ename
        if had_market_cname is not UNSET:
            field_dict["HAD_MARKET_CNAME"] = had_market_cname
        if had_market_ename is not UNSET:
            field_dict["HAD_MARKET_ENAME"] = had_market_ename
        if file_name is not UNSET:
            field_dict["FILE_NAME"] = file_name
        if shape_length is not UNSET:
            field_dict["Shape_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("Shape", UNSET)

        def _parse_planno(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planno = _parse_planno(d.pop("PLANNO", UNSET))

        def _parse_rcom_ename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rcom_ename = _parse_rcom_ename(d.pop("RCOM_ENAME", UNSET))

        def _parse_rcom_cname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rcom_cname = _parse_rcom_cname(d.pop("RCOM_CNAME", UNSET))

        def _parse_vil_ename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vil_ename = _parse_vil_ename(d.pop("VIL_ENAME", UNSET))

        def _parse_vil_cname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vil_cname = _parse_vil_cname(d.pop("VIL_CNAME", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("DISTRICT", UNSET))

        def _parse_had_district_ename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        had_district_ename = _parse_had_district_ename(
            d.pop("HAD_DISTRICT_ENAME", UNSET)
        )

        def _parse_had_district_cname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        had_district_cname = _parse_had_district_cname(
            d.pop("HAD_DISTRICT_CNAME", UNSET)
        )

        def _parse_pdf_en_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pdf_en_url = _parse_pdf_en_url(d.pop("PDF_EN_URL", UNSET))

        def _parse_pdf_cn_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pdf_cn_url = _parse_pdf_cn_url(d.pop("PDF_CN_URL", UNSET))

        def _parse_pdf_zh_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pdf_zh_url = _parse_pdf_zh_url(d.pop("PDF_ZH_URL", UNSET))

        def _parse_had_rcom_cname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        had_rcom_cname = _parse_had_rcom_cname(d.pop("HAD_RCOM_CNAME", UNSET))

        def _parse_had_rcom_ename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        had_rcom_ename = _parse_had_rcom_ename(d.pop("HAD_RCOM_ENAME", UNSET))

        def _parse_had_vil_cname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        had_vil_cname = _parse_had_vil_cname(d.pop("HAD_VIL_CNAME", UNSET))

        def _parse_had_vil_ename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        had_vil_ename = _parse_had_vil_ename(d.pop("HAD_VIL_ENAME", UNSET))

        def _parse_had_market_cname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        had_market_cname = _parse_had_market_cname(d.pop("HAD_MARKET_CNAME", UNSET))

        def _parse_had_market_ename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        had_market_ename = _parse_had_market_ename(d.pop("HAD_MARKET_ENAME", UNSET))

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("FILE_NAME", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape_Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape_Area", UNSET))

        wfs_map_server_wfs_village_2023_attributes = cls(
            objectid=objectid,
            shape=shape,
            planno=planno,
            rcom_ename=rcom_ename,
            rcom_cname=rcom_cname,
            vil_ename=vil_ename,
            vil_cname=vil_cname,
            district=district,
            had_district_ename=had_district_ename,
            had_district_cname=had_district_cname,
            pdf_en_url=pdf_en_url,
            pdf_cn_url=pdf_cn_url,
            pdf_zh_url=pdf_zh_url,
            had_rcom_cname=had_rcom_cname,
            had_rcom_ename=had_rcom_ename,
            had_vil_cname=had_vil_cname,
            had_vil_ename=had_vil_ename,
            had_market_cname=had_market_cname,
            had_market_ename=had_market_ename,
            file_name=file_name,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_village_2023_attributes.additional_properties = d
        return wfs_map_server_wfs_village_2023_attributes

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
