import os

if os.path.isfile('urls.txt'):
    os.remove('urls.txt')

with open('urls.txt', 'a') as f:
    zoom = "P0"
    x =int(66)
    y = int(63)
    for i in range(0, x):
        for j in range(0, y):
            url = f"https://act-webstatic.hoyoverse.com/map_manage/map/2/253e4ea4c79eb920429e26720cebf6ef/{i}_{j}_{zoom}.png\n"
            # SIMULANKA url = f"https://act-webstatic.hoyoverse.com/map_manage/map/35/e5b74781addbfb04d4ae5271588a7a11/{i}_{j}_{zoom}.png\n"
            f.write(url)