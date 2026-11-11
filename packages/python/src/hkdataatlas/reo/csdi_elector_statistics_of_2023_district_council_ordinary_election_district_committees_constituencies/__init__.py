"""A client library for accessing Registration and Electoral Office — Elector Statistics of 2023 District Council Ordinary Election District Committees Constituencies"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
