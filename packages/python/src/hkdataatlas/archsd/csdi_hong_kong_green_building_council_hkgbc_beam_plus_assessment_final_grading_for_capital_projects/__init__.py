"""A client library for accessing Architectural Services Department — Hong Kong Green Building Council (HKGBC) BEAM Plus Assessment Final Grading for Capital Projects"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
