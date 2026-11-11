"""A client library for accessing Register of Securities Staff of AIs (eRegister)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
