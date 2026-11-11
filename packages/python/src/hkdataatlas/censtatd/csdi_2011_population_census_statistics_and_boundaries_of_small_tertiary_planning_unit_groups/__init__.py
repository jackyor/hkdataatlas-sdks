"""A client library for accessing Census and Statistics Department — 2011 Population Census (Statistics and Boundaries of Small Tertiary Planning Unit Groups)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
