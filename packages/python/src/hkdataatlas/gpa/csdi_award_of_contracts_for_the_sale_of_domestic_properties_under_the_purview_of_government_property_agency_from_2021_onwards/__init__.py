"""A client library for accessing Government Property Agency — Award of Contracts for the Sale of Domestic Properties under the purview of Government Property Agency (From 2021 onwards)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
