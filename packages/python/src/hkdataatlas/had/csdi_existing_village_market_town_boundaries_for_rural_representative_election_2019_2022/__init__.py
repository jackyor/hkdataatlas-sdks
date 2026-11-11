"""A client library for accessing Home Affairs Department — Existing Village/ Market Town Boundaries for Rural Representative Election (2019-2022)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
