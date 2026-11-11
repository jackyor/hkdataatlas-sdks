"""A client library for accessing Government Property Agency — Automatic vending machines installed inside government buildings by GPA"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
