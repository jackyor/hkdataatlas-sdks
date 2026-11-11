"""A client library for accessing Buildings Department — Statutory Notices issued on prescribed inspection/repair for windows"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
