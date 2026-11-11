"""A client library for accessing Social Welfare Department — Residential Care Homes for Persons with Disabilities (RCHDs) Participating in the Bought Place Scheme for RCHDs"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
