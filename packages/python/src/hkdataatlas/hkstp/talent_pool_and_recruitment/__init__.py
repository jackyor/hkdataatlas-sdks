"""A client library for accessing Talent Pool and Recruitment API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
