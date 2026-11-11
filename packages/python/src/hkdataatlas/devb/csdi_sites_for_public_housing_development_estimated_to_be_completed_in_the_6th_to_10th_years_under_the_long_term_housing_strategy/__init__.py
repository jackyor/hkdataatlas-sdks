"""A client library for accessing Development Bureau — Sites for Public Housing Development Estimated to be Completed in the 6th to 10th Years Under the Long Term Housing Strategy"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
