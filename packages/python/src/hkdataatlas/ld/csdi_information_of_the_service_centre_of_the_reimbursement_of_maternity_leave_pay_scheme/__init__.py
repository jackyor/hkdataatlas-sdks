"""A client library for accessing Labour Department — Information of the Service Centre of the Reimbursement of Maternity Leave Pay Scheme"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
