"""A client library for accessing Analytical accounts of the Exchange Fund"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
