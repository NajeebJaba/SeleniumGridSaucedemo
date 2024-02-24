import time
import unittest
from selenium import webdriver
from logic.login_page import LoginPage
import concurrent.futures

class GridTest(unittest.TestCase):
    HUB_URL = 'http://localhost:444/wd/hub'

    def setUp(self):
        self.chrome_cap = webdriver.ChromeOptions()
        self.chrome_cap.capabilities['platformName'] = 'windows'

        self.fireFox_cap = webdriver.FirefoxOptions()
        self.fireFox_cap.capabilities['platformName'] = 'windows'

        self.edge_cap = webdriver.EdgeOptions()
        self.edge_cap.capabilities['platformName'] = 'windows'

        #enter the browsers to list
        self.cap_list = [self.chrome_cap, self.fireFox_cap,self.edge_cap]


    def test_run_grid(self):
        for caps in self.cap_list:
            self.test_execute(caps)

    def test_grid_parallel(self):
        with concurrent.futures.ThreadPollExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.test_execute, self.cap_list)
            time.sleep(60)

    def test_execute(self, caps):
        #defining the driver in browser, similar to "driver = webdriver.Chrome()" ,but no need to define cap
        driver = webdriver.Remote(command_executor=self.HUB_URL, options=caps)
        # driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")

        title = driver.title
        expected_title = "Swag Labs"
        print("test run on", caps.capabilities)
        self.assertEqual(expected_title, title, "Title doesn't match expected value")
        time.sleep(60)
        driver.quit()


        self.login_page = LoginPage(driver)
        self.login_page.login_button("standard_user", "secret_sauce")







