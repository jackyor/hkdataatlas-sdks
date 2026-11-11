"""A client library for accessing Hong Kong Housing Authority — Transactions in the Sale of Green Form Subsidised Home Ownership Scheme Flats (GSH) 2022"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
