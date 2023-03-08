from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture(params = ["chrome", "edge"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "edge":
        web_driver = webdriver.Edge(executable_path = r"C:\Users\VREDDYK\OneDrive - Capgemini\Desktop\Drivers\msedgedriver.exe")

    request.cls.driver = web_driver
    web_driver.get("http://www.google.com")

    yield
    web_driver.quit()


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_Google(BaseTest):

    def test_google_title(self):
        assert self.driver.title == "Google"

    def test_google_url(self):
        assert self.driver.current_url == "https://www.google.com/?gws_rd=ssl"
