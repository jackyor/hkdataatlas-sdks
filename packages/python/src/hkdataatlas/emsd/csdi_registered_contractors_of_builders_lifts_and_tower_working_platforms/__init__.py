"""A client library for accessing Electrical and Mechanical Services Department — Registered Contractors of Builders' Lifts and Tower Working Platforms"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
