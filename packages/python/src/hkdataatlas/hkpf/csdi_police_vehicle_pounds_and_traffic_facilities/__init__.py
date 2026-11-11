"""A client library for accessing Hong Kong Police Force — Police Vehicle Pounds and Traffic Facilities"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
