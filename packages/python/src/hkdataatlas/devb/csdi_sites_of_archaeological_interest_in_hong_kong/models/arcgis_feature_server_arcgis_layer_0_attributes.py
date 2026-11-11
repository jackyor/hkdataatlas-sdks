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
        file_ref (None | str | Unset): Publisher field type: esriFieldTypeString
        name (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        address (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district (None | str | Unset): Publisher field type: esriFieldTypeString
        data_owner (None | str | Unset): Publisher field type: esriFieldTypeString
        distric_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        dec_year (int | None | Unset): Publisher field type: esriFieldTypeInteger
        dec_ye_tc (int | None | Unset): Publisher field type: esriFieldTypeInteger
        fileref_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        detail (None | str | Unset): Publisher field type: esriFieldTypeString
        detail_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        dataset (None | str | Unset): Publisher field type: esriFieldTypeString
        dataset_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        arch_pd (None | str | Unset): Publisher field type: esriFieldTypeString
        arch_pd_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        url_image (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    file_ref: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    data_owner: None | str | Unset = UNSET
    distric_tc: None | str | Unset = UNSET
    dec_year: int | None | Unset = UNSET
    dec_ye_tc: int | None | Unset = UNSET
    fileref_tc: None | str | Unset = UNSET
    detail: None | str | Unset = UNSET
    detail_tc: None | str | Unset = UNSET
    dataset: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    arch_pd: None | str | Unset = UNSET
    arch_pd_tc: None | str | Unset = UNSET
    url_image: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_ref: None | str | Unset
        if isinstance(self.file_ref, Unset):
            file_ref = UNSET
        else:
            file_ref = self.file_ref

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        data_owner: None | str | Unset
        if isinstance(self.data_owner, Unset):
            data_owner = UNSET
        else:
            data_owner = self.data_owner

        distric_tc: None | str | Unset
        if isinstance(self.distric_tc, Unset):
            distric_tc = UNSET
        else:
            distric_tc = self.distric_tc

        dec_year: int | None | Unset
        if isinstance(self.dec_year, Unset):
            dec_year = UNSET
        else:
            dec_year = self.dec_year

        dec_ye_tc: int | None | Unset
        if isinstance(self.dec_ye_tc, Unset):
            dec_ye_tc = UNSET
        else:
            dec_ye_tc = self.dec_ye_tc

        fileref_tc: None | str | Unset
        if isinstance(self.fileref_tc, Unset):
            fileref_tc = UNSET
        else:
            fileref_tc = self.fileref_tc

        detail: None | str | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        detail_tc: None | str | Unset
        if isinstance(self.detail_tc, Unset):
            detail_tc = UNSET
        else:
            detail_tc = self.detail_tc

        dataset: None | str | Unset
        if isinstance(self.dataset, Unset):
            dataset = UNSET
        else:
            dataset = self.dataset

        dataset_tc: None | str | Unset
        if isinstance(self.dataset_tc, Unset):
            dataset_tc = UNSET
        else:
            dataset_tc = self.dataset_tc

        arch_pd: None | str | Unset
        if isinstance(self.arch_pd, Unset):
            arch_pd = UNSET
        else:
            arch_pd = self.arch_pd

        arch_pd_tc: None | str | Unset
        if isinstance(self.arch_pd_tc, Unset):
            arch_pd_tc = UNSET
        else:
            arch_pd_tc = self.arch_pd_tc

        url_image: None | str | Unset
        if isinstance(self.url_image, Unset):
            url_image = UNSET
        else:
            url_image = self.url_image

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_ref is not UNSET:
            field_dict["FILE_REF"] = file_ref
        if name is not UNSET:
            field_dict["NAME"] = name
        if name_tc is not UNSET:
            field_dict["NAME_TC"] = name_tc
        if address is not UNSET:
            field_dict["ADDRESS"] = address
        if address_tc is not UNSET:
            field_dict["ADDRESS_TC"] = address_tc
        if district is not UNSET:
            field_dict["DISTRICT"] = district
        if data_owner is not UNSET:
            field_dict["DATA_OWNER"] = data_owner
        if distric_tc is not UNSET:
            field_dict["DISTRIC_TC"] = distric_tc
        if dec_year is not UNSET:
            field_dict["DEC_YEAR"] = dec_year
        if dec_ye_tc is not UNSET:
            field_dict["DEC_YE_TC"] = dec_ye_tc
        if fileref_tc is not UNSET:
            field_dict["FILEREF_TC"] = fileref_tc
        if detail is not UNSET:
            field_dict["DETAIL"] = detail
        if detail_tc is not UNSET:
            field_dict["DETAIL_TC"] = detail_tc
        if dataset is not UNSET:
            field_dict["DATASET"] = dataset
        if dataset_tc is not UNSET:
            field_dict["DATASET_TC"] = dataset_tc
        if arch_pd is not UNSET:
            field_dict["ARCH_PD"] = arch_pd
        if arch_pd_tc is not UNSET:
            field_dict["ARCH_PD_TC"] = arch_pd_tc
        if url_image is not UNSET:
            field_dict["URL_IMAGE"] = url_image
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_file_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_ref = _parse_file_ref(d.pop("FILE_REF", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("NAME", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("NAME_TC", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("ADDRESS", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("ADDRESS_TC", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("DISTRICT", UNSET))

        def _parse_data_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_owner = _parse_data_owner(d.pop("DATA_OWNER", UNSET))

        def _parse_distric_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        distric_tc = _parse_distric_tc(d.pop("DISTRIC_TC", UNSET))

        def _parse_dec_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dec_year = _parse_dec_year(d.pop("DEC_YEAR", UNSET))

        def _parse_dec_ye_tc(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dec_ye_tc = _parse_dec_ye_tc(d.pop("DEC_YE_TC", UNSET))

        def _parse_fileref_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fileref_tc = _parse_fileref_tc(d.pop("FILEREF_TC", UNSET))

        def _parse_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail = _parse_detail(d.pop("DETAIL", UNSET))

        def _parse_detail_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail_tc = _parse_detail_tc(d.pop("DETAIL_TC", UNSET))

        def _parse_dataset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset = _parse_dataset(d.pop("DATASET", UNSET))

        def _parse_dataset_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_tc = _parse_dataset_tc(d.pop("DATASET_TC", UNSET))

        def _parse_arch_pd(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        arch_pd = _parse_arch_pd(d.pop("ARCH_PD", UNSET))

        def _parse_arch_pd_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        arch_pd_tc = _parse_arch_pd_tc(d.pop("ARCH_PD_TC", UNSET))

        def _parse_url_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_image = _parse_url_image(d.pop("URL_IMAGE", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            file_ref=file_ref,
            name=name,
            name_tc=name_tc,
            address=address,
            address_tc=address_tc,
            district=district,
            data_owner=data_owner,
            distric_tc=distric_tc,
            dec_year=dec_year,
            dec_ye_tc=dec_ye_tc,
            fileref_tc=fileref_tc,
            detail=detail,
            detail_tc=detail_tc,
            dataset=dataset,
            dataset_tc=dataset_tc,
            arch_pd=arch_pd,
            arch_pd_tc=arch_pd_tc,
            url_image=url_image,
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
