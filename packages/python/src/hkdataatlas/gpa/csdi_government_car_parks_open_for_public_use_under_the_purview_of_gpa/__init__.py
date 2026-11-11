"""A client library for accessing Government Property Agency — Government car parks open for public use under the purview of GPA"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
