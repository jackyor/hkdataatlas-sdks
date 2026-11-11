"""A client library for accessing Education Bureau — List of Local Kindergartens (KGs) Not Joining the KG Education Scheme in the Current School Year but Participating in the “K1 Admission Arrangements”"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
