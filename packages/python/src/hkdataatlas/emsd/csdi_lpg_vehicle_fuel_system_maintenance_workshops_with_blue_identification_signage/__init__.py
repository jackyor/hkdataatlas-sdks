"""A client library for accessing Electrical and Mechanical Services Department — LPG Vehicle Fuel System Maintenance Workshops with Blue Identification Signage"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
