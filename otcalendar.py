__author__ = '@nitin-krishna'

import pandas as pd
import utils


class OTCalendar(object):

    def __init__(self, date_picker):
        self.date_picker = date_picker
        self.picker_obj = date_picker.find_element_by_class_name('picker')  # class='picker down'

    def get_header(self):
        header_elem = self.picker_obj.find_element_by_class_name('picker__header')
        return OTCalendarHeader(header_elem)

    def get_table(self):
        table_elem = self.picker_obj.find_element_by_class_name('picker__table')
        return OTCalendarTable(table_elem)

    def select_date(self, date):
        self._advance_to(date.month, date.year)
        self._get_day_elem(date.day).click()

    def _advance_to(self, month, year):
        curr_month = self.get_month()
        curr_year = self.get_year()
        num_iter = 12 * (year - curr_year) + (month - curr_month)
        utils.repeat(self._navigate_to_next_month, num_iter)

    def _navigate_to_next_month(self):  # TODO: wait til element is clickable
        self.open()
        self.get_header().iterate()

    def _get_day_elem(self, date):
        self.get_table().get_day_elem(date)

    def get_month(self):
        self.open()
        return self.get_header().get_month()

    def get_year(self):
        self.open()
        return self.get_header().get_year()

    def open(self):
        if not self.is_open(): self.date_picker.click()

    def close(self):
        if self.is_open(): self.date_picker.click()

    def is_open(self):
        sub_date_picker = self.date_picker.find_element_by_name('datepicker')
        return sub_date_picker.get_attribute('aria-expanded') == 'true'


class OTCalendarHeader(object):

    def __init__(self, header):
        self.header = header

    def get_month(self):
        month_str = self.header.find_element_by_class_name('picker__month').text
        month_int = pd.to_datetime(month_str, format='%B').month
        return month_int

    def get_year(self):
        year_str = self.header.find_element_by_class_name('picker__year').text
        year_int = int(year_str)
        return year_int

    def iterate(self):
        self.header.find_element_by_class_name('picker__nav--next').click()


class OTCalendarTable(object):

    def __init__(self, table):
        self.table = table

    def get_day_elem(self, day):
        day_elements = self.table.find_elements_by_css_selector('.picker__day.picker__day--infocus')
        import pdb; pdb.set_trace()
        for day_elem in day_elements:
            if int(day_elem.text) == day:
                return day_elem
        raise LookupError('Could not find requested day {:d} in calendar'.format(day))
