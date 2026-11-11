"""A client library for accessing KMB Real-time Arrival Information API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
