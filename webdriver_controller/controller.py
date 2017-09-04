import shutil

from webdriver_controller import config
from webdriver_controller.drivers.chromedriver import ChromeDriver
from webdriver_controller.drivers.selenium_standalone import SeleniumStandalone
from webdriver_controller.utils import async_client
from webdriver_controller.utils import tools


class WebdriverController(object):
    def download(self):
        tools.check_installation_folder()
        tools.check_version_file()

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

        tools.write_version_file(version_info)
        tools.remove_outdated_version_file()

    def cleanup(self):
        if tools.is_installation_folder_existed():
            print('deleting {} ...'.format(config.INSTALLATION_FOLDER))
            shutil.rmtree(config.INSTALLATION_FOLDER)
        else:
            print('no Selenium Webdriver installation found')

    def list(self):
        if tools.is_installation_folder_existed():
            if tools.is_version_file_existed():
                version_info = tools.read_version_file()

                print('ChromeDriver version: {}'.format(
                    version_info.get('chrome')))
                print('Selenium standalone version: {}'.format(
                    version_info.get('selenium')))
            else:
                print('no installation file found')
        else:
            print('no Selenium Webdriver installation found')
