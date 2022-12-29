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

    def test_replica_created_default_dst_success(self):
        """Tests that a copy of a folder is created in the same directory if no destination path is given."""
        test_replica = Replica(self.tmp_test_src)
        self.assertEqual(len(os.listdir(self.tmp_test_container)), 2)

    def test_replica_created_success(self):
        """Tests that a copy of a folder is created at the given destination path."""
        test_replica = Replica(self.tmp_test_src, self.tmp_test_dst)
        self.assertEqual(len(os.listdir(self.tmp_test_dst)),
                         len(os.listdir(self.tmp_test_src)))


class TestCliArguments(TestCase):
    """Test that CLI arguments can be passed successfully."""

    def setUp(self):
        self.tmp_test_container = tempfile.mkdtemp()
        self.tmp_test_src = tempfile.mkdtemp(dir=self.tmp_test_container)
        self.tmp_test_dst = tempfile.mkdtemp(dir=self.tmp_test_container)

    def tearDown(self):
        shutil.rmtree(self.tmp_test_container)

    def test_source_argument_correct(self):
        with patch.object(sys, 'argv', ['replica_manager.py', self.tmp_test_src]):
            test_replica = Replica(sys.argv[1])
            self.assertEqual(test_replica.src, self.tmp_test_src)

    def test_destination_argument_correct(self):
        with patch.object(sys, 'argv', ['replica_manager.py', self.tmp_test_src, self.tmp_test_dst]):
            test_replica = Replica(sys.argv[1], )
            self.assertEqual(test_replica.dst, self.tmp_test_dst)


if __name__ == '__main__':
    unittest.main()
