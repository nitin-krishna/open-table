__author__ = '@nitin-krishna'

import time as t
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class Reserver(object):
    HOME_URL = r'https://www.opentable.com/new-york-city-restaurants'

    def __init__(self, restaurant_name, date, time, size):
        self._time = time
        self._date = date
        self._restaurant_name = restaurant_name
        self._size = size

    def reserve(self):
        self._open_driver()
        self._populate_homepage()

    def _open_driver(self):
        driver = webdriver.Chrome()
        driver.get(Reserver.HOME_URL)
        self.driver = driver

    def _populate_homepage(self):
        self._populate_homepage_date()
        self._populate_homepage_time()
        self._populate_homepage_size()
        self._populate_homepage_name()

    def _populate_homepage_date(self):
        pass

    def _populate_homepage_time(self):
        pass

    def _populate_homepage_size(self):
        size_elem = self.driver.find_element_by_name('Select_1')
        select_size = Select(size_elem)
        value = str(min(self._size, 21))
        select_size.select_by_value(value)

    def _populate_homepage_name(self):
        pass
