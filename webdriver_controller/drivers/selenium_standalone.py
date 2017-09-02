import re

import requests
import xmltodict

from webdriver_controller import config


class SeleniumStandalone(object):
    def __init__(self):
        self.version = self.get_latest_version()
        self.filename = 'selenium-server-standalone-{}.jar'.format(
            self.version)

        version_key = self.version[:(self.version.find('.', -1) - 1)]
        self.download_url = '{}{}/{}'.format(
            config.STORAGE_URLS.get('selenium'), version_key, self.filename)

    def get_latest_version(self) -> str:
        resp = requests.get(config.STORAGE_URLS.get('selenium'))
        if resp.status_code != 200:
            resp.raise_for_status()

        doc = xmltodict.parse(resp.content)
        items = doc.get('ListBucketResult').get('Contents')

        for item in reversed(items):
            if 'standalone' in item.get('Key') and 'beta' not in item.get(
                    'Key'):
                selenium_key = item.get('Key').strip()
                break

        pattern = re.compile('selenium-server-standalone-(.*).jar')
        version = pattern.match(selenium_key.split('/')[1]).group(1)

        return version
