import unittest
import os
import json
from instance import app_config
from app import app, db
from pprint import pprint


class RoutesTestCase(unittest.TestCase):
    """unit test for all api the routes"""

    def test_index_page(self):
        """unit test the index page route"""
        client = app.test_client(self)
        response = client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_creat_page(self):
        """unit test the create feature page"""
        client = app.test_client(self)
        response = client.get('/feature-requests/create', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        app.config.from_object(app_config["testing"])
        self.client = app.test_client()
        self.client_data = {'name': 'britecore'}
        self.production_area = {'name': 'software'}
        self.feature_request = {'title': 'Send email notification',
                                'description': 'the system should send email when an action is taken',
                                'client_id': 1,
                                'priority': 1,
                                'product_area_id': 1,
                                'target_date': '2018-11-26'}
        self.update_feature_request = {'title': 'check notification',
                                'description': 'the system should send email when an action is taken',
                                'client_id': 1,
                                'priority': 2,
                                'product_area_id': 1,
                                'target_date': '2018-12-07'}
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
        """Test API can get all client (GET request)."""
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
        """Test API can get all feature request (POST request)"""
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


    def test_feature_request_update(self):
        """Test API can update a feature request (POST request)"""
        res = self.client.post('api/clients', data=self.client_data)
        self.assertEqual(res.status_code, 201)
        res = self.client.post('api/production-areas', data=self.production_area)
        self.assertEqual(res.status_code, 201)
        res = self.client.post('api/feature-requests', data=self.feature_request)
        self.assertEqual(res.status_code, 201)
        data = json.loads(res.data.decode('utf-8').replace("'", "\""))
        res = self.client.put('api/feature-requests/' + str(data['id']), data=self.update_feature_request)
        self.assertEqual(res.status_code, 200)
        self.assertIn('check notification', str(res.data))



    def test_feature_request_delete(self):
        """Test API can delete a feature request (POST request)"""
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