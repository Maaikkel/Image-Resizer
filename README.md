# JPEG Image Resizer

A simple image resizer that i made for my own purposes as a part of Python learning.
It processes a image, which to path is given as an argument in command line when running the script.
Script also accepts path to directory (it looks for all .jpg/.jpeg in directory and converts all of them.)
Script doesn't do any changes to the original file(s), in parent directory it creates a whole new directory called 'resized' and place resized image(s) there.

## Example usage

```bash
  python resizer.py "path_to_directory" "path_to_image"
```