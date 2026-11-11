"""A client library for accessing Transactions in the Sale of Home Ownership Scheme Flats (HOS) 2022"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
