"""A client library for accessing Loans and advances for use in Hong Kong by economic sector - Deposit-taking companies"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
