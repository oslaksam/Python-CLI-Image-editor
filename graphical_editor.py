import os
import filtering.filtering
import filtering.helpers
from filtering.helpers import *
import argparse

# Create and add the arguments to the parser
zero_100 = set(range(0, 101))
arg_parser = argparse.ArgumentParser(description="Process a picture.",
                                     epilog="Example: python graphic_editor.py --rotate --bw --lighten 25  "
                                            "/home/usr/Desktop/pic.jpg /home/usr/Desktop/pic_edit.jpg")
arg_parser.add_argument('--identity', action='store_true', help='aplikuje identity kernel')
arg_parser.add_argument('--emboss', action='store_true', help='provede emboss')
arg_parser.add_argument('--edge_detection', action='store_true', help='detekce hran')
arg_parser.add_argument('--blur3', action='store_true', help='rozmaž obraz 3x3 kernelem')
arg_parser.add_argument('--blur5', action='store_true', help='rozmaž obraz 5x5 kernelem')
arg_parser.add_argument('--rotate', action='store_true', help='převrácení obrazu směrem doprava o 90°')
arg_parser.add_argument('--mirror', action='store_true', help='zrcadlení')
arg_parser.add_argument('--inverse', action='store_true', help='inverzní obraz (negativ)')
arg_parser.add_argument('--bw', action='store_true', help='převod do odstínů šedi')
arg_parser.add_argument('--lighten', type=int, choices=zero_100, action='store',
                        help='zesvětlení <procent: 0-100>', metavar='INT: 0-100')
arg_parser.add_argument('--darken', type=int, choices=zero_100, action='store',
                        help='ztmavení <procent: 0-100>', metavar='INT: 0-100')
arg_parser.add_argument('--sharpen', action='store_true', help='zvýraznění hran (tzv. “unsharp mask”) ')
arg_parser.add_argument('input', help='INPUT_IMAGE_PATH')
arg_parser.add_argument('output', help='OUTPUT_IMAGE_PATH')
arguments = arg_parser.parse_args()
# Argparser will take care of wrong arguments


if os.access(sys.argv[-2], os.R_OK):  # Check if we can read the picture
    # Read the picture and save it as np.array
    picture = read_image(sys.argv[-2])
else:
    print("File does not exist or you do not have permission to read it")
    sys.exit()
if len(directory) == 0:
    print("ok")
elif not (os.access(directory, os.X_OK | os.W_OK)):  # Check if we can write file to the directory
    print("You cannot write into the selected directory")
    sys.exit()
# A given image has to have either 2 (grayscale) or 3 (RGB) dimensions
assert picture.ndim in [2, 3]

# Select options from arguments passed as arguments
list_of_selected_options = [arg[2:] for arg in sys.argv if "--" in arg]

# Apply options to the picture
for option in list_of_selected_options:
    # This is only useful for darken or lighten functions
    percentage = getattr(arguments, option)
    # Find appropriate function in the filtering module
    filter_function = getattr(filtering.filtering, option)
    # If value is an int, then we are calling darken or lighten functions that take an additional precentage (int)
    # argument
    if type(percentage) == int:
        picture = filter_function(picture, percentage)
    else:
        picture = filter_function(picture)
# Save the picture
if picture.ndim == 2:
    # BW
    save_image(picture.astype(dtype=np.uint8), arguments.output, 'L')
else:
    # RGB
    save_image(picture.astype(dtype=np.uint8), arguments.output, 'RGB')
display_image(arguments.output)
