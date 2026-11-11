"""A client library for accessing University Grants Committee Secretariat — Senior-year Student Admissions (Full-time equivalent) of UGC-funded Programmes by University and Mode of Study"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
