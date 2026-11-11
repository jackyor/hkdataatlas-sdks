"""A client library for accessing Labour Department — Organisations providing career development services under the Youth Employment and Training Programme"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
