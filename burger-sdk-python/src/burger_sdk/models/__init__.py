"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .apierror import APIError
from .burgercreate import BurgerCreate, BurgerCreateTypedDict
from .burgeroutput import BurgerOutput, BurgerOutputTypedDict
from .burgerupdate import BurgerUpdate, BurgerUpdateTypedDict
from .deleteburgerop import DeleteBurgerRequest, DeleteBurgerRequestTypedDict
from .httpvalidationerror import HTTPValidationError, HTTPValidationErrorData
from .ordercreate import OrderCreate, OrderCreateTypedDict
from .orderoutput import OrderOutput, OrderOutputTypedDict, OrderStatus
from .orderupdate import OrderUpdate, OrderUpdateOrderStatus, OrderUpdateTypedDict
from .readburgerop import ReadBurgerRequest, ReadBurgerRequestTypedDict
from .readorderop import ReadOrderRequest, ReadOrderRequestTypedDict
from .responsemessage import ResponseMessage, ResponseMessageTypedDict
from .responsemessage_error import ResponseMessageError, ResponseMessageErrorData
from .updateburgerop import UpdateBurgerRequest, UpdateBurgerRequestTypedDict
from .updateorderop import UpdateOrderRequest, UpdateOrderRequestTypedDict
from .validationerror import (
    Loc,
    LocTypedDict,
    ValidationError,
    ValidationErrorTypedDict,
)

__all__ = [
    "APIError",
    "BurgerCreate",
    "BurgerCreateTypedDict",
    "BurgerOutput",
    "BurgerOutputTypedDict",
    "BurgerUpdate",
    "BurgerUpdateTypedDict",
    "DeleteBurgerRequest",
    "DeleteBurgerRequestTypedDict",
    "HTTPValidationError",
    "HTTPValidationErrorData",
    "Loc",
    "LocTypedDict",
    "OrderCreate",
    "OrderCreateTypedDict",
    "OrderOutput",
    "OrderOutputTypedDict",
    "OrderStatus",
    "OrderUpdate",
    "OrderUpdateOrderStatus",
    "OrderUpdateTypedDict",
    "ReadBurgerRequest",
    "ReadBurgerRequestTypedDict",
    "ReadOrderRequest",
    "ReadOrderRequestTypedDict",
    "ResponseMessage",
    "ResponseMessageError",
    "ResponseMessageErrorData",
    "ResponseMessageTypedDict",
    "UpdateBurgerRequest",
    "UpdateBurgerRequestTypedDict",
    "UpdateOrderRequest",
    "UpdateOrderRequestTypedDict",
    "ValidationError",
    "ValidationErrorTypedDict",
]