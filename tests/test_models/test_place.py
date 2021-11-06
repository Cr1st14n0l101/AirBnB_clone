#!/usr/bin/python3
"""Test for class Place"""
from datetime import datetime
from typing import List
import unittest
from unittest.case import TestCase
from models.base_model import BaseModel
from models.place import Place
from models.city import City
from models.user import User


class TestPlace(unittest.TestCase):
    """All test to class Place"""

    def test_00_type_instances(self):
        """test the class type"""
        new_Place = Place()
        self.assertIsInstance(new_Place, Place)
        self.assertIsInstance(new_Place, BaseModel)
        new_city = City()
        self.assertIsInstance(new_city, City)
        self.assertIsInstance(new_city, BaseModel)
        new_user = User()
        self.assertIsInstance(new_user, User)
        self.assertIsInstance(new_user, BaseModel)

    def test_00_type_not_instances(self):
        """test for the instance datatype"""
        new_Place = Place()
        self.assertNotIsInstance(new_Place, list)
        self.assertNotIsInstance(new_Place, dict)
        self.assertNotIsInstance(new_Place, tuple)
        self.assertNotIsInstance(new_Place, str)

    def test_01_types(self):
        """test the type for the attributes of a object"""
        new_Place = Place()
        self.assertEqual(type(new_Place.id), str)
        self.assertEqual(type(new_Place.city_id), str)
        self.assertEqual(type(new_Place.user_id), str)
        self.assertEqual(type(new_Place.name), str)
        self.assertEqual(type(new_Place.description), str)
        self.assertEqual(type(new_Place.number_rooms), int)
        self.assertEqual(type(new_Place.number_bathrooms), int)
        self.assertEqual(type(new_Place.max_guest), int)
        self.assertEqual(type(new_Place.price_by_night), int)
        self.assertEqual(type(new_Place.latitude), float)
        self.assertEqual(type(new_Place.longitude), float)
        self.assertEqual(type(new_Place.amenity_ids), list)
        self.assertEqual(type(new_Place.created_at), datetime)
        self.assertEqual(type(new_Place.updated_at), datetime)
        self.assertEqual(type(new_Place.to_dict()['__class__']), str)
        self.assertEqual(new_Place.to_dict()['__class__'], "Place")
        self.assertIsInstance(new_Place.to_dict(), dict)

        new_dict = new_Place.to_dict()
        self.assertNotEqual(new_dict, new_Place.__dict__)

    def test_02_has_attributes(self):
        """test that verify if has a object"""
        new_Place = Place()
        self.assertTrue(hasattr(new_Place, "id"))
        self.assertTrue(hasattr(new_Place, "city_id"))
        self.assertTrue(hasattr(new_Place, "user_id"))
        self.assertTrue(hasattr(new_Place, "name"))
        self.assertTrue(hasattr(new_Place, "description"))
        self.assertTrue(hasattr(new_Place, "number_rooms"))
        self.assertTrue(hasattr(new_Place, "number_bathrooms"))
        self.assertTrue(hasattr(new_Place, "max_guest"))
        self.assertTrue(hasattr(new_Place, "price_by_night"))
        self.assertTrue(hasattr(new_Place, "latitude"))
        self.assertTrue(hasattr(new_Place, "longitude"))
        self.assertTrue(hasattr(new_Place, "amenity_ids"))
        self.assertTrue(hasattr(new_Place, "created_at"))
        self.assertTrue(hasattr(new_Place, "updated_at"))
        new_Place.other = "etc"
        self.assertTrue(hasattr(new_Place, "other"))

    def test_02_no_has_attributes(self):
        """test that verify if hasn't a object"""
        new_Place2 = Place()
        self.assertTrue(hasattr(new_Place2, "name"))

    def test_03_object_dict(self):
        """
            test for verify the creation of attribute
            for a object in his dictionary representation
        """
        new_obj_dict_city = {
            "id": "1b33cf03-2759-48c2-a2f1-fa99021669e7",
            "created_at": "2021-11-05T11:14:41.993355",
            "updated_at": "2021-11-05T11:14:41.993399",
            "__class__": "City"
        }
        new_obj_city = City(**new_obj_dict_city)

        new_obj_dict_user = {
            "id": "1b33cf03-2759-48c2-a2f1-fa99021669e8",
            "created_at": "2021-11-05T11:14:41.993355",
            "updated_at": "2021-11-05T11:14:41.993399",
            "__class__": "User"
        }
        new_obj_city = City(**new_obj_dict_user)


        new_obj_dict = {
            "id": "1b33cf03-2759-48c2-a2f1-fa99021669e9",
            "created_at": "2021-11-05T11:14:41.993355",
            "updated_at": "2021-11-05T11:14:41.993399",
            "city_id": "1b33cf03-2759-48c2-a2f1-fa99021669e7",
            "user_id": "1b33cf03-2759-48c2-a2f1-fa99021669e8",
            "name": "Place",
            "description": "description place",
            "number_rooms": 5,
            "number_bathrooms": 2,
            "max_guest": 8,
            "price_by_night": 1500,
            "latitude": 12.5,
            "longitude": 40.3,
            "amenity_ids": [],
            "__class__": "Place"
        }
        new_obj = Place(**new_obj_dict)
        self.assertIsInstance(new_obj, Place)
        self.assertIsInstance(new_obj, BaseModel)
        self.assertTrue(hasattr(new_obj, "id"))
        self.assertTrue(hasattr(new_obj, "city_id"))
        self.assertTrue(hasattr(new_obj, "user_id"))
        self.assertTrue(hasattr(new_obj, "name"))
        self.assertTrue(hasattr(new_obj, "description"))
        self.assertTrue(hasattr(new_obj, "number_rooms"))
        self.assertTrue(hasattr(new_obj, "number_bathrooms"))
        self.assertTrue(hasattr(new_obj, "max_guest"))
        self.assertTrue(hasattr(new_obj, "price_by_night"))
        self.assertTrue(hasattr(new_obj, "latitude"))
        self.assertTrue(hasattr(new_obj, "longitude"))
        self.assertTrue(hasattr(new_obj, "amenity_ids"))
        self.assertTrue(hasattr(new_obj, "created_at"))
        self.assertTrue(hasattr(new_obj, "updated_at"))
        self.assertEqual(new_obj.id, "1b33cf03-2759-48c2-a2f1-fa99021669e9")
        self.assertEqual(new_obj.city_id, "1b33cf03-2759-48c2-a2f1-fa99021669e7")
        self.assertEqual(new_obj.user_id, "1b33cf03-2759-48c2-a2f1-fa99021669e8")
        self.assertEqual(new_obj.created_at, datetime(
            2021, 11, 5, 11, 14, 41, 993355))
        self.assertEqual(new_obj.updated_at, datetime(
            2021, 11, 5, 11, 14, 41, 993399))
        self.assertEqual(type(new_obj.id), str)
        self.assertEqual(type(new_obj.city_id), str)
        self.assertEqual(type(new_obj.user_id), str)
        self.assertEqual(type(new_obj.name), str)
        self.assertEqual(type(new_obj.description), str)
        self.assertEqual(type(new_obj.number_rooms), int)
        self.assertEqual(type(new_obj.number_bathrooms), int)
        self.assertEqual(type(new_obj.max_guest), int)
        self.assertEqual(type(new_obj.price_by_night), int)
        self.assertEqual(type(new_obj.latitude), float)
        self.assertEqual(type(new_obj.longitude), float)
        self.assertEqual(type(new_obj.amenity_ids), list)
        self.assertEqual(type(new_obj.created_at), datetime)
        self.assertEqual(type(new_obj.updated_at), datetime)
        self.assertEqual(type(new_obj.to_dict()['__class__']), str)

    def test_04_save_success(self):
        """test for verifiy the file saved"""
        new_obj = Place()
        date_update = new_obj.updated_at
        new_obj.save()
        self.assertNotEqual(date_update, new_obj.updated_at)
        self.assertEqual(type(new_obj.updated_at), datetime)

    def test_05_errors(self):
        """test that verify the errors"""
        new_Place = Place()
        with self.assertRaises(TypeError):
            list(new_Place)
        with self.assertRaises(TypeError):
            dict(new_Place)
        with self.assertRaises(KeyError):
            print(new_Place.__dict__["hola"])
        with self.assertRaises(KeyError):
            print(new_Place.__dict__["hola"])
        with self.assertRaises(TypeError):
            new_Place.__str__["hola"]
        with self.assertRaises(TypeError):
            new_Place["hola"]
