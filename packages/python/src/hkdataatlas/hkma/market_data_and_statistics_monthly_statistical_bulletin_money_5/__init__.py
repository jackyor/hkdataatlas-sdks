"""A client library for accessing Components of money supply - Foreign currency (Adjusted to exclude foreign currency swap deposits)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
