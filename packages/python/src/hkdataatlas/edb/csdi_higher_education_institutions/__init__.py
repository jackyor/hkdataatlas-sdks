"""A client library for accessing Education Bureau — Higher Education Institutions"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
