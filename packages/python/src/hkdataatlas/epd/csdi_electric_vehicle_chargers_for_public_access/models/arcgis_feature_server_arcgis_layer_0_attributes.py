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
        name_of_district_council_district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        location_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_district_council_district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        location_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_district_council_district_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        location_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        standard_bs1363_no (None | str | Unset): Publisher field type: esriFieldTypeString
        medium_ccs_dc_combo_no (None | str | Unset): Publisher field type: esriFieldTypeString
        medium_iec62196_no (None | str | Unset): Publisher field type: esriFieldTypeString
        medium_saej1772_no (None | str | Unset): Publisher field type: esriFieldTypeString
        medium_gb_t20234_2_ac_no (None | str | Unset): Publisher field type: esriFieldTypeString
        medium_others_no (None | str | Unset): Publisher field type: esriFieldTypeString
        quick_ch_ade_mo_no (None | str | Unset): Publisher field type: esriFieldTypeString
        quick_ccs_dc_combo_no (None | str | Unset): Publisher field type: esriFieldTypeString
        quick_iec62196_no (None | str | Unset): Publisher field type: esriFieldTypeString
        quick_gb_t20234_3_dc_no (None | str | Unset): Publisher field type: esriFieldTypeString
        quick_others_no (None | str | Unset): Publisher field type: esriFieldTypeString
        fast_ch_ade_mo_no (None | str | Unset): Publisher field type: esriFieldTypeString
        fast_ccs_dc_combo_no (None | str | Unset): Publisher field type: esriFieldTypeString
        fast_gb_t20234_3_dc_no (None | str | Unset): Publisher field type: esriFieldTypeString
        fast_others_no (None | str | Unset): Publisher field type: esriFieldTypeString
        remark_for_others (None | str | Unset): Publisher field type: esriFieldTypeString
        data_path (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    name_of_district_council_district_en: None | str | Unset = UNSET
    location_en: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    name_of_district_council_district_tc: None | str | Unset = UNSET
    location_tc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    name_of_district_council_district_sc: None | str | Unset = UNSET
    location_sc: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    standard_bs1363_no: None | str | Unset = UNSET
    medium_ccs_dc_combo_no: None | str | Unset = UNSET
    medium_iec62196_no: None | str | Unset = UNSET
    medium_saej1772_no: None | str | Unset = UNSET
    medium_gb_t20234_2_ac_no: None | str | Unset = UNSET
    medium_others_no: None | str | Unset = UNSET
    quick_ch_ade_mo_no: None | str | Unset = UNSET
    quick_ccs_dc_combo_no: None | str | Unset = UNSET
    quick_iec62196_no: None | str | Unset = UNSET
    quick_gb_t20234_3_dc_no: None | str | Unset = UNSET
    quick_others_no: None | str | Unset = UNSET
    fast_ch_ade_mo_no: None | str | Unset = UNSET
    fast_ccs_dc_combo_no: None | str | Unset = UNSET
    fast_gb_t20234_3_dc_no: None | str | Unset = UNSET
    fast_others_no: None | str | Unset = UNSET
    remark_for_others: None | str | Unset = UNSET
    data_path: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_of_district_council_district_en: None | str | Unset
        if isinstance(self.name_of_district_council_district_en, Unset):
            name_of_district_council_district_en = UNSET
        else:
            name_of_district_council_district_en = (
                self.name_of_district_council_district_en
            )

        location_en: None | str | Unset
        if isinstance(self.location_en, Unset):
            location_en = UNSET
        else:
            location_en = self.location_en

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        name_of_district_council_district_tc: None | str | Unset
        if isinstance(self.name_of_district_council_district_tc, Unset):
            name_of_district_council_district_tc = UNSET
        else:
            name_of_district_council_district_tc = (
                self.name_of_district_council_district_tc
            )

        location_tc: None | str | Unset
        if isinstance(self.location_tc, Unset):
            location_tc = UNSET
        else:
            location_tc = self.location_tc

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        name_of_district_council_district_sc: None | str | Unset
        if isinstance(self.name_of_district_council_district_sc, Unset):
            name_of_district_council_district_sc = UNSET
        else:
            name_of_district_council_district_sc = (
                self.name_of_district_council_district_sc
            )

        location_sc: None | str | Unset
        if isinstance(self.location_sc, Unset):
            location_sc = UNSET
        else:
            location_sc = self.location_sc

        address_sc: None | str | Unset
        if isinstance(self.address_sc, Unset):
            address_sc = UNSET
        else:
            address_sc = self.address_sc

        standard_bs1363_no: None | str | Unset
        if isinstance(self.standard_bs1363_no, Unset):
            standard_bs1363_no = UNSET
        else:
            standard_bs1363_no = self.standard_bs1363_no

        medium_ccs_dc_combo_no: None | str | Unset
        if isinstance(self.medium_ccs_dc_combo_no, Unset):
            medium_ccs_dc_combo_no = UNSET
        else:
            medium_ccs_dc_combo_no = self.medium_ccs_dc_combo_no

        medium_iec62196_no: None | str | Unset
        if isinstance(self.medium_iec62196_no, Unset):
            medium_iec62196_no = UNSET
        else:
            medium_iec62196_no = self.medium_iec62196_no

        medium_saej1772_no: None | str | Unset
        if isinstance(self.medium_saej1772_no, Unset):
            medium_saej1772_no = UNSET
        else:
            medium_saej1772_no = self.medium_saej1772_no

        medium_gb_t20234_2_ac_no: None | str | Unset
        if isinstance(self.medium_gb_t20234_2_ac_no, Unset):
            medium_gb_t20234_2_ac_no = UNSET
        else:
            medium_gb_t20234_2_ac_no = self.medium_gb_t20234_2_ac_no

        medium_others_no: None | str | Unset
        if isinstance(self.medium_others_no, Unset):
            medium_others_no = UNSET
        else:
            medium_others_no = self.medium_others_no

        quick_ch_ade_mo_no: None | str | Unset
        if isinstance(self.quick_ch_ade_mo_no, Unset):
            quick_ch_ade_mo_no = UNSET
        else:
            quick_ch_ade_mo_no = self.quick_ch_ade_mo_no

        quick_ccs_dc_combo_no: None | str | Unset
        if isinstance(self.quick_ccs_dc_combo_no, Unset):
            quick_ccs_dc_combo_no = UNSET
        else:
            quick_ccs_dc_combo_no = self.quick_ccs_dc_combo_no

        quick_iec62196_no: None | str | Unset
        if isinstance(self.quick_iec62196_no, Unset):
            quick_iec62196_no = UNSET
        else:
            quick_iec62196_no = self.quick_iec62196_no

        quick_gb_t20234_3_dc_no: None | str | Unset
        if isinstance(self.quick_gb_t20234_3_dc_no, Unset):
            quick_gb_t20234_3_dc_no = UNSET
        else:
            quick_gb_t20234_3_dc_no = self.quick_gb_t20234_3_dc_no

        quick_others_no: None | str | Unset
        if isinstance(self.quick_others_no, Unset):
            quick_others_no = UNSET
        else:
            quick_others_no = self.quick_others_no

        fast_ch_ade_mo_no: None | str | Unset
        if isinstance(self.fast_ch_ade_mo_no, Unset):
            fast_ch_ade_mo_no = UNSET
        else:
            fast_ch_ade_mo_no = self.fast_ch_ade_mo_no

        fast_ccs_dc_combo_no: None | str | Unset
        if isinstance(self.fast_ccs_dc_combo_no, Unset):
            fast_ccs_dc_combo_no = UNSET
        else:
            fast_ccs_dc_combo_no = self.fast_ccs_dc_combo_no

        fast_gb_t20234_3_dc_no: None | str | Unset
        if isinstance(self.fast_gb_t20234_3_dc_no, Unset):
            fast_gb_t20234_3_dc_no = UNSET
        else:
            fast_gb_t20234_3_dc_no = self.fast_gb_t20234_3_dc_no

        fast_others_no: None | str | Unset
        if isinstance(self.fast_others_no, Unset):
            fast_others_no = UNSET
        else:
            fast_others_no = self.fast_others_no

        remark_for_others: None | str | Unset
        if isinstance(self.remark_for_others, Unset):
            remark_for_others = UNSET
        else:
            remark_for_others = self.remark_for_others

        data_path: None | str | Unset
        if isinstance(self.data_path, Unset):
            data_path = UNSET
        else:
            data_path = self.data_path

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name_of_district_council_district_en is not UNSET:
            field_dict["NAME_OF_DISTRICT_COUNCIL_DISTRICT_EN"] = (
                name_of_district_council_district_en
            )
        if location_en is not UNSET:
            field_dict["LOCATION_EN"] = location_en
        if address_en is not UNSET:
            field_dict["ADDRESS_EN"] = address_en
        if name_of_district_council_district_tc is not UNSET:
            field_dict["NAME_OF_DISTRICT_COUNCIL_DISTRICT_TC"] = (
                name_of_district_council_district_tc
            )
        if location_tc is not UNSET:
            field_dict["LOCATION_TC"] = location_tc
        if address_tc is not UNSET:
            field_dict["ADDRESS_TC"] = address_tc
        if name_of_district_council_district_sc is not UNSET:
            field_dict["NAME_OF_DISTRICT_COUNCIL_DISTRICT_SC"] = (
                name_of_district_council_district_sc
            )
        if location_sc is not UNSET:
            field_dict["LOCATION_SC"] = location_sc
        if address_sc is not UNSET:
            field_dict["ADDRESS_SC"] = address_sc
        if standard_bs1363_no is not UNSET:
            field_dict["STANDARD_BS1363_no"] = standard_bs1363_no
        if medium_ccs_dc_combo_no is not UNSET:
            field_dict["MEDIUM_CCS_DC_COMBO_no"] = medium_ccs_dc_combo_no
        if medium_iec62196_no is not UNSET:
            field_dict["MEDIUM_IEC62196_no"] = medium_iec62196_no
        if medium_saej1772_no is not UNSET:
            field_dict["MEDIUM_SAEJ1772_no"] = medium_saej1772_no
        if medium_gb_t20234_2_ac_no is not UNSET:
            field_dict["MEDIUM_GB_T20234_2_AC__no"] = medium_gb_t20234_2_ac_no
        if medium_others_no is not UNSET:
            field_dict["MEDIUM_OTHERS_no"] = medium_others_no
        if quick_ch_ade_mo_no is not UNSET:
            field_dict["QUICK_CHAdeMO_no"] = quick_ch_ade_mo_no
        if quick_ccs_dc_combo_no is not UNSET:
            field_dict["QUICK_CCS_DC_COMBO_no"] = quick_ccs_dc_combo_no
        if quick_iec62196_no is not UNSET:
            field_dict["QUICK_IEC62196_no"] = quick_iec62196_no
        if quick_gb_t20234_3_dc_no is not UNSET:
            field_dict["QUICK_GB_T20234_3_DC__no"] = quick_gb_t20234_3_dc_no
        if quick_others_no is not UNSET:
            field_dict["QUICK_OTHERS_no"] = quick_others_no
        if fast_ch_ade_mo_no is not UNSET:
            field_dict["FAST_CHAdeMO_no"] = fast_ch_ade_mo_no
        if fast_ccs_dc_combo_no is not UNSET:
            field_dict["FAST_CCS_DC_COMBO_no"] = fast_ccs_dc_combo_no
        if fast_gb_t20234_3_dc_no is not UNSET:
            field_dict["FAST_GB_T20234_3_DC__no"] = fast_gb_t20234_3_dc_no
        if fast_others_no is not UNSET:
            field_dict["FAST_OTHERS_no"] = fast_others_no
        if remark_for_others is not UNSET:
            field_dict["REMARK_FOR__OTHERS_"] = remark_for_others
        if data_path is not UNSET:
            field_dict["DATA_PATH"] = data_path
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_name_of_district_council_district_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_district_council_district_en = (
            _parse_name_of_district_council_district_en(
                d.pop("NAME_OF_DISTRICT_COUNCIL_DISTRICT_EN", UNSET)
            )
        )

        def _parse_location_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_en = _parse_location_en(d.pop("LOCATION_EN", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("ADDRESS_EN", UNSET))

        def _parse_name_of_district_council_district_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_district_council_district_tc = (
            _parse_name_of_district_council_district_tc(
                d.pop("NAME_OF_DISTRICT_COUNCIL_DISTRICT_TC", UNSET)
            )
        )

        def _parse_location_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_tc = _parse_location_tc(d.pop("LOCATION_TC", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("ADDRESS_TC", UNSET))

        def _parse_name_of_district_council_district_sc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_district_council_district_sc = (
            _parse_name_of_district_council_district_sc(
                d.pop("NAME_OF_DISTRICT_COUNCIL_DISTRICT_SC", UNSET)
            )
        )

        def _parse_location_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_sc = _parse_location_sc(d.pop("LOCATION_SC", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("ADDRESS_SC", UNSET))

        def _parse_standard_bs1363_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        standard_bs1363_no = _parse_standard_bs1363_no(
            d.pop("STANDARD_BS1363_no", UNSET)
        )

        def _parse_medium_ccs_dc_combo_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        medium_ccs_dc_combo_no = _parse_medium_ccs_dc_combo_no(
            d.pop("MEDIUM_CCS_DC_COMBO_no", UNSET)
        )

        def _parse_medium_iec62196_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        medium_iec62196_no = _parse_medium_iec62196_no(
            d.pop("MEDIUM_IEC62196_no", UNSET)
        )

        def _parse_medium_saej1772_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        medium_saej1772_no = _parse_medium_saej1772_no(
            d.pop("MEDIUM_SAEJ1772_no", UNSET)
        )

        def _parse_medium_gb_t20234_2_ac_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        medium_gb_t20234_2_ac_no = _parse_medium_gb_t20234_2_ac_no(
            d.pop("MEDIUM_GB_T20234_2_AC__no", UNSET)
        )

        def _parse_medium_others_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        medium_others_no = _parse_medium_others_no(d.pop("MEDIUM_OTHERS_no", UNSET))

        def _parse_quick_ch_ade_mo_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quick_ch_ade_mo_no = _parse_quick_ch_ade_mo_no(d.pop("QUICK_CHAdeMO_no", UNSET))

        def _parse_quick_ccs_dc_combo_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quick_ccs_dc_combo_no = _parse_quick_ccs_dc_combo_no(
            d.pop("QUICK_CCS_DC_COMBO_no", UNSET)
        )

        def _parse_quick_iec62196_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quick_iec62196_no = _parse_quick_iec62196_no(d.pop("QUICK_IEC62196_no", UNSET))

        def _parse_quick_gb_t20234_3_dc_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quick_gb_t20234_3_dc_no = _parse_quick_gb_t20234_3_dc_no(
            d.pop("QUICK_GB_T20234_3_DC__no", UNSET)
        )

        def _parse_quick_others_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quick_others_no = _parse_quick_others_no(d.pop("QUICK_OTHERS_no", UNSET))

        def _parse_fast_ch_ade_mo_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fast_ch_ade_mo_no = _parse_fast_ch_ade_mo_no(d.pop("FAST_CHAdeMO_no", UNSET))

        def _parse_fast_ccs_dc_combo_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fast_ccs_dc_combo_no = _parse_fast_ccs_dc_combo_no(
            d.pop("FAST_CCS_DC_COMBO_no", UNSET)
        )

        def _parse_fast_gb_t20234_3_dc_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fast_gb_t20234_3_dc_no = _parse_fast_gb_t20234_3_dc_no(
            d.pop("FAST_GB_T20234_3_DC__no", UNSET)
        )

        def _parse_fast_others_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fast_others_no = _parse_fast_others_no(d.pop("FAST_OTHERS_no", UNSET))

        def _parse_remark_for_others(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark_for_others = _parse_remark_for_others(
            d.pop("REMARK_FOR__OTHERS_", UNSET)
        )

        def _parse_data_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_path = _parse_data_path(d.pop("DATA_PATH", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            name_of_district_council_district_en=name_of_district_council_district_en,
            location_en=location_en,
            address_en=address_en,
            name_of_district_council_district_tc=name_of_district_council_district_tc,
            location_tc=location_tc,
            address_tc=address_tc,
            name_of_district_council_district_sc=name_of_district_council_district_sc,
            location_sc=location_sc,
            address_sc=address_sc,
            standard_bs1363_no=standard_bs1363_no,
            medium_ccs_dc_combo_no=medium_ccs_dc_combo_no,
            medium_iec62196_no=medium_iec62196_no,
            medium_saej1772_no=medium_saej1772_no,
            medium_gb_t20234_2_ac_no=medium_gb_t20234_2_ac_no,
            medium_others_no=medium_others_no,
            quick_ch_ade_mo_no=quick_ch_ade_mo_no,
            quick_ccs_dc_combo_no=quick_ccs_dc_combo_no,
            quick_iec62196_no=quick_iec62196_no,
            quick_gb_t20234_3_dc_no=quick_gb_t20234_3_dc_no,
            quick_others_no=quick_others_no,
            fast_ch_ade_mo_no=fast_ch_ade_mo_no,
            fast_ccs_dc_combo_no=fast_ccs_dc_combo_no,
            fast_gb_t20234_3_dc_no=fast_gb_t20234_3_dc_no,
            fast_others_no=fast_others_no,
            remark_for_others=remark_for_others,
            data_path=data_path,
            objectid=objectid,
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
