"""A client library for accessing Information of Other Self-Service Machines of Retail Banks(except Automated Teller Machines)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
