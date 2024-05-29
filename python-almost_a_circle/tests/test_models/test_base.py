import json, os, unittest, sys
from models.base import Base
from models.rectangle import Rectangle
"""unit test for base"""


class BaseTest(unittest.TestCase):
    def setUp(self):
        """set up"""
        Base.__Base__nb_objects = 0

    def test_init(self):
        """testing init"""
        base_class = Base()
        self.assertEqual(base_class.id, 1)

    def test_to_json_string(self):
        """testing from_json_string"""
        self.assertEqual(Base.to_json_string('[{"id": 1}]'), [{"id": 1}])
        self.assertEqual(Base.to_json_string(''), [])
        self.assertEqual(Base.to_json_string(None), [])
    
    