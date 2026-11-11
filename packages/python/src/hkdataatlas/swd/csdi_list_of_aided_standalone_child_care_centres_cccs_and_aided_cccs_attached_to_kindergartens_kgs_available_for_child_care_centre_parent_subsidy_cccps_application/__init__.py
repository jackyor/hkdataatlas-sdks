"""A client library for accessing Social Welfare Department — List of aided standalone Child Care Centres (CCCs) and aided CCCs attached to Kindergartens (KGs) available for Child Care Centre Parent Subsidy (CCCPS) application"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
