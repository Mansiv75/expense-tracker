import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from api.app import app, db
from werkzeug.security import generate_password_hash
from api.models import User

class BasicTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app
        cls.client= cls.app.test_client()
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        cls.app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
        cls.db=db
        cls.app_context = cls.app.app_context()
        cls.app_context.push()

        with cls.app.app_context():
            cls.db = db
            cls.db.create_all()

            hashed_password = generate_password_hash('testpass')
            new_user = User(username='testuser', password=hashed_password)
            cls.db.session.add(new_user)
            cls.db.session.commit()    

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            cls.db.drop_all()
        cls.app_context.pop()

    
    def test_signup(self):
        response = self.client.post('/api/users', json={'username':'newuser', 'password':'newpass'})
        self.assertEqual(response.status_code, 201)

    
    def test_login(self):
        response = self.client.post('/api/login', json={'username':'testuser', 'password':'testpass'})
        print(response.json)  # Debug output
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)
if __name__ == '__main__':
    unittest.main()