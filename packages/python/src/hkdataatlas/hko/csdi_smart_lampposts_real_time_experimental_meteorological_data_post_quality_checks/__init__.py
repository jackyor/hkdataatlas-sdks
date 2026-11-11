"""A client library for accessing Hong Kong Observatory — Smart lampposts real-time experimental meteorological data (Post quality checks)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
