"""A client library for accessing Education Bureau — Primary One Admission (POA) School Net Boundaries"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
