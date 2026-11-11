"""A client library for accessing Civil Aid Service — Path information of CAS Hiking Trails Patrolling Duties (HTPD)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
