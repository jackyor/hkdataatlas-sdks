"""A client library for accessing Government Property Agency — Automatic teller machines in government buildings under the purview of GPA"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
