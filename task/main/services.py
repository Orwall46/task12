import datetime
import random
import string
import PIL
from django.core.files import File
from io import BytesIO
from PIL import Image


def make_thumbnail(image):
    letters = string.ascii_letters
    random_let = (''.join(random.choice(letters) for i in range(3)))
    now = datetime.datetime.now()
    time = str(now.day)+str(now.month)+str(now.year)+str(now.second)+str(now.microsecond)+str(random_let)

    with Image.open(image) as im:
        rgb_im = im.convert('RGB')
        rgb_im.thumbnail((1200, 900), PIL.Image.ANTIALIAS)
        thumb_io = BytesIO()
        rgb_im.save(thumb_io, format='webp', quality=75)
        thumbnail = File(thumb_io, name=time+'.webp')

    return thumbnail
