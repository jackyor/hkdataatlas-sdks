"""A client library for accessing Transport Department — Distribution of Metered Parking Spaces and Occupancy of those Installed with New Parking Meters"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
