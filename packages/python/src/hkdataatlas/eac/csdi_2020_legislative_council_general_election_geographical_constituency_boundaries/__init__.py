"""A client library for accessing Electoral Affairs Commission — 2020 Legislative Council General Election Geographical Constituency Boundaries"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
