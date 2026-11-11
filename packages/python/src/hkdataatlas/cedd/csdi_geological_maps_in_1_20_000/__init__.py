"""A client library for accessing Civil Engineering and Development Department — Geological Maps in 1:20,000"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
