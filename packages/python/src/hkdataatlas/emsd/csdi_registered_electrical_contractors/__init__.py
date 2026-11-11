"""A client library for accessing Electrical and Mechanical Services Department — Registered Electrical Contractors"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
