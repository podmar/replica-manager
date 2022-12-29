# [x] write a program that copies an existing folder into a new folder
# [x] apply command line arguments for paths source and replica
# [x] build a main function
# [x] build logging functionality (creation/copying/removal operations)
# [] apply copy at interval
# [] write a readme
# [] apply a hashing algorithm

import shutil
import sys
import logging

import logger_settings


def main() -> None:
    try:
        logger_settings.set_logger(sys.argv[3])
        replica = Replica(sys.argv[1], sys.argv[2])
    except IndexError:
        print('Required arguments not specified. Use following CLI arguments:\nreplica_manager.py <source_folder_path> <destination_folder_path> <synchronization_interval> <log_file_path>')


class Replica:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        self.create_replica()

    def create_replica(self) -> None:
        """A function creating a copy of an existing folder to the destination directory."""
        shutil.copytree(self.src, self.dst)
        logging.info("a replica has been created")


if __name__ == "__main__":
    main()
