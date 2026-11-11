"""A client library for accessing Transport Department — Junctions with Red Light Camera System installed"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
