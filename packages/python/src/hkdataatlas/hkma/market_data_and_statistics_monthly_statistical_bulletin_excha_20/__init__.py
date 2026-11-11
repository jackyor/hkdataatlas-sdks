"""A client library for accessing Exchange rates and the effective exchange rate indices - End of period figures"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
