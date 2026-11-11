"""A client library for accessing Lands Department — True Digital Orthophoto (TDOP) Series"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
