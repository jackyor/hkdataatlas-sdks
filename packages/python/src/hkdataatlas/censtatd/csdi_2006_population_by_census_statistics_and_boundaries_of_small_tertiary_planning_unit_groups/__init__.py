"""A client library for accessing Census and Statistics Department — 2006 Population By-census (Statistics and Boundaries of Small Tertiary Planning Unit Groups)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
