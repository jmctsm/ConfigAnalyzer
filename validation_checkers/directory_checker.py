import os
from typing import List


def directory_checker(folder_to_check: str) -> List[str]:
    """
    will verify that this is a folder, it exists, and then will return all
    file names and paths in it back to the main function
    Args:
        folder_to_check : folder name to check
    return:
        list : list of files including their path or one element "Nothing"

    """

    if not isinstance(folder_to_check, str):
        raise TypeError(f"{folder_to_check} needs to be a string")
    if not os.path.exists(folder_to_check):
        raise ValueError(f"{folder_to_check} does not exist")
    if not os.path.isdir(folder_to_check):
        raise ValueError(f"{folder_to_check} is not a valid directory")

    # now we know the folder_to_check is a string, exists, and is a directory
    # Let's walk it
    for root, dirs, files in os.walk(folder_to_check):
        for name in files:
            print(os.path.join(root, name))

    return ["Nothing"]