# get all modules without version numbers from a requirements_01.txt file
from os import access, R_OK, W_OK
from shutil import copy2
from file_handling import overwrite_file


def strip_version_numbers(f, f_old):
    if access(f, R_OK and W_OK):
        try:
            f_old = overwrite_file(f_old)
            copy2(f, f_old)
        except IOError:
            print(f"file {f} could not be copied to {f_old} ")
    else:
        print(f"file {f} is not accessible for read or write operations.\n")
        print(" Program aborted")
        return
    with open(f, 'w') as file_out:
        with open(f_old) as file_object:
            for line in file_object:
                module_name = line.split('=')
                file_out.write(f"{module_name[0]}\n")


if __name__ == "__main__":
    strip_version_numbers(f='heroku.txt', f_old='old.txt')
