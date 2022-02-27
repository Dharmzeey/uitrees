from django.core.files import File

from PIL import Image
from io import BytesIO

# THIS FUNCTION HELPS TO COMPRESS IMAGES UPLOADED TO THE SERVER
# THE UPLOAD, SPECIAL PLACES AND REQUEST MAKES USE OF IT


def compress(image):
    if not image:
        return
    size_500 = (500,500)
    img = Image.open(image)
    img.thumbnail(size_500)

    im_io = BytesIO()
    img.save(im_io, 'JPEG', optimize=True)
    new_image = File(im_io, name=image.name)
    return new_image
