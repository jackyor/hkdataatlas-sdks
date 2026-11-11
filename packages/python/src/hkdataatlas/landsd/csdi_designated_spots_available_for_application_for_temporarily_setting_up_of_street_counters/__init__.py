"""A client library for accessing Lands Department — Designated spots available for application for temporarily setting up of street counters"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
