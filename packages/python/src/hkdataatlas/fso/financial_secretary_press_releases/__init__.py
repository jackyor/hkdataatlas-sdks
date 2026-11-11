"""A client library for accessing Financial Secretary - Press Releases"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
