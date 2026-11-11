"""A client library for accessing Trade-Interactive Data Dissemination Service (Trade-IDDS) API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
