#!/usr/bin/python3
"""Test for class City"""
from datetime import datetime
from typing import List
import unittest
from unittest.case import TestCase
from models.base_model import BaseModel
from models.city import City
from models.state import State


class TestCity(unittest.TestCase):
    """All test to class City"""

    def test_00_type_instances(self):
        """test the class type"""
        new_obj_dict = {
            "id": "1b33cf03-2759-48c2-a2f1-fa99021669e9",
            "created_at": "2021-11-05T11:14:41.993355",
            "updated_at": "2021-11-05T11:14:41.993399",
            "__class__": "State",
            "name": "Miami"
        }
        new_obj_state = State(**new_obj_dict)
        new_City = City()
        new_City.state_id = new_obj_state.id
        self.assertIsInstance(new_obj_state, State)
        self.assertIsInstance(new_obj_state, BaseModel)
        self.assertIsInstance(new_City, City)
        self.assertIsInstance(new_City, BaseModel)

    def test_00_type_not_instances(self):
        """test for the instance datatype"""
        new_City = City()
        self.assertNotIsInstance(new_City, list)
        self.assertNotIsInstance(new_City, dict)
        self.assertNotIsInstance(new_City, tuple)
        self.assertNotIsInstance(new_City, str)

    def test_01_types(self):
        """test the type for the attributes of a object"""
        new_City = City()
        self.assertEqual(type(new_City.id), str)
        self.assertEqual(type(new_City.created_at), datetime)
        self.assertEqual(type(new_City.updated_at), datetime)
        self.assertEqual(type(new_City.state_id), str)
        self.assertEqual(type(new_City.name), str)
        self.assertEqual(type(new_City.to_dict()['__class__']), str)
        self.assertEqual(new_City.to_dict()['__class__'], "City")
        self.assertIsInstance(new_City.to_dict(), dict)

        new_dict = new_City.to_dict()
        self.assertNotEqual(new_dict, new_City.__dict__)

    def test_02_has_attributes(self):
        """test that verify if has a object"""
        new_City = City()
        self.assertTrue(hasattr(new_City, "id"))
        self.assertTrue(hasattr(new_City, "created_at"))
        self.assertTrue(hasattr(new_City, "updated_at"))
        self.assertTrue(hasattr(new_City, "state_id"))
        self.assertTrue(hasattr(new_City, "name"))
        new_City.other = "ETC"
        self.assertTrue(hasattr(new_City, "other"))

    def test_02_no_has_attributes(self):
        """test that verify if hasn't a object"""
        new_City2 = City()
        self.assertTrue(hasattr(new_City2, "name"))

    def test_03_object_dict(self):
        """
            test for verify the creation of attribute
            for a object in his dictionary representation
        """
        new_obj_dict_state = {
            "id": "1b33cf03-2759-48c2-a2f1-fa9902166910",
            "created_at": "2021-11-05T11:14:41.993355",
            "updated_at": "2021-11-05T11:14:41.993399",
            "__class__": "State",
            "name": "Miami"
        }
        new_obj_state = State(**new_obj_dict_state)
        new_obj_dict = {
            "id": "1b33cf03-2759-48c2-a2f1-fa99021669e9",
            "created_at": "2021-11-05T11:14:41.993355",
            "updated_at": "2021-11-05T11:14:41.993399",
            "__class__": "City",
            "name": "New York"
        }
        new_obj = City(**new_obj_dict)
        new_obj.state_id = new_obj_state.id
        self.assertIsInstance(new_obj, City)
        self.assertIsInstance(new_obj, BaseModel)
        self.assertIsInstance(new_obj_state, State)
        self.assertIsInstance(new_obj_state, BaseModel)
        self.assertTrue(hasattr(new_obj, "id"))
        self.assertTrue(hasattr(new_obj, "created_at"))
        self.assertTrue(hasattr(new_obj, "updated_at"))
        self.assertTrue(hasattr(new_obj, "state_id"))
        self.assertTrue(hasattr(new_obj, "name"))
        self.assertEqual(new_obj.id, "1b33cf03-2759-48c2-a2f1-fa99021669e9")
        self.assertEqual(new_obj.state_id, "1b33cf03-2759-48c2-a2f1-fa9902166910")
        self.assertEqual(new_obj.created_at, datetime(
            2021, 11, 5, 11, 14, 41, 993355))
        self.assertEqual(new_obj.updated_at, datetime(
            2021, 11, 5, 11, 14, 41, 993399))
        self.assertEqual(new_obj.name, "New York")
        self.assertEqual(type(new_obj.id), str)
        self.assertEqual(type(new_obj.state_id), str)
        self.assertEqual(type(new_obj.created_at), datetime)
        self.assertEqual(type(new_obj.updated_at), datetime)
        self.assertEqual(type(new_obj.name), str)
        self.assertEqual(type(new_obj.to_dict()['__class__']), str)

    def test_04_save_success(self):
        """test for verifiy the file saved"""
        new_obj = City()
        date_update = new_obj.updated_at
        new_obj.save()
        self.assertNotEqual(date_update, new_obj.updated_at)
        self.assertEqual(type(new_obj.updated_at), datetime)

    def test_05_errors(self):
        """test that verify the errors"""
        new_City = City()
        with self.assertRaises(TypeError):
            list(new_City)
        with self.assertRaises(TypeError):
            dict(new_City)
        with self.assertRaises(KeyError):
            print(new_City.__dict__["hola"])
        with self.assertRaises(KeyError):
            print(new_City.__dict__["hola"])
        with self.assertRaises(TypeError):
            new_City.__str__["hola"]
        with self.assertRaises(TypeError):
            new_City["hola"]
