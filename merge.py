from PIL import Image
from matplotlib.pyplot import imshow
from enums import *
import math
import os
import numpy as np
from process_transparency import process_transparency

# Transparent blocks
# full transparent b9688cf5174db38d1771ba15232ebdd80e1d2af8eb1d21f3a4512bf809ac6850


def main(obj: Dimensions, str_obj):
    print(f"Merging {str_obj}")
    # w = (abs(obj.getXmin()) + abs(obj.getXmax())+1) * 256
    # h = (abs(obj.getYmin()) + abs(obj.getYmax())+1) * 256

    # Mihoyo
    w = (abs(obj.getXmax()) - abs(obj.getXmin())+1) * 256
    h = (abs(obj.getYmax()) - abs(obj.getYmin())+1) * 256

    print([w, h])


    directory = os.listdir(f"T:\\map-isles\\{str_obj}")

    print(f"Found {len(directory)} files")

    background = Image.new("RGBA", (w, h), (255, 255, 255, 255))

    # Mihoyo only
    x = 0
    y = 0
    ctr = 0
    offsetX = obj.getXmin()
    offsetY = obj.getYmin()
    print([offsetX, offsetY])
    for i in range(obj.getXmin(), obj.getXmax()+1):
        for j in reversed(range(obj.getYmin(), obj.getYmax()+1)):
            # print(f"tile-{i}_{j}.jpg")
            # tile = Image.open(f"map-isles\\{str_obj}\\tile-{i}_{j}.jpg")
            tile = Image.open(f"T:\\map-isles\\{str_obj}\\{i}_{j}_{obj.getZoomValue()}.png").convert("RGBA")
            tile = process_transparency(tile)
            # background.paste(tile, (x*256, y*256))
            background.paste(tile, ((i-offsetX)*256, (j-offsetY)*256))
            ctr += 1
            if ctr % 100 == 0:
                print(f"Progress: {round(ctr / len(directory), 5)}")
            # print(f"Pasted tile position {i} {j}")
            y += 1
        y = 0
        x += 1

    # Appsample
    # x = 0
    # y = 0
    # ctr = 0
    # for i in range(obj.getXmin(), obj.getXmax()+1):
    #     for j in reversed(range(obj.getYmin(), obj.getYmax()+1)):
    #         # print(f"tile-{i}_{j}.jpg")
    #         tile = Image.open(f"T:\\map-isles\\{str_obj}\\tile-{i}_{j}.jpg")
    #         background.paste(tile, (x*256, y*256))
    #         ctr += 1
    #         if ctr % 100 == 0:
    #             print(f"Progress: {round(ctr / len(directory), 5)}")
    #         y += 1
    #     y = 0
    #     x += 1

    # display(background)
    # imshow(np.asarray(background))
    print("Saving image.")
    background.save(f"T:\\{str_obj}.png")
    print("Saved.")


# obj = TEYVAT_12
# str_obj = "TEYVAT_12"

array = [
    # [TEYVAT_15, "TEYVAT_15"],
    # [TEYVAT_14, "TEYVAT_14"],
    # [TEYVAT_13, "TEYVAT_13"],
    # [TEYVAT_12, "TEYVAT_12"],
    [TEYVAT_P0, "TEYVAT_P0"],
]

for i in array:
    main(i[0], i[1])
