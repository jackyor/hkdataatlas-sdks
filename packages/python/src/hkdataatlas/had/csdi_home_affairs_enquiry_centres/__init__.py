"""A client library for accessing Home Affairs Department — Home Affairs Enquiry Centres"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
