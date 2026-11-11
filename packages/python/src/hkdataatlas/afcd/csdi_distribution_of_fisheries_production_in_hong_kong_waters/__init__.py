"""A client library for accessing Agriculture, Fisheries and Conservation Department — Distribution of Fisheries Production in Hong Kong Waters"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
