"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from burger_sdk.types import BaseModel
from typing_extensions import TypedDict


class ResponseMessageTypedDict(TypedDict):
    r"""A response message"""

    message: str
    r"""The response message"""


class ResponseMessage(BaseModel):
    r"""A response message"""

    message: str
    r"""The response message"""