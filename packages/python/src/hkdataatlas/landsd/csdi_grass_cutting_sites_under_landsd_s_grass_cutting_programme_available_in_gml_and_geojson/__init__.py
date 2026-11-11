"""A client library for accessing Lands Department — Grass-cutting Sites under LandsD's Grass-cutting Programme (Available in GML and GeoJSON)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
