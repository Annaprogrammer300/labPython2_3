import os
import shutil
import csv
import random

from progress.bar import IncrementalBar


def rename(new_folder_name: str) -> dict:
    """The function renames files and changes the hierarchy, 

    Args:
        new_folder_name (str): path to destination directory

    Returns:
        dict: key - file path, value - class label
    """
    random_numbers = random.sample(range(0, 10001), 5000)
    count = 0
    class_nums = {}
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
                os.path.join(relative_path, f'{random_numbers[count]}.txt'))
            class_nums[random_numbers[count]] = i
            count += 1
        for old_name, new_name in zip(relative_paths, new_relative_paths):
            bar.next()
            os.replace(old_name, new_name)
        os.chdir(f'{new_folder_name}')

        if os.path.isdir(str(i)):
            os.rmdir(str(i))

        os.chdir('..')
    return class_nums

