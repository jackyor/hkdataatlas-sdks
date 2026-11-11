"""A client library for accessing Transport Department — Locations of Licensing and Driving Services Offices, Driving Test and Vehicle Examination Centres, Public Vehicles Unit and Driving-offence Points Office"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
