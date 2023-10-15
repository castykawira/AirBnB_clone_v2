#!/usr/bin/python3
"""file_storage.py test cases"""
import unittest
import json
import os
import models
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """FileStorage class test cases"""

    def setUp(self):
        """Environment set up"""
        self.storage = FileStorage()

    def tearDown(self):
        """Test clean up"""
        FileStorage._FileStorage__objects = {}

    def test_new_model_key_in_objects(self):
        """Checks for the 'model' key in the updated __objects attribute"""
        base_model = BaseModel()
        self.storage.new(base_model)
        model_key = 'BaseModel.' + base_model.id
        self.assertIn(model_key, self.storage.all())

    def test_equality_of_created_model_and_model_in_objects(self):
        """Check equality of created model with __objects attribute"""
        base_model = BaseModel()
        self.storage.new(base_model)
        model_key = 'BaseModel.' + base_model.id
        model_in_objects = self.storage.all()[model_key]
        self.assertEqual(base_model, model_in_objects)

    def test_all_method_returns_dictionary(self):
        """Verify if the 'all' method returns a dictionary"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_file_exists_after_save(self):
        """Verify file existence after using the save method"""
        base_model = BaseModel()
        self.storage.new(base_model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_ids_consistency_after_reload(self):
        """Check if saved models have the same IDs after reloading"""
        base_model = BaseModel()
        self.storage.new(base_model)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        model_key = 'BaseModel.' + base_model.id
        self.assertEqual(base_model.id, new_storage.all()[model_key].id)

    def test_inequality_of_updated_at_before_and_after_save(self):
        """Confirm inequality of 'updated_at' attribute before
        and after 'save' method"""
        base_model = BaseModel()
        self.storage.new(base_model)
        old_updated_at = base_model.updated_at
        self.storage.save()
        new_updated_at = base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)


if __name__ == '__main__':
    unittest.main()
