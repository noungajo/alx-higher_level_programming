#!/usr/bin/python3
"""
JSON_module

Contains a function that returns an object (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Function that returns an object
    represented by a JSON string
    """
    return json.loads(my_str)
