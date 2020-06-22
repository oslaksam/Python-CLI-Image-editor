import numpy as np
from PIL import Image
import sys


def read_image(file_name: str) -> np.array:
    return np.asarray(Image.open(file_name), dtype=np.uint8)


def image_from_array(array: np.array, mode) -> Image:
    return Image.fromarray(array, mode=mode)


def display_image(file_name: str) -> None:
    image = Image.open(file_name)
    image.show()


def save_image(array: np.array, file_path, mode='RGB') -> None:
    image_from_array(array, mode=mode).save(file_path)


tmp = sys.argv[-1].split("/")
tmp = tmp[0:-1]
directory = "/".join(tmp)

identity_kernel = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
])

sharpening_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0],
])

approx_gaussian_blur_3_kernel = (1 / 16) * np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1],
])

approx_gaussian_blur_5_kernel = (1 / 256) * np.array([
    [1, 4, 6, 4, 1],
    [4, 16, 24, 16, 4],
    [6, 24, 36, 24, 6],
    [4, 16, 24, 16, 4],
    [1, 4, 6, 4, 1],
])

edge_detection_kernel = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1],
])

embossing_kernel = np.array([
    [-2, -1, 0],
    [-1, 1, 1],
    [0, 1, 2]
])
