"""A client library for accessing Census and Statistics Department — 2016 Population By-census (Statistics and Boundaries of District Council Constituency Areas)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
