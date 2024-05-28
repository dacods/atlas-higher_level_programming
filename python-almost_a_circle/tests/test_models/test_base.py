import json, os, unittest, sys
from models.base import Base
from models.rectangle import Rectangle
"""unit test for base"""


class BaseTest(unittest.TestCase):
    def setUp(self):
        Base.__Base__nb_objects = 0

    def test_init(self):
        base_class = Base()
        self.assertEqual(base_class.id, 1)
    
    def test_json_string(self):
        self.assertEqual(Base.from_json_string('["id": 1]'), [{"id": 1}])
        self.assertEqual(Base.from_json_string(''), [])
        self.assertEqual(Base.from_json_string(None), [])
    
    