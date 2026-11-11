"""A client library for accessing Home Affairs Department — Centres administering declarations and service time slots"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
