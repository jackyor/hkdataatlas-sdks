"""A client library for accessing Government Property Agency — Award of Contracts for Leasing of Non-domestic Properties (Automatic Teller Machine Sites / Automatic Vending Machine Sites / Shops / Car Parks) under the purview of Government Property Agency (From 2021 onwards)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
