"""A client library for accessing Lands Department — Public Facilities (excluding Public Open Space) (Available in GML)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
