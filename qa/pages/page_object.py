from __future__ import absolute_import


class PageObject(object):

    def __init__(self, url):
        self._url = url
        self._driver = None

    @property
    def driver(self):
        assert self._driver, "PageObject has not been attached to a Window"
        return self._driver

    @property
    def url(self):
        return self._url
