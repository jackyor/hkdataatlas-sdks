"""A client library for accessing University Grants Committee Secretariat — Employment Situation of Graduates of Full-time UGC-funded Programmes by University, Level of Study, Employment Situation and Occupation"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
