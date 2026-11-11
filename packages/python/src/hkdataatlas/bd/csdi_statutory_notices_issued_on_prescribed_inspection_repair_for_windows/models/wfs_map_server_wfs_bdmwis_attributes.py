from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsBDMWISAttributes")


@_attrs_define
class WfsMapServerWfsBDMWISAttributes:
    """
    Attributes:
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        dataset_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        dataset_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        block_id_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        block_id_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        block_type_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        block_type_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        cum_mwis_notice_issued_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        cum_mwis_notice_issued_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        csuid_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        csuid_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        northing (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        easting (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        latitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        longitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        last_update (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    shape: Any | Unset = UNSET
    objectid: int | Unset = UNSET
    dataset_en: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    block_id_en: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    block_id_tc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    block_type_en: None | str | Unset = UNSET
    block_type_tc: None | str | Unset = UNSET
    cum_mwis_notice_issued_en: None | str | Unset = UNSET
    cum_mwis_notice_issued_tc: None | str | Unset = UNSET
    csuid_en: None | str | Unset = UNSET
    csuid_tc: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    easting: float | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    last_update: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shape = self.shape

        objectid = self.objectid

        dataset_en: None | str | Unset
        if isinstance(self.dataset_en, Unset):
            dataset_en = UNSET
        else:
            dataset_en = self.dataset_en

        dataset_tc: None | str | Unset
        if isinstance(self.dataset_tc, Unset):
            dataset_tc = UNSET
        else:
            dataset_tc = self.dataset_tc

        block_id_en: None | str | Unset
        if isinstance(self.block_id_en, Unset):
            block_id_en = UNSET
        else:
            block_id_en = self.block_id_en

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        block_id_tc: None | str | Unset
        if isinstance(self.block_id_tc, Unset):
            block_id_tc = UNSET
        else:
            block_id_tc = self.block_id_tc

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        block_type_en: None | str | Unset
        if isinstance(self.block_type_en, Unset):
            block_type_en = UNSET
        else:
            block_type_en = self.block_type_en

        block_type_tc: None | str | Unset
        if isinstance(self.block_type_tc, Unset):
            block_type_tc = UNSET
        else:
            block_type_tc = self.block_type_tc

        cum_mwis_notice_issued_en: None | str | Unset
        if isinstance(self.cum_mwis_notice_issued_en, Unset):
            cum_mwis_notice_issued_en = UNSET
        else:
            cum_mwis_notice_issued_en = self.cum_mwis_notice_issued_en

        cum_mwis_notice_issued_tc: None | str | Unset
        if isinstance(self.cum_mwis_notice_issued_tc, Unset):
            cum_mwis_notice_issued_tc = UNSET
        else:
            cum_mwis_notice_issued_tc = self.cum_mwis_notice_issued_tc

        csuid_en: None | str | Unset
        if isinstance(self.csuid_en, Unset):
            csuid_en = UNSET
        else:
            csuid_en = self.csuid_en

        csuid_tc: None | str | Unset
        if isinstance(self.csuid_tc, Unset):
            csuid_tc = UNSET
        else:
            csuid_tc = self.csuid_tc

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        last_update: None | str | Unset
        if isinstance(self.last_update, Unset):
            last_update = UNSET
        else:
            last_update = self.last_update

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shape is not UNSET:
            field_dict["shape"] = shape
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if dataset_en is not UNSET:
            field_dict["DatasetEN"] = dataset_en
        if dataset_tc is not UNSET:
            field_dict["DatasetTC"] = dataset_tc
        if block_id_en is not UNSET:
            field_dict["BLOCK_ID_EN"] = block_id_en
        if address_en is not UNSET:
            field_dict["AddressEN"] = address_en
        if block_id_tc is not UNSET:
            field_dict["BLOCK_ID_TC"] = block_id_tc
        if address_tc is not UNSET:
            field_dict["AddressTC"] = address_tc
        if block_type_en is not UNSET:
            field_dict["Block_TypeEN"] = block_type_en
        if block_type_tc is not UNSET:
            field_dict["Block_TypeTC"] = block_type_tc
        if cum_mwis_notice_issued_en is not UNSET:
            field_dict["Cum_MWIS_Notice_Issued_EN"] = cum_mwis_notice_issued_en
        if cum_mwis_notice_issued_tc is not UNSET:
            field_dict["Cum_MWIS_Notice_Issued_TC"] = cum_mwis_notice_issued_tc
        if csuid_en is not UNSET:
            field_dict["CSUID_EN"] = csuid_en
        if csuid_tc is not UNSET:
            field_dict["CSUID_TC"] = csuid_tc
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if last_update is not UNSET:
            field_dict["LastUpdate"] = last_update

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        shape = d.pop("shape", UNSET)

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_dataset_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_en = _parse_dataset_en(d.pop("DatasetEN", UNSET))

        def _parse_dataset_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_tc = _parse_dataset_tc(d.pop("DatasetTC", UNSET))

        def _parse_block_id_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        block_id_en = _parse_block_id_en(d.pop("BLOCK_ID_EN", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("AddressEN", UNSET))

        def _parse_block_id_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        block_id_tc = _parse_block_id_tc(d.pop("BLOCK_ID_TC", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("AddressTC", UNSET))

        def _parse_block_type_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        block_type_en = _parse_block_type_en(d.pop("Block_TypeEN", UNSET))

        def _parse_block_type_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        block_type_tc = _parse_block_type_tc(d.pop("Block_TypeTC", UNSET))

        def _parse_cum_mwis_notice_issued_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cum_mwis_notice_issued_en = _parse_cum_mwis_notice_issued_en(
            d.pop("Cum_MWIS_Notice_Issued_EN", UNSET)
        )

        def _parse_cum_mwis_notice_issued_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cum_mwis_notice_issued_tc = _parse_cum_mwis_notice_issued_tc(
            d.pop("Cum_MWIS_Notice_Issued_TC", UNSET)
        )

        def _parse_csuid_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        csuid_en = _parse_csuid_en(d.pop("CSUID_EN", UNSET))

        def _parse_csuid_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        csuid_tc = _parse_csuid_tc(d.pop("CSUID_TC", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("Easting", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        def _parse_last_update(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_update = _parse_last_update(d.pop("LastUpdate", UNSET))

        wfs_map_server_wfs_bdmwis_attributes = cls(
            shape=shape,
            objectid=objectid,
            dataset_en=dataset_en,
            dataset_tc=dataset_tc,
            block_id_en=block_id_en,
            address_en=address_en,
            block_id_tc=block_id_tc,
            address_tc=address_tc,
            block_type_en=block_type_en,
            block_type_tc=block_type_tc,
            cum_mwis_notice_issued_en=cum_mwis_notice_issued_en,
            cum_mwis_notice_issued_tc=cum_mwis_notice_issued_tc,
            csuid_en=csuid_en,
            csuid_tc=csuid_tc,
            northing=northing,
            easting=easting,
            latitude=latitude,
            longitude=longitude,
            last_update=last_update,
        )

        wfs_map_server_wfs_bdmwis_attributes.additional_properties = d
        return wfs_map_server_wfs_bdmwis_attributes

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
