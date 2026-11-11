"""A client library for accessing Social Welfare Department — Po Leung Kuk Tsui Lam Centre Victim Support Programme for Victims of Family Violence"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
