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
    "http": "http://localhost:8080",
    "https": "https://localhost:8080"
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

    def __init__(self, x_min = 0, y_min = 0, x_max = 0, y_max = 0, zoom = 10, url = None, endpoint = None) -> None:
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

    def getZoomValue(self) -> int:
        return self.zoom

    def getAllValues(self) -> list:
        return [self.getXValues(), self.getYValues()]


def filename(x, y) -> str:
    return f"tile-{x}_{y}.jpg"

def main(obj: object, path) -> None:
    r = requests.Session()

    maps = obj

    if not os.path.exists(f"map-isles\\{path}"):
        os.mkdir(f"map-isles\\{path}")

    for i in range(maps.getXmin(), maps.getXmax()+1):
        for j in range(maps.getYmin(), maps.getYmax()+1):
            data = r.get(f"{maps.getURL()}/{maps.getEndpoint()}/{maps.getZoomValue()}/{filename(i, j)}", headers=headers, proxies=proxy, verify=False)

            if data.status_code == 200:
                with open(f"map-isles\\{path}\\{filename(i, j)}", "wb") as f:
                    f.write(data.content)
                    log.debug(f"{filename(i, j)} written to file.")
            elif data.status_code == 404:
                log.error(f"{filename(i, j)} was not found on the server.")
            elif data.status_code == 403:
                log.error(f"{filename(i, j)} returned 403 Forbidden status.")


if __name__ == '__main__':
    main(GOLDEN_APPLE_ARCHIPELAGO_13, "GOLDEN_APPLE_ARCHIPELAGO_13")