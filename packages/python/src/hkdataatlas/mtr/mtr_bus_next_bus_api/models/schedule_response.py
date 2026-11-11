from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bus_stop import BusStop


T = TypeVar("T", bound="ScheduleResponse")


@_attrs_define
class ScheduleResponse:
    """Returned schedule data. Properties below are documented in the data dictionary or visible in the publisher's
    example. The dictionary identifies deprecated fields; it does not state that they are absent from responses.

        Attributes:
            app_refresh_time_in_second (str | Unset): Time interval between each refresh.
            bus_stop (list[BusStop] | Unset): Array of bus stops on the selected route.
            case_number (int | Unset): Deprecated.
            case_number_detail (str | Unset): Deprecated.
            footer_remarks (str | Unset): Disclaimer for estimated time provided.
            route_colour (str | Unset): Deprecated.
            route_name (str | Unset): Route name.
            route_status (str | Unset): Deprecated.
            route_status_colour (str | Unset): Deprecated.
            route_status_remark_content (None | str | Unset): Deprecated. The example contains null.
            route_status_remark_footer_remark (str | Unset): Deprecated.
            route_status_remark_title (None | str | Unset): Deprecated. The example contains null.
            route_status_time (str | Unset): System date and time. The dictionary gives format `yyyy-MM-dd HH:mm`; the
                example instead represents it as `2021/08/24 11:29`. Both documented forms are retained without imposing a
                restrictive format.
            status (str | Unset): System status code: `1` = normal; `0` = error or alert.
    """

    app_refresh_time_in_second: str | Unset = UNSET
    bus_stop: list[BusStop] | Unset = UNSET
    case_number: int | Unset = UNSET
    case_number_detail: str | Unset = UNSET
    footer_remarks: str | Unset = UNSET
    route_colour: str | Unset = UNSET
    route_name: str | Unset = UNSET
    route_status: str | Unset = UNSET
    route_status_colour: str | Unset = UNSET
    route_status_remark_content: None | str | Unset = UNSET
    route_status_remark_footer_remark: str | Unset = UNSET
    route_status_remark_title: None | str | Unset = UNSET
    route_status_time: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_refresh_time_in_second = self.app_refresh_time_in_second

        bus_stop: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bus_stop, Unset):
            bus_stop = []
            for bus_stop_item_data in self.bus_stop:
                bus_stop_item = bus_stop_item_data.to_dict()
                bus_stop.append(bus_stop_item)

        case_number = self.case_number

        case_number_detail = self.case_number_detail

        footer_remarks = self.footer_remarks

        route_colour = self.route_colour

        route_name = self.route_name

        route_status = self.route_status

        route_status_colour = self.route_status_colour

        route_status_remark_content: None | str | Unset
        if isinstance(self.route_status_remark_content, Unset):
            route_status_remark_content = UNSET
        else:
            route_status_remark_content = self.route_status_remark_content

        route_status_remark_footer_remark = self.route_status_remark_footer_remark

        route_status_remark_title: None | str | Unset
        if isinstance(self.route_status_remark_title, Unset):
            route_status_remark_title = UNSET
        else:
            route_status_remark_title = self.route_status_remark_title

        route_status_time = self.route_status_time

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_refresh_time_in_second is not UNSET:
            field_dict["appRefreshTimeInSecond"] = app_refresh_time_in_second
        if bus_stop is not UNSET:
            field_dict["busStop"] = bus_stop
        if case_number is not UNSET:
            field_dict["caseNumber"] = case_number
        if case_number_detail is not UNSET:
            field_dict["caseNumberDetail"] = case_number_detail
        if footer_remarks is not UNSET:
            field_dict["footerRemarks"] = footer_remarks
        if route_colour is not UNSET:
            field_dict["routeColour"] = route_colour
        if route_name is not UNSET:
            field_dict["routeName"] = route_name
        if route_status is not UNSET:
            field_dict["routeStatus"] = route_status
        if route_status_colour is not UNSET:
            field_dict["routeStatusColour"] = route_status_colour
        if route_status_remark_content is not UNSET:
            field_dict["routeStatusRemarkContent"] = route_status_remark_content
        if route_status_remark_footer_remark is not UNSET:
            field_dict["routeStatusRemarkFooterRemark"] = (
                route_status_remark_footer_remark
            )
        if route_status_remark_title is not UNSET:
            field_dict["routeStatusRemarkTitle"] = route_status_remark_title
        if route_status_time is not UNSET:
            field_dict["routeStatusTime"] = route_status_time
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bus_stop import BusStop

        d = dict(src_dict)
        app_refresh_time_in_second = d.pop("appRefreshTimeInSecond", UNSET)

        _bus_stop = d.pop("busStop", UNSET)
        bus_stop: list[BusStop] | Unset = UNSET
        if _bus_stop is not UNSET:
            bus_stop = []
            for bus_stop_item_data in _bus_stop:
                bus_stop_item = BusStop.from_dict(bus_stop_item_data)

                bus_stop.append(bus_stop_item)

        case_number = d.pop("caseNumber", UNSET)

        case_number_detail = d.pop("caseNumberDetail", UNSET)

        footer_remarks = d.pop("footerRemarks", UNSET)

        route_colour = d.pop("routeColour", UNSET)

        route_name = d.pop("routeName", UNSET)

        route_status = d.pop("routeStatus", UNSET)

        route_status_colour = d.pop("routeStatusColour", UNSET)

        def _parse_route_status_remark_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        route_status_remark_content = _parse_route_status_remark_content(
            d.pop("routeStatusRemarkContent", UNSET)
        )

        route_status_remark_footer_remark = d.pop(
            "routeStatusRemarkFooterRemark", UNSET
        )

        def _parse_route_status_remark_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        route_status_remark_title = _parse_route_status_remark_title(
            d.pop("routeStatusRemarkTitle", UNSET)
        )

        route_status_time = d.pop("routeStatusTime", UNSET)

        status = d.pop("status", UNSET)

        schedule_response = cls(
            app_refresh_time_in_second=app_refresh_time_in_second,
            bus_stop=bus_stop,
            case_number=case_number,
            case_number_detail=case_number_detail,
            footer_remarks=footer_remarks,
            route_colour=route_colour,
            route_name=route_name,
            route_status=route_status,
            route_status_colour=route_status_colour,
            route_status_remark_content=route_status_remark_content,
            route_status_remark_footer_remark=route_status_remark_footer_remark,
            route_status_remark_title=route_status_remark_title,
            route_status_time=route_status_time,
            status=status,
        )

        schedule_response.additional_properties = d
        return schedule_response

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
