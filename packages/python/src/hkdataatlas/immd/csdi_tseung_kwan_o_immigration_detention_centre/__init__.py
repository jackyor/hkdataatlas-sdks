"""A client library for accessing Immigration Department — Tseung Kwan O Immigration Detention Centre"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
