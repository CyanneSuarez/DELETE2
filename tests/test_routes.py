import unittest
from flask import Flask
from flask_testing import TestCase
from DELETE2 import create_app, db
from DELETE2.models import Product

class TestProductRoutes(TestCase):

    def create_app(self):
        app = create_app('testing')  # Ensure you have a testing configuration
        return app

    def setUp(self):
        db.create_all()
        self.product = Product(name="Test Product", description="This is a test product", price=9.99, stock=10)
        db.session.add(self.product)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_delete_product(self):
        # Perform a DELETE request to delete the product
        response = self.client.delete(f'/products/{self.product.id}')
        self.assertEqual(response.status_code, 200)

        # Verify the deletion
        deleted_product = Product.query.get(self.product.id)
        self.assertIsNone(deleted_product)

if __name__ == '__main__':
    unittest.main()
