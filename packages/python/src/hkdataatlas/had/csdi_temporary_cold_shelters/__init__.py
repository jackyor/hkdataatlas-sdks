"""A client library for accessing Home Affairs Department — Temporary cold shelters"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
