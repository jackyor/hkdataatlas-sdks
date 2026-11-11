from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsRGCfgttgAttributes")


@_attrs_define
class WfsMapServerWfsRGCfgttgAttributes:
    """
    Attributes:
        head_office_address_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        head_office_address_traditional_chinese (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        name_of_registered_gas_contractor_english (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        name_of_registered_gas_contractor_traditional_chinese (None | str | Unset): Native XSD type . Requiredness is
            not projected from XML occurrence into all JSON queries.
        rgc_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        region_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        region_traditional_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        tel_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    head_office_address_english: None | str | Unset = UNSET
    head_office_address_traditional_chinese: None | str | Unset = UNSET
    name_of_registered_gas_contractor_english: None | str | Unset = UNSET
    name_of_registered_gas_contractor_traditional_chinese: None | str | Unset = UNSET
    rgc_no: None | str | Unset = UNSET
    region_english: None | str | Unset = UNSET
    region_traditional_chinese: None | str | Unset = UNSET
    tel_no: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        head_office_address_english: None | str | Unset
        if isinstance(self.head_office_address_english, Unset):
            head_office_address_english = UNSET
        else:
            head_office_address_english = self.head_office_address_english

        head_office_address_traditional_chinese: None | str | Unset
        if isinstance(self.head_office_address_traditional_chinese, Unset):
            head_office_address_traditional_chinese = UNSET
        else:
            head_office_address_traditional_chinese = (
                self.head_office_address_traditional_chinese
            )

        name_of_registered_gas_contractor_english: None | str | Unset
        if isinstance(self.name_of_registered_gas_contractor_english, Unset):
            name_of_registered_gas_contractor_english = UNSET
        else:
            name_of_registered_gas_contractor_english = (
                self.name_of_registered_gas_contractor_english
            )

        name_of_registered_gas_contractor_traditional_chinese: None | str | Unset
        if isinstance(
            self.name_of_registered_gas_contractor_traditional_chinese, Unset
        ):
            name_of_registered_gas_contractor_traditional_chinese = UNSET
        else:
            name_of_registered_gas_contractor_traditional_chinese = (
                self.name_of_registered_gas_contractor_traditional_chinese
            )

        rgc_no: None | str | Unset
        if isinstance(self.rgc_no, Unset):
            rgc_no = UNSET
        else:
            rgc_no = self.rgc_no

        region_english: None | str | Unset
        if isinstance(self.region_english, Unset):
            region_english = UNSET
        else:
            region_english = self.region_english

        region_traditional_chinese: None | str | Unset
        if isinstance(self.region_traditional_chinese, Unset):
            region_traditional_chinese = UNSET
        else:
            region_traditional_chinese = self.region_traditional_chinese

        tel_no: None | str | Unset
        if isinstance(self.tel_no, Unset):
            tel_no = UNSET
        else:
            tel_no = self.tel_no

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if head_office_address_english is not UNSET:
            field_dict["Head_Office_Address_English"] = head_office_address_english
        if head_office_address_traditional_chinese is not UNSET:
            field_dict["Head_Office_Address_Traditional_Chinese"] = (
                head_office_address_traditional_chinese
            )
        if name_of_registered_gas_contractor_english is not UNSET:
            field_dict["Name_of_Registered_Gas_Contractor_English"] = (
                name_of_registered_gas_contractor_english
            )
        if name_of_registered_gas_contractor_traditional_chinese is not UNSET:
            field_dict["Name_of_Registered_Gas_Contractor_Traditional_Chinese"] = (
                name_of_registered_gas_contractor_traditional_chinese
            )
        if rgc_no is not UNSET:
            field_dict["RGC_No"] = rgc_no
        if region_english is not UNSET:
            field_dict["Region_English"] = region_english
        if region_traditional_chinese is not UNSET:
            field_dict["Region_Traditional_Chinese"] = region_traditional_chinese
        if tel_no is not UNSET:
            field_dict["Tel_No"] = tel_no
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_head_office_address_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        head_office_address_english = _parse_head_office_address_english(
            d.pop("Head_Office_Address_English", UNSET)
        )

        def _parse_head_office_address_traditional_chinese(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        head_office_address_traditional_chinese = (
            _parse_head_office_address_traditional_chinese(
                d.pop("Head_Office_Address_Traditional_Chinese", UNSET)
            )
        )

        def _parse_name_of_registered_gas_contractor_english(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_registered_gas_contractor_english = (
            _parse_name_of_registered_gas_contractor_english(
                d.pop("Name_of_Registered_Gas_Contractor_English", UNSET)
            )
        )

        def _parse_name_of_registered_gas_contractor_traditional_chinese(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_registered_gas_contractor_traditional_chinese = (
            _parse_name_of_registered_gas_contractor_traditional_chinese(
                d.pop("Name_of_Registered_Gas_Contractor_Traditional_Chinese", UNSET)
            )
        )

        def _parse_rgc_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rgc_no = _parse_rgc_no(d.pop("RGC_No", UNSET))

        def _parse_region_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_english = _parse_region_english(d.pop("Region_English", UNSET))

        def _parse_region_traditional_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_traditional_chinese = _parse_region_traditional_chinese(
            d.pop("Region_Traditional_Chinese", UNSET)
        )

        def _parse_tel_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tel_no = _parse_tel_no(d.pop("Tel_No", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfs_rg_cfgttg_attributes = cls(
            head_office_address_english=head_office_address_english,
            head_office_address_traditional_chinese=head_office_address_traditional_chinese,
            name_of_registered_gas_contractor_english=name_of_registered_gas_contractor_english,
            name_of_registered_gas_contractor_traditional_chinese=name_of_registered_gas_contractor_traditional_chinese,
            rgc_no=rgc_no,
            region_english=region_english,
            region_traditional_chinese=region_traditional_chinese,
            tel_no=tel_no,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfs_rg_cfgttg_attributes.additional_properties = d
        return wfs_map_server_wfs_rg_cfgttg_attributes

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
