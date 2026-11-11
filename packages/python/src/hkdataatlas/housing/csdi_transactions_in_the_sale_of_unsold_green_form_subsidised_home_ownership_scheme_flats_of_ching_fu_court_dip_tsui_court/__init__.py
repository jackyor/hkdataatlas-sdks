"""A client library for accessing Hong Kong Housing Authority — Transactions in the Sale of Unsold Green Form Subsidised Home Ownership Scheme Flats of Ching Fu Court & Dip Tsui Court"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
