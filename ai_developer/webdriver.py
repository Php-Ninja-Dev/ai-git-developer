'''Module for handling web driver interactions in the AI Developer codebase'''
import subprocess
import selenium
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.options import Options

'''Class for interacting with the web driver'''

class WebdriverAction:
    def __init__(self, executable_path):

    def __init__(self):
        pass

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
