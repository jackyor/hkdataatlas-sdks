"""A client library for accessing Water Supplies Department — Reservoirs and irrigation reservoirs open to public for fishing"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
