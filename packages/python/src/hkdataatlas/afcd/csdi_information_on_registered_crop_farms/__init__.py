"""A client library for accessing Agriculture, Fisheries and Conservation Department — Information on Registered Crop Farms"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
