"""A client library for accessing Land Parcel and Public Utility Number Search API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
