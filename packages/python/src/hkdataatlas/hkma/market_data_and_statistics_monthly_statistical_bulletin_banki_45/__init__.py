"""A client library for accessing Mainland-related lending and other non-bank exposures - Mainland-related lending by type of borrowers"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
