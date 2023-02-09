"""The solution of the second problem."""


from typing import Generator, Callable, Union, List


def create_handlers(callback: Callable) -> Generator:
    """Create handlers.

    Args:
        callback (Callable): any function.

    Yields:
        Generator: functions that were generated.
    """
    for step in range(5):
        yield lambda: callback(step)


def execute_handlers(handlers: Union[Generator, List]) -> None:
    """Call functions.

    Args:
        handlers (Union[Generator, List]): functions that we should execute.
    """
    for handler in handlers:
        print(handler())


def add_one(number: int) -> int:
    """Add one to number.

    Args:
        number (int): any number.

    Returns:
        int: number + 1.
    """
    return number+1


execute_handlers(create_handlers(add_one))
