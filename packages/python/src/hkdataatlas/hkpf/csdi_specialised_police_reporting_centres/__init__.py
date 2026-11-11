"""A client library for accessing Hong Kong Police Force — Specialised Police Reporting Centres"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
