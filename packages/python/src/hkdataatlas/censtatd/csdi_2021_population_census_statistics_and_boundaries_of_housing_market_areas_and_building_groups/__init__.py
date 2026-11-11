"""A client library for accessing Census and Statistics Department — 2021 Population Census (Statistics and Boundaries of Housing Market Areas and Building Groups)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
