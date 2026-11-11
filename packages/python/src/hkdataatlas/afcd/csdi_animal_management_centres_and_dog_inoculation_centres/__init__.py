"""A client library for accessing Agriculture, Fisheries and Conservation Department — Animal Management Centres and Dog Inoculation Centres"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
