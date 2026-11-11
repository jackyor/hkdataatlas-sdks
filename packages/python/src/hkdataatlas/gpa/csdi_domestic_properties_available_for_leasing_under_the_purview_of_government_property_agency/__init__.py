"""A client library for accessing Government Property Agency — Domestic Properties Available for Leasing under the purview of Government Property Agency"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
