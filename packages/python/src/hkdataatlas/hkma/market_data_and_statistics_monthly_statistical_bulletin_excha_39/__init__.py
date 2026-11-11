"""A client library for accessing Data template on international reserves and foreign currency liquidity"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
