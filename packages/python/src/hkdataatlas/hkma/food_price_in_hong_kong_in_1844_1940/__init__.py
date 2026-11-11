"""A client library for accessing HKIMR - Food Price in Hong Kong in 1844-1940"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
