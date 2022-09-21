from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from ..models.user import User
from ..database import get_db_connection, close_db_connection, commit_and_close_db_connection
from ..database import user_db
from ..schemas.user_schema import UserSchema
from ..exceptions import InvalidUserPayload
#from app import flask_bcrypt

user_schema = UserSchema()

class UsersApi(Resource):
	decorators = [jwt_required()]
	def get(self):
		conn = get_db_connection()
		users = user_db.get_users(conn)
		close_db_connection(conn)
		return users

	def post(self):
		errors = user_schema.validate(request.json)
		print("errors: "+str(errors))
		if errors:
			raise InvalidUserPayload(errors, 400)
		user_dict = user_schema.load(request.get_json())
		#user_dict['password'] = flask_bcrypt.generate_password_hash(user_dict['password'])
		conn = get_db_connection()
		user_db.create_users(conn, User(request.json))
		users = user_db.get_users(conn)
		commit_and_close_db_connection(conn)
		return users, 201

	def put(self):
		return {'message': 'Hello PUT'}

	def delete(self):
		return {'message': 'Hello DELETE'}