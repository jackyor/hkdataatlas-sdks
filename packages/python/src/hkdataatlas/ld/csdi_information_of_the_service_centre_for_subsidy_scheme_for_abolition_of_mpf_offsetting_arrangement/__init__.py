"""A client library for accessing Labour Department — Information of the Service Centre for Subsidy Scheme for Abolition of MPF Offsetting Arrangement"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
