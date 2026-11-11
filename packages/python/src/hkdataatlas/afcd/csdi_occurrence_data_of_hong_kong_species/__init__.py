"""A client library for accessing Agriculture, Fisheries and Conservation Department — Occurrence Data of Hong Kong Species"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
