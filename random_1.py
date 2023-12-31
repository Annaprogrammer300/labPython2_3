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


def move_dataset(old_folder_name: str, new_folder_name: str) -> None:
    """The function copies files to a new directory

    Args:
        old_folder_name (str): path to source directory
        new_folder_name (str): path to destination directory
    """
    old_path = os.path.relpath(f'{old_folder_name}')
    new_path = os.path.relpath(f'{new_folder_name}')
    shutil.copytree(old_path, new_path)


def make_csv_random(new_folder_name: str, class_number: dict) -> None:
    """The function writes data to a csv file in the following format: absolute path, relative path, class label

    Args:
        new_folder_name (str): path to destination directory
        class_number (dict): key - file path, value - class label
    """
    bar = IncrementalBar(f'Writting csv', max=5000)
    work_catalog = os.getcwd()
    os.chdir(new_folder_name)
    names = os.listdir()
    os.chdir(work_catalog)
    f = open("paths3.csv", 'w')
    writer = csv.writer(f, delimiter=',', lineterminator='\n')
    for name in names:
        absolute_path = os.path.abspath(new_folder_name)
        absolute_path_file = os.path.join(absolute_path, name)
        relative_path = os.path.relpath(f'{new_folder_name}')
        relative_path_file = os.path.join(relative_path, name)
        name = name.replace('.txt', '')
        writer.writerow(
            [absolute_path_file, relative_path_file, class_number[int(name)]])
        bar.next()


def main(old_folder_name: str, new_folder_name: str) -> None:
    move_dataset(old_folder_name, new_folder_name)
    make_csv_random(new_folder_name, rename(new_folder_name))