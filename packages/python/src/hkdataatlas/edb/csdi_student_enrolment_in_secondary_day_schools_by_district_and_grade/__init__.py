"""A client library for accessing Education Bureau — Student Enrolment in Secondary Day Schools by District and Grade"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
