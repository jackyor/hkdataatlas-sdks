"""A client library for accessing University Grants Committee Secretariat — Student Enrolment (Headcount) of UGC-funded Programmes by University, Level of Study, Mode of Study and Academic Programme Category"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
