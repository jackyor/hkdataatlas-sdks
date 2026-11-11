"""A client library for accessing HKSTPC Carpark Vacancy API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
