"""A client library for accessing Digital Policy Office — “iAM Smart” registration locations"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
