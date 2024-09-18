import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from api.app import app, db

class BasicTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app
        cls.client= cls.app.test_client()
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        cls.app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
        cls.db=db
        cls.db.create_all()

    @classmethod
    def tearDownClass(cls):
        cls.db.session.remove()
        cls.db.drop_all()

    
    def test_signup(self):
        response = self.client.post('/api/users', json={'username':'testuser', 'password':'testpass'})
        self.assertEqual(response.status_code, 201)

    
    def test_login(self):
        response = self.client.post('/api/login', json={'username':'testuser', 'password':'testpass'})
        self.assertEqual(response.status_code, 200)
if __name__ == '__main__':
    unittest.main()