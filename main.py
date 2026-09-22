import logging
import requests
import time
import os
from enums import *
from color import ColoredFormatter
import urllib3


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

class Dimensions():

    def __init__(self, x_min = 0, y_min = 0, x_max = 0, y_max = 0, zoom = 10, url = "", endpoint = "") -> None:
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        self.zoom = zoom
        self.url = url
        self.endpoint = endpoint

    def setPos(self, x_min, y_min, x_max, y_max) -> None:
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def getXmin(self) -> int:
        return self.x_min

    def getXmax(self) -> int:
        return self.x_max

    def getYmin(self) -> int:
        return self.y_min

    def getYmax(self) -> int:
        return self.y_max

    def getURL(self) -> str:
        return self.url

    def getEndpoint(self) -> str:
        return self.endpoint

    def getXValues(self) -> list:
        return [self.x_min, self.x_max]

    def getYValues(self) -> list:
        return [self.y_min, self.y_max]

    def getZoomValue(self):
        return self.zoom

    def getAllValues(self) -> list:
        return [self.getXValues(), self.getYValues()]


def filename(x, y) -> str:
    return f"tile-{x}_{y}.jpg"

def main(obj: Dimensions, path) -> None:
    r = requests.Session()

    if os.path.isfile(f'{path}-urls.txt'):
        os.remove(f'{path}-urls.txt')

    maps = obj

    if not os.path.exists(f"map-isles\\{path}"):
        os.mkdir(f"map-isles\\{path}")

    for i in range(maps.getXmin(), maps.getXmax()+1):
        for j in range(maps.getYmin(), maps.getYmax()+1):

            # Appsample
            # with open(f'{path}-urls.txt', 'a') as f:
            #     url = f"{maps.getURL()}/{maps.getEndpoint()}/{maps.getZoomValue()}/{filename(i, j)}\n"
            #     f.write(url)

            # Mihoyo (FROST_MOON_P0)
            # with open(f'{path}-urls.txt', 'a') as f:
            #     url = f"{FROST_MOON_URL}/{FROST_MOON_P0_ENDPOINT}/{i}_{j}_{maps.getZoomValue()}.png\n"
            #     f.write(url)

            # Mihoyo
            with open(f'{path}-urls.txt', 'a') as f:
                url = f"{MHY_TEYVAT_P0_URL}/{MHY_TEYVAT_P0_ENDPOINT}/{i}_{j}_{maps.getZoomValue()}.png\n"
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


if __name__ == '__main__':
    array = [
        # [TEYVAT_15, "TEYVAT_15"],
        # [TEYVAT_14, "TEYVAT_14"],
        # [TEYVAT_13, "TEYVAT_13"],
        # [TEYVAT_12, "TEYVAT_12"],
        # [FROST_MOON_P0, "FROST_MOON_P0"],
        [TEYVAT_P0, "TEYVAT_P0"],
    ]

    for i in array:
        main(i[0], i[1])

    # main(TEYVAT_15, "TEYVAT_15")
