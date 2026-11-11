"""A client library for accessing Exchange rates and the effective exchange rate indices - Daily figures"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
