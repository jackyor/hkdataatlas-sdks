"""A client library for accessing Buildings Department — Statutory Notices complied with/withdrawn/superseded on prescribed inspection/repair for buildings"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
