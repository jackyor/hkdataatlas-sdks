"""A client library for accessing Customs and Excise Department — List of General Bonded, Public Bonded and C&E Warehouses"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
