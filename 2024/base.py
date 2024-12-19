from enum import Enum, auto
from functools import wraps
from pathlib import Path
from typing import (
    Callable,
    Generic,
    TypeVar,
    Union,
    cast,
    final,
    overload
)


class AoCException(Exception):
    """
    custom error class for issues related to creating/running solutions
    """


class InputTypes(Enum):
    # one solid block of text; the default
    TEXT = auto()
    # str[], split by a specified separator (default newline)
    STRSPLIT = auto()


# almost always int, but occasionally str; None is fine to disable a part
ResultType = Union[int, str, None]


InputType = Union[str, int, list[int], list[str], list[list[int]]]
I = TypeVar("I", bound=InputType)


class BaseSoluton(Generic[I]):
    separator = "\n"

    # Solution Subclasses define these
    input_type: InputTypes = InputTypes.TEXT
    _year: int
    _day: int

    def __init__(self, use_test_data=False):
        self.use_test_data = use_test_data
        self.input = cast(I, self.read_input())

    @property
    def year(self):
        if not hasattr(self, "_year"):
            raise NotImplementedError("explicitly define Solution._year")
        return self._year

    @property
    def day(self):
        if not hasattr(self, "_day"):
            raise NotImplementedError("explicitly define Soluiton._day")
        return self._day

    def solve(self):
        """
        Returns a 2-tuple with the answers.
        """
        return self.part_1(), self.part_2()

    def part_1(self) -> ResultType:
        raise NotImplementedError

    def part_2(self) -> ResultType:
        raise NotImplementedError

    @final
    def read_input(self) -> InputType:
        """
        handles locating, reading, and parsing input files
        """
        input_file = Path(
            Path(__file__).parent,
            # the 4-digit year
            str(self.year),
            # padded day folder
            f"day_{self.day:02}",
            # either the real input or the test input
            f"input{'.test' if self.use_test_data else ''}.txt",
        )
        if not input_file.exists():
            raise AoCException(
                f'Failed to find an input file at path "./{input_file.relative_to(Path.cwd())}". You can run `./start --year {self.year} {self.day}` to create it.'
            )

        data = input_file.read_text().strip("\n")

        if not data:
            raise AoCException(
                f'Found a file at path "./{input_file.relative_to(Path.cwd())}", but it was empty. Make sure to paste some input!'
            )

        if self.input_type is InputTypes.TEXT:
            return data

        if self.input_type is InputTypes.STRSPLIT:
            # default to newlines
            parts = data.split(self.separator)

            return parts

    #raise ValueError(f"Unrecognized input_type: {self.input_type}")


class StrSplitSolution(BaseSoluton[list[str]]):
    """
    input is a str[], spli by a specified seperator (default newline)
    """

    input_type = InputTypes.STRSPLIT


# https://stackoverflow.com/a/65681955/1825390
SolutionClassType = TypeVar("SolutionClassType", bound=BaseSoluton)


# these types ensure the return type of the function matchs `@answer`
# see:  https://github.com/microsoft/pyright/discussions/4317#discussioncomment-4386187
R = TypeVar("R")  # return type generic


@overload
def answer(
    expected: R
) -> Callable[[Callable[[SolutionClassType], R]], Callable[[SolutionClassType], R]]: ...


def answer(
        expected: R
) -> Callable[[Callable[[SolutionClassType], R]], Callable[[SolutionClassType], R]]:
    """
    Decorator to assert the result of the funtion is a certain thing.
    This is specifically designed to be used on instance methods of BaseSolution.
    It only throws error when _not_ using test data.

    Usage:
    ```py
    @answer(3)
    def f(i):
        return i

    f(1) # throws
    f(3) # returns 3 like normal
    """

    def deco(func: Callable[[SolutionClassType], R]):
        @wraps(func)
        # uses 'self' because that's what's passed to the original solution function
        def wrapper(self: SolutionClassType):
            result = func(self)
            #only assert the answer for non-test data
            if not self.use_test_data and result is not None and result != expected:
                _, year, day, _ = self.__module__.split(".")
                raise AoCException(
                    f"Failed @answer assertion for {year} / {day} / {func.__name__}:\n returned {result}\n expected: {expected}"
                )
            return result

        return wrapper

    return deco
