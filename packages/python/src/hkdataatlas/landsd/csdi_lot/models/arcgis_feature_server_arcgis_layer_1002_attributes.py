from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1002Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1002Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        memorial_no (str | Unset): Publisher field type: esriFieldTypeString
        instrument_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
        main_nature_code (str | Unset): Publisher field type: esriFieldTypeString
        sub_nature_code (str | Unset): Publisher field type: esriFieldTypeString
        nature_description (str | Unset): Publisher field type: esriFieldTypeString
        nature_description_chn (None | str | Unset): Publisher field type: esriFieldTypeString
        consideration_part_code (None | str | Unset): Publisher field type: esriFieldTypeString
        consideration (float | None | Unset): Publisher field type: esriFieldTypeDouble
        consideration_text (None | str | Unset): Publisher field type: esriFieldTypeString
        consideration_text_chn (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    memorial_no: str | Unset = UNSET
    instrument_date: Any | Unset = UNSET
    main_nature_code: str | Unset = UNSET
    sub_nature_code: str | Unset = UNSET
    nature_description: str | Unset = UNSET
    nature_description_chn: None | str | Unset = UNSET
    consideration_part_code: None | str | Unset = UNSET
    consideration: float | None | Unset = UNSET
    consideration_text: None | str | Unset = UNSET
    consideration_text_chn: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        memorial_no = self.memorial_no

        instrument_date = self.instrument_date

        main_nature_code = self.main_nature_code

        sub_nature_code = self.sub_nature_code

        nature_description = self.nature_description

        nature_description_chn: None | str | Unset
        if isinstance(self.nature_description_chn, Unset):
            nature_description_chn = UNSET
        else:
            nature_description_chn = self.nature_description_chn

        consideration_part_code: None | str | Unset
        if isinstance(self.consideration_part_code, Unset):
            consideration_part_code = UNSET
        else:
            consideration_part_code = self.consideration_part_code

        consideration: float | None | Unset
        if isinstance(self.consideration, Unset):
            consideration = UNSET
        else:
            consideration = self.consideration

        consideration_text: None | str | Unset
        if isinstance(self.consideration_text, Unset):
            consideration_text = UNSET
        else:
            consideration_text = self.consideration_text

        consideration_text_chn: None | str | Unset
        if isinstance(self.consideration_text_chn, Unset):
            consideration_text_chn = UNSET
        else:
            consideration_text_chn = self.consideration_text_chn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if memorial_no is not UNSET:
            field_dict["MemorialNo"] = memorial_no
        if instrument_date is not UNSET:
            field_dict["InstrumentDate"] = instrument_date
        if main_nature_code is not UNSET:
            field_dict["MainNatureCode"] = main_nature_code
        if sub_nature_code is not UNSET:
            field_dict["SubNatureCode"] = sub_nature_code
        if nature_description is not UNSET:
            field_dict["NatureDescription"] = nature_description
        if nature_description_chn is not UNSET:
            field_dict["NatureDescriptionCHN"] = nature_description_chn
        if consideration_part_code is not UNSET:
            field_dict["ConsiderationPartCode"] = consideration_part_code
        if consideration is not UNSET:
            field_dict["Consideration"] = consideration
        if consideration_text is not UNSET:
            field_dict["ConsiderationText"] = consideration_text
        if consideration_text_chn is not UNSET:
            field_dict["ConsiderationTextCHN"] = consideration_text_chn

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        memorial_no = d.pop("MemorialNo", UNSET)

        instrument_date = d.pop("InstrumentDate", UNSET)

        main_nature_code = d.pop("MainNatureCode", UNSET)

        sub_nature_code = d.pop("SubNatureCode", UNSET)

        nature_description = d.pop("NatureDescription", UNSET)

        def _parse_nature_description_chn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nature_description_chn = _parse_nature_description_chn(
            d.pop("NatureDescriptionCHN", UNSET)
        )

        def _parse_consideration_part_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        consideration_part_code = _parse_consideration_part_code(
            d.pop("ConsiderationPartCode", UNSET)
        )

        def _parse_consideration(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        consideration = _parse_consideration(d.pop("Consideration", UNSET))

        def _parse_consideration_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        consideration_text = _parse_consideration_text(
            d.pop("ConsiderationText", UNSET)
        )

        def _parse_consideration_text_chn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        consideration_text_chn = _parse_consideration_text_chn(
            d.pop("ConsiderationTextCHN", UNSET)
        )

        arcgis_feature_server_arcgis_layer_1002_attributes = cls(
            objectid=objectid,
            memorial_no=memorial_no,
            instrument_date=instrument_date,
            main_nature_code=main_nature_code,
            sub_nature_code=sub_nature_code,
            nature_description=nature_description,
            nature_description_chn=nature_description_chn,
            consideration_part_code=consideration_part_code,
            consideration=consideration,
            consideration_text=consideration_text,
            consideration_text_chn=consideration_text_chn,
        )

        arcgis_feature_server_arcgis_layer_1002_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1002_attributes

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
