"""A client library for accessing Home Affairs Department — District Offices and Sub-offices"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
