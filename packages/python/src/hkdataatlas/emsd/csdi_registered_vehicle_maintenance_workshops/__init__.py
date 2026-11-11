"""A client library for accessing Electrical and Mechanical Services Department — Registered Vehicle Maintenance Workshops"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
