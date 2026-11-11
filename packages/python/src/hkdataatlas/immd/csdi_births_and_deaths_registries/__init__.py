"""A client library for accessing Immigration Department — Births and Deaths Registries"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
