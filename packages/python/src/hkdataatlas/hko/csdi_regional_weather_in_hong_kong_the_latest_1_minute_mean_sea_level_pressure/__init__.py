"""A client library for accessing Hong Kong Observatory — Regional weather in Hong Kong – the latest 1-minute mean sea level pressure"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
