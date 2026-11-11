"""A client library for accessing Transport Department — Traffic data from AI Video Analytics System of CCTVs"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
