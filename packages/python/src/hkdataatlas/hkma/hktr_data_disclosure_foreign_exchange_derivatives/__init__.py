"""A client library for accessing HKTR Data Disclosure – Foreign Exchange Derivatives-positions"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
