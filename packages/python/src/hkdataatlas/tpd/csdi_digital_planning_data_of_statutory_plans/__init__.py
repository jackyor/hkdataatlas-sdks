"""A client library for accessing Town Planning Board — Digital Planning Data of Statutory Plans"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
