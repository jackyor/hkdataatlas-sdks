"""A client library for accessing Drainage Services Department — List of Facilities (Sewage Treatment Facilities, Stormwater Pumping Stations and Inflatable Dams)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
