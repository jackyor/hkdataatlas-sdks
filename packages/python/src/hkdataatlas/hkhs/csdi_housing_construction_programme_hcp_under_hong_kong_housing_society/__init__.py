"""A client library for accessing Hong Kong Housing Society — Housing Construction Programme (HCP) under Hong Kong Housing Society"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
