"""A client library for accessing Education Bureau — Profile of Kindergartens and Kindergarten-cum-Child Care Centres"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
