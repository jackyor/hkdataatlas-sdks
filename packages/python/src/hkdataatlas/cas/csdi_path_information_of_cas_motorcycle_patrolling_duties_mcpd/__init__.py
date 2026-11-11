"""A client library for accessing Civil Aid Service — Path information of CAS Motorcycle Patrolling Duties (MCPD)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
