"""A client library for accessing Architectural Services Department — Government buildings and facilities maintained by ArchSD"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
