import json
import shutil

from webdriver_controller import config
from webdriver_controller.drivers.chromedriver import ChromeDriver
from webdriver_controller.drivers.selenium_standalone import SeleniumStandalone
from webdriver_controller.tools import async_client


class WebdriverController(object):
    def _check_installation_folder(self) -> None:
        if not config.INSTALLATION_FOLDER.exists():
            config.INSTALLATION_FOLDER.mkdir()

    def _check_version_file(self) -> None:
        if config.VERSION_FILE.exists():
            config.VERSION_FILE.rename(config.OUTDATED_VERSION_FILE)

    def _remove_outdated_version_file(self) -> None:
        if config.OUTDATED_VERSION_FILE.exists():
            config.OUTDATED_VERSION_FILE.unlink()

    def _write_version_file(self, version_info: dict) -> None:
        with open(config.VERSION_FILE, 'w') as fh:
            json.dump(version_info, fh)

    def download(self):
        self._check_installation_folder()
        self._check_version_file()

        chromedriver = ChromeDriver()
        selenium_standalone = SeleniumStandalone()

        dl_list = [chromedriver.download_url, selenium_standalone.download_url]
        async_client.download(dl_list)

        chromedriver.unzip_file()

        # write Webdriver version to file
        version_info = {
            'chrome': chromedriver.version,
            'selenium': selenium_standalone.version
        }

        self._write_version_file(version_info)
        self._remove_outdated_version_file()

    def cleanup(self):
        if config.INSTALLATION_FOLDER.exists():
            print('deleting {} ...'.format(config.INSTALLATION_FOLDER))
            shutil.rmtree(config.INSTALLATION_FOLDER)
        else:
            print('no Selenium Webdriver installation found')

    def list(self):
        if config.INSTALLATION_FOLDER.exists():
            if config.VERSION_FILE.exists():
                version_info = {}
                with open(config.VERSION_FILE, 'r') as fh:
                    version_info = json.load(fh)

                print('ChromeDriver version: {}'.format(
                    version_info.get('chrome')))
                print('Selenium standalone version: {}'.format(
                    version_info.get('selenium')))
            else:
                print('no installation file found')
        else:
            print('no Selenium Webdriver installation found')
