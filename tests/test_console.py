#!/usr/bin/python3
""" Module for testing console"""
import unittest
import os
import io
import sys
import json
from console import HBNBCommand as hbnb


class ColsoleTests(unittest.TestCase):
    """ Module for testing console"""

    def test_kwargs_create(self):
        """ """
        console = hbnb()
        captured_output = io.StringIO()
        sys.stdout = captured_output

        obj_id = console.onecmd('create City name="NAME"')
        sys.stdout = sys.__stdout__

        with open('file.json', encoding='UTF-8') as file_obj:
            json_dict = json.load(file_obj)

            for key, value in json_dict.items():
                obj_key = 'City.' + str(obj_id)
                if key == obj_key:
                    self.assertTrue(value['name'] == 'NAME')
