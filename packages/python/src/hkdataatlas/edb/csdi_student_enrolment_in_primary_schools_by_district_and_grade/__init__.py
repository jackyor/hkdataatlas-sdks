"""A client library for accessing Education Bureau — Student Enrolment in Primary Schools by District and Grade"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
