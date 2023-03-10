"""
Tests for the replica manager.
"""

from unittest import TestCase
from unittest.mock import patch
import shutil
import tempfile
import os
import sys
import time

from replica_manager import Replica


class TestReplicaCreated(TestCase):
    """Test that a replica of a given folder is created."""

    def setUp(self):
        self.tmp_test_container = tempfile.mkdtemp()
        self.tmp_test_src = tempfile.mkdtemp(dir=self.tmp_test_container)
        self.tmp_test_file = tempfile.mkstemp(dir=self.tmp_test_src)
        self.tmp_test_dst = f'{self.tmp_test_container}/test_replica_folder'

    def tearDown(self):
        shutil.rmtree(self.tmp_test_container)

    def test_replica_folder_created_success(self):
        """Tests that a copy of the source folder is created in the destination directory"""
        test_replica = Replica(self.tmp_test_src, self.tmp_test_dst, 1)
        self.assertEqual(len(os.listdir(self.tmp_test_dst)), 1)

    def test_replica_folder_contains_files(self):
        """Tests that replica folder contains original files from the source folder"""
        test_replica = Replica(self.tmp_test_src, self.tmp_test_dst, 1)
        self.assertEqual(len(os.listdir(self.tmp_test_dst)), 1)

# TODO: test that if a replica not created an exception is raised


class TestCliArguments(TestCase):
    """Test that CLI arguments can be passed successfully."""

    def setUp(self):
        self.tmp_test_container = tempfile.mkdtemp()
        self.tmp_test_src = tempfile.mkdtemp(dir=self.tmp_test_container)
        self.tmp_test_dst = f'{self.tmp_test_container}/test_replica_folder'

    def tearDown(self):
        shutil.rmtree(self.tmp_test_container)

    def test_source_argument_correct(self):
        """Tests that the source argument is passed successfully."""
        with patch.object(sys, 'argv', ['replica_manager.py', self.tmp_test_src, self.tmp_test_dst]):
            test_replica = Replica(sys.argv[1], sys.argv[2], 1)
            self.assertEqual(test_replica.src, self.tmp_test_src)

    def test_destination_argument_correct(self):
        """Tests that the destination argument is passed successfully."""
        replica_dir_path = f'{self.tmp_test_dst}/test_replica_folder'
        with patch.object(sys, 'argv', ['replica_manager.py', self.tmp_test_src, self.tmp_test_dst]):
            test_replica = Replica(sys.argv[1], sys.argv[2], 1)
            self.assertEqual(test_replica.dst, self.tmp_test_dst)


class TestFileOperationMethods(TestCase):
    """Test that the replica folder is updated after changes in source are made"""

    def setUp(self):
        self.tmp_test_container = tempfile.mkdtemp()
        self.tmp_test_src = tempfile.mkdtemp(dir=self.tmp_test_container)
        self.tmp_test_file = tempfile.mkstemp(dir=self.tmp_test_src)
        self.tmp_test_dst = f'{self.tmp_test_container}/test_replica_folder'

    def tearDown(self):
        shutil.rmtree(self.tmp_test_container)

    def test_replica_contains_new_files(self):
        """Tests that update replica method copies files added to the souce directory."""
        test_replica = Replica(self.tmp_test_src, self.tmp_test_dst, 1)
        self.assertEqual(len(os.listdir(self.tmp_test_dst)), 1)
        tmp_added_test_file = tempfile.mkstemp(dir=self.tmp_test_src)
        test_replica.update_replica()
        self.assertEqual(len(os.listdir(self.tmp_test_dst)), 2)

# TODO: add tests on copy, delete and file changed method
# TODO: test if logs are created and have relevant content


if __name__ == '__main__':
    unittest.main()
