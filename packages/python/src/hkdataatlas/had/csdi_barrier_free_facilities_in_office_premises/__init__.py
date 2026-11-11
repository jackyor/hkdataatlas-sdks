"""A client library for accessing Home Affairs Department — Barrier-free facilities in office premises"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
