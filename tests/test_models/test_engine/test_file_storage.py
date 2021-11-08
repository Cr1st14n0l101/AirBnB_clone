#!/usr/bin/python3
"""Test for class FileStorage"""
from datetime import datetime
from typing import List
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """All test to class FileStorage"""

    def test_00_type_instances(self):
        """test the class type"""
        new_FileStorage = FileStorage()
        self.assertIsInstance(new_FileStorage, FileStorage)

    def test_00_type_not_instances(self):
        """test for the instance datatype"""
        new_FileStorage = FileStorage()
        self.assertNotIsInstance(new_FileStorage, list)
        self.assertNotIsInstance(new_FileStorage, dict)
        self.assertNotIsInstance(new_FileStorage, tuple)
        self.assertNotIsInstance(new_FileStorage, str)

    def test_05_errors(self):
        """test that verify the errors"""
        new_FileStorage = FileStorage()
        with self.assertRaises(TypeError):
            list(new_FileStorage)
        with self.assertRaises(TypeError):
            dict(new_FileStorage)
        with self.assertRaises(KeyError):
            print(new_FileStorage.__dict__["hola"])
        with self.assertRaises(KeyError):
            print(new_FileStorage.__dict__["hola"])
        with self.assertRaises(TypeError):
            new_FileStorage.__str__["hola"]
        with self.assertRaises(TypeError):
            new_FileStorage["hola"]
