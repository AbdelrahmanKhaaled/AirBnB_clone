#!/usr/bin/python3
'''Test Model.'''
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
        def test_init(self):
            mini_model = BaseModel()
            self.assertIsNotNone(mini_model.id)
            self.assertIsNotNone(mini_model.created_at)
            self.assertIsNotNone(mini_model.updated_at)

        def test_save(self):
            mini_model = BaseModel()
            self.assertNotEqual(mini_model.updated_at, mini_model.save())

        def test_to_dict(self):
            mini_model = BaseModel()
            mini_model_dict = mini_model.to_dict()
            self.assertIsInstance(mini_model_dict, dict)
            self.assertEqual(mini_model_dict["__class__"], 'BaseModel')
            self.assertEqual(mini_model_dict["id"], mini_model.id)
            self.assertEqual(mini_model_dict["created_at"], mini_model.created_at.isoformat())
            self.assertEqual(mini_model_dict["updated_at"], mini_model.updated_at.isoformat())

        def test_str(self):
            mini_model = BaseModel()
            self.assertEqual(mini_model.__str__(), "[BaseModel] ({}) {}".format(mini_model.id, mini_model.__dict__))

if __name__ == "__main__":
    unittest.main()
