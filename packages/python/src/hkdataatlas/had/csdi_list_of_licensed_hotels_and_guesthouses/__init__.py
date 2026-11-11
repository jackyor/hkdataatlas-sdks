"""A client library for accessing Home Affairs Department — List of licensed hotels and guesthouses"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
