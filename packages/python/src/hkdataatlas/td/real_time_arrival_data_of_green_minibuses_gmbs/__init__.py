"""A client library for accessing Green Minibus Real-Time Arrival Information System API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
