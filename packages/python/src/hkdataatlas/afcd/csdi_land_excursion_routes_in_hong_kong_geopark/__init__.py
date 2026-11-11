"""A client library for accessing Agriculture, Fisheries and Conservation Department — Land Excursion Routes in Hong Kong Geopark"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
