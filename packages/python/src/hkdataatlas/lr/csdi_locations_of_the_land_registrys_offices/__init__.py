"""A client library for accessing Land Registry — Locations of the Land Registry’s offices"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
