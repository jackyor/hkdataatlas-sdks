"""A client library for accessing Census and Statistics Department — 2016 Population By-census (Statistics of Subdivided Units by District Council District)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
