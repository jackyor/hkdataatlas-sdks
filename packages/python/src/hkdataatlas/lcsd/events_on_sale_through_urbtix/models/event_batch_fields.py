from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventBatchFields")


@_attrs_define
class EventBatchFields:
    """Field dictionary for the dataset. This is not a complete XML document schema; element nesting, field requiredness,
    and the overall response structure are not specified.

        Attributes:
            city_eg (str | Unset): City English name.
            city_tc (str | Unset): City Chinese name.
            ed_date (str | Unset): Event end date. Documented type: date; an example shown in the dictionary is 20211015.
                The example uses YYYYMMDD representation.
            event_code (str | Unset): Event code.
            event_eg (str | Unset): Event English name.
            event_tc (str | Unset): Event Chinese name.
            image_link (str | Unset): Event image URL.
            main_cat_eg (str | Unset): Event category English name. The dotted spelling is as documented.
            main_cat_tc (str | Unset): Event category Chinese name. The dotted spelling is as documented.
            performance_performance_datetime (str | Unset): Performance date and time. Documented type: datetime; example:
                2021/10/15 19:45 Fri. The dotted spelling is as documented.
            performance_reference_link (str | Unset): Performance URL. The dotted spelling is as documented.
            performance_ref_no (float | Unset): Performance reference number. Documented type: numeric. The dotted spelling
                is as documented.
            performance_title_eg (str | Unset): Performance English name. The dotted spelling is as documented.
            performance_title_tc (str | Unset): Performance Chinese name. The dotted spelling is as documented.
            reference_link (str | Unset): Event URL.
            region_eg (str | Unset): Region English name.
            region_tc (str | Unset): Region Chinese name.
            send_date (str | Unset): Data creation date. Documented type: date; example: 20210912. The example uses YYYYMMDD
                representation.
            st_date (str | Unset): Event start date. Documented type: date; example: 20211015. The example uses YYYYMMDD
                representation.
            sub_cat_eg (str | Unset): Event sub-category English name. The dotted spelling is as documented.
            sub_cat_tc (str | Unset): Event sub-category Chinese name. The dotted spelling is as documented.
            system (str | Unset): System.
            total (float | Unset): Number of events. Documented type: numeric.
            venue_code (str | Unset): Venue code.
            venue_eg (str | Unset): Venue English name.
            venue_tc (str | Unset): Venue Chinese name.
    """

    city_eg: str | Unset = UNSET
    city_tc: str | Unset = UNSET
    ed_date: str | Unset = UNSET
    event_code: str | Unset = UNSET
    event_eg: str | Unset = UNSET
    event_tc: str | Unset = UNSET
    image_link: str | Unset = UNSET
    main_cat_eg: str | Unset = UNSET
    main_cat_tc: str | Unset = UNSET
    performance_performance_datetime: str | Unset = UNSET
    performance_reference_link: str | Unset = UNSET
    performance_ref_no: float | Unset = UNSET
    performance_title_eg: str | Unset = UNSET
    performance_title_tc: str | Unset = UNSET
    reference_link: str | Unset = UNSET
    region_eg: str | Unset = UNSET
    region_tc: str | Unset = UNSET
    send_date: str | Unset = UNSET
    st_date: str | Unset = UNSET
    sub_cat_eg: str | Unset = UNSET
    sub_cat_tc: str | Unset = UNSET
    system: str | Unset = UNSET
    total: float | Unset = UNSET
    venue_code: str | Unset = UNSET
    venue_eg: str | Unset = UNSET
    venue_tc: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        city_eg = self.city_eg

        city_tc = self.city_tc

        ed_date = self.ed_date

        event_code = self.event_code

        event_eg = self.event_eg

        event_tc = self.event_tc

        image_link = self.image_link

        main_cat_eg = self.main_cat_eg

        main_cat_tc = self.main_cat_tc

        performance_performance_datetime = self.performance_performance_datetime

        performance_reference_link = self.performance_reference_link

        performance_ref_no = self.performance_ref_no

        performance_title_eg = self.performance_title_eg

        performance_title_tc = self.performance_title_tc

        reference_link = self.reference_link

        region_eg = self.region_eg

        region_tc = self.region_tc

        send_date = self.send_date

        st_date = self.st_date

        sub_cat_eg = self.sub_cat_eg

        sub_cat_tc = self.sub_cat_tc

        system = self.system

        total = self.total

        venue_code = self.venue_code

        venue_eg = self.venue_eg

        venue_tc = self.venue_tc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city_eg is not UNSET:
            field_dict["CITY_EG"] = city_eg
        if city_tc is not UNSET:
            field_dict["CITY_TC"] = city_tc
        if ed_date is not UNSET:
            field_dict["ED_DATE"] = ed_date
        if event_code is not UNSET:
            field_dict["EVENT_CODE"] = event_code
        if event_eg is not UNSET:
            field_dict["EVENT_EG"] = event_eg
        if event_tc is not UNSET:
            field_dict["EVENT_TC"] = event_tc
        if image_link is not UNSET:
            field_dict["IMAGE_LINK"] = image_link
        if main_cat_eg is not UNSET:
            field_dict["MAIN_CAT.EG"] = main_cat_eg
        if main_cat_tc is not UNSET:
            field_dict["MAIN_CAT.TC"] = main_cat_tc
        if performance_performance_datetime is not UNSET:
            field_dict["PERFORMANCE.PERFORMANCE_DATETIME"] = (
                performance_performance_datetime
            )
        if performance_reference_link is not UNSET:
            field_dict["PERFORMANCE.REFERENCE_LINK"] = performance_reference_link
        if performance_ref_no is not UNSET:
            field_dict["PERFORMANCE.REF_NO"] = performance_ref_no
        if performance_title_eg is not UNSET:
            field_dict["PERFORMANCE.TITLE_EG"] = performance_title_eg
        if performance_title_tc is not UNSET:
            field_dict["PERFORMANCE.TITLE_TC"] = performance_title_tc
        if reference_link is not UNSET:
            field_dict["REFERENCE_LINK"] = reference_link
        if region_eg is not UNSET:
            field_dict["REGION_EG"] = region_eg
        if region_tc is not UNSET:
            field_dict["REGION_TC"] = region_tc
        if send_date is not UNSET:
            field_dict["SEND_DATE"] = send_date
        if st_date is not UNSET:
            field_dict["ST_DATE"] = st_date
        if sub_cat_eg is not UNSET:
            field_dict["SUB_CAT.EG"] = sub_cat_eg
        if sub_cat_tc is not UNSET:
            field_dict["SUB_CAT.TC"] = sub_cat_tc
        if system is not UNSET:
            field_dict["SYSTEM"] = system
        if total is not UNSET:
            field_dict["TOTAL"] = total
        if venue_code is not UNSET:
            field_dict["VENUE_CODE"] = venue_code
        if venue_eg is not UNSET:
            field_dict["VENUE_EG"] = venue_eg
        if venue_tc is not UNSET:
            field_dict["VENUE_TC"] = venue_tc

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        city_eg = d.pop("CITY_EG", UNSET)

        city_tc = d.pop("CITY_TC", UNSET)

        ed_date = d.pop("ED_DATE", UNSET)

        event_code = d.pop("EVENT_CODE", UNSET)

        event_eg = d.pop("EVENT_EG", UNSET)

        event_tc = d.pop("EVENT_TC", UNSET)

        image_link = d.pop("IMAGE_LINK", UNSET)

        main_cat_eg = d.pop("MAIN_CAT.EG", UNSET)

        main_cat_tc = d.pop("MAIN_CAT.TC", UNSET)

        performance_performance_datetime = d.pop(
            "PERFORMANCE.PERFORMANCE_DATETIME", UNSET
        )

        performance_reference_link = d.pop("PERFORMANCE.REFERENCE_LINK", UNSET)

        performance_ref_no = d.pop("PERFORMANCE.REF_NO", UNSET)

        performance_title_eg = d.pop("PERFORMANCE.TITLE_EG", UNSET)

        performance_title_tc = d.pop("PERFORMANCE.TITLE_TC", UNSET)

        reference_link = d.pop("REFERENCE_LINK", UNSET)

        region_eg = d.pop("REGION_EG", UNSET)

        region_tc = d.pop("REGION_TC", UNSET)

        send_date = d.pop("SEND_DATE", UNSET)

        st_date = d.pop("ST_DATE", UNSET)

        sub_cat_eg = d.pop("SUB_CAT.EG", UNSET)

        sub_cat_tc = d.pop("SUB_CAT.TC", UNSET)

        system = d.pop("SYSTEM", UNSET)

        total = d.pop("TOTAL", UNSET)

        venue_code = d.pop("VENUE_CODE", UNSET)

        venue_eg = d.pop("VENUE_EG", UNSET)

        venue_tc = d.pop("VENUE_TC", UNSET)

        event_batch_fields = cls(
            city_eg=city_eg,
            city_tc=city_tc,
            ed_date=ed_date,
            event_code=event_code,
            event_eg=event_eg,
            event_tc=event_tc,
            image_link=image_link,
            main_cat_eg=main_cat_eg,
            main_cat_tc=main_cat_tc,
            performance_performance_datetime=performance_performance_datetime,
            performance_reference_link=performance_reference_link,
            performance_ref_no=performance_ref_no,
            performance_title_eg=performance_title_eg,
            performance_title_tc=performance_title_tc,
            reference_link=reference_link,
            region_eg=region_eg,
            region_tc=region_tc,
            send_date=send_date,
            st_date=st_date,
            sub_cat_eg=sub_cat_eg,
            sub_cat_tc=sub_cat_tc,
            system=system,
            total=total,
            venue_code=venue_code,
            venue_eg=venue_eg,
            venue_tc=venue_tc,
        )

        event_batch_fields.additional_properties = d
        return event_batch_fields

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
