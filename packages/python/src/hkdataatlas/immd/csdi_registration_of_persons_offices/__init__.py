"""A client library for accessing Immigration Department — Registration of Persons Offices"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
