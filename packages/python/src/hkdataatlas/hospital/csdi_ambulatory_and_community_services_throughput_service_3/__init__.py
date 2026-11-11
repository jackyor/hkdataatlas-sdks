"""A client library for accessing Hospital Authority — Ambulatory and Community Services Throughput"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
