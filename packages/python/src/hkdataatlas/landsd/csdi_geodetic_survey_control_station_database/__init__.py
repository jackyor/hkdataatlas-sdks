"""A client library for accessing Lands Department — Geodetic Survey Control Station Database"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
