from PIL import Image
# from Pillow import Image
from io import BytesIO

def compress(path):
    img = Image.open(path)
    buffer_file = BytesIO()
    img.save(buffer_file, 'JPEG', quality=60)
    return 'jpeg', buffer_file.getvalue()

def register(context, plugin_config):
    jpeg_extensions = ['jpeg', 'jpg']
    context.includer.add(jpeg_extensions, compress)
