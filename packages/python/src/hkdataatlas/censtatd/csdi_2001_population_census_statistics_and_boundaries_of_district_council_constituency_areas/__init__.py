"""A client library for accessing Census and Statistics Department — 2001 Population Census (Statistics and Boundaries of District Council Constituency Areas)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
