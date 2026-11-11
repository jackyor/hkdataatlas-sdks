"""A client library for accessing Clearing House Statistics - Turnover of RMB FPS payment (Volume)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
