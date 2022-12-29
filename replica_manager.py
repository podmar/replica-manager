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
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        self.create_replica()

    def create_replica(self) -> None:
        """A function creating a copy of an existing folder to the destination directory."""
        shutil.copytree(self.src, self.dst)


if __name__ == "__main__":
    try:
        replica = Replica(sys.argv[1], sys.argv[2])
    except IndexError:
        print('Required arguments not specified. Use following CLI arguments:\nreplica_manager.py <source_folder_path> <destination_folder_path> <synchronization_interval> <log_file_path>')
