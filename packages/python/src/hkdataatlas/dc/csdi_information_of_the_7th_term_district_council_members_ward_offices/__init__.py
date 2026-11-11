"""A client library for accessing District Councils — Information of the 7th term District Council Members' ward offices"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
