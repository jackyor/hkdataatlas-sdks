"""A client library for accessing Buildings Department — Statutory Orders issued on defective drains of the buildings"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
