"""A client library for accessing Environmental Protection Department — Pollution Load Inventory for Water Quality Modelling"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
