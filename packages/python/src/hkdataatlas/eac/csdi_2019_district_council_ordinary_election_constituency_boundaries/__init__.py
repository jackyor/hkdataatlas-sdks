"""A client library for accessing Electoral Affairs Commission — 2019 District Council Ordinary Election Constituency Boundaries"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
