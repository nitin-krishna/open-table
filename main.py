__author__ = '@nitin-krishna'

import time as t
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from otcalendar import OTCalendar
import utils


class OpenTableReserver(object):
    HOME_URL = r'https://www.opentable.com/new-york-city-restaurants'

    def __init__(self, restaurant_name, date, time, size):
        """
        :str restaurant_name: name of restaurant
        :str date: date of reservation, format 2019/01/01, 01/01/2019, 2019-01-01, 01-01-2019
        :str time: time of reservation, format 4:00 PM
        :int size: party size
        """
        self._restaurant_name = restaurant_name.strip()
        self._date = utils.format_date(date)
        self._time = utils.format_time(time)
        self._size = size
        self._open_driver()

    def reserve(self):
        self._populate_homepage()

    def _open_driver(self):
        driver = webdriver.Chrome()
        driver.get(OpenTableReserver.HOME_URL)
        self.driver = driver

    def _populate_homepage(self):
        self._populate_homepage_date()
        self._populate_homepage_time()
        self._populate_homepage_size()
        self._populate_homepage_name()

    def _populate_homepage_date(self):  # TODO: test more, need to wait for elements to be clickable
        date_picker = self.driver.find_element_by_class_name('date-picker')
        cal = OTCalendar(date_picker)
        cal.select_date(self._date)

    def _populate_homepage_time(self):
        time_picker = self.driver.find_element_by_class_name('time-picker')
        elem = time_picker.find_element_by_tag_name('select')
        value = self._time.strftime('%H:%M')
        Select(elem).select_by_value(value)

    def _populate_homepage_size(self):
        size_picker = self.driver.find_element_by_class_name('party-size-picker')
        elem = size_picker.find_element_by_tag_name('select')
        value = str(min(self._size, 21))
        Select(elem).select_by_value(value)

    def _populate_homepage_name(self):
        elem = self.driver.find_element_by_name('searchText')
        elem.clear()
        elem.send_keys(self._restaurant_name)
        elem.send_keys(Keys.ESCAPE)
