"""A client library for accessing Government Property Agency — Properties managed by Government Property Agency through Property Management Services Contracts -- Joint-user Government Offices"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
