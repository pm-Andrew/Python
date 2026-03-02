# pillow.py
# Andrew

from PIL import Image
from PIL import ImageFilter


def main():
    with Image.open("cs50-shirt-img.png") as img:

        img = img.rotate(360)
        img = img.filter(ImageFilter.FIND_EDGES)
        # img = img.filter(ImageFilter.BLUR)
        img.save("out.png")

        # print(img.size)
        # print(img.format)

main()
