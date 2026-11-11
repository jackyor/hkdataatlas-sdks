"""A client library for accessing Agriculture, Fisheries and Conservation Department — Information on trees in major recreational sites of Country Parks"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
