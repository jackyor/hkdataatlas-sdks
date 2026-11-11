"""A client library for accessing Buildings Department — Statutory Orders complied with/withdrawn/superseded on dangerous buildings"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
