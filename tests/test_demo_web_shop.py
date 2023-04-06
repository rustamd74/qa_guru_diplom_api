import os
import allure
from allure_commons.types import Severity

from selene import have

EMAIL = os.getenv('EMAIL')


@allure.title('Authorized user login')
@allure.tag('ui with api')
@allure.label('owner', 'dzhafarov_ro')
@allure.severity(Severity.CRITICAL)
@allure.feature('autorization')
@allure.suite('demowebshop')
def test_auth_login(auth_user):
    with allure.step('Checking for Successful Authorization'):
        auth_user.open('')
        auth_user.element('.account').should(have.text(EMAIL))


@allure.title('Adding a Product to the Cart')
@allure.tag('ui with api')
@allure.label('owner', 'dzhafarov_ro')
@allure.severity(Severity.NORMAL)
@allure.feature('product')
@allure.suite('demowebshop')
def test_add_to_cart(auth_user, demoshop):
    with allure.step('Product selection'):
        auth_user.open('/notebooks')
    with allure.step("Add to cart"):
        auth_user.element('.button-2 ').click()
    pass


@allure.title('Checking that the product has been added to the cart')
@allure.tag('ui with api')
@allure.label('owner', 'dzhafarov_ro')
@allure.severity(Severity.CRITICAL)
@allure.feature('product')
@allure.suite('demowebshop')
def test_checking_shopping_cart(demoshop):
    with allure.step('Checking shopping cart'):
        response = demoshop.demoqa.post("/addproducttocart/catalog/31/1/1")
        assert response.status_code == 200


@allure.title('Removing a product from the cart')
@allure.tag('ui with api')
@allure.label('owner', 'dzhafarov_ro')
@allure.severity(Severity.CRITICAL)
@allure.feature('product')
@allure.suite('demowebshop')
def test_update_shopping_cart(auth_user, demoshop):
    with allure.step('Selecting product in cart'):
        auth_user.open('')
        auth_user.element('.ico-cart').click()
    with allure.step('Removing an item from the cart'):
        auth_user.element('.qty-input').clear().send_keys(0).press_enter()
    with allure.step('Checking if the cart is empty'):
        auth_user.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


@allure.title('Exit from personal account')
@allure.tag('ui with api')
@allure.label('owner', 'dzhafarov_ro')
@allure.severity(Severity.CRITICAL)
@allure.feature('autorization')
@allure.suite('demowebshop')
def test_logout(demoshop):
    with allure.step('Checking the logout'):
        demoshop.demoqa.get('/logout')
