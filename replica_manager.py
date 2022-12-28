# [x] write a program that copies an existing folder into a new folder
# [] apply command line arguments for paths source and replica
# [] build logging functionality
# [] apply copy at interval
# [] apply a hashing algorithm

import shutil


def create_replica(path: str) -> None:
    """A function creating a copy of an existing folder"""

    # define path to the default destination
    last_dst_index = path[:-1].rfind('/')
    default_dst = f'{path[:last_dst_index]}/replica_{path[last_dst_index+1:]}'

    # create a copy of the directory
    shutil.copytree(path, default_dst)

    return
