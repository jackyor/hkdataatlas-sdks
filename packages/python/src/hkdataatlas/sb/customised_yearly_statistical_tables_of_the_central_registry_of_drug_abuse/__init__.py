"""A client library for accessing CRDA Statistical Tables Customization Service"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
