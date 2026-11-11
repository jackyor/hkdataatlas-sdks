"""A client library for accessing Taxi Fleet Information (Amigo) Webx API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
