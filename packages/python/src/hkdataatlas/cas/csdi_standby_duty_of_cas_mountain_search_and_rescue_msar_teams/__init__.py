"""A client library for accessing Civil Aid Service — Standby duty of CAS Mountain Search and Rescue (MSaR) Teams"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
