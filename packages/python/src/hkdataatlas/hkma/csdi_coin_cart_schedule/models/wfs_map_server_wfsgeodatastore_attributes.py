from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsgeodatastoreAttributes")


@_attrs_define
class WfsMapServerWfsgeodatastoreAttributes:
    """
    Attributes:
        address_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        coin_cart_web_page_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        coin_cart_web_page_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        coin_cart_web_page_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        end_date_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        end_date_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        end_date_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        photo_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        photo_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        photo_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        realtime_loc_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        realtime_loc_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        realtime_loc_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        remarks_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        remarks_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        remarks_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        start_date_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        start_date_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        start_date_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    address_en: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    coin_cart_web_page_en: None | str | Unset = UNSET
    coin_cart_web_page_sc: None | str | Unset = UNSET
    coin_cart_web_page_tc: None | str | Unset = UNSET
    end_date_en: None | str | Unset = UNSET
    end_date_sc: None | str | Unset = UNSET
    end_date_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_sc: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    photo_en: None | str | Unset = UNSET
    photo_sc: None | str | Unset = UNSET
    photo_tc: None | str | Unset = UNSET
    realtime_loc_en: None | str | Unset = UNSET
    realtime_loc_sc: None | str | Unset = UNSET
    realtime_loc_tc: None | str | Unset = UNSET
    remarks_en: None | str | Unset = UNSET
    remarks_sc: None | str | Unset = UNSET
    remarks_tc: None | str | Unset = UNSET
    start_date_en: None | str | Unset = UNSET
    start_date_sc: None | str | Unset = UNSET
    start_date_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_sc: None | str | Unset
        if isinstance(self.address_sc, Unset):
            address_sc = UNSET
        else:
            address_sc = self.address_sc

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        coin_cart_web_page_en: None | str | Unset
        if isinstance(self.coin_cart_web_page_en, Unset):
            coin_cart_web_page_en = UNSET
        else:
            coin_cart_web_page_en = self.coin_cart_web_page_en

        coin_cart_web_page_sc: None | str | Unset
        if isinstance(self.coin_cart_web_page_sc, Unset):
            coin_cart_web_page_sc = UNSET
        else:
            coin_cart_web_page_sc = self.coin_cart_web_page_sc

        coin_cart_web_page_tc: None | str | Unset
        if isinstance(self.coin_cart_web_page_tc, Unset):
            coin_cart_web_page_tc = UNSET
        else:
            coin_cart_web_page_tc = self.coin_cart_web_page_tc

        end_date_en: None | str | Unset
        if isinstance(self.end_date_en, Unset):
            end_date_en = UNSET
        else:
            end_date_en = self.end_date_en

        end_date_sc: None | str | Unset
        if isinstance(self.end_date_sc, Unset):
            end_date_sc = UNSET
        else:
            end_date_sc = self.end_date_sc

        end_date_tc: None | str | Unset
        if isinstance(self.end_date_tc, Unset):
            end_date_tc = UNSET
        else:
            end_date_tc = self.end_date_tc

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        name_sc: None | str | Unset
        if isinstance(self.name_sc, Unset):
            name_sc = UNSET
        else:
            name_sc = self.name_sc

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        photo_en: None | str | Unset
        if isinstance(self.photo_en, Unset):
            photo_en = UNSET
        else:
            photo_en = self.photo_en

        photo_sc: None | str | Unset
        if isinstance(self.photo_sc, Unset):
            photo_sc = UNSET
        else:
            photo_sc = self.photo_sc

        photo_tc: None | str | Unset
        if isinstance(self.photo_tc, Unset):
            photo_tc = UNSET
        else:
            photo_tc = self.photo_tc

        realtime_loc_en: None | str | Unset
        if isinstance(self.realtime_loc_en, Unset):
            realtime_loc_en = UNSET
        else:
            realtime_loc_en = self.realtime_loc_en

        realtime_loc_sc: None | str | Unset
        if isinstance(self.realtime_loc_sc, Unset):
            realtime_loc_sc = UNSET
        else:
            realtime_loc_sc = self.realtime_loc_sc

        realtime_loc_tc: None | str | Unset
        if isinstance(self.realtime_loc_tc, Unset):
            realtime_loc_tc = UNSET
        else:
            realtime_loc_tc = self.realtime_loc_tc

        remarks_en: None | str | Unset
        if isinstance(self.remarks_en, Unset):
            remarks_en = UNSET
        else:
            remarks_en = self.remarks_en

        remarks_sc: None | str | Unset
        if isinstance(self.remarks_sc, Unset):
            remarks_sc = UNSET
        else:
            remarks_sc = self.remarks_sc

        remarks_tc: None | str | Unset
        if isinstance(self.remarks_tc, Unset):
            remarks_tc = UNSET
        else:
            remarks_tc = self.remarks_tc

        start_date_en: None | str | Unset
        if isinstance(self.start_date_en, Unset):
            start_date_en = UNSET
        else:
            start_date_en = self.start_date_en

        start_date_sc: None | str | Unset
        if isinstance(self.start_date_sc, Unset):
            start_date_sc = UNSET
        else:
            start_date_sc = self.start_date_sc

        start_date_tc: None | str | Unset
        if isinstance(self.start_date_tc, Unset):
            start_date_tc = UNSET
        else:
            start_date_tc = self.start_date_tc

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_en is not UNSET:
            field_dict["Address_EN"] = address_en
        if address_sc is not UNSET:
            field_dict["Address_SC"] = address_sc
        if address_tc is not UNSET:
            field_dict["Address_TC"] = address_tc
        if coin_cart_web_page_en is not UNSET:
            field_dict["CoinCart_WebPage_EN"] = coin_cart_web_page_en
        if coin_cart_web_page_sc is not UNSET:
            field_dict["CoinCart_WebPage_SC"] = coin_cart_web_page_sc
        if coin_cart_web_page_tc is not UNSET:
            field_dict["CoinCart_WebPage_TC"] = coin_cart_web_page_tc
        if end_date_en is not UNSET:
            field_dict["EndDate_EN"] = end_date_en
        if end_date_sc is not UNSET:
            field_dict["EndDate_SC"] = end_date_sc
        if end_date_tc is not UNSET:
            field_dict["EndDate_TC"] = end_date_tc
        if name_en is not UNSET:
            field_dict["NAME_EN"] = name_en
        if name_sc is not UNSET:
            field_dict["NAME_SC"] = name_sc
        if name_tc is not UNSET:
            field_dict["NAME_TC"] = name_tc
        if photo_en is not UNSET:
            field_dict["Photo_EN"] = photo_en
        if photo_sc is not UNSET:
            field_dict["Photo_SC"] = photo_sc
        if photo_tc is not UNSET:
            field_dict["Photo_TC"] = photo_tc
        if realtime_loc_en is not UNSET:
            field_dict["RealtimeLoc_EN"] = realtime_loc_en
        if realtime_loc_sc is not UNSET:
            field_dict["RealtimeLoc_SC"] = realtime_loc_sc
        if realtime_loc_tc is not UNSET:
            field_dict["RealtimeLoc_TC"] = realtime_loc_tc
        if remarks_en is not UNSET:
            field_dict["Remarks_EN"] = remarks_en
        if remarks_sc is not UNSET:
            field_dict["Remarks_SC"] = remarks_sc
        if remarks_tc is not UNSET:
            field_dict["Remarks_TC"] = remarks_tc
        if start_date_en is not UNSET:
            field_dict["StartDate_EN"] = start_date_en
        if start_date_sc is not UNSET:
            field_dict["StartDate_SC"] = start_date_sc
        if start_date_tc is not UNSET:
            field_dict["StartDate_TC"] = start_date_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("Address_EN", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("Address_SC", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("Address_TC", UNSET))

        def _parse_coin_cart_web_page_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        coin_cart_web_page_en = _parse_coin_cart_web_page_en(
            d.pop("CoinCart_WebPage_EN", UNSET)
        )

        def _parse_coin_cart_web_page_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        coin_cart_web_page_sc = _parse_coin_cart_web_page_sc(
            d.pop("CoinCart_WebPage_SC", UNSET)
        )

        def _parse_coin_cart_web_page_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        coin_cart_web_page_tc = _parse_coin_cart_web_page_tc(
            d.pop("CoinCart_WebPage_TC", UNSET)
        )

        def _parse_end_date_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_date_en = _parse_end_date_en(d.pop("EndDate_EN", UNSET))

        def _parse_end_date_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_date_sc = _parse_end_date_sc(d.pop("EndDate_SC", UNSET))

        def _parse_end_date_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_date_tc = _parse_end_date_tc(d.pop("EndDate_TC", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("NAME_EN", UNSET))

        def _parse_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_sc = _parse_name_sc(d.pop("NAME_SC", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("NAME_TC", UNSET))

        def _parse_photo_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo_en = _parse_photo_en(d.pop("Photo_EN", UNSET))

        def _parse_photo_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo_sc = _parse_photo_sc(d.pop("Photo_SC", UNSET))

        def _parse_photo_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo_tc = _parse_photo_tc(d.pop("Photo_TC", UNSET))

        def _parse_realtime_loc_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        realtime_loc_en = _parse_realtime_loc_en(d.pop("RealtimeLoc_EN", UNSET))

        def _parse_realtime_loc_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        realtime_loc_sc = _parse_realtime_loc_sc(d.pop("RealtimeLoc_SC", UNSET))

        def _parse_realtime_loc_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        realtime_loc_tc = _parse_realtime_loc_tc(d.pop("RealtimeLoc_TC", UNSET))

        def _parse_remarks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_en = _parse_remarks_en(d.pop("Remarks_EN", UNSET))

        def _parse_remarks_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_sc = _parse_remarks_sc(d.pop("Remarks_SC", UNSET))

        def _parse_remarks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_tc = _parse_remarks_tc(d.pop("Remarks_TC", UNSET))

        def _parse_start_date_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_date_en = _parse_start_date_en(d.pop("StartDate_EN", UNSET))

        def _parse_start_date_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_date_sc = _parse_start_date_sc(d.pop("StartDate_SC", UNSET))

        def _parse_start_date_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_date_tc = _parse_start_date_tc(d.pop("StartDate_TC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeodatastore_attributes = cls(
            address_en=address_en,
            address_sc=address_sc,
            address_tc=address_tc,
            coin_cart_web_page_en=coin_cart_web_page_en,
            coin_cart_web_page_sc=coin_cart_web_page_sc,
            coin_cart_web_page_tc=coin_cart_web_page_tc,
            end_date_en=end_date_en,
            end_date_sc=end_date_sc,
            end_date_tc=end_date_tc,
            name_en=name_en,
            name_sc=name_sc,
            name_tc=name_tc,
            photo_en=photo_en,
            photo_sc=photo_sc,
            photo_tc=photo_tc,
            realtime_loc_en=realtime_loc_en,
            realtime_loc_sc=realtime_loc_sc,
            realtime_loc_tc=realtime_loc_tc,
            remarks_en=remarks_en,
            remarks_sc=remarks_sc,
            remarks_tc=remarks_tc,
            start_date_en=start_date_en,
            start_date_sc=start_date_sc,
            start_date_tc=start_date_tc,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfsgeodatastore_attributes.additional_properties = d
        return wfs_map_server_wfsgeodatastore_attributes

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
