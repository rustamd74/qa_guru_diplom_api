import allure

from allure_commons.types import Severity
from pytest_voluptuous import S

from schemas.user import create_single_user, login_successful, register_single_user, unregister_single_user, \
    login_unsuccessful


@allure.title('Registration with valid email and password')
@allure.tag('api')
@allure.label('owner', 'dzhafarov_ro')
@allure.severity(Severity.CRITICAL)
@allure.feature('registration')
@allure.suite('regress')
def test_register_successful(regress_api):
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    with allure.step('Login with email and password'):
        register_user = regress_api.post('/api/register', data=data)

    with allure.step('Check status code 200'):
        assert register_user.status_code == 200

    with allure.step('Check register user schemas'):
        assert S(register_single_user) == register_user.json()

    with allure.step('Check register user id'):
        assert register_user.json()['id']

    with allure.step('Check register user token'):
        assert register_user.json()['token']


@allure.title('Registration with one email without a password')
@allure.tag('api')
@allure.label('owner', 'dzhafarov_ro')
@allure.severity(Severity.CRITICAL)
@allure.feature('registration')
@allure.suite('regress')
def test_register_unsuccessful(regress_api):
    data = {
        "email": "sydney@fife"
    }
    with allure.step('Registration without password'):
        register_user = regress_api.post("/api/register", data=data)

    with allure.step('Check status code 400'):
        assert register_user.status_code == 400

    with allure.step('Check register user schemas'):
        assert S(unregister_single_user) == register_user.json()


@allure.title('Authorization check')
@allure.tag('api')
@allure.label('owner', 'dzhafarov_ro')
@allure.severity(Severity.CRITICAL)
@allure.feature('registration')
@allure.suite('regress')
def test_login_successful(regress_api):
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    with allure.step('Login with email and password'):
        login_user = regress_api.post("/api/login", data=data)

    with allure.step('Check status code 200'):
        assert login_user.status_code == 200

    with allure.step('Check login user schemas'):
        assert S(login_successful) == login_user.json()

    with allure.step('Check login user token'):
        assert login_user.json()['token']


@allure.title('Login with one email without password')
@allure.tag('api')
@allure.label('owner', 'dzhafarov_ro')
@allure.severity(Severity.CRITICAL)
@allure.feature('registration')
@allure.suite('regress')
def test_login_unsuccessful(regress_api):
    data = {
        "email": "peter@klaven"
    }
    with allure.step('Login without password'):
        unlogin_user = regress_api.post("/api/login", data=data)

    with allure.step('Check status code 400'):
        assert unlogin_user.status_code == 400

    with allure.step('Check un login user schemas'):
        assert S(login_unsuccessful) == unlogin_user.json()


@allure.title('Create user')
@allure.tag('api')
@allure.label('owner', 'dzhafarov_ro')
@allure.severity(Severity.CRITICAL)
@allure.feature('registration')
@allure.suite('regress')
def test_create(regress_api):
    data = {
        "name": "morpheus",
        "job": "leader",
        "id": "778",
        "createdAt": "2023-03-08T11:28:46.826Z"
    }
    with allure.step('Create user'):
        create_user = regress_api.post("/api/users", data=data)

    with allure.step('Check status code 201'):
        assert create_user.status_code == 201

    with allure.step('Check create user schemas'):
        assert S(create_single_user) == create_user.json()


@allure.title('Delete user')
@allure.tag('api')
@allure.label('owner', 'dzhafarov_ro')
@allure.severity(Severity.CRITICAL)
@allure.feature('registration')
@allure.suite('regress')
def test_delete(regress_api):
    with allure.step('Delete user'):
        delete_user = regress_api.delete("/api/users/2")

    with allure.step('Check status code 204'):
        assert delete_user.status_code == 204
