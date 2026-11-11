"""A client library for accessing Administration Wing, Chief Secretary for Administration's Office — Exhibition Hall of the Government Records Service"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
