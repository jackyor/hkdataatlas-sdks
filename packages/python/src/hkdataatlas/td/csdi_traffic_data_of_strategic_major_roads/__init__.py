"""A client library for accessing Transport Department — Traffic Data of Strategic / Major Roads"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
