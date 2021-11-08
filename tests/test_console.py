#!/usr/bin/python3
"""TestConsole module"""
import unittest
import sys
from io import StringIO
import re
from unittest.mock import patch
from console import HBNBCommand
from models import *
import random


class TestConsole(unittest.TestCase):
    """
        TestConsole class
    """
    classes = ["User", "State", "Review", "Place", "City", "BaseModel"]

    def test_help_console_cmd(self):
        """
        Test <help>
        """
        expected = """
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
\n"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertEqual(expected, f.getvalue())

    def test_create_console_cmd_should_fail_without_clsname(self):
        """
        Test <create>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            expected = "** class name missing **\n"
            self.assertEqual(expected, f.getvalue())

    def test_create_console_cmd_should_fail_with_wrong_clsname(self):
        """
        Test <create WrongClsName>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create WrongClsName")
            expected = "** class doesn't exist **\n"
            self.assertEqual(expected, f.getvalue())

    def test_create_console_cmd_should_work_properly(self):
        """
        Test <create BaseModel>
        """
        for className in TestConsole.classes:
            instance_before = len(storage.all())
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(className))
                instance_after = len(storage.all())
                key_id = className + "." + f.getvalue().strip("\n")
                self.assertIn(key_id, storage.all().keys())
                self.assertEqual(instance_before + 1, instance_after)

    def test_show_console_cmd_should_fails_without_clsname(self):
        """
        Tests <show>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            expected = "** class name missing **\n"
            self.assertEqual(expected, f.getvalue())

    def test_show_console_cmd_should_fail_with_wrong_clsname(self):
        """
        Test <show WrongClsName>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show WrongClsName")
            expected = "** class doesn't exist **\n"
            self.assertEqual(expected, f.getvalue())

    def test_show_console_cmd_should_fail_without_id(self):
        """
        Test <show BaseModel>
        """
        for className in TestConsole.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show {}".format(className))
                expected = "** instance id missing **\n"
                self.assertEqual(expected, f.getvalue())

    def test_show_console_cmd_should_fail_with_wrong_id(self):
        """
        Test <show BaseModel 1212121212>
        """
        for className in TestConsole.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show {} 1212121212".format(className))
                expected = "** no instance found **\n"
                self.assertEqual(expected, f.getvalue())

    def test_destroy_console_cmd_should_fails_without_clsname(self):
        """
        Tests <destroy>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            expected = "** class name missing **\n"
            self.assertEqual(expected, f.getvalue())

    def test_destroy_console_cmd_should_fail_with_wrong_clsname(self):
        """
        Test <destroy WrongClsName>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy WrongClsName")
            expected = "** class doesn't exist **\n"
            self.assertEqual(expected, f.getvalue())

    def test_destroy_console_cmd_should_fail_without_id(self):
        """
        Test <destroy BaseModel>
        """
        for className in TestConsole.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy {}".format(className))
                expected = "** instance id missing **\n"
                self.assertEqual(expected, f.getvalue())

    def test_destroy_console_cmd_should_fail_with_wrong_id(self):
        """
        Test <destroy BaseModel 1212121212>
        """
        for className in TestConsole.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy {} 12121212".format(className))
                expected = "** no instance found **\n"
                self.assertEqual(expected, f.getvalue())

    def test_destroy_console_cmd_work_as_expected(self):
        """
        Test <destroy BaseModel id>
        objects = storage.all()
        length_before = len(objects)
        while length_before > 0:
            key = random.choice(list(objects.keys()))
            id = key.split(".")[1]
            className = key.split(".")[0]
            HBNBCommand().onecmd("destroy {} {}".format(className, id))
            length_after = len(objects)
            self.assertEqual(length_before - 1, length_after)
            self.assertNotIn(key, storage.all().keys())
            length_before = length_after
        """

    def test_all_console_cmd_should_fail_with_wrong_clsname(self):
        """
        Test <all WrongClsName>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all WrongClsName")
            expected = "** class doesn't exist **\n"
            self.assertEqual(expected, f.getvalue())

    def test_update_console_cmd_should_fails_without_clsname(self):
        """
        Tests <update>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            expected = "** class name missing **\n"
            self.assertEqual(expected, f.getvalue())

    def test_update_console_cmd_should_fail_with_wrong_clsname(self):
        """
        Test <update WrongClsName>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update WrongClsName")
            expected = "** class doesn't exist **\n"
            self.assertEqual(expected, f.getvalue())

    def test_update_console_cmd_should_fail_without_id(self):
        """
        Test <update BaseModel>
        """
        for className in TestConsole.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update {}".format(className))
                expected = "** instance id missing **\n"
                self.assertEqual(expected, f.getvalue())

    def test_update_console_cmd_should_fail_with_wrong_id(self):
        """
        Test <update BaseModel 1212121212>
        """
        for className in TestConsole.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update {} 1212121".format(className))
                expected = "** no instance found **\n"
                self.assertEqual(expected, f.getvalue())
