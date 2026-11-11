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
        cp_id (None | str | Unset): Publisher field type: esriFieldTypeString
        cp_state (None | str | Unset): Publisher field type: esriFieldTypeString
        district_id (None | str | Unset): Publisher field type: esriFieldTypeString
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address2_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        address2_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        address2_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        lat (None | str | Unset): Publisher field type: esriFieldTypeString
        lgt (None | str | Unset): Publisher field type: esriFieldTypeString
        waste_type (None | str | Unset): Publisher field type: esriFieldTypeString
        legend (None | str | Unset): Publisher field type: esriFieldTypeString
        accessibilty_notes (None | str | Unset): Publisher field type: esriFieldTypeString
        contact_en (None | str | Unset): Publisher field type: esriFieldTypeString
        contact_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        contact_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        openhour_en (None | str | Unset): Publisher field type: esriFieldTypeString
        openhour_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        openhour_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    cp_id: None | str | Unset = UNSET
    cp_state: None | str | Unset = UNSET
    district_id: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    address2_en: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    address2_tc: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    address2_sc: None | str | Unset = UNSET
    lat: None | str | Unset = UNSET
    lgt: None | str | Unset = UNSET
    waste_type: None | str | Unset = UNSET
    legend: None | str | Unset = UNSET
    accessibilty_notes: None | str | Unset = UNSET
    contact_en: None | str | Unset = UNSET
    contact_tc: None | str | Unset = UNSET
    contact_sc: None | str | Unset = UNSET
    openhour_en: None | str | Unset = UNSET
    openhour_tc: None | str | Unset = UNSET
    openhour_sc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cp_id: None | str | Unset
        if isinstance(self.cp_id, Unset):
            cp_id = UNSET
        else:
            cp_id = self.cp_id

        cp_state: None | str | Unset
        if isinstance(self.cp_state, Unset):
            cp_state = UNSET
        else:
            cp_state = self.cp_state

        district_id: None | str | Unset
        if isinstance(self.district_id, Unset):
            district_id = UNSET
        else:
            district_id = self.district_id

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address2_en: None | str | Unset
        if isinstance(self.address2_en, Unset):
            address2_en = UNSET
        else:
            address2_en = self.address2_en

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        address2_tc: None | str | Unset
        if isinstance(self.address2_tc, Unset):
            address2_tc = UNSET
        else:
            address2_tc = self.address2_tc

        address_sc: None | str | Unset
        if isinstance(self.address_sc, Unset):
            address_sc = UNSET
        else:
            address_sc = self.address_sc

        address2_sc: None | str | Unset
        if isinstance(self.address2_sc, Unset):
            address2_sc = UNSET
        else:
            address2_sc = self.address2_sc

        lat: None | str | Unset
        if isinstance(self.lat, Unset):
            lat = UNSET
        else:
            lat = self.lat

        lgt: None | str | Unset
        if isinstance(self.lgt, Unset):
            lgt = UNSET
        else:
            lgt = self.lgt

        waste_type: None | str | Unset
        if isinstance(self.waste_type, Unset):
            waste_type = UNSET
        else:
            waste_type = self.waste_type

        legend: None | str | Unset
        if isinstance(self.legend, Unset):
            legend = UNSET
        else:
            legend = self.legend

        accessibilty_notes: None | str | Unset
        if isinstance(self.accessibilty_notes, Unset):
            accessibilty_notes = UNSET
        else:
            accessibilty_notes = self.accessibilty_notes

        contact_en: None | str | Unset
        if isinstance(self.contact_en, Unset):
            contact_en = UNSET
        else:
            contact_en = self.contact_en

        contact_tc: None | str | Unset
        if isinstance(self.contact_tc, Unset):
            contact_tc = UNSET
        else:
            contact_tc = self.contact_tc

        contact_sc: None | str | Unset
        if isinstance(self.contact_sc, Unset):
            contact_sc = UNSET
        else:
            contact_sc = self.contact_sc

        openhour_en: None | str | Unset
        if isinstance(self.openhour_en, Unset):
            openhour_en = UNSET
        else:
            openhour_en = self.openhour_en

        openhour_tc: None | str | Unset
        if isinstance(self.openhour_tc, Unset):
            openhour_tc = UNSET
        else:
            openhour_tc = self.openhour_tc

        openhour_sc: None | str | Unset
        if isinstance(self.openhour_sc, Unset):
            openhour_sc = UNSET
        else:
            openhour_sc = self.openhour_sc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cp_id is not UNSET:
            field_dict["cp_id"] = cp_id
        if cp_state is not UNSET:
            field_dict["cp_state"] = cp_state
        if district_id is not UNSET:
            field_dict["district_id"] = district_id
        if address_en is not UNSET:
            field_dict["address_en"] = address_en
        if address2_en is not UNSET:
            field_dict["address2_en"] = address2_en
        if address_tc is not UNSET:
            field_dict["address_tc"] = address_tc
        if address2_tc is not UNSET:
            field_dict["address2_tc"] = address2_tc
        if address_sc is not UNSET:
            field_dict["address_sc"] = address_sc
        if address2_sc is not UNSET:
            field_dict["address2_sc"] = address2_sc
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lgt is not UNSET:
            field_dict["lgt"] = lgt
        if waste_type is not UNSET:
            field_dict["waste_type"] = waste_type
        if legend is not UNSET:
            field_dict["legend"] = legend
        if accessibilty_notes is not UNSET:
            field_dict["accessibilty_notes"] = accessibilty_notes
        if contact_en is not UNSET:
            field_dict["contact_en"] = contact_en
        if contact_tc is not UNSET:
            field_dict["contact_tc"] = contact_tc
        if contact_sc is not UNSET:
            field_dict["contact_sc"] = contact_sc
        if openhour_en is not UNSET:
            field_dict["openhour_en"] = openhour_en
        if openhour_tc is not UNSET:
            field_dict["openhour_tc"] = openhour_tc
        if openhour_sc is not UNSET:
            field_dict["openhour_sc"] = openhour_sc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_cp_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cp_id = _parse_cp_id(d.pop("cp_id", UNSET))

        def _parse_cp_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cp_state = _parse_cp_state(d.pop("cp_state", UNSET))

        def _parse_district_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_id = _parse_district_id(d.pop("district_id", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("address_en", UNSET))

        def _parse_address2_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address2_en = _parse_address2_en(d.pop("address2_en", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("address_tc", UNSET))

        def _parse_address2_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address2_tc = _parse_address2_tc(d.pop("address2_tc", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("address_sc", UNSET))

        def _parse_address2_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address2_sc = _parse_address2_sc(d.pop("address2_sc", UNSET))

        def _parse_lat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lat = _parse_lat(d.pop("lat", UNSET))

        def _parse_lgt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lgt = _parse_lgt(d.pop("lgt", UNSET))

        def _parse_waste_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        waste_type = _parse_waste_type(d.pop("waste_type", UNSET))

        def _parse_legend(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legend = _parse_legend(d.pop("legend", UNSET))

        def _parse_accessibilty_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accessibilty_notes = _parse_accessibilty_notes(
            d.pop("accessibilty_notes", UNSET)
        )

        def _parse_contact_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_en = _parse_contact_en(d.pop("contact_en", UNSET))

        def _parse_contact_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_tc = _parse_contact_tc(d.pop("contact_tc", UNSET))

        def _parse_contact_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_sc = _parse_contact_sc(d.pop("contact_sc", UNSET))

        def _parse_openhour_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        openhour_en = _parse_openhour_en(d.pop("openhour_en", UNSET))

        def _parse_openhour_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        openhour_tc = _parse_openhour_tc(d.pop("openhour_tc", UNSET))

        def _parse_openhour_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        openhour_sc = _parse_openhour_sc(d.pop("openhour_sc", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            cp_id=cp_id,
            cp_state=cp_state,
            district_id=district_id,
            address_en=address_en,
            address2_en=address2_en,
            address_tc=address_tc,
            address2_tc=address2_tc,
            address_sc=address_sc,
            address2_sc=address2_sc,
            lat=lat,
            lgt=lgt,
            waste_type=waste_type,
            legend=legend,
            accessibilty_notes=accessibilty_notes,
            contact_en=contact_en,
            contact_tc=contact_tc,
            contact_sc=contact_sc,
            openhour_en=openhour_en,
            openhour_tc=openhour_tc,
            openhour_sc=openhour_sc,
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
