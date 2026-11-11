"""A client library for accessing Hong Kong Police Force — Police Posts/Control Points/Reporting Centres"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
