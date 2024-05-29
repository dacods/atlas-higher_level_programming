#!/bin/usr/python3
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

if __name__ == '__main__':
    unittest.main()