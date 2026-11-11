"""A client library for accessing List of outstanding Government Bonds under the Infrastructure Bond Programme and Government Sustainable Bond Programme"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
