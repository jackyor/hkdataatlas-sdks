"""A client library for accessing University Grants Committee Secretariat — Geo-referenced data of UGC-funded institutions"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
