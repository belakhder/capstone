import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from starter.auth import * 
from starter.models import *


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    #Set up CORS
    CORS(app)
  

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                            'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                            'GET,PATCH,POST,DELETE,OPTIONS')
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    @app.route('/account',methods=['GET'])
    @requires_auth('get:accounts')
    def get_accounts(payload):

        accounts=Account.query.all()
        if len(accounts)==0:
            abort(404)
        nb_sub=len(accounts)
        output=accounts_Schema.dump(accounts)
        return {
            'success': True,
            'info_accounts':output,
            'number of subscribers':nb_sub
        }

    @app.route('/account/<int:account_id>',methods=['GET'])
    @requires_auth('get:account')
    def get_account(payload,account_id):

        account= Account.query.get(account_id)

        if not account:
            abort(404)
        output=account_Schema.dump(account)
        return {
            'success': True,
            'info_account':output,
        }

    @app.route('/account',methods=['POST'])
    @requires_auth('post:account')
    def post_account(payload):
        body=request.get_json()
        first_name=body.get('first_name')
        last_name=body.get('last_name')
        email=body.get('email')
        phone=body.get('phone')
        account=Account()

        if isinstance(first_name,str)==True:
            if len(first_name)<50 and len(first_name)>0:
                setattr(account,'first_name',first_name)
            else:
                abort(400)
        else:
            abort(400)

        if isinstance(last_name,str)==True:
            if len(last_name)<50 and len(last_name)>0:
                setattr(account,'last_name',last_name)
            else:
                abort(400)
        else:
            abort(400)


        if isinstance(email,str)==True:
            if len(email)<100 and len(email)>0:
                setattr(account,'email',email)
            else:
                abort(400)
        else:
            abort(400)

        if isinstance(phone,str)==True:
            if len(phone)<100 and len(phone)>0:
                setattr(account,'phone',phone)
            else:
                abort(400)
        else:
            abort(400)

       
        db.session.add(account)
        db.session.commit()
       

        output=account_Schema.dump(account)
        return {
            'success': True,
            'created_account':output
        }
    @app.route('/account/<int:id>',methods=['PATCH'])
    @requires_auth('patch:account')
    def patch_account(payload,id):

        account = Account.query.get(id)
        if not account:
            abort(404)

        body=request.get_json()
        first_name=body.get('first_name')
        last_name=body.get('last_name')
        email=body.get('email')
        phone=body.get('phone')

        body=request.get_json()
        if len(body.keys())!=0:
            if first_name:
                if isinstance(first_name,str)==True:
                    if len(first_name)<50 and len(first_name)>0:
                        setattr(account,'first_name',first_name)
                    else:
                        abort(400)
                else:
                    abort(400)

            if last_name:
                if isinstance(last_name,str)==True:
                    if len(last_name)<50 and len(last_name)>0:
                        setattr(account,'last_name',last_name)
                    else:
                        abort(400)
                else:
                    abort(400)
            if email:
                if isinstance(email,str)==True:
                    if len(email)<100 and len(email)>0:
                        setattr(account,'email',email)
                    else:
                        abort(400)
                else:
                    abort(400)
            if phone:
                if isinstance(phone,str)==True:
                    if len(phone)<50 and len(phone)>0:
                        setattr(account,'phone',phone)

                    else:
                        abort(400)
                else:
                    abort(400)
        else:
            abort(400)
            
        try:
            db.session.commit()
            output=account_Schema.dump(account)
        except:
            abort(422)
        return {
            'success': True,
            'updated_account':output
        }

    @app.route('/account/<int:id>',methods=['DELETE'])
    @requires_auth('delete:account')
    def delete_account(payload,id):
     
        account = Account.query.filter_by(id=id).one_or_none()

     
        if not account:
            abort(404)
        try:
            db.session.delete(account)
            db.session.commit()
        except:
            pass
        return {
            'success': True,
            'deleted_id':id
        }
    @app.route('/address/<int:id>',methods=['GET'])
    @requires_auth('get:address')
    def get_address(payload,id):

        address = Address.query.get(id)
        if not address:
            abort(404)
        output=address_Schema.dump(address)
        return {
            'success': True,
            'info_address':output,
        }
    @app.route('/address',methods=['GET'])
    @requires_auth('get:addresses')
    def get_addresses(payload):

        addresses=Address.query.all()
        if len(addresses)==0:
            abort(404)
        nb_sub=len(addresses)
        output=addresses_Schema.dump(addresses)
        return {
            'success': True,
            'info_addresses':output,
            'number of addreses':nb_sub
        }
    @app.route('/address',methods=['POST'])
    @requires_auth('post:address')
    def post_address(payload):
        body=request.get_json()
        city=body.get('city')
        state=body.get('state')
        postal_code=body.get('postal_code')
        country=body.get('country')
        account_id=body.get('account_id')
        address=Address()
        if city:
            if isinstance(city,str)==True:
                if len(city)<50 and len(city)>0:
                    setattr(address,'city',city)
                else:
                    abort(400)
            else:
                abort(400)
        else:
            abort(400)
        
        if state:
            if isinstance(state,str)==True:
                if len(state)<50 and len(state)>0:
                    setattr(address,'state',state)
                else:
                    abort(400)
            else:
                abort(400)
        
        if account_id:
            if isinstance(account_id,int)==True:
                    setattr(address,'account_id',account_id)
            else:
                abort(400)
        else:
            abort(400)

        if postal_code:
            if isinstance(postal_code,int)==True:
                setattr(address,'postal_code',postal_code)
            else:
                abort(400)
        if country:
            if isinstance(country,str)==True:
                if len(country)<50 and len(country)>0:
                    setattr(address,'country',country)
                else:
                    abort(400)
            else:
                abort(400)
        else:
            abort(400)
        try:
            db.session.add(address)
            db.session.commit()
        except:
            abort(422)

        output=address_Schema.dump(address)
        return {
            'success': True,
            'created_address':output
        }
    @app.route('/address/<int:id>',methods=['PATCH'])
    @requires_auth('get:address')
    def patch_address(payload,id):

        address =Address.query.get(id)
        if not address:
            abort(404)
        
        body=request.get_json()
        body=request.get_json()
        city=body.get('city')
        state=body.get('state')
        postal_code=body.get('postal_code')
        country=body.get('country')
        account_id=body.get('account_id')
        

        body=request.get_json()
        if len(body.keys())!=0:
            if city:
                if isinstance(city,str)==True:
                    if len(city)<50 and len(city)>0:
                        setattr(address,'city',city)
                    else:
                        abort(400)
                else:
                    abort(400)
                if state:
                    if isinstance(state,str)==True:
                        if len(state)<50 and len(state)>0:
                            setattr(address,'state',state)
                        else:
                            abort(400)
                    else:
                        abort(400)
                if postal_code:
                    if isinstance(postal_code,int)==True:
                        setattr(address,'postal_code',postal_code)
                    else:
                        abort(400)
                if account_id:
                    if isinstance(account_id,int)==True:
                        setattr(address,'account_id',account_id)
                    else:
                        abort(400)
                if country:
                    if isinstance(country,str)==True:
                        if len(country)<50 and len(country)>0:
                            setattr(address,'country',country)
                        else:
                            abort(400)
                    else:
                        abort(400)
        try:
            db.session.commit()
            output=address_Schema.dump(address)
        except:
            abort(422)
        return {
            'success': True,
            'updated_address':output
        }
    @app.route('/address/<int:id>',methods=['DELETE'])
    @requires_auth('delete:address')
    def delete_address(payload,id):
     
        address = Address.query.filter_by(id=id).one_or_none()
      
        if not address:
            abort(404)
        try:
            db.session.delete(address)
            db.session.commit()
        except:
            abort(422)
        return {
            'success': True,
            'deleted_id':id,
        }

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422
    @app.errorhandler(AuthError)
    def authentification_failed(AuthError): 
        return jsonify({
            "success": False, 
            "error": AuthError.status_code,
            "message": AuthError.error['description']
            }), AuthError.status_code

    return app


