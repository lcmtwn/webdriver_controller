import requests


class DownloaderMixin():
    def download(self, url: str, file_path: str) -> None:
        resp = requests.get(url, stream=True)
        if resp.status_code != 200:
            resp.raise_for_status()

        with open(file_path, 'wb') as fd:
            print('downloading driver from {} ...'.format(url))
            for chunk in resp.iter_content(chunk_size=1024):
                fd.write(chunk)