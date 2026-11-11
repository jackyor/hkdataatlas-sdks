"""A client library for accessing Register of AIs and LROs (VPR)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
