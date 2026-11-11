"""A client library for accessing Home Affairs Department — Barrier-free facilities in community halls/ community centres"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
