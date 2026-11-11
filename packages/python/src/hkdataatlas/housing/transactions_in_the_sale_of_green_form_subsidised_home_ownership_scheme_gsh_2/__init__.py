"""A client library for accessing Transactions in the Sale of GSH Flats 2023 API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
