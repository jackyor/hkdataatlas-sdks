"""A client library for accessing Hong Kong Housing Authority — Transactions in the Sale of Home Ownership Scheme (HOS) Flats 2023"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
