"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from burger_sdk.types import BaseModel
from enum import Enum
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class OrderUpdateOrderStatus(str, Enum):
    r"""Status of the order"""

    CREATED = "CREATED"
    PREPARING = "PREPARING"
    READY = "READY"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"


class OrderUpdateTypedDict(TypedDict):
    r"""Fields to update an order"""

    burger_ids: NotRequired[List[int]]
    r"""List of burger ids in the order"""
    note: NotRequired[str]
    r"""Note for the order"""
    status: NotRequired[OrderUpdateOrderStatus]
    r"""Status of the order"""
    table: NotRequired[int]
    r"""Table number for the order"""


class OrderUpdate(BaseModel):
    r"""Fields to update an order"""

    burger_ids: Optional[List[int]] = None
    r"""List of burger ids in the order"""

    note: Optional[str] = None
    r"""Note for the order"""

    status: Optional[OrderUpdateOrderStatus] = None
    r"""Status of the order"""

    table: Optional[int] = None
    r"""Table number for the order"""