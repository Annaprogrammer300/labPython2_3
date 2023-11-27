import os
import csv

from typing import List

from progress.bar import IncrementalBar


def get_absolute_paths(num_mark: int, folder_name: str) -> List[str]:
    """
    The function gets absolute paths to files and returns a list with absolute paths

    Args:
        num_mark (int): class num
        folder_name (str): path of initial dataset

    Returns:
        List[str]: list of absolute path
    """
    absolute_path = os.path.abspath(f'{folder_name}')
    class_path = os.path.join(absolute_path, str(num_mark))
    names = os.listdir(class_path)
    absolute_paths = []
    for name in names:
        absolute_paths.append(os.path.join(class_path, name))
    return absolute_paths



def get_relative_paths(num_mark: int, folder_name: str) -> List[str]:
    """
    The function gets absolute paths to files and returns a list with relative paths
    Args:
        num_mark (int): class num
        folder_name (str): folder path with files

    Returns:
        List[str]: list of relative paths
    """
    relative_path = os.path.relpath(f'{folder_name}')
    class_path = os.path.join(relative_path, str(num_mark))
    names = os.listdir(class_path)
    relative_paths = []
    for name in names:
        relative_paths.append(os.path.join(class_path, name))
    return relative_paths

