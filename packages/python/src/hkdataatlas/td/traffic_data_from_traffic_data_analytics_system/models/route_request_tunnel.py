from typing import Literal

RouteRequestTunnel = Literal["cht", "eht", "wht"]

ROUTE_REQUEST_TUNNEL_VALUES: set[RouteRequestTunnel] = {
    "cht",
    "eht",
    "wht",
}


def check_route_request_tunnel(value: str) -> RouteRequestTunnel:
    if value in ROUTE_REQUEST_TUNNEL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROUTE_REQUEST_TUNNEL_VALUES!r}"
    )
