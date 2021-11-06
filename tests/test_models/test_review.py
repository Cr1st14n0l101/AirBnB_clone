#!/usr/bin/python3
"""Test for class Review"""
from datetime import datetime
from typing import List
import unittest
from unittest.case import TestCase
from models.base_model import BaseModel
from models.review import Review
from models.place import Place
from models.user import User


class TestReview(unittest.TestCase):
    """All test to class Review"""

    def test_00_type_instances(self):
        """test the class type"""
        new_Review = Review()
        self.assertIsInstance(new_Review, Review)
        self.assertIsInstance(new_Review, BaseModel)

    def test_00_type_not_instances(self):
        """test for the instance datatype"""
        new_Review = Review()
        self.assertNotIsInstance(new_Review, list)
        self.assertNotIsInstance(new_Review, dict)
        self.assertNotIsInstance(new_Review, tuple)
        self.assertNotIsInstance(new_Review, str)

    def test_01_types(self):
        """test the type for the attributes of a object"""
        new_Review = Review()
        self.assertEqual(type(new_Review.id), str)
        self.assertEqual(type(new_Review.created_at), datetime)
        self.assertEqual(type(new_Review.updated_at), datetime)
        self.assertEqual(type(new_Review.to_dict()['__class__']), str)
        self.assertEqual(new_Review.to_dict()['__class__'], "Review")
        self.assertIsInstance(new_Review.to_dict(), dict)

        new_dict = new_Review.to_dict()
        self.assertNotEqual(new_dict, new_Review.__dict__)

    def test_02_has_attributes(self):
        """test that verify if has a object"""
        new_Review = Review()
        self.assertTrue(hasattr(new_Review, "id"))
        self.assertTrue(hasattr(new_Review, "created_at"))
        self.assertTrue(hasattr(new_Review, "updated_at"))

    def test_03_object_dict(self):
        """
            test for verify the creation of attribute
            for a object in his dictionary representation
        """
        new_obj_dict = {
            "id": "1b33cf03-2759-48c2-a2f1-fa99021669e9",
            "created_at": "2021-11-05T11:14:41.993355",
            "updated_at": "2021-11-05T11:14:41.993399",
            "__class__": "Review",
        }
        new_obj = Review(**new_obj_dict)
        self.assertIsInstance(new_obj, Review)
        self.assertIsInstance(new_obj, BaseModel)
        self.assertTrue(hasattr(new_obj, "id"))
        self.assertTrue(hasattr(new_obj, "created_at"))
        self.assertTrue(hasattr(new_obj, "updated_at"))
        self.assertEqual(new_obj.id, "1b33cf03-2759-48c2-a2f1-fa99021669e9")
        self.assertEqual(new_obj.created_at, datetime(
            2021, 11, 5, 11, 14, 41, 993355))
        self.assertEqual(new_obj.updated_at, datetime(
            2021, 11, 5, 11, 14, 41, 993399))
        self.assertEqual(type(new_obj.id), str)
        self.assertEqual(type(new_obj.created_at), datetime)
        self.assertEqual(type(new_obj.updated_at), datetime)
        self.assertEqual(type(new_obj.to_dict()['__class__']), str)

    def test_04_save_success(self):
        """test for verifiy the file saved"""
        new_obj = Review()
        date_update = new_obj.updated_at
        new_obj.save()
        self.assertNotEqual(date_update, new_obj.updated_at)
        self.assertEqual(type(new_obj.updated_at), datetime)

    def test_05_errors(self):
        """test that verify the errors"""
        new_Review = Review()
        with self.assertRaises(TypeError):
            list(new_Review)
        with self.assertRaises(TypeError):
            dict(new_Review)
        with self.assertRaises(KeyError):
            print(new_Review.__dict__["hola"])
        with self.assertRaises(KeyError):
            print(new_Review.__dict__["hola"])
        with self.assertRaises(TypeError):
            new_Review.__str__["hola"]
        with self.assertRaises(TypeError):
            new_Review["hola"]
