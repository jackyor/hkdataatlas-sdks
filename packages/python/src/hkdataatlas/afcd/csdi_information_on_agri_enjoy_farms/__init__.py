"""A client library for accessing Agriculture, Fisheries and Conservation Department — Information on "Agri enJoy" farms"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
