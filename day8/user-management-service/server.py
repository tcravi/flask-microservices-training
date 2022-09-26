from app import app, restful_api
from app.api.users_api import UsersApi
from app.api.user_api import UserApi
from app.api.addresses_api import AddressesApi
from app.api.address_api import AddressApi
from app.api.auth_api import AuthApi, RegisterApi

if __name__ == '__main__':
    app.run()