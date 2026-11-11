"""A client library for accessing Highways Department — Walkability Projects"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
