"""A client library for accessing Department of Health — Baby-care Facilities in Government Premises"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
