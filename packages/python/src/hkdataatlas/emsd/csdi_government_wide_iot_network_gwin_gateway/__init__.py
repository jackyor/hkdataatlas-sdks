"""A client library for accessing Electrical and Mechanical Services Department — Government Wide IoT Network (GWIN) Gateway"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
