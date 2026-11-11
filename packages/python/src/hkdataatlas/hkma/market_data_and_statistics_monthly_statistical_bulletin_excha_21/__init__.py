"""A client library for accessing Exchange rates and the effective exchange rate indices - Period average figures"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
