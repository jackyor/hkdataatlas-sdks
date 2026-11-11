"""A client library for accessing Agriculture, Fisheries and Conservation Department — Location of Pesticides Licensees"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
