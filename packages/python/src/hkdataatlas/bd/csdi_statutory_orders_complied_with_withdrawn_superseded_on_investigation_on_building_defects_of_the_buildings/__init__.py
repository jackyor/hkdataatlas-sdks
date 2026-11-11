"""A client library for accessing Buildings Department — Statutory Orders complied with/withdrawn/superseded on investigation on building defects of the buildings"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
