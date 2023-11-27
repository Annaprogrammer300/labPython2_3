import os
import csv
import shutil

from progress.bar import IncrementalBar


def rename(new_folder_name: str) -> None:
    """The function renames files and changes the hierarchy

    Args:
        new_folder_name (str): path to destination directory
    """
    for i in range(1, 6):
        bar = IncrementalBar(f'Renaming class_{i}', max=1000)
        relative_path = os.path.relpath(f'{new_folder_name}')
        class_path = os.path.join(relative_path, str(i))
        names = os.listdir(class_path)
        relative_paths = []
        new_relative_paths = []
        for name in names:
            relative_paths.append(os.path.join(class_path, name))
        for name in names:
            new_relative_paths.append(
                os.path.join(relative_path, f'{i}_{name}'))
        for old_name, new_name in zip(relative_paths, new_relative_paths):
            bar.next()
            os.replace(old_name, new_name)
        os.chdir(f'{new_folder_name}')

        if os.path.isdir(str(i)):
            os.rmdir(str(i))

        os.chdir('..')

def move_dataset(old_folder_name: str, new_folder_name: str) -> None:
    """The function gets old and new folders paths and copies files to a new directory

    Args:
        old_folder_name (str): path to source directory
        new_folder_name (str): path to destination directory 
    """
    old_path = os.path.relpath(f'{old_folder_name}')
    new_path = os.path.relpath(f'{new_folder_name}')
    shutil.copytree(old_path, new_path)

    