import subprocess

import requests

from webdriver_controller import config
from webdriver_controller.tools import tools


class ChromeDriver(object):
    def __init__(self):
        self.version = self.get_latest_version()
        self.filename = 'chromedriver_{}.zip'.format(tools.get_platform())
        self.download_url = '{}{}/{}'.format(
            config.STORAGE_URLS.get('chromedriver'), self.version,
            self.filename)

    def get_latest_version(self) -> str:
        host = config.STORAGE_URLS.get('chromedriver')
        latest_rel_doc_url = '{}LATEST_RELEASE'.format(host)

        resp = requests.get(latest_rel_doc_url)
        if resp.status_code != 200:
            resp.raise_for_status()

        latest_verison = resp.text.strip()

        return latest_verison

    def unzip_file(self):
        dest = '{}/{}'.format(config.INSTALLATION_FOLDER, self.filename)

        # unzip the driver
        subprocess.run(
            ['unzip', '-oq', dest, '-d', config.INSTALLATION_FOLDER])
