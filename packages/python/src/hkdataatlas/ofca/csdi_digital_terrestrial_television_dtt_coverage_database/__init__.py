"""A client library for accessing Office of the Communications Authority — Digital Terrestrial Television (DTT) Coverage Database"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
