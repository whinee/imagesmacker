from alltheutils.base_exceptions import (
    CustomBaseException,
    custom_exception,
)
from alltheutils.exceptions import ValidationError


class DrawDataError(BaseException):
    pass


class DrawDataValidationError(DrawDataError, ValidationError):  # type: ignore
    pass


@custom_exception
class DrawDataTypeNotInFieldAttrs(DrawDataValidationError, CustomBaseException):  # type: ignore
    def __init__(self, type: str) -> None:
        """
        Raised when the type is not in the provided field attributes.

        Args:
        - type (`str`): Type of the data that is not found in the provided field attributes.

        """
        self.message = f"Type `{type}` not in the provided field attributes."


@custom_exception
class DrawDataTypeInvalid(DrawDataValidationError, CustomBaseException):  # type: ignore
    def __init__(self, type: str) -> None:
        """
        Raised when the type is invalid.

        Args:
        - type (`str`): Type of the data that is invalid.

        """
        self.message = f"Type `{type}` is an invalid type."
