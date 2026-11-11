"""A client library for accessing HKTR Data Disclosure – Interest Rate Derivatives-positions"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
