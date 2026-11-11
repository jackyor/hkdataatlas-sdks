"""A client library for accessing Administration Wing, Chief Secretary for Administration's Office — Information on Legal Advice Scheme for Unrepresented Litigants on Civil Procedures"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
