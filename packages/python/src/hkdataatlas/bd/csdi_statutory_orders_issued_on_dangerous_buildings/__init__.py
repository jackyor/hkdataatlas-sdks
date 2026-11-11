"""A client library for accessing Buildings Department — Statutory Orders issued on dangerous buildings"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
