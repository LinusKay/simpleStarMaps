from PIL import Image, ImageDraw, ImageFilter
import random

STARMAPCOUNT = 7

imgSize = 300
backColour = 0

starColourMinMax = (150, 255)
starSizeMinMax = (1, 5)
primaryStarSizeMinMax = (8, 12)
starCountMinMax = (6, 130)
primaryStarCountMinMax = (4, 8)
primaryStarBorder = 50

mapCount = 0
starCount = 0

def primaryStarBoundsLimit(num):
  return max(min(num, imgSize - primaryStarBorder), 0 + primaryStarBorder)

for starmap in range(STARMAPCOUNT):
    im = Image.new('RGB', (imgSize, imgSize), (backColour, backColour, backColour))
    draw = ImageDraw.Draw(im)

    maxStars = random.randint(starCountMinMax[0], starCountMinMax[1])
    primaryStarCount = random.randint(primaryStarCountMinMax[0], primaryStarCountMinMax[1])

    for star in range(maxStars):
        if starCount < primaryStarCount:
            starSize = random.randint(primaryStarSizeMinMax[0], primaryStarSizeMinMax[1])
            x0 = primaryStarBoundsLimit(random.randint(0,imgSize))
            y0 = primaryStarBoundsLimit(random.randint(0,imgSize))
            x1 = primaryStarBoundsLimit(x0 + starSize)
            y1 = primaryStarBoundsLimit(y0 + starSize)
        else:
            starSize = random.randint(starSizeMinMax[0], starSizeMinMax[1])
            x0 = random.randint(0,imgSize)
            y0 = random.randint(0,imgSize)
            x1 = x0 + starSize
            y1 = y0 + starSize

        starColour = random.randint(starColourMinMax[0], starColourMinMax[1])
        draw.ellipse((x0, y0, x1, y1), fill=(starColour, starColour, starColour), outline=(0, 0, 0))
        starCount += 1

    im = im.filter(ImageFilter.GaussianBlur(3))
    im.save(str(mapCount) + '.jpg', quality=95)
    mapCount += 1
    starCount = 0