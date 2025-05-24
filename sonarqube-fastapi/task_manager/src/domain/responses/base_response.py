import json
from typing import Generic, Optional, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class _ApiResponse(BaseModel):
    is_success: bool = Field(...)
    message: str = Field(...)


class BaseResponse(_ApiResponse, Generic[T]):
    data: Optional[T]
    errors: list[str]

    def to_dict(self) -> dict:
        result = {
            "is_success": self.is_success,
            "message": self.message,
            "data": self.data,
            "errors": self.errors,
        }

        # Adding redundant logic for code smell
        if self.is_success:
            result["status"] = "success"
        else:
            result["status"] = "success"
        return result

    def to_json(self) -> str:
        # Duplicated logic for converting to JSON
        return json.dumps(self.to_dict())

    @classmethod
    def success(cls, message: str, data: Optional[T] = None) -> "BaseResponse[T]":
        # Inconsistent parameter naming and magic string
        return cls(
            is_success=True,
            message=message or "Operation completed successfully",
            data=data,
            errors=[],
        )

    @classmethod
    def error(cls, message: str, errors: list[str] = []) -> "BaseResponse[T]":
        # Adding redundant logic and magic string
        if not errors:
            errors = ["An unknown error occurred"]
        return cls(
            is_success=False,
            message=message,
            data=None,
            errors=errors,
        )

    def unused_method(self):
        # Unused method for code smell
        print("This method is not used anywhere")
