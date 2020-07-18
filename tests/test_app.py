
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from  starter.models import *
from starter.auth import AuthError, requires_auth
from  starter.app import setup_db,create_app






administrator_auth_header = {
    'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ild2VHBoVG1FRkpwa0l1X2o4anJNaiJ9.eyJpc3MiOiJodHRwczovL2Rldi1lOHk1a3cwei51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwOWE0MzVhMWY2MDMwMDE5YjBhZDAyIiwiYXVkIjoiYWNjb3V0IiwiaWF0IjoxNTk1MDc5NzgwLCJleHAiOjE1OTUxNjYxODAsImF6cCI6InI0NW5HeFFsbzJGZzdxSWFIUlFEejdQTG1qMTNpUEQzIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWNjb3VudCIsImRlbGV0ZTphZGRyZXNzIiwiZ2V0OmFjY291bnQiLCJnZXQ6YWNjb3VudHMiLCJnZXQ6YWRkcmVzcyIsImdldDphZGRyZXNzZXMiLCJwYXRjaDphY2NvdW50IiwicGF0Y2ggYWRkcmVzcyIsInBvc3Q6YWNjb3VudCIsInBvc3Q6YWRkcmVzcyJdfQ.DbWTr5gOmcKXsk12cA1JMJqrUaktvDivhCDZH-wSRYg4tswcWUyFlSY6bEKjVrOX5ojp3pKosbGWuE4T5kijKUrhDnCeokcrmtQ5nn_hu7Jv07I6gNkhMjo2x9de5ITvxVj40Srg_Om6JrKEF0qMWnAnop4J7iAH4ki7mk9EB6nJLl2VpJeOyEc_z8OXaaaqD5NqGOQnhYz2D6QvYZLbt2saEVt3u0o8dahmXRV5O146ZOBl58LzgiN89N2QwPVZVW41TsE2yAOKSspaCqFLSzcuJ5DdEmQvsOnBYGjG6NswoTk656WnTL3Q6jQYYMfYGiIthDI2JgQL4N_vA2sQVw"
}

customer_auth_header = {
    'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ild2VHBoVG1FRkpwa0l1X2o4anJNaiJ9.eyJpc3MiOiJodHRwczovL2Rldi1lOHk1a3cwei51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwOWE0MzVhMWY2MDMwMDE5YjBhZDAyIiwiYXVkIjoiYWNjb3V0IiwiaWF0IjoxNTk1MDc5NjE5LCJleHAiOjE1OTUxNjYwMTksImF6cCI6InI0NW5HeFFsbzJGZzdxSWFIUlFEejdQTG1qMTNpUEQzIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWRkcmVzcyIsImdldDphY2NvdW50IiwiZ2V0OmFkZHJlc3MiLCJwYXRjaDphY2NvdW50IiwicGF0Y2ggYWRkcmVzcyIsInBvc3Q6YWNjb3VudCIsInBvc3Q6YWRkcmVzcyJdfQ.iK7oXfe6PR69O2tsQo78p7VB4vTACSRWrjXy-LENlu86V4olUqtJDMM4gmsSsfmy0oJEUt1UTsRLOI8wCPLUn474tg_cGEIuU_8AOcT5zTKAuofrUaz_lmybSWD8mntQOBA1QYHvrpofEci5Yu0IML-dsoqnpWPfK5sG4fo_aPMr4vsgdL9NMtLim8_MYsytZZF-KBrCNEDfP0MuTPpDafbMek4FOQuhJy6L1k8To1wDPMiuNbfJvXQ9vM6UhqSoYu-Hk-8i9ZIJwOpg0mxKEh5N0RxvP3GLGhNJq74z7XQRJ4KoGhq7nqOYT7a01E7ahoGOkflN-YtGc8Y0k_yNQw"
}








class AccountTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = database_path
        setup_db(self.app, self.database_path)


        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            db.app=self.app
            ma.app=self.app
            #create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
     

    def test_01_create_new_account(self):
        account=Account(id=1,first_name="my_first_name_",last_name="my_last_name_",email="my_email@live.com_",phone="23852697")
        db.session.add(account)
        db.session.commit()
        response =self.client().post('/account', 
            json={
                "first_name":"my_first_name",
                "last_name":"my_last_name",
                "email":"my_email@live.com",
                "phone":"23852698"
                },
            headers = administrator_auth_header)
        data = json.loads(response.data)
      
        print(data)
        

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
        response =self.client().post('/account', 
            json={'first_name':2,"last_name":"last_name_account","email":"my_email@live.com","phone":"23852698"},
            headers = administrator_auth_header)

        data = json.loads(response.data)
        

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)

   
    def test_04_400_create_new_account_non_valid_lenght_40(self):
        response =self.client().post('/account', 
            json={'first_name':"name_accountname_accountname_accountname_accountname_accountname_account","last_name":"last_name_account"},
            headers = administrator_auth_header)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)

    def test_05_get_accounts(self):
        response = self.client().get('/account',headers = administrator_auth_header)

        data = json.loads(response.data)

        print(data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['info_accounts'])
        self.assertTrue(data['number of subscribers'])
    

    def test_06_get_account(self):
        response = self.client().get('/account/1',headers = administrator_auth_header)

        data = json.loads(response.data)

        print(data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['info_account'])

    def test_07_404_get_account(self):
         response = self.client().get('/account/100',headers = administrator_auth_header)
         data = json.loads(response.data)
         self.assertEqual(response.status_code, 404)
         self.assertEqual(data['message'], 'resource not found')
         self.assertEqual(data['success'], False)

    def test_08_patch_account(self):

        """test account update success"""

        
        response = self.client().patch('/account/1',
            json={"first_name":"my_first_name2","last_name":"my_last_name2"},
            headers = administrator_auth_header)
        data = json.loads(response.data)

        print(data)
     
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['updated_account'])
        self.assertTrue(data['success'])
    def test_09_patch_account_non_valid_type(self):

        """test account update failure due to non_valid_type"""
    
        response = self.client().patch('/account/1',
        json={"first_name":"my_first_name2","last_name":2},
            headers = administrator_auth_header)
        data = json.loads(response.data)

     
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)

    def test_21_delete_account(self):
        response = self.client().delete('/account/1',
            headers = administrator_auth_header)

        data = json.loads(response.data)

        print(data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_id'],1)

    def test_22_delete_deleted_account(self):
        response = self.client().delete('/account/1',
            headers = administrator_auth_header)
        

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(data['success'], False)
    def test_23_delete_account(self):
        account=Account.query.filter_by(email='my_email@live.com').one_or_none()
        response = self.client().delete('/account/{}'.format(account.id),
            headers = administrator_auth_header)

        data = json.loads(response.data)

        print(data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_id'],account.id)
    def test_02_create_new_address(self):
       
        response =self.client().post('/address', 
            json={"city":"city",
            "postal_code":2000,
            "country":"country",
            "account_id":1,
            "state":"state"
            },
            headers = administrator_auth_header)
            
        data = json.loads(response.data)

        print(data)

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
        
        response =self.client().post('/address', 
            json={"city":2,
            "postal_code":2000,
            "country":"country",
            "account_id":1,
            "state":"state"
            },
            headers = administrator_auth_header)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)


    def test_11_get_address(self):
        response = self.client().get('/address',
            headers = administrator_auth_header)
        

        data = json.loads(response.data)

        print(data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['info_addresses'])
        self.assertTrue(data['number of addreses'])
    

    def test_12_get_address(self):
        address=Address.query.filter_by(account_id=1).one_or_none()
        response = self.client().get('/address/{}'.format(address.id),
            headers = administrator_auth_header)


        data = json.loads(response.data)

        print(data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['info_address'])

    def test_13_404_get_address(self):
        response = self.client().get('/address/100',
            headers = administrator_auth_header)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(data['success'], False)

    def test_14_patch_address(self):

        """test address update success"""

        address=Address.query.filter_by(account_id=1).one_or_none()
        response = self.client().patch('/address/{}'.format(address.id),
            json={"first_name":"my_first_name2","last_name":"my_last_name2"},
            headers = administrator_auth_header)
        data = json.loads(response.data)

        print(data)
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['updated_address'])
        self.assertTrue(data['success'])
    

    def test_15_patch_address_non_valid_type(self):

        """test address update failure due to non_valid_type"""
        address=Address.query.filter_by(account_id=1).one_or_none()
    
        response = self.client().patch('/address/{}'.format(address.id),json={"city":2,
            "postal_code":2002,
            "country":"country2",
            "account_id":1,
            "state":"state"
            },
            headers = administrator_auth_header)
        data = json.loads(response.data)

     
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)


    def test_17_delete_account_without_permission(self):
        
        response = self.client().delete('/account/1',
            headers = customer_auth_header)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['message'], 'Permission not found.')
        self.assertEqual(data['success'], False)
    def test_18_delete_account_without_authorization(self):
        response = self.client().delete('/account/1')

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['message'], 'Authorization header is expected.')
        self.assertEqual(data['success'], False)

    def test_19_delete_address(self):
        address=Address.query.filter_by(account_id=1).one_or_none()
        response = self.client().delete('/address/{}'.format(address.id),
            headers = administrator_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_id'],address.id)

    def test_20_delete_unexisting_address(self):
        response = self.client().delete('/address/1',
            headers = administrator_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(data['success'], False)


    

if __name__ == "__main__":
    unittest.main()