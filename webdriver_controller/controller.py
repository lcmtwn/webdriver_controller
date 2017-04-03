from pathlib import Path
import shutil

from webdriver_controller import config
from webdriver_controller.drivers.chromedriver import ChromeDriver
from webdriver_controller.drivers.selenium_standalone import SeleniumStandalone


class WebdriverController(object):
    _installation_folder = Path('{}{}'.format(Path.cwd(),
                                              config.INSTALLATION_FOLDER))

    def download(self):
        if not self._installation_folder.exists():
            self._installation_folder.mkdir()

        chromedriver = ChromeDriver()
        chromedriver.download_driver()

        selenium_standalone = SeleniumStandalone()
        selenium_standalone.download_driver()

    def cleanup(self):
        if self._installation_folder.exists():
            print('deleting {} ...'.format(self._installation_folder))
            shutil.rmtree(self._installation_folder)
        else:
            print('no Selenium Webdriver installation found')
