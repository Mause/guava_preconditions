from typing import Optional, TypeVar

T = TypeVar("T")


def checkArgument(expression: bool):
    "Ensures the truth of an expression involving one or more parameters to the calling method."


def checkArgument(expression: bool, errorMessage: Any):
    "Ensures the truth of an expression involving one or more parameters to the calling method."


def checkArgument(expression: bool, errorMessageTemplate: str, *errorMessageArgs: Any):
    "Ensures the truth of an expression involving one or more parameters to the calling method."


def checkElementIndex(index: int, size: int) -> int:
    "Ensures that index specifies a valid element in an array, list or string of size size."


def checkElementIndex(index: int, size: int, desc: str) -> int:
    "Ensures that index specifies a valid element in an array, list or string of size size."


def checkNotNull(reference: Optional[T]) -> T:
    "Ensures that an object reference passed as a parameter to the calling method is not null."


def checkNotNull(reference: Optional[T], errorMessage: Any) -> T:
    "Ensures that an object reference passed as a parameter to the calling method is not null."


def checkNotNull(
    reference: Optional[T], errorMessageTemplate: str, *errorMessageArgs: Any
) -> T:
    "Ensures that an object reference passed as a parameter to the calling method is not null."


def checkPositionIndex(index: int, size: int) -> int:
    "Ensures that index specifies a valid position in an array, list or string of size size."


def checkPositionIndex(index: int, size: int, desc: str) -> int:
    "Ensures that index specifies a valid position in an array, list or string of size size."


def checkPositionIndexes(start: int, end: int, size: int):
    "Ensures that start and end specify a valid positions in an array, list or string of size size, and are in order."


def checkState(expression: bool):
    "Ensures the truth of an expression involving the state of the calling instance, but not involving any parameters to the calling method."


def checkState(expression: bool, errorMessage: Any):
    "Ensures the truth of an expression involving the state of the calling instance, but not involving any parameters to the calling method."


def checkState(expression: bool, errorMessageTemplate: str, *errorMessageArgs: Any):
    "Ensures the truth of an expression involving the state of the calling instance, but not involving any parameters to the calling method."
