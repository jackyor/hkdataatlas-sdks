"""A client library for accessing Home Affairs Department — List of projects under the Signature Project Scheme"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
