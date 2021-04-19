# conf_analysis.py

"""
This app will call all the other pieces for config analysis for best practices
as well we check STIGs if needed.
"""
import re

import conf_analysis.validation_checkers


def main(folder_name: str, stig_check: bool = False) -> int:
    """
    requires a folder to look at and then config files are needed to be named

    {IP}_{startup|running|candidate}.txt

    or

    {IP}_{startup|running|candidate}.txt

    if STIG check is False, no STIG checking is done

    Args:
        folder_name : folder location to start looking in.  Recursively will traverse
            into any folders within this folder
        stig_check : boolean to know if running stig checks or not

    Returns:
        int : 0 for all good.  1 for returned due to error
    """
    files_in_directory = (
        conf_analysis.validation_checkers.directory_checker.directory_checker(
            folder_name
        )
    )
    # if the length of the files returned is 1 and is only a string of "Nothing"
    # no files to scan.
    if len(files_in_directory) == 1 and files_in_directory[0] == "Nothing":
        print("Apparently there were no files to check.  Exiting")
        return 1

    # run through all files and see if the filename matches what is expected.  If so
    # add that a config file to use for scanning
    filename_pattern = "\d+\.\d+\.\d+\.\d+_[startup|running|candidate][_full]*.txt"
    files_to_check = []
    for filename in files_in_directory:
        if re.search(filename_pattern, filename):
            files_to_check.append(filename)


if __name__ == "__main__":
    import time

    start_time = time.time()
    main()
    duration = time.time() - start_time
    print(f"Total time was {duration} seconds")
