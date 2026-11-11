"""A client library for accessing List of hotlines for authenticating the identity of callers claiming to be bank representatives"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
