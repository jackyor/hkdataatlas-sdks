"""A client library for accessing Digital Policy Office — List of community and mobile help desks for digital service under the “Smart Silver” Community Digital Inclusion Programme"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
