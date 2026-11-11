"""A client library for accessing Clearing House Statistics - Turnover of HKD FPS payment (Value)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
