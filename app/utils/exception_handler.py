from functools import wraps
from typing import Union, Tuple
from fastapi import HTTPException
from pydantic import ValidationError

from database.core import NotFoundError


def loc_to_dot_sep(loc: Tuple[Union[str, int], ...]) -> str:
    path = ""
    for i, x in enumerate(loc):
        if isinstance(x, str):
            if i > 0:
                path += "."
            path += x
        elif isinstance(x, int):
            path += f"[{x}]"
        else:
            raise TypeError("Unexpected type")
    return path


def exception_handler(func):
    """This decorator handles the validation error after one
    tries to validate the data in the request and not found error in db"""

    @wraps(func)
    def wrapper(*arg, **kw):
        try:
            return func(*arg, **kw)
        except NotFoundError as not_found_error:
            raise HTTPException(status_code=404) from not_found_error
        except ValidationError as error:
            try:
                errors = [
                    {
                        "message": error.get("msg"),
                        "input": (
                            {
                                error.get("loc")[0]: error.get("input", {}).get(
                                    error.get("loc")[0]
                                )
                            }
                            if isinstance(error.get("input"), dict)
                            else error.get("input")
                        ),
                        "path": loc_to_dot_sep(error.get("loc")),
                    }
                    for error in error.errors()
                ]
                raise ValidationError(errors)
            except TypeError:
                raise ValidationError from error

    return wrapper
