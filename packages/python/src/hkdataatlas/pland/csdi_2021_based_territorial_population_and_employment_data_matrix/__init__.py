"""A client library for accessing Planning Department — 2021-based Territorial Population and Employment Data Matrix"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
