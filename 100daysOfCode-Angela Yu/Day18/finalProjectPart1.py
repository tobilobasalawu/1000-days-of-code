import colorgram

colors = colorgram.extract('hirstPainting.jpg', 16)
colorStorage = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    colorRange = (r, g, b)
    colorStorage.append(colorRange)