import sys
import traceback
from types import TracebackType
from termcolor import colored


def initialize_custom_exception_hook() -> None:
    sys.excepthook = handle_exception


def handle_exception(exception_type: type, exception: BaseException, exception_traceback: TracebackType) -> None:
    print(f'''
    {colored(' Unexpected error ', 'white', 'on_red')} {exception_type.__name__}: {exception}
    {colored(''.join(traceback.format_stack()), 'light_grey')}''')