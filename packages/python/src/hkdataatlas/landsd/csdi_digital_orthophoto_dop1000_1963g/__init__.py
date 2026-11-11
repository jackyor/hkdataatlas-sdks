"""A client library for accessing Lands Department — Digital Orthophoto DOP1000-1963G"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
