"""A client library for accessing Office for Film, Newspaper and Article Administration — List of Registered Newspapers and Periodicals"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
