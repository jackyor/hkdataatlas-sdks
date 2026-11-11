"""A client library for accessing Drainage Services Department — EcoDMS - River Channels"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
