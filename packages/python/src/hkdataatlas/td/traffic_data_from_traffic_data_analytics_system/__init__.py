"""A client library for accessing Traffic Data from Traffic Data Analytics System API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
