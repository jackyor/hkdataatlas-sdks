"""A client library for accessing Development Bureau — Real-time Parking Vacancy Data in Kowloon East (i.e. Kwun Tong, Kowloon Bay and San Po Kong Business Areas, and Kai Tak Development Area)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
