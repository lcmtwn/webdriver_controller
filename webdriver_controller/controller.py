import os
import shutil

from webdriver_controller import config
from webdriver_controller.downloader import chromedriver
from webdriver_controller.downloader import selenium_standalone


class WebdriverController(object):
    _installation_folder = '{}{}'.format(os.getcwd(),
                                         config.INSTALLATION_FOLDER)

    def __init__(self):
        pass

    def download(self):
        if not os.path.exists(self._installation_folder):
            os.makedirs(self._installation_folder)

        chromedriver.download()
        selenium_standalone.download()

    def cleanup(self):
        if os.path.exists(self._installation_folder):
            print('deleting {} ...'.format(self._installation_folder))
            shutil.rmtree(self._installation_folder)
        else:
            print('no Selenium Webdriver installation found')
