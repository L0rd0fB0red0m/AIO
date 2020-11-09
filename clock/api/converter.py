from PIL import Image, ImageDraw, ImageFont
import numpy as np
import datetime

"""Two colors: 1 main color and 1 accent color. These are labeled in the matrix as 1 and 2"""

def text_converter(text, height):
    """Converts a text to a pixel-matrix
    returns: np.array((16, x))"""

    font = ImageFont.truetype("verdanab.ttf", height)
    size = font.getsize(text)
    img = Image.new("1",size,"black")
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, "white", font=font)
    pixels = np.array(img, dtype=np.uint8)
    return pixels


digits = {
    1 : [[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]],
    2 : [[1,1,1],[0,0,1],[1,1,1],[1,0,0],[1,1,1]],
    3 : [[1,1,1],[0,0,1],[1,1,1],[0,0,1],[1,1,1]],
    4 : [[1,0,1],[1,0,1],[1,1,1],[0,0,1],[0,0,1]],
    5 : [[1,1,1],[1,0,0],[1,1,1],[0,0,1],[1,1,1]],
    6 : [[1,1,1],[1,0,0],[1,1,1],[1,0,1],[1,1,1]],
    7 : [[1,1,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]],
    8 : [[1,1,1],[1,0,1],[1,1,1],[1,0,1],[1,1,1]],
    9 : [[1,1,1],[1,0,1],[1,1,1],[0,0,1],[1,1,1]],
    0 : [[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]]
}

##place of numbers, invariable
digit_position = [[2,4], [2,10], [9,4], [9,10]]

def time_converter(time=datetime.datetime.now().strftime("%H%M")):
    """Converts 4-digit time to a pixel-matrix
    returns: np.array((16, 16))"""
    #time = datetime.datetime.now().strftime("%H%M")
    pixels = np.zeros((16,16),dtype=np.uint8)
    time = "0" * (4 - len(str(time))) + str(time)
    time_split = [int(i) for i in time]

    for i in range(4):
        x = digit_position[i][0]
        y = digit_position[i][1]
        number = digits[time_split[i]]
        pixels[x: x + 5, y: y + 3] = np.array(number)

    return pixels


days = np.append(np.zeros((15,16)), np.array([0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,1])).reshape((16,16))
def date_converter():
    today = datetime.datetime.today()
    weekday = datetime.datetime.weekday(today)
    # size of the reduced array according to weekday
    size = [2,4,6,8,10,13,16]

    pixels = days.copy() #base color background
    lrow = np.append(pixels[15,:size[weekday]], [0 for i in range(16 - size[weekday])])
    lrow = np.append(np.zeros((15,16)), lrow).reshape((16,16))
    pixels += lrow
    return pixels




weather_categories = {
    "cloud": "cloud",
    "cloud_with_rain": "rain and cloud",
    "thunder_cloud_rain": "thunder and cloud",
    "droplet": "rain and cloud",
    "cloud_snow": "snow and cloud",
    "sun": "sun",
    "Mist": "fog and clouds",
    "Smoke": "Smoke",
    "Haze": "Haze",
    "Dust": "Dust",
    "Fog": "fog",
    "Sand": "Sand",
    "Dust": "Dust",
    "Ash": "Ash",
    "Squal": "Squal",
    "Tornado": "Tornado",
}

def weather_converter(name):
    result = np.zeros((16,16))
    cwd = __file__.replace("\\","/") # for windows
    cwd = cwd.rsplit("/", 1)[0]  # the current working directory (where this file is)
    if len(cwd) == 0:
        cwd = "."
    icon_spritesheet = cwd + "/weather-icons.bmp"

    icons = Image.open(icon_spritesheet)
    icons_full = np.array(icons)

    icon_loc = ["sun","moon","sun and clouds", "moon and clouds", "cloud","fog and clouds","2 clouds", "3 clouds", "rain and cloud", "rain and clouds", "rain and cloud and sun", "rain and cloud and moon", "thunder and cloud", "thunder and cloud and moon", "snow and cloud", "snow and cloud and moon", "fog","fog night"]
    #ordered 1 2 \n 3 4 \ 5 5 ...
    name = weather_categories[name]
    try:
        iy, ix = int(icon_loc.index(name)/2), icon_loc.index(name)%2
        # x and y coords
    except:
        return np.zeros((16,16,3))

    icon_single = icons_full[16*iy:16*(iy + 1),16*ix:16*(ix + 1),...]
    return icon_single
