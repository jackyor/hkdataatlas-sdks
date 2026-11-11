"""A client library for accessing Hong Kong Observatory — Latest 15-minute mean UV index from 7:00 a.m. to 6:00 p.m. Hong Kong time"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
