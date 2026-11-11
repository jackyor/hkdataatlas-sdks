"""A client library for accessing Education Bureau — Secondary School Places Allocation (SSPA) System School Net Information"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
