# [x] write a program that copies an existing folder into a new folder
# [] apply command line arguments for paths source and replica
# [] build a main function
# [] build logging functionality
# [] apply copy at interval
# [] write a readme
# [] apply a hashing algorithm

import shutil
import sys


class Replica:
    def __init__(self, src):
        self.src = src
        self.create_replica()

    def create_replica(self) -> None:
        """A function creating a copy of an existing folder."""

        # define path to the default destination
        last_dst_index = self.src[:-1].rfind('/')
        default_dst = f'{self.src[:last_dst_index]}/replica_{self.src[last_dst_index+1:]}'

        # create a copy of the directory
        shutil.copytree(self.src, default_dst)

        return


if __name__ == "__main__":
    try:
        replica = Replica(sys.argv[1])
    except IndexError:
        print('No source folder given. Use following CLI arguments:\nreplica_manager.py <source_folder_path> <destination_folder_path> <synchronization_interval> <log_file_path>')
