"""A client library for accessing Hospital Authority — List of Hospital Authority Hospitals/Institutions/Specialist Outpatient Clinics/Family Medicine Clinics"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
