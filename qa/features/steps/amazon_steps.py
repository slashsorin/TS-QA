from __future__ import absolute_import

from pages.amazon_product_page import AmazonProductPage
from pages.added_to_basket_page import AddedToBasketPage
from pages.shopping_basket_page import ShoppingBasketPage

from behave import *


@given('I visit a product page on amazon.com')
def step(context):
    context.window.visit(AmazonProductPage())


@when('I click on the Add to Cart button')
def step(context):
    context.window.page.add_to_cart()
    context.window.page.dismiss_protection_plan_popover()
    context.window.visit(AddedToBasketPage())


@then('the product is added to the basket')
def step(context):
    assert context.window.page.is_confirmed()


@when('I go to my shopping basket page')
def step(context):
    context.window.page.view_shopping_basket()
    context.window.visit(ShoppingBasketPage())


@then('I can view my product')
def step(context):
    assert context.window.page.is_product_displayed()
