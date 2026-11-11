"""A client library for accessing Education Bureau — Non-aided Child Care Centre attached to Kindergarten"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
