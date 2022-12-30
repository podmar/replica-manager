# [x] write a program that copies an existing folder into a new folder
# [x] apply command line arguments for paths source and replica
# [x] build a main function
# [x] build logging functionality (creation/copying/removal operations)
# [x] compare and update replica
#   [x] - copy new files that are not in the replica
#   [x] - check for changes and add them to the replica
#   [] - remove deleted files
# [] apply interval
# [] write a readme
# [] apply a hashing algorithm ?
# [] apply threading ?
# [] refactor CLI arg tests
# touch test2.txt
# python replica_manager.py /Users/martapodziewska/Documents/test_folder /Users/martapodziewska/Documents/replica_1818_test_folder /Users/martapodziewska/Documents/log1852.log

import shutil
import sys
import logging
import filecmp
import os
import time

import logger_settings


def main() -> None:
    try:
        logger_settings.set_logger(sys.argv[3])
        replica = Replica(sys.argv[1], sys.argv[2])
    except IndexError:
        print('Required arguments not specified. Use following CLI arguments:\nreplica_manager.py <source_folder_path> <destination_folder_path> <synchronization_interval> <log_file_path>')

    if replica:
        time.sleep(5)
        # for iteration in range(5):
        replica.update_replica()
        #     time.sleep(3)


class Replica:
    def __init__(self, src: str, dst: str):
        self.src = src
        self.dst = dst
        self.create_replica()

    def create_replica(self) -> None:
        """A function creating a copy of an existing folder to the destination directory."""
        shutil.copytree(self.src, self.dst)
        logging.info("A replica folder has been created.")

    def update_replica(self) -> None:
        src_filelist = os.listdir(self.src)
        dst_filelist = os.listdir(self.dst)

        for file in src_filelist:
            if file in dst_filelist:
                if self.file_changed(file):
                    self.delete_file(file)
                    self.copy_file(file)

                else:
                    continue
            else:
                self.copy_file(file)

    def file_changed(self, file_name: str) -> bool:
        src_file_path = f'{self.src}/{file_name}'
        dst_file_path = f'{self.dst}/{file_name}'
        return filecmp.cmp(src_file_path, dst_file_path)

    def copy_file(self, file_name: str) -> None:
        """Given the file name, the method copies it to destination folder"""
        src_file_path = f'{self.src}/{file_name}'
        dst_file_path = f'{self.dst}/{file_name}'
        shutil.copy2(src_file_path, dst_file_path)

    def delete_file(self, file_name: str) -> None:
        """Removes a file from the replica (destination) directory"""
        file_path = f'{self.dst}/{file_name}'
        os.remove(file_path)


if __name__ == "__main__":
    main()
