# FSND capstone project 


## synopsis:

the application consists in the creation of a user account where there is all information concerning a potential customer

Getting Started:

## Installing Dependencies:

Python 3.7

#### create and activate a virtual envirnment:

virtualenv -p python3 env

source env/scripts/activate 

#### PIP Dependencies:

pip install -r requirements.txt

Running the app:

python app.py

## Models 

account and address

#### Roles and permissions:

* administrator

delete:account	delete an existing account		

delete:address	delete address		

get:account	get info account from database		

get:accounts	get info for many accounts		

get:address	get info address		

get:addresses	get info addresses		

patch:account	modify account info		

patch address	modify info address		

post:account	create new account		

post:address	create address		


* customer

delete:address	delete address	Account	

get:account	get info account from database	Account	

get:address	get info address	Account	

patch:account	modify account info	Account	

patch address	modify info address	Account	

post:account	create new account	Account	

post:address	create address	Account	

## Endpoints :
```

POST  ('/account', json={ "first_name":"my_first_name", "last_name":"my_last_name", "email":"my_email@live.com", "phone":"23852698" }, headers = administrator_auth_header) 


{'created_account': {'email': 'my_email@live.com', 'first_name': 'my_first_name', 'id': 1, 'last_name': 'my_last_name', 'phone': '23852698'}, 'success': True}

GET ('/account',headers = administrator_auth_header)


{'info_accounts': [{'email': 'my_email@live.com', 'first_name': 'my_first_name', 'id': 1, 'last_name': 'my_last_name', 'phone': '23852698'}], 'number of subscribers': 1, 'success': True}

GET ('/account/1',headers = administrator_auth_header)


{'info_account': {'email': 'my_email@live.com', 'first_name': 'my_first_name', 'id': 1, 'last_name': 'my_last_name', 'phone': '23852698'}, 'success': True}

PATCH ('/account/1', json={"first_name":"my_first_name2","last_name":"my_last_name2"}, headers = administrator_auth_header) 


{'success': True, 'updated_account': {'email': 'my_email@live.com', 'first_name': 'my_first_name2', 'id': 1, 'last_name': 'my_last_name2', 'phone': '23852698'}}

POST ('/address', json={"city":"city", "postal_code":2000, "country":"country", "account_id":1, "state":"state" }, headers = administrator_auth_header)

{'info_addresses': [{'account_id': 1, 'city': 'city', 'country': 'country', 'id': 1, 'postal_code': 2000, 'state': 'state'}], 'number of addreses': 1, 'success': True}    

GET ('/address', headers = administrator_auth_header)

{'info_address': {'account_id': 1, 'city': 'city', 'country': 'country', 'id': 1, 'postal_code': 2000, 'state': 'state'}, 'success': True}

PATCH ('/address/1', json={"first_name":"my_first_name2","last_name":"my_last_name2"}, headers = administrator_auth_header)


{'success': True, 'updated_address': {'account_id': 1, 'city': 'city', 'country': 'country', 'id': 1, 'postal_code': 2000, 'state': 'state'}}

DELETE ('/address/1', headers = administrator_auth_header)

{'deleted_id': 1, 'success': True}

POST ('/address', json={"city":"city", "postal_code":2000, "country":"country", "account_id":1, "state":"state" },
 headers = administrator_auth_header)

{'created_address': {'account_id': 1, 'city': 'city', 'country': 'country', 'id': 1, 'postal_code': 2000, 'state': 'state'}, 'success': True}


DELETE ('/account/1', headers = administrator_auth_header)

{'deleted_id': 1, 'success': True}


```




## Testing

Python test_app.py