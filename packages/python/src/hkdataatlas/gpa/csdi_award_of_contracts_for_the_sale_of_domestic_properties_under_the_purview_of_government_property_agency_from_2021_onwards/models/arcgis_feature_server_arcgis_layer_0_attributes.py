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
        en_address (None | str | Unset): Publisher field type: esriFieldTypeString
        en_consideration (None | str | Unset): Publisher field type: esriFieldTypeString
        en_district (None | str | Unset): Publisher field type: esriFieldTypeString
        en_name (None | str | Unset): Publisher field type: esriFieldTypeString
        en_website (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_address (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_consideration (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_district (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_name (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_website (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_address (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_consideration (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_district (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_name (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_website (None | str | Unset): Publisher field type: esriFieldTypeString
        tender_auction_reference_no (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    en_address: None | str | Unset = UNSET
    en_consideration: None | str | Unset = UNSET
    en_district: None | str | Unset = UNSET
    en_name: None | str | Unset = UNSET
    en_website: None | str | Unset = UNSET
    sc_address: None | str | Unset = UNSET
    sc_consideration: None | str | Unset = UNSET
    sc_district: None | str | Unset = UNSET
    sc_name: None | str | Unset = UNSET
    sc_website: None | str | Unset = UNSET
    tc_address: None | str | Unset = UNSET
    tc_consideration: None | str | Unset = UNSET
    tc_district: None | str | Unset = UNSET
    tc_name: None | str | Unset = UNSET
    tc_website: None | str | Unset = UNSET
    tender_auction_reference_no: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        en_address: None | str | Unset
        if isinstance(self.en_address, Unset):
            en_address = UNSET
        else:
            en_address = self.en_address

        en_consideration: None | str | Unset
        if isinstance(self.en_consideration, Unset):
            en_consideration = UNSET
        else:
            en_consideration = self.en_consideration

        en_district: None | str | Unset
        if isinstance(self.en_district, Unset):
            en_district = UNSET
        else:
            en_district = self.en_district

        en_name: None | str | Unset
        if isinstance(self.en_name, Unset):
            en_name = UNSET
        else:
            en_name = self.en_name

        en_website: None | str | Unset
        if isinstance(self.en_website, Unset):
            en_website = UNSET
        else:
            en_website = self.en_website

        sc_address: None | str | Unset
        if isinstance(self.sc_address, Unset):
            sc_address = UNSET
        else:
            sc_address = self.sc_address

        sc_consideration: None | str | Unset
        if isinstance(self.sc_consideration, Unset):
            sc_consideration = UNSET
        else:
            sc_consideration = self.sc_consideration

        sc_district: None | str | Unset
        if isinstance(self.sc_district, Unset):
            sc_district = UNSET
        else:
            sc_district = self.sc_district

        sc_name: None | str | Unset
        if isinstance(self.sc_name, Unset):
            sc_name = UNSET
        else:
            sc_name = self.sc_name

        sc_website: None | str | Unset
        if isinstance(self.sc_website, Unset):
            sc_website = UNSET
        else:
            sc_website = self.sc_website

        tc_address: None | str | Unset
        if isinstance(self.tc_address, Unset):
            tc_address = UNSET
        else:
            tc_address = self.tc_address

        tc_consideration: None | str | Unset
        if isinstance(self.tc_consideration, Unset):
            tc_consideration = UNSET
        else:
            tc_consideration = self.tc_consideration

        tc_district: None | str | Unset
        if isinstance(self.tc_district, Unset):
            tc_district = UNSET
        else:
            tc_district = self.tc_district

        tc_name: None | str | Unset
        if isinstance(self.tc_name, Unset):
            tc_name = UNSET
        else:
            tc_name = self.tc_name

        tc_website: None | str | Unset
        if isinstance(self.tc_website, Unset):
            tc_website = UNSET
        else:
            tc_website = self.tc_website

        tender_auction_reference_no: None | str | Unset
        if isinstance(self.tender_auction_reference_no, Unset):
            tender_auction_reference_no = UNSET
        else:
            tender_auction_reference_no = self.tender_auction_reference_no

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if en_address is not UNSET:
            field_dict["en_address"] = en_address
        if en_consideration is not UNSET:
            field_dict["en_consideration"] = en_consideration
        if en_district is not UNSET:
            field_dict["en_district"] = en_district
        if en_name is not UNSET:
            field_dict["en_name"] = en_name
        if en_website is not UNSET:
            field_dict["en_website"] = en_website
        if sc_address is not UNSET:
            field_dict["sc_address"] = sc_address
        if sc_consideration is not UNSET:
            field_dict["sc_consideration"] = sc_consideration
        if sc_district is not UNSET:
            field_dict["sc_district"] = sc_district
        if sc_name is not UNSET:
            field_dict["sc_name"] = sc_name
        if sc_website is not UNSET:
            field_dict["sc_website"] = sc_website
        if tc_address is not UNSET:
            field_dict["tc_address"] = tc_address
        if tc_consideration is not UNSET:
            field_dict["tc_consideration"] = tc_consideration
        if tc_district is not UNSET:
            field_dict["tc_district"] = tc_district
        if tc_name is not UNSET:
            field_dict["tc_name"] = tc_name
        if tc_website is not UNSET:
            field_dict["tc_website"] = tc_website
        if tender_auction_reference_no is not UNSET:
            field_dict["tender_auction_reference_no"] = tender_auction_reference_no
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_en_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_address = _parse_en_address(d.pop("en_address", UNSET))

        def _parse_en_consideration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_consideration = _parse_en_consideration(d.pop("en_consideration", UNSET))

        def _parse_en_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_district = _parse_en_district(d.pop("en_district", UNSET))

        def _parse_en_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_name = _parse_en_name(d.pop("en_name", UNSET))

        def _parse_en_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_website = _parse_en_website(d.pop("en_website", UNSET))

        def _parse_sc_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_address = _parse_sc_address(d.pop("sc_address", UNSET))

        def _parse_sc_consideration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_consideration = _parse_sc_consideration(d.pop("sc_consideration", UNSET))

        def _parse_sc_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_district = _parse_sc_district(d.pop("sc_district", UNSET))

        def _parse_sc_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_name = _parse_sc_name(d.pop("sc_name", UNSET))

        def _parse_sc_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_website = _parse_sc_website(d.pop("sc_website", UNSET))

        def _parse_tc_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_address = _parse_tc_address(d.pop("tc_address", UNSET))

        def _parse_tc_consideration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_consideration = _parse_tc_consideration(d.pop("tc_consideration", UNSET))

        def _parse_tc_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_district = _parse_tc_district(d.pop("tc_district", UNSET))

        def _parse_tc_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_name = _parse_tc_name(d.pop("tc_name", UNSET))

        def _parse_tc_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_website = _parse_tc_website(d.pop("tc_website", UNSET))

        def _parse_tender_auction_reference_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tender_auction_reference_no = _parse_tender_auction_reference_no(
            d.pop("tender_auction_reference_no", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            en_address=en_address,
            en_consideration=en_consideration,
            en_district=en_district,
            en_name=en_name,
            en_website=en_website,
            sc_address=sc_address,
            sc_consideration=sc_consideration,
            sc_district=sc_district,
            sc_name=sc_name,
            sc_website=sc_website,
            tc_address=tc_address,
            tc_consideration=tc_consideration,
            tc_district=tc_district,
            tc_name=tc_name,
            tc_website=tc_website,
            tender_auction_reference_no=tender_auction_reference_no,
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
