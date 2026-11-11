"""A client library for accessing Electoral Affairs Commission — District Council Geographical Constituency Boundaries of the 2023 District Council Ordinary Election"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
