# Graphic editor

The output of my semester work is a CLI application that can load an input image, perform selected basic graphic operations on it and save the output.
All operations with images take full advantage of matrix operations and numpy functionality, as we showed in the exercise. Pillow library methods are used to load and save the image.
Operations can be freely combined using switches (see Command example). The operations will be applied gradually from left to right. The list of operations is easily expandable.

## Requirements
In the requirements.txt file
## Use

```bash
python graphical_editor.py [options] INPUT_IMAGE_PATH OUTPUT_IMAGE_PATH
```
## Switches

    applies identity kernel; --identity
    performs emboss; --emboss
    edge detection; --edge_detection
    blur image 3x3 with kernel; --blur3
    blur image with 5x5 kernel; --blur5
    flip the image 90 ° to the right; --rotate
    mirroring; --mirror
    inverse image (negative); --inverse
    grayscale conversion; --bw
    lightening; --lighten <percentage: 0-100>
    darkening; --darken <percentage: 0-100>
    edge highlighting (so-called “unsharp mask”); --sharpen



## Example command

```bash
python graphic_editor.py --rotate --bw --lighten 25 INPUT_IMAGE_PATH OUTPUT_IMAGE_PATH
```
This command loads an image from INPUT_IMAGE_PATH, performs 90 ° right flip, grayscale, and 25% lighten on operations. And exactly in that order. The resulting image is stored at OUTPUT_IMAGE_PATH
## License
[MIT] (https://choosealicense.com/licenses/mit/)
