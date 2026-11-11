"""A client library for accessing Availability of Computer Facilities at Hong Kong Public Libraries"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
