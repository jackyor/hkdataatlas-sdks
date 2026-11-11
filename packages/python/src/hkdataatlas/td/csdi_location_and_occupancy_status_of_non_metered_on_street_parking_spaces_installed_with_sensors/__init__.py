"""A client library for accessing Transport Department — Location and occupancy status of non-metered on-street parking spaces installed with sensors"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
