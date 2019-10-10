from selenium import webdriver
import unittest, time, re
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        # открытие главной страницы
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        wd = self.wd
        self.wd.quit()
