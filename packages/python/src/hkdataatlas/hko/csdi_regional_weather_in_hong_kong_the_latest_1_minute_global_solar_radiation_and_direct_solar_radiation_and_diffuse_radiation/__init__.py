"""A client library for accessing Hong Kong Observatory — Regional weather in Hong Kong – the latest 1-minute global solar radiation and direct solar radiation and diffuse radiation"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
