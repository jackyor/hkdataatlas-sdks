"""A client library for accessing Environmental Protection Department — Open Space Database of Recycling Station"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
