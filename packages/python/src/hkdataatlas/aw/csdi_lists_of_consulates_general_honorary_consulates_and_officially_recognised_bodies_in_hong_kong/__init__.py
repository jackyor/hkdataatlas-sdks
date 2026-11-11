"""A client library for accessing Administration Wing, Chief Secretary for Administration's Office — Lists of Consulates-General, Honorary Consulates and Officially Recognised Bodies in Hong Kong"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
