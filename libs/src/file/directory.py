import io
import sys
import os
import pathlib


def get_total_lines() -> int:
    """
    Get the total amount of lines in all files in a directory.
    --

    :param directory: The directory to search for files.
    """
    if not os.path.exists('./'):
        return 0
    else:
        return sum(
            [
            len(open(f, 'r', encoding='utf-8').readlines()) for f in [
                f for f in pathlib.Path('./').glob('**/*.py') 
                if f.is_file() and f'.venv' not in str(f)
            ]
            ]
        )