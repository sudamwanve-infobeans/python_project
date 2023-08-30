import os

from PIL import Image
from flask import url_for, current_app


def add_blog_img(pic_upload):

    filename = pic_upload.filename
    filepath = os.path.join(current_app.root_path, 'static/blogs/', filename)

    output_size = (200,200)
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return filename