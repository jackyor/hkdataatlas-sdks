"""A client library for accessing Marine Department — Speed Restricted Zones"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
