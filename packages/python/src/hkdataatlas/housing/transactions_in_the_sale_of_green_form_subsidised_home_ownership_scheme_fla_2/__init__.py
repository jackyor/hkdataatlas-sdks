"""A client library for accessing Transactions in the Sale of GSH Flats 2020/21"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
