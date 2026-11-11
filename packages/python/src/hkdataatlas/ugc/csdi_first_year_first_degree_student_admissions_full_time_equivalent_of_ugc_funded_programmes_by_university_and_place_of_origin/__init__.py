"""A client library for accessing University Grants Committee Secretariat — First-year-first-degree Student Admissions (Full-time equivalent) of UGC-funded Programmes by University and Place of Origin"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
