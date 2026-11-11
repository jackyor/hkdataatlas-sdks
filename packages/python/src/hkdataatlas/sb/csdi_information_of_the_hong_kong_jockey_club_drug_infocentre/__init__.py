"""A client library for accessing Security Bureau — Information of the Hong Kong Jockey Club Drug InfoCentre"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
