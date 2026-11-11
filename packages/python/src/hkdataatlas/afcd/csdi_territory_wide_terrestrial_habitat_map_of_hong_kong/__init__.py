"""A client library for accessing Agriculture, Fisheries and Conservation Department — Territory-wide Terrestrial Habitat Map of Hong Kong"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
