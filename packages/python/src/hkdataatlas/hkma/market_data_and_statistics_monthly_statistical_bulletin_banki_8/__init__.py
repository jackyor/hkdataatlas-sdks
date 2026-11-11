"""A client library for accessing Loans and advances by type - Deposit-taking companies"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
