"""A client library for accessing Constitutional and Mainland Affairs Bureau — Information of Hong Kong Offices in the Mainland and Taiwan"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
