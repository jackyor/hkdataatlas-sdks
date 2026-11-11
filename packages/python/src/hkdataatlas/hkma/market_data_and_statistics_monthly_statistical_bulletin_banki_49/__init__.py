"""A client library for accessing Residential Mortgage Loans in Negative Equity"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
