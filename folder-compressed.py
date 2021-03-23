from PIL import Image
import PIL
import os
import glob


def compress_images(directory=False, quality=30):
    if directory:
        os.chdir(directory)

    files = os.listdir()

    images = [file for file in files if file.endswith(('jpg', 'png', 'jpeg', 'JPG'))]

    for image in images:

        # print(image)

        img = Image.open(image)

        img.save('Compressed_' + image, optimize=True, quality=quality)


# current_directory = os.getcwd()
# ¿Que directorio?
name_d = input('Ruta del directorio: ')

# print('Se recomienda una calidad entre 35 a 40 dependiendo la imagen')
# quality_d = int(input('Calidad: '))

# cut_url = name_d.find("IMAGES") + len("IMAGES") + 1;
# lot_directory = name_d[cut_url:]
# directory = current_directory + '/'  + lot_directory
directory = name_d;
compress_images(directory=directory, quality=35)

# directory = 'C:/Users/Alexis/Desktop/IMAGES/S4-DESTINOS-NACIONALES/Destinos Nacionales/Cancún/Fiesta Americana Cancún Villas/Galería del hotel/Galería del hotel-Compress'
# directory = 'C:/Users/Alexis/Desktop/IMAGES/S4-DESTINOS-NACIONALES/Destinos Nacionales/Veracruz/' + name_d
# print(directory)

