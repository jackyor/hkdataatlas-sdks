"""A client library for accessing Transport Department — Routes and fares of public transport (GeoJSON)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
