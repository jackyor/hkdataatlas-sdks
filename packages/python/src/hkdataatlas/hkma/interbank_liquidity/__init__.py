"""A client library for accessing Daily Figures of Interbank Liquidity"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
