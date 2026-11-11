"""A client library for accessing Heat Stress at Work Warning API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
