"""A client library for accessing Social Welfare Department — List of Kindergartens (KGs) /Kindergarten-cum-Child Care Centres (KG-cum-CCCs) Participating in On-site Pre-school Rehabilitation Services (OPRS)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
