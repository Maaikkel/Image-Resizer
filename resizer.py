from PIL import Image
from pathlib import Path, PurePath
from sys import argv
from os import system

def process_image(input_path):
    parent_directory = PurePath(input_path).parent
    resized_directory = Path(str(parent_directory) + '/resized/')
    if not Path.exists(resized_directory):
        Path.mkdir(resized_directory)
    
    try:
        img_path = Path(input_path)
        print("Processing ", img_path, " ... ", end='')
        image = Image.open(img_path)
        image_name = PurePath(img_path).stem
        output_image = PurePath.joinpath(
            resized_directory, image_name + '.jpg')
        image.thumbnail((2000, 2000), resample=Image.LANCZOS, reducing_gap=3.0)
        image.save(output_image)
        print("OK")
    except OSError:
        print("FAILED - I/O error occured")

def process_directory(input_path):
    for image in (list(input_path.glob('*.jpg')) + list(input_path.glob('*.jpeg'))):
            process_image(image)

if __name__ == "__main__":
    path_gen = (path for path in argv[1:len(argv)])

    while current_value := next(path_gen, False):
        input_path = Path(current_value)

        if input_path.is_dir():
            process_directory(input_path)
        else:
            process_image(input_path)
    system('pause')