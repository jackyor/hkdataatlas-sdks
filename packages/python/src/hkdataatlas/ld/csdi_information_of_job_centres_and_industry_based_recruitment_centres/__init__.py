"""A client library for accessing Labour Department — Information of Job Centres and Industry-based Recruitment Centres"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
