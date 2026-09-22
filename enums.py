from main import Dimensions
import math

# URLs
TEYVAT_URL = "https://game-cdn.appsample.com"
# TEYVAT_ENDPOINT = "gim/map-teyvat/v52-rc2"
# TEYVAT_ENDPOINT = "gim/map-teyvat/v55-rc1"
# TEYVAT_ENDPOINT = "gim/map-teyvat/v55-rc1"
TEYVAT_ENDPOINT = "gim/map-teyvat/v58-rc2"

GOLDEN_APPLE_ARCHIPELAGO_URL = ""
GOLDEN_APPLE_ARCHIPELAGO_ENDPOINT = ""

ENKANOMIYA_URL = ""
ENKANOMIYA_ENDPOINT = ""

CHASM_URL = ""
CHASM_ENDPOINT = ""

VELURIAM_MIRAGE_URL = "https://game-cdn.appsample.com"
VELURIAM_MIRAGE_ENDPOINT = "gim/map-veluriyam-mirage/rc2"

SEA_OF_BYGONE_ERA_URL = "https://game-cdn.appsample.com"
SEA_OF_BYGONE_ERA_ENDPOINT = "gim/map-bygone-eras/v1"

# From official mihoyo
# Filenames are X_Y_(P0|N1|N2|N3).<image_format (png) default webp>
SIMULANKA_URL = "https://act-webstatic.hoyoverse.com"
SIMULANKA_ENDPOINT = "map_manage/map/35/e5b74781addbfb04d4ae5271588a7a11"

MHY_TEYVAT_P0_URL = "https://act-webstatic.hoyoverse.com"
# MHY_TEYVAT_P0_ENDPOINT = "map_manage/map/2/9e1c6c4d2bac013bc0cdd81c58733f47" # 5.2
# MHY_TEYVAT_P0_ENDPOINT = "map_manage/map/2/b8dda0da78acc2aba67a395117bf0bc2/" # 5.5
# MHY_TEYVAT_P0_ENDPOINT = "map_manage/map/2/73865667c73faf29f8a0bc9f10d560c7" # 5.6
# MHY_TEYVAT_P0_ENDPOINT = "map_manage/map/2/84e91c043f30df2655d34a5543be7b17" # 5.8
# MHY_TEYVAT_P0_ENDPOINT = "map_manage/map/2/38c777262414ff6a7b3e73829d4a7ab1" # 6.0 / Luna I
# MHY_TEYVAT_P0_ENDPOINT = "map_manage/map/2/0f333192efeebcdfc400f2c49f5128bb" # 6.3 / Luna IV
# MHY_TEYVAT_P0_ENDPOINT = "map_manage/map/2/c0eaef431637950e44ef47dc2ba0c105" # 6.7 / Luna VIII
MHY_TEYVAT_P0_ENDPOINT = "map_manage/map/2/eea752b746ae1f2e0c1988a574f2b7b0" # 7.0

# Coordinate enums
# For each dimensions, negative values are on the left and bottom
# otherwise on its opposing direction

# Syntax:
# Dimensions(x_min, y_min, x_max, y_max)
# 5.5
# x1 = -64
# y1 = -64
# x2 = 63
# y2 = 41

# 5.6
# x1 = -64
# y1 = -64
# x2 = 63
# y2 = 41

# 5.8
x1 = -64
y1 = -64
x2 = 63
y2 = 41

# TEYVAT_10 = Dimensions(0, 0, 0, 0, 10, TEYVAT_URL, TEYVAT_ENDPOINT)
# TEYVAT_11 = Dimensions(0, 0, 0, 0, 11, TEYVAT_URL, TEYVAT_ENDPOINT)
TEYVAT_12 = Dimensions(int(x1 / 8), int(y1 / 8), int(math.floor(x2 / 8)), int(math.floor(y2 / 8)), 12, TEYVAT_URL, TEYVAT_ENDPOINT)
TEYVAT_13 = Dimensions(int(x1 / 4), int(y1 / 4), int(math.floor(x2 / 4)), int(math.floor(y2 / 4)), 13, TEYVAT_URL, TEYVAT_ENDPOINT)
TEYVAT_14 = Dimensions(int(x1 / 2), int(y1 / 2), int(math.floor(x2 / 2)), int(math.floor(y2 / 2)), 14, TEYVAT_URL, TEYVAT_ENDPOINT)
TEYVAT_15 = Dimensions(x1, y1, x2, y2, 15, TEYVAT_URL, TEYVAT_ENDPOINT)

GOLDEN_APPLE_ARCHIPELAGO_10 = Dimensions(-2, -2, 1, 1, 10, GOLDEN_APPLE_ARCHIPELAGO_URL, GOLDEN_APPLE_ARCHIPELAGO_ENDPOINT)
GOLDEN_APPLE_ARCHIPELAGO_11 = Dimensions(-4, -4, 3, 3, 11, GOLDEN_APPLE_ARCHIPELAGO_URL, GOLDEN_APPLE_ARCHIPELAGO_ENDPOINT)
GOLDEN_APPLE_ARCHIPELAGO_12 = Dimensions(-8, -8, 7, 7, 12, GOLDEN_APPLE_ARCHIPELAGO_URL, GOLDEN_APPLE_ARCHIPELAGO_ENDPOINT)
GOLDEN_APPLE_ARCHIPELAGO_13 = Dimensions(-16, -16, 15, 15, 13, GOLDEN_APPLE_ARCHIPELAGO_URL, GOLDEN_APPLE_ARCHIPELAGO_ENDPOINT)

VELURIAM_MIRAGE_10 = Dimensions(-2, -2, 1, 1, 10, VELURIAM_MIRAGE_URL, VELURIAM_MIRAGE_ENDPOINT)
VELURIAM_MIRAGE_11 = Dimensions(-4, -4, 3, 3, 11, VELURIAM_MIRAGE_URL, VELURIAM_MIRAGE_ENDPOINT)
VELURIAM_MIRAGE_12 = Dimensions(-8, -8, 7, 7, 12, VELURIAM_MIRAGE_URL, VELURIAM_MIRAGE_ENDPOINT)
VELURIAM_MIRAGE_13 = Dimensions(-16, -16, 15, 15, 13, VELURIAM_MIRAGE_URL, VELURIAM_MIRAGE_ENDPOINT)

SEA_OF_BYGONE_ERA_10 = Dimensions(-2, -2, 1, 1, 10, SEA_OF_BYGONE_ERA_URL, SEA_OF_BYGONE_ERA_ENDPOINT)
SEA_OF_BYGONE_ERA_11 = Dimensions(-4, -4, 3, 3, 11, SEA_OF_BYGONE_ERA_URL, SEA_OF_BYGONE_ERA_ENDPOINT)
SEA_OF_BYGONE_ERA_12 = Dimensions(-8, -8, 7, 7, 12, SEA_OF_BYGONE_ERA_URL, SEA_OF_BYGONE_ERA_ENDPOINT)
SEA_OF_BYGONE_ERA_13 = Dimensions(-16, -16, 15, 15, 13, SEA_OF_BYGONE_ERA_URL, SEA_OF_BYGONE_ERA_ENDPOINT)

SIMULANKA_P0 = Dimensions(0, 0, 31, 31, 13, "P0", None)
SIMULANKA_N1 = Dimensions(0, 0, 15, 15, "N1", "N1", None)
SIMULANKA_N2 = Dimensions(0, 0, 7, 7, "N2", "N2", None)
SIMULANKA_N3 = Dimensions(0, 0, 3, 3, "N3", "N3", None)

# TEYVAT_P0 = Dimensions(0, 0, 87, 72, "P0", "P0", None) # 5.2
# TEYVAT_P0 = Dimensions(7, 0, 88, 51, "P0", "P0", None) # 5.5
# TEYVAT_P0 = Dimensions(15, 0, 89, 51, "P0", "P0", None) # 5.6
# TEYVAT_P0 = Dimensions(21, 4, 106, 59, "P0", "P0", None) # 5.8
# TEYVAT_P0 = Dimensions(21, 4, 120, 66, "P0", "P0", None) # 6.0 / Luna I
# TEYVAT_P0 = Dimensions(19, 3, 108, 60, "P0", "P0", None) # 6.3 / Luna IV
# TEYVAT_P0 = Dimensions(27, 3, 113, 60, "P0", "P0", None) # 6.7 / Luna VIII
TEYVAT_P0 = Dimensions(30, 0, 113, 71, "P0", "P0", None) # 7.0 // raw 26, 0, 115, 71
