"""A client library for accessing Hospital Authority — Accident and Emergency Waiting Time"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
