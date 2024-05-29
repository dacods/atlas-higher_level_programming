from models.base import Base
import unittest
"""unit test for base"""


class BaseTest(unittest.TestCase):
    def setUp(self):
        """set up"""
        Base._Base__nb_objects = 0
        self.base = Base()

    def test_init(self):
        """testing init"""
        base_class = Base()
        self.assertEqual(base_class.id, 1)


if __name__ == '__main__':
    unittest.main()
