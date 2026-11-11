"""A client library for accessing Hong Kong Observatory — Regional weather in Hong Kong - past 24-hour temperature difference"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
