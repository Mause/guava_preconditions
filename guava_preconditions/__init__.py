from typing import Any, Optional, TypeVar

T = TypeVar("T")


def checkArgument(
    expression: bool, errorMessageTemplate: Optional[str] = None, *errorMessageArgs: Any
) -> None:
    "Ensures the truth of an expression involving one or more parameters to the calling method."


def checkElementIndex(index: int, size: int, desc: str = None) -> int:
    "Ensures that index specifies a valid element in an array, list or string of size size."


def checkNotNull(
    reference: Optional[T], errorMessageTemplate: str, *errorMessageArgs: Any
) -> T:
    "Ensures that an object reference passed as a parameter to the calling method is not null."


def checkPositionIndex(index: int, size: int, desc: str = None) -> int:
    "Ensures that index specifies a valid position in an array, list or string of size size."


def checkPositionIndexes(start: int, end: int, size: int) -> None:
    "Ensures that start and end specify a valid positions in an array, list or string of size size, and are in order."


def checkState(
    expression: bool, errorMessageTemplate: str = None, *errorMessageArgs: Any
) -> None:
    "Ensures the truth of an expression involving the state of the calling instance, but not involving any parameters to the calling method."
