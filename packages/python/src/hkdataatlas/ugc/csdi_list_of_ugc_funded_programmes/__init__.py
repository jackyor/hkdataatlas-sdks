"""A client library for accessing University Grants Committee Secretariat — List of UGC-funded Programmes"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
