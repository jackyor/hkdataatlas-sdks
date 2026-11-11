"""A client library for accessing Hong Kong Police Force — Police Offices Providing Services on Matters related to Licensing, Permit, Certificate Application"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
