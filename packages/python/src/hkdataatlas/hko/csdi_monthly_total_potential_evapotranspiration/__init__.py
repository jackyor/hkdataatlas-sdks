"""A client library for accessing Hong Kong Observatory — Monthly total potential evapotranspiration"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
