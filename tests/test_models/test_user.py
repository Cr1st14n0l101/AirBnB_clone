#!/usr/bin/python3
"""Test for class User"""

from datetime import datetime
from typing import List
import unittest
from unittest.case import TestCase
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """All test to class User"""
    def test_00_type_instances(self):
        """test the class type"""
        new_user = User()
        self.assertIsInstance(new_user, User)
        self.assertIsInstance(new_user, BaseModel)

    def test_00_type_not_instances(self):
        """test for the instance datatype"""
        new_user = User()
        self.assertNotIsInstance(new_user, list)
        self.assertNotIsInstance(new_user, dict)
        self.assertNotIsInstance(new_user, tuple)
        self.assertNotIsInstance(new_user, str)

    def test_01_types(self):
        """test the type for the attributes of a object"""
        new_user = User()
        self.assertEqual(type(new_user.id), str)
        self.assertEqual(type(new_user.created_at), datetime)
        self.assertEqual(type(new_user.updated_at), datetime)
        self.assertEqual(type(new_user.to_dict()['__class__']), str)
        self.assertEqual(new_user.to_dict()['__class__'], "User")
        self.assertIsInstance(new_user.to_dict(), dict)

        new_dict = new_user.to_dict()
        self.assertNotEqual(new_dict, new_user.__dict__)

    def test_02_has_attributes(self):
        """test that verify if has a object"""
        new_user = User()
        self.assertTrue(hasattr(new_user, "id"))
        self.assertTrue(hasattr(new_user, "created_at"))
        self.assertTrue(hasattr(new_user, "updated_at"))
        new_user.first_name = "pedro"
        new_user.last_name = "pedralta"
        new_user.email = "email@gmail.com"
        new_user.password = "1234"
        self.assertTrue(hasattr(new_user, "first_name"))
        self.assertTrue(hasattr(new_user, "last_name"))
        self.assertTrue(hasattr(new_user, "email"))
        self.assertTrue(hasattr(new_user, "password"))

    def test_02_no_has_attributes(self):
        """test that verify if hasn't a object"""
        new_user2 = User()
        self.assertTrue(hasattr(new_user2, "first_name"))
        self.assertTrue(hasattr(new_user2, "last_name"))
        self.assertTrue(hasattr(new_user2, "email"))
        self.assertTrue(hasattr(new_user2, "password"))

    def test_03_object_dict(self):
        """
            test for verify the creation of attribute 
            for a object in his dictionary representation
        """
        new_obj_dict = {
            "id": "1b33cf03-2759-48c2-a2f1-fa99021669e9",
            "created_at": "2021-11-05T11:14:41.993355",
            "updated_at": "2021-11-05T11:14:41.993399",
            "__class__": "User",
            "first_name": "Pedro",
            "last_name": "Pedralta",
            "password": "1234",
            "email": "email@gmail.com"
        }
        new_obj = User(**new_obj_dict)
        self.assertIsInstance(new_obj, User)
        self.assertIsInstance(new_obj, BaseModel)
        self.assertTrue(hasattr(new_obj, "id"))
        self.assertTrue(hasattr(new_obj, "created_at"))
        self.assertTrue(hasattr(new_obj, "updated_at"))
        self.assertTrue(hasattr(new_obj, "first_name"))
        self.assertTrue(hasattr(new_obj, "last_name"))
        self.assertTrue(hasattr(new_obj, "email"))
        self.assertTrue(hasattr(new_obj, "password"))
        self.assertTrue(hasattr(new_obj, "__class__"))
        self.assertEqual(new_obj.id, "1b33cf03-2759-48c2-a2f1-fa99021669e9")
        self.assertEqual(new_obj.created_at, datetime(
            2021, 11, 5, 11, 14, 41, 993355))
        self.assertEqual(new_obj.updated_at, datetime(
            2021, 11, 5, 11, 14, 41, 993399))
        self.assertEqual(new_obj.first_name, "Pedro")
        self.assertEqual(new_obj.email, "email@gmail.com")
        self.assertEqual(new_obj.password, "1234")
        self.assertEqual(new_obj.last_name, "Pedralta")
        self.assertEqual(type(new_obj.id), str)
        self.assertEqual(type(new_obj.created_at), datetime)
        self.assertEqual(type(new_obj.updated_at), datetime)
        self.assertEqual(type(new_obj.first_name), str)
        self.assertEqual(type(new_obj.email), str)
        self.assertEqual(type(new_obj.password), str)
        self.assertEqual(type(new_obj.last_name), str)
        new_obj.password = 123456
        self.assertEqual(type(new_obj.password), int)
        self.assertEqual(type(new_obj.to_dict()['__class__']), str)

    def test_04_save_success(self):
        """test for verifiy the file saved"""
        new_obj = User()
        date_update = new_obj.updated_at
        new_obj.save()
        self.assertNotEqual(date_update, new_obj.updated_at)
        self.assertEqual(type(new_obj.updated_at), datetime)

    def test_05_errors(self):
        """test that verify the errors"""
        new_user = User()
        with self.assertRaises(TypeError):
            list(new_user)
        with self.assertRaises(TypeError):
            dict(new_user)
        with self.assertRaises(KeyError):
            print(new_user.__dict__["hola"])
        with self.assertRaises(KeyError):
            print(new_user.__dict__["hola"])
        with self.assertRaises(TypeError):
            new_user.__str__["hola"]
        with self.assertRaises(TypeError):
            new_user["hola"]
