"""A client library for accessing Government Property Agency — Open Space for Public Use in Joint-user Government Offices managed by Government Property Agency"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
