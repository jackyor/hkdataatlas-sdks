"""A client library for accessing Transport Department — Real-time arrival data of green minibuses (GMBs)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
