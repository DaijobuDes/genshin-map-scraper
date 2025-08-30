import logging
import requests
import time
import os
from enums import *
from color import ColoredFormatter
import urllib3
from main import Dimensions

# Disable HTTPS verification
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
}

proxy = {
    "http": "http://100.89.204.43:8080",
    "https": "https://100.89.204.43:8080"
}


# Console logging
log = logging.getLogger('map-fetch')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
cf = ColoredFormatter("[%(asctime)s][%(name)s][%(levelname)s] = %(message)s (%(filename)s:%(lineno)d)")
ch.setFormatter(cf)
log.addHandler(ch)

# Set log level
log.setLevel(logging.DEBUG)
# End of console logging


def main(obj: Dimensions, path) -> None:
    r = requests.Session()

    if os.path.isfile('urls.txt'):
        os.remove('urls.txt')

    maps = obj

    if not os.path.exists(f"map-isles\\{path}"):
        os.mkdir(f"map-isles\\{path}")

    for i in range(maps.getXmin(), maps.getXmax()+1):
        for j in range(maps.getYmin(), maps.getYmax()+1):

            # Appsample
            # with open('urls.txt', 'a') as f:
            #     url = f"{maps.getURL()}/{maps.getEndpoint()}/{maps.getZoomValue()}/{filename(i, j)}\n"
            #     f.write(url)

            # Mihoyo
            with open('urls.txt', 'a') as f:
                url = f"{SIMULANKA_URL}/{SIMULANKA_ENDPOINT}/{i}_{j}_{maps.getZoomValue()}\n"
                f.write(url)

            # data = r.get(f"{maps.getURL()}/{maps.getEndpoint()}/{maps.getZoomValue()}/{filename(i, j)}", headers=headers, verify=False, proxies=proxy)
            # if data.status_code == 200:
            #     with open(f"map-isles\\{path}\\{filename(i, j)}", "wb") as f:
            #         f.write(data.content)
            #         log.debug(f"{filename(i, j)} written to file.")
            # elif data.status_code == 404:
            #     log.error(f"{filename(i, j)} was not found on the server.")
            # elif data.status_code == 403:
            #     log.error(f"{filename(i, j)} returned 403 Forbidden status.")
