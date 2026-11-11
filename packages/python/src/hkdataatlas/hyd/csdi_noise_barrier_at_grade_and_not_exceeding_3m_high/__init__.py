"""A client library for accessing Highways Department — Noise Barrier (at grade and not exceeding 3m high)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
