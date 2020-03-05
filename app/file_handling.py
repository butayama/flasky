import pickle
from os.path import join, exists, isfile, dirname
from os import F_OK, access, makedirs


def overwrite_file(filename):
    """loop until overwrite existing file or input of a new filename"""
    dump_file = False
    while not dump_file:
        if exists(filename):
            overwrite = input(f"overwrite {filename} (y/n): ")
            if overwrite in ["y", "Y"]:
                dump_file = True
            if overwrite in ["n", "N"]:
                new_name = input(f"new filename: ")
                filename = join(dirname(filename), new_name)
        else:
            dump_file = True

    return filename


def write_pickle(dic_a, filename):
    """write a dictionary to pickle file 'filename'"""
    try:
        with open(filename, "wb") as f:
            pickle.dump(dic_a, f)
    except IOError:
        raise IOError("no write permission")


def text_file(filename):
    """does nothing with 'filename'
    up to now it's just a test if 'open(filename, 'w') is possible without IOError"""
    try:
        with open(filename, 'w') as f:
            pass
    except IOError:
        raise IOError("no write permission")


def verify_path(pathname):
    """creates path 'pathname' if it does not exist yet"""
    if not access(pathname, F_OK):
        try:
            makedirs(pathname)
        except IOError:
            raise IOError("no write permission")


def store_pickle_file(dic_a, path_file_name):
    """writes a dictionary into a pickle file after reassuring that no existing file is overwritten without consent"""
    if isfile(path_file_name):
        path_file_name = overwrite_file(path_file_name)
    verify_path(dirname(path_file_name))
    write_pickle(dic_a, path_file_name)


def text_file_object(path_file_name):
    """checks path_file_name, reassuring that no existing file is overwritten without consent"""
    if isfile(path_file_name):
        path_file_name = overwrite_file(path_file_name)
    verify_path(dirname(path_file_name))
    text_file(path_file_name)
