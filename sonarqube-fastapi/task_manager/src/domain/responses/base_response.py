from typing import Generic, Optional, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class _ApiResponse(BaseModel):
    is_success: bool = Field(...)
    message: str = Field(...)


class BaseResponse(_ApiResponse, Generic[T]):
    data: Optional[T] = None
    errors: list[str] = []

    @classmethod
    def success(cls, message: str, data: Optional[T] = None) -> "BaseResponse[T]":
        return cls(
            is_success=True,
            message=message,
            data=data,
            errors=[],
        )

    @classmethod
    def error(cls, message: str, errors: list[str] = []) -> "BaseResponse[T]":
        return cls(
            is_success=False,
            message=message,
            data=None,
            errors=errors,
        )
