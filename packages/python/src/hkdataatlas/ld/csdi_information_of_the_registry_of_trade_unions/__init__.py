"""A client library for accessing Labour Department — Information of the Registry of Trade Unions"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
