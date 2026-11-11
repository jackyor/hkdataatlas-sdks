"""A client library for accessing Components of money supply - Hong Kong dollar (Adjusted to include foreign currency swap deposits)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
