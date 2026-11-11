"""A client library for accessing Hospital Authority — Inpatient and Day Inpatient Services Throughput"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
