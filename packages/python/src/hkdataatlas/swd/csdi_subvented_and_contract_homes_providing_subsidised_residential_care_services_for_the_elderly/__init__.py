"""A client library for accessing Social Welfare Department — Subvented and Contract Homes providing Subsidised Residential Care Services for the Elderly"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
