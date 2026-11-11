"""A client library for accessing Fraudulent Bank Websites, Phishing E-mails and Similar Scams (Warning notices about bogus websites/phone calls)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
