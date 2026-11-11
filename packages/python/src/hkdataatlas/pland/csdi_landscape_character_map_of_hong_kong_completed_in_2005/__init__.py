"""A client library for accessing Planning Department — Landscape Character Map of Hong Kong (completed in 2005)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
