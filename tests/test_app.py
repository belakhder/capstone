import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from  starter.models import *
from starter.auth import AuthError, requires_auth
from  starter.app import setup_db,create_app
from dotenv import load_dotenv



load_dotenv()

class AccountTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.administrator_auth_header = {'Authorization': "Bearer"+" "
            + str(os.getenv('administrator_auth'))}
        self.customer_auth_header = {'Authorization': "Bearer"+" "
            + str(os.getenv('customer_auth'))}
        self.database_path = database_path
        setup_db(self.app, self.database_path)
        

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            db.app=self.app
            ma.app=self.app
            #create all tables
            self.db.create_all()
       
    
     

    def test_01_create_new_account(self):
        ''' account creation success '''
        response =self.client().post('/account', 
            json={
                "first_name":"my_first_name",
                "last_name":"my_last_name",
                "email":"my_email@live.com",
                "phone":"23852698"
                },
            headers = self.administrator_auth_header)
        data = json.loads(response.data)
        
        

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['created_account'])
        self.assertTrue(data['created_account']['first_name'])
        self.assertTrue(data['created_account']['last_name'])
        self.assertTrue(data['created_account']['email'])
        self.assertTrue(data['created_account']['phone'])
        self.assertEqual(data['created_account']['phone'],'23852698')
        self.assertEqual(data['created_account']['email'],'my_email@live.com')
        self.assertEqual(data['created_account']['first_name'],'my_first_name')
        self.assertEqual(data['created_account']['last_name'],'my_last_name')

    
    def test_03_400_create_new_account_non_valid_type(self):
        ''' creation account failure due to non valide type '''

        response =self.client().post('/account', 
            json={'first_name':2,
                "last_name":"last_name_account",
                "email":"my_email@live.com",
                "phone":"23852698"},
            headers = self.administrator_auth_header)

        data = json.loads(response.data)
        

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)

   
    def test_04_400_create_new_account_non_valid_lenght_40(self):
        '''creation account failure due to non valid lenght'''
        response =self.client().post('/account', 
            json={'first_name':"name_accountname_accountname_accountname_accountname",
                "last_name":"last_name_account"},
            headers = self.administrator_auth_header)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)

    def test_05_get_accounts(self):
        ''' test get all accounts'''
        response = self.client().get('/account',
            headers = self.administrator_auth_header)

        data = json.loads(response.data)

        

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['info_accounts'])
        self.assertTrue(data['number of subscribers'])

  
       

    def test_06_get_account(self):
        ''' test get one account'''
        response = self.client().get('/account/1',
            headers = self.administrator_auth_header)

        data = json.loads(response.data)

        

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['info_account'])

    def test_07_404_get_account(self):
        '''test get unexisting account'''
        response = self.client().get('/account/100',
        headers = self.administrator_auth_header)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(data['success'], False)

    def test_08_patch_account(self):
        '''test account update success'''
        response = self.client().patch('/account/1',
            json={"first_name":"my_first_name2","last_name":"my_last_name2"},
            headers = self.administrator_auth_header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['updated_account'])
        self.assertTrue(data['success'])
    def test_09_patch_account_non_valid_type(self):
        """test account update failure due to non_valid_type"""
        response = self.client().patch('/account/1',
        json={"first_name":"my_first_name2","last_name":2},
            headers = self.administrator_auth_header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)

    def test_21_delete_account(self):
        ''' test delete account success'''
        response = self.client().delete('/account/1',
            headers = self.administrator_auth_header)

        data = json.loads(response.data)

        

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_id'],1)

    def test_22_delete_deleted_account(self):
        '''test delete deleted account'''
        response = self.client().delete('/account/1',
            headers = self.administrator_auth_header)
        

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(data['success'], False)

    def test_02_create_new_address(self):
        '''test creation address success '''
       
        response =self.client().post('/address', 
            json={"city":"city",
            "postal_code":2000,
            "country":"country",
            "account_id":1,
            "state":"state"
            },
            headers = self.administrator_auth_header)
            
        data = json.loads(response.data)

        

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['created_address'])
        self.assertTrue(data['created_address']['city'])
        self.assertTrue(data['created_address']['postal_code'])
        self.assertTrue(data['created_address']['country'])
        self.assertTrue(data['created_address']['state'])
        self.assertEqual(data['created_address']['city'],'city')
        self.assertEqual(data['created_address']['account_id'],1)
        self.assertEqual(data['created_address']['state'],'state')
    
    
    def test_10_400_create_new_address_non_valid_type(self):
        '''test creation address failure due due to non valid type '''
        
        response =self.client().post('/address', 
            json={"city":2,
            "postal_code":2000,
            "country":"country",
            "account_id":1,
            "state":"state"
            },
            headers = self.administrator_auth_header)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)


    def test_11_get_address(self):
        ''' test get all addresses'''
        response = self.client().get('/address',
            headers = self.administrator_auth_header)
        

        data = json.loads(response.data)

        

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['info_addresses'])
        self.assertTrue(data['number of addreses'])
    

    def test_12_get_address(self):
        '''test get one address'''
        address=Address.query.filter_by(account_id=1).one_or_none()
        response = self.client().get('/address/{}'.format(address.id),
            headers = self.administrator_auth_header)


        data = json.loads(response.data)

        

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['info_address'])

    def test_13_404_get_address(self):
        '''test get unexisting address'''
        response = self.client().get('/address/100',
            headers = self.administrator_auth_header)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(data['success'], False)

    def test_14_patch_address(self):

        """test address update success"""

        address=Address.query.filter_by(account_id=1).one_or_none()
        response = self.client().patch('/address/{}'.format(address.id),
            json={"first_name":"my_first_name2","last_name":"my_last_name2"},
            headers = self.administrator_auth_header)
        data = json.loads(response.data)

        
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['updated_address'])
        self.assertTrue(data['success'])
    

    def test_15_patch_address_non_valid_type(self):

        """test address update failure due to non_valid_type"""
        address=Address.query.filter_by(account_id=1).one_or_none()
    
        response = self.client().patch('/address/{}'.format(address.id),json={
            "city":2,
            "postal_code":2002,
            "country":"country2",
            "account_id":1,
            "state":"state"
            },
            headers = self.administrator_auth_header)
        data = json.loads(response.data)

     
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)


    def test_17_delete_account_without_permission(self):
        ''' test delete address without deletion permission '''
        
        response = self.client().delete('/account/1',
            headers = self.customer_auth_header)

        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['message'], 'Permission not found.')
        self.assertEqual(data['success'], False)
    def test_18_delete_account_without_authorization(self):
        '''test delete account without authorisation'''
        response = self.client().delete('/account/1')

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['message'], 'Authorization header is expected.')
        self.assertEqual(data['success'], False)

    def test_19_delete_address(self):
        ''' test deletion address success'''
        address=Address.query.filter_by(account_id=1).one_or_none()
        response = self.client().delete('/address/{}'.format(address.id),
            headers = self.administrator_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_id'],address.id)

    def test_20_delete_unexisting_address(self):
        '''test delete unexisting address'''
        response = self.client().delete('/address/1',
            headers = self.administrator_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(data['success'], False)


    db.drop_all()

    

if __name__ == "__main__":
    unittest.main()