import colorgram

colors = colorgram.extract("hirstPainting.jpg", 16)
colorStorage = []

for i in colors:
    r = colors.rgb.r
    g = colors.rgb.g
    b = colors.rgb.b

    colorRange = (r, g, b)
    colorStorage.append(colorRange)