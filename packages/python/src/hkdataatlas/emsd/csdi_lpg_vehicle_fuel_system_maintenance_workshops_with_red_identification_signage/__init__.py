"""A client library for accessing Electrical and Mechanical Services Department — LPG Vehicle Fuel System Maintenance Workshops with Red Identification Signage"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
