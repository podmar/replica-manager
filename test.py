"""
Tests for the replica manager.
"""

from unittest import TestCase
from unittest.mock import patch
import shutil
import tempfile
import os
import sys

from replica_manager import Replica


class TestReplicaCreated(TestCase):
    """Test that a replica of a given folder is created."""

    def setUp(self):
        self.tmp_test_container = tempfile.mkdtemp()
        self.tmp_test_src = tempfile.mkdtemp(dir=self.tmp_test_container)
        self.tmp_test_file = tempfile.mkstemp(dir=self.tmp_test_src)
        self.tmp_test_dst = tempfile.mkdtemp(dir=self.tmp_test_container)

    def tearDown(self):
        shutil.rmtree(self.tmp_test_container)

    def test_replica_folder_created_success(self):
        """Tests that a copy of the source folder is created in the destination directory"""
        replica_dir_path = f'{self.tmp_test_dst}/test_replica_folder'
        test_replica = Replica(self.tmp_test_src, replica_dir_path)
        self.assertEqual(len(os.listdir(self.tmp_test_dst)), 1)

    def test_replica_folder_contains_files(self):
        """Tests that replica folder contains original files from the source folder"""
        replica_dir_path = f'{self.tmp_test_dst}/test_replica_folder'
        test_replica = Replica(self.tmp_test_src, replica_dir_path)
        self.assertEqual(len(os.listdir(replica_dir_path)), 1)


class TestCliArguments(TestCase):
    """Test that CLI arguments can be passed successfully."""

    def setUp(self):
        self.tmp_test_container = tempfile.mkdtemp()
        self.tmp_test_src = tempfile.mkdtemp(dir=self.tmp_test_container)
        self.tmp_test_dst = tempfile.mkdtemp(dir=self.tmp_test_container)

    def tearDown(self):
        shutil.rmtree(self.tmp_test_container)

    def test_source_argument_correct(self):
        replica_dir_path = f'{self.tmp_test_dst}/test_replica_folder'
        with patch.object(sys, 'argv', ['replica_manager.py', self.tmp_test_src, replica_dir_path]):
            test_replica = Replica(sys.argv[1], sys.argv[2])
            self.assertEqual(test_replica.src, self.tmp_test_src)

    def test_destination_argument_correct(self):
        replica_dir_path = f'{self.tmp_test_dst}/test_replica_folder'
        with patch.object(sys, 'argv', ['replica_manager.py', self.tmp_test_src, replica_dir_path]):
            test_replica = Replica(sys.argv[1], sys.argv[2])
            self.assertEqual(test_replica.dst, replica_dir_path)


if __name__ == '__main__':
    unittest.main()
