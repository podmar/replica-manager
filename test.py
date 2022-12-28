"""
Tests for the replica manager
"""

from unittest import TestCase
import tempfile
import os

from replica_manager import create_replica


class TestReplicaCreated(TestCase):
    """Test that a replica of a given folder is created"""

    def test_replica_created_success(self):
        """Tests that a copy of a folder is created in the same directory"""
        with tempfile.TemporaryDirectory() as tmp_container_dir:
            tmp_source_dir = tempfile.mkdtemp(dir=tmp_container_dir)
            create_replica(tmp_source_dir)
            self.assertEqual(len(os.listdir(tmp_container_dir)), 2)
