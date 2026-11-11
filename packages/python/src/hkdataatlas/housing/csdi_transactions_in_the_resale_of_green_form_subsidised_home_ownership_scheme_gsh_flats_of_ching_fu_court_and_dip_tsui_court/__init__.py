"""A client library for accessing Hong Kong Housing Authority — Transactions in the Resale of Green Form Subsidised Home Ownership Scheme (GSH) Flats of Ching Fu Court and Dip Tsui Court"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
