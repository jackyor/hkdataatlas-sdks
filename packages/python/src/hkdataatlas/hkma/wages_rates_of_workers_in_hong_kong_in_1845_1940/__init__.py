"""A client library for accessing HKIMR - Wages Rates of Workers in Hong Kong"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
