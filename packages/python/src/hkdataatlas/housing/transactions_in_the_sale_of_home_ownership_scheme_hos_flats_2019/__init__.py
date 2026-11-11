"""A client library for accessing Transactions in the Sale of HOS Flats 2019 API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
