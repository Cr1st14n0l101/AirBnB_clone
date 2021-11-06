#!/usr/bin/python3
"""Module for test ModelBase"""
from models.base_model import BaseModel
import unittest
import time
from datetime import datetime
from unittest import mock
base_doc = BaseModel.__doc__


class TestBaseModel(unittest.TestCase):
    """Test Case For Base Model"""

    @mock.patch('models.storage')  # patch and bring the storage module
    def test_base_case(self, mock_storage):
        """test for the base case in BaseModel Class"""
        instance = BaseModel()
        self.assertEqual(type(instance), BaseModel)
        instance.name = "Cristian"
        instance.phone = 123456789
        type_attr = {
            "id": str,
            "updated_at": datetime,
            "created_at": datetime,
            "name": str,
            "phone": int
        }
        for attr, type_at in type_attr.items():
            with self.subTest(attr=attr, typ=type_at):
                self.assertIn(attr, instance.__dict__)
                self.assertIs(type(instance.__dict__[attr]), type_at)
            self.assertTrue(mock_storage.new_called)
            self.assertEqual(instance.name, "Cristian")
            self.assertEqual(instance.phone, 123456789)

    def test_time_data(self):
        """Test the datatime for the BaseModels Class, must be different"""
        tc_before = datetime.now()
        instance1 = BaseModel()
        tc_after = datetime.now()
        self.assertTrue(tc_before <= instance1.created_at <= tc_after)
        time.sleep(0.5)
        instance2 = BaseModel()
        self.assertEqual(instance1.created_at, instance1.updated_at)
        self.assertNotEqual(instance1.created_at, instance2.created_at)
        self.assertNotEqual(instance1.updated_at, instance2.updated_at)

    def test_uiid(self):
        """Test if the uuid is different for each class"""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)
        uuid = instance1.id
        with self.subTest(uuid=uuid):
            self.assertIs(type(uuid), str)

    def test_BaseModels_dictionary(self):
        """Test to dic method in base model"""
        instance = BaseModel()
        instance.name = "Cristian"
        instance.num = 95
        dict_inst = instance.to_dict()
        attribute = [
                        "id",
                        "created_at",
                        "updated_at",
                        "name",
                        "num",
                        "__class__"]
        self.assertCountEqual(dict_inst.keys(), attribute)
        self.assertEqual(dict_inst['__class__'], 'BaseModel')
        self.assertEqual(dict_inst['name'], "Cristian")
        self.assertEqual(dict_inst['num'], 95)

    def to_dict_value(self):
        """test that to dict return are correct or no"""
        time_f = "%Y-%m-%dT%H:%M:%S.%f"
        instance = BaseModel()
        dict_base = instance.to_dict()
        self.assertEqual(dict_base["__class__"], "BaseModel")
        self.assertEqual(type(dict_base["created_at"]), str)
        self.assertEqual(type(dict_base["updated_at"]), str)
        self.assertEqual(
                            dict_base["created_at"],
                            instance.created_at.strftime(time_f)
                                    )
        self.assertEqual(
                            dict_base["updated_at"],
                            instance.updated_at.strftime(time_f)
                                    )

    def test_str(self):
        """test str magic method"""
        instance = BaseModel()
        correct_str = "[BaseModel] ({}) {}".format(
                                                    instance.id,
                                                    instance.__dict__
                                                        )
        self.assertEqual(correct_str, str(instance))

    @mock.patch("models.storage")
    def test_save(self, mock_storage):
        """test save and update at is working and storage call save"""
        instance = BaseModel()
        old_value_created = instance.created_at
        old_value_update = instance.updated_at
        instance.save()
        new_value_created = instance.created_at
        new_value_updated = instance.updated_at
        self.assertNotEqual(old_value_update, new_value_updated)
        self.assertEqual(old_value_created, new_value_created)
        self.assertTrue(mock_storage.save.called)

    def test_save_with_time(self):
        """Tests the public instance method save()"""
        b = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        b.save()
        diff = b.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
