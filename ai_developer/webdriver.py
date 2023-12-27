
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WebdriverAction:
    def __init__(self, executable_path):
        self.executable_path = executable_path
        self.driver = None

    def start_webdriver(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(self.executable_path, options=chrome_options)

    def visit_webpage(self, url):
        if not self.driver:
            self.start_webdriver()
        self.driver.get(url)
        page_html = self.driver.page_source
        return page_html

    def close_webdriver(self):
        if self.driver:
            self.driver.quit()
