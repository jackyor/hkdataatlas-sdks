"""A client library for accessing Buildings Department — Statutory Orders issued on unauthorised building works of the buildings"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
