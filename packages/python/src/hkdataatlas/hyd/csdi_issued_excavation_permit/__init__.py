"""A client library for accessing Highways Department — Issued Excavation Permit"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
