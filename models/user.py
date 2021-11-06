#!/usr/bin/python3
"""Module for State class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for the User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
