from PIL import Image
import PIL
import os


def compress_images(directory=False, quality=30):
    if directory:
        os.chdir(directory)

    files = os.listdir()

    images = [file for file in files if file.endswith(('jpg', 'png', 'jpeg'))]

    for image in images:
        
        img = Image.open(image)
        
        img.save('Compressed_' + image, optimize=True, quality=quality)


# ¿Que directorio?
directory = input('Ruta del directorio: ')
compress_images(directory=directory, quality=35)
