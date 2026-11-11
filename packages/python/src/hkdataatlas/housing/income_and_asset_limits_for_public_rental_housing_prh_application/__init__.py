"""A client library for accessing Income and Asset Limits for Public Rental Housing (PRH) Application API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
