import unittest
import os
import json
from instance import app_config
from app import app, db
from pprint import pprint


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        """initial test. ensure flask was set up correctly"""
        client = app.test_client(self)
        response = client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


class RoutesTestCase(unittest.TestCase):
    """unit test for all the routes"""

    def setUp(self):
        app.config.from_object(app_config["testing"])
        self.client = app.test_client()
        self.client_data = {'name': 'britecore'}
        self.production_area = {'name': 'software'}
        self.feature_request = {'title': 'Send email notification',
                                'description': 'the system should send email when an action is taken',
                                'client_id': 1,
                                'priority': 1,
                                'production_area_id': 1,
                                'target_date': '2018-11-26'}
        # binds the app to the current context
        with app.app_context():
            # create all tables
            db.create_all()

    # tests here


    def test_client_creation(self):
        """Test API can create a client (POST request)"""
        res = self.client.post('api/clients', data=self.client_data)
        self.assertEqual(res.status_code, 201)
        self.assertIn('britecore', str(res.data))

    def test_api_can_get_all_clients(self):
        """Test API can get a client (GET request)."""
        res = self.client.post('api/clients', data=self.client_data)
        self.assertEqual(res.status_code, 201)
        res = self.client.get('api/clients')
        self.assertEqual(res.status_code, 200)
        self.assertIn('britecore', str(res.data))

    def test_client_creation(self):
        """Test API can create a client (POST request)"""
        res = self.client.post('api/production-areas', data=self.production_area)
        self.assertEqual(res.status_code, 201)
        self.assertIn('software', str(res.data))


    def test_feature_request_creation(self):
        """Test API can create a feature request (POST request)"""
        res = self.client.post('api/clients', data=self.client_data)
        self.assertEqual(res.status_code, 201)
        res = self.client.post('api/production-areas', data=self.production_area)
        self.assertEqual(res.status_code, 201)
        res = self.client.post('api/feature-requests', data=self.feature_request)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Send email notification', str(res.data))


    def test_get_all_feature_request(self):
        """Test API can create a feature request (POST request)"""
        res = self.client.post('api/clients', data=self.client_data)
        self.assertEqual(res.status_code, 201)
        res = self.client.post('api/production-areas', data=self.production_area)
        self.assertEqual(res.status_code, 201)
        res = self.client.post('api/feature-requests', data=self.feature_request)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Send email notification', str(res.data))
        res = self.client.get('api/feature-requests')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Send email notification', str(res.data))


    def test_feature_request_delete(self):
        """Test API can create a feature request (POST request)"""
        res = self.client.post('api/clients', data=self.client_data)
        self.assertEqual(res.status_code, 201)
        res = self.client.post('api/production-areas', data=self.production_area)
        self.assertEqual(res.status_code, 201)
        res = self.client.post('api/feature-requests', data=self.feature_request)
        self.assertEqual(res.status_code, 201)
        data = json.loads(res.data.decode('utf-8').replace("'", "\""))
        res = self.client.delete('/api/feature-requests/' + str(data['id']))
        self.assertEqual(res.status_code, 204)







    def tearDown(self):
        with app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()




if __name__ == '__main__':
    unittest.main()