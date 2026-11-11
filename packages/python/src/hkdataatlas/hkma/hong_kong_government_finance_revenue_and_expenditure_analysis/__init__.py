"""A client library for accessing HKIMR - Hong Kong Government Finance: Revenue and Expenditure, Analysis/Breakdown of Government Expenditure"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
