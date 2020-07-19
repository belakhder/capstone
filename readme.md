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

## Deployed heruko link

https://app-fethi.herokuapp.com/

## Testion via heruko

heroku run python manage.py test  --app app-fethi

## tokens 
```
administrator_auth =eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ild2VHBoVG1FRkpwa0l1X2o4anJNaiJ9.eyJpc3MiOiJodHRwczovL2Rldi1lOHk1a3cwei51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwOWE0MzVhMWY2MDMwMDE5YjBhZDAyIiwiYXVkIjoiYWNjb3V0IiwiaWF0IjoxNTk1MTcwODIxLCJleHAiOjE1OTUyNTcyMjEsImF6cCI6InI0NW5HeFFsbzJGZzdxSWFIUlFEejdQTG1qMTNpUEQzIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWNjb3VudCIsImRlbGV0ZTphZGRyZXNzIiwiZ2V0OmFjY291bnQiLCJnZXQ6YWNjb3VudHMiLCJnZXQ6YWRkcmVzcyIsImdldDphZGRyZXNzZXMiLCJwYXRjaDphY2NvdW50IiwicGF0Y2ggYWRkcmVzcyIsInBvc3Q6YWNjb3VudCIsInBvc3Q6YWRkcmVzcyJdfQ.NW8W3EYUmWmoBJPgkuqUH7kb7oZbNVUkZOYnsnFBZ8G0B-uf7mxvMMUpgyiaOnshf5U7AvdD22G6baHjstHCmGhNYQAGXwS-oH4GAMMwZ27Gpv16EcLx5OyzXqOTlQLe7BZVu9DMFKF4ko6IFQXRNoApE5tnr00o7N4qnb1yLSoDmGtRo8mHp9x9Wvcr87JRLPsAWqHy8QsLXFizKc7s55zFwWeuXYNEz-8Q5FD9iRYJUwYir-2FE94hnrIev5pIogp2tnGAQj3DRY_KhGE44pmiDu-fhCY7ZZbCTf4KlDQjEGT7ZQWYAPNwX4ACftCNqnYKN4g1p0i6PD4zxFYyCg
```
```
customer_auth_header =eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ild2VHBoVG1FRkpwa0l1X2o4anJNaiJ9.eyJpc3MiOiJodHRwczovL2Rldi1lOHk1a3cwei51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwOWE0MzVhMWY2MDMwMDE5YjBhZDAyIiwiYXVkIjoiYWNjb3V0IiwiaWF0IjoxNTk1MTcxMDUyLCJleHAiOjE1OTUyNTc0NTIsImF6cCI6InI0NW5HeFFsbzJGZzdxSWFIUlFEejdQTG1qMTNpUEQzIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWRkcmVzcyIsImdldDphY2NvdW50IiwiZ2V0OmFkZHJlc3MiLCJwYXRjaDphY2NvdW50IiwicGF0Y2ggYWRkcmVzcyIsInBvc3Q6YWNjb3VudCIsInBvc3Q6YWRkcmVzcyJdfQ.H8uHMU8maB3DJ6yaiEoURpj-oEjuyFv_v1atVo6eEQaOE1JbGMejdqM8NIhqG9t-56oThzQ-C5Xp6jjcuJmwDG-WfcB6aV_yGKmzPOM0jTaknJxLqduLokRpZHCals8BMY4kbn3_splkI_N_XfxS__vlKAr311lMQY6baljY52R3M5CBG3k3TImUNGgqi9_SKsRT4h54PDbHCRDyjWByiEdv8e8rFunltI4ViwzyVTkgYth-WFoH_pi3e2nGOztoVnli-AWVXj-JsGCmq-dsztl0ypT9B7gJ3mvX3B1VdSFJerTv5CBfk9jrS5wxP1Y-VQzed2yUJlzH0oJWg7HGYw
```
