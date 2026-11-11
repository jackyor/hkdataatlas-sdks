"""A client library for accessing Department of Justice - Blog of Secretary for Justice and Deputy Secretary for Justice"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
