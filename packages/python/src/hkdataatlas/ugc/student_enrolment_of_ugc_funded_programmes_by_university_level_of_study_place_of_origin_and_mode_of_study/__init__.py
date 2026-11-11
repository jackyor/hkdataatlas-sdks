"""A client library for accessing University Grants Committee Secretariat — Student Enrolment of UGC-funded Programmes by University, Level of Study, Place of Origin and Mode of Study"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
