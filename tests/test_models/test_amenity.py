#!/usr/bin/python3
"""Test for class Amenity"""
from datetime import datetime
from typing import List
import unittest
from unittest.case import TestCase
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """All test to class Amenity"""

    def test_00_type_instances(self):
        """test the class type"""
        new_Amenity = Amenity()
        self.assertIsInstance(new_Amenity, Amenity)
        self.assertIsInstance(new_Amenity, BaseModel)

    def test_00_type_not_instances(self):
        """test for the instance datatype"""
        new_Amenity = Amenity()
        self.assertNotIsInstance(new_Amenity, list)
        self.assertNotIsInstance(new_Amenity, dict)
        self.assertNotIsInstance(new_Amenity, tuple)
        self.assertNotIsInstance(new_Amenity, str)

    def test_01_types(self):
        """test the type for the attributes of a object"""
        new_Amenity = Amenity()
        self.assertEqual(type(new_Amenity.id), str)
        self.assertEqual(type(new_Amenity.created_at), datetime)
        self.assertEqual(type(new_Amenity.updated_at), datetime)
        self.assertEqual(type(new_Amenity.to_dict()['__class__']), str)
        self.assertEqual(new_Amenity.to_dict()['__class__'], "Amenity")
        self.assertIsInstance(new_Amenity.to_dict(), dict)

        new_dict = new_Amenity.to_dict()
        self.assertNotEqual(new_dict, new_Amenity.__dict__)

    def test_02_has_attributes(self):
        """test that verify if has a object"""
        new_Amenity = Amenity()
        self.assertTrue(hasattr(new_Amenity, "id"))
        self.assertTrue(hasattr(new_Amenity, "created_at"))
        self.assertTrue(hasattr(new_Amenity, "updated_at"))
        new_Amenity.name = "cleaning"
        self.assertTrue(hasattr(new_Amenity, "name"))

    def test_02_no_has_attributes(self):
        """test that verify if hasn't a object"""
        new_Amenity2 = Amenity()
        self.assertTrue(hasattr(new_Amenity2, "name"))

    def test_03_object_dict(self):
        """
            test for verify the creation of attribute
            for a object in his dictionary representation
        """
        new_obj_dict = {
            "id": "1b33cf03-2759-48c2-a2f1-fa99021669e9",
            "created_at": "2021-11-05T11:14:41.993355",
            "updated_at": "2021-11-05T11:14:41.993399",
            "__class__": "Amenity",
            "name": "cleaning"
        }
        new_obj = Amenity(**new_obj_dict)
        self.assertIsInstance(new_obj, Amenity)
        self.assertIsInstance(new_obj, BaseModel)
        self.assertTrue(hasattr(new_obj, "id"))
        self.assertTrue(hasattr(new_obj, "created_at"))
        self.assertTrue(hasattr(new_obj, "updated_at"))
        self.assertTrue(hasattr(new_obj, "name"))
        self.assertEqual(new_obj.id, "1b33cf03-2759-48c2-a2f1-fa99021669e9")
        self.assertEqual(new_obj.created_at, datetime(
            2021, 11, 5, 11, 14, 41, 993355))
        self.assertEqual(new_obj.updated_at, datetime(
            2021, 11, 5, 11, 14, 41, 993399))
        self.assertEqual(new_obj.name, "cleaning")
        self.assertEqual(type(new_obj.id), str)
        self.assertEqual(type(new_obj.created_at), datetime)
        self.assertEqual(type(new_obj.updated_at), datetime)
        self.assertEqual(type(new_obj.name), str)
        self.assertEqual(type(new_obj.to_dict()['__class__']), str)

    def test_04_save_success(self):
        """test for verifiy the file saved"""
        new_obj = Amenity()
        date_update = new_obj.updated_at
        new_obj.save()
        self.assertNotEqual(date_update, new_obj.updated_at)
        self.assertEqual(type(new_obj.updated_at), datetime)

    def test_05_errors(self):
        """test that verify the errors"""
        new_Amenity = Amenity()
        with self.assertRaises(TypeError):
            list(new_Amenity)
        with self.assertRaises(TypeError):
            dict(new_Amenity)
        with self.assertRaises(KeyError):
            print(new_Amenity.__dict__["hola"])
        with self.assertRaises(KeyError):
            print(new_Amenity.__dict__["hola"])
        with self.assertRaises(TypeError):
            new_Amenity.__str__["hola"]
        with self.assertRaises(TypeError):
            new_Amenity["hola"]
