"""A client library for accessing Hong Kong Observatory — Regional weather in Hong Kong – the maximum and minimum air temperature from 1-minute mean temperatures since midnight"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
