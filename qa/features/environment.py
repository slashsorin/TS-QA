from __future__ import absolute_import

from helpers.driver import DriverFactory
from pages.window import Window


def before_all(context):
    context.driver_factory = DriverFactory(browser_name='chrome')


def before_scenario(context, scenario):
    context.driver = context.driver_factory.create()
    context.window = Window(context.driver)
