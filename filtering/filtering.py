from filtering.helpers import *

# My homework implementation of convolution

"""def conv2d(image, kernel):
    image = image.astype('float')
    # Flip kernel , in both horizontal and vertical direction
    kernel = np.flip(np.flip(kernel.astype('float'), 1), 0)
    (k1, k2) = kernel.shape
    (i1, i2) = image.shape
    # pad 3x3
    if kernel.shape[0] == 3:
        image = np.pad(image, ((1, 1), (1, 1)), 'constant', constant_values=0).astype("float")
    else:
        # pad 5x5
        image = np.pad(image, ((2, 2), (2, 2)), 'constant', constant_values=0).astype("float")
    (j1, j2) = image.shape
    a = j1 - k1 + 1
    b = j2 - k2 + 1
    convolution = np.zeros((i1, i2)).astype("float")
    for x in range(a):
        for y in range(b):
            tmp = image[x:x + k1, y:y + k2]
            out_pix = np.sum(tmp * kernel)
            if out_pix > 255:
                convolution[x, y] = 255
            elif out_pix < 0:
                convolution[x, y] = 0
            else:
                convolution[x, y] = out_pix
    return convolution.astype("uint8")
"""


# 2d convolution inspired by Martin Koryťák and Ngo Hong Son
def conv2d(image: np.array, kernel: np.array) -> np.array:
    # Flip kernel , in both horizontal and vertical direction
    kernel = np.flip(np.flip(kernel.astype('float'), 1), 0)
    i = kernel.shape[0] // 2
    j = kernel.shape[1] // 2
    padding = np.pad(image, ((i, j), (i, j)), 'constant', constant_values=0).astype(np.float)
    strides = padding.strides + padding.strides
    strided = np.lib.stride_tricks.as_strided(padding, image.shape + kernel.shape, strides)
    convolution = strided * kernel
    sum1 = np.sum(convolution, axis=-1)
    sum2 = np.sum(sum1, axis=-1)
    cut = np.clip(sum2, 0, 255)
    return cut.astype(np.uint8)


# Apply_filter implemented in homework03
def apply_filter(image: np.array, kernel: np.array) -> np.array:
    # A given image has to have either 2 (grayscale) or 3 (RGB) dimensions
    assert image.ndim in [2, 3]
    # A given filter has to be 2 dimensional and square
    assert kernel.ndim == 2
    assert kernel.shape[0] == kernel.shape[1]

    if image.ndim in [2]:
        return conv2d(image, kernel)
    if image.ndim in [3]:
        conv3d = []
        for dim in range(3):
            conv_dim = conv2d(image[:, :, dim], kernel.astype(np.float))
            conv_dim = conv_dim.astype(np.uint8)
            conv3d.append(conv_dim)
        fin = np.stack(conv3d, axis=2).astype(np.uint8)
        return fin.astype(np.uint8)


# Every function bellow corresponds to an option in argparser option selection

def identity(image: np.array) -> np.array:
    return apply_filter(image, identity_kernel).astype(np.uint8)


def emboss(image: np.array) -> np.array:
    return apply_filter(image, embossing_kernel).astype(np.uint8)


def blur3(image: np.array) -> np.array:
    return apply_filter(image, approx_gaussian_blur_3_kernel).astype(np.uint8)


def blur5(image: np.array) -> np.array:
    return apply_filter(image, approx_gaussian_blur_5_kernel).astype(np.uint8)


def edge_detection(image: np.array) -> np.array:
    return apply_filter(image, edge_detection_kernel).astype(np.uint8)


def sharpen(image: np.array) -> np.array:
    return apply_filter(image, sharpening_kernel).astype(np.uint8)


def bw(image: np.array) -> np.array:
    return np.average(image.astype(np.float), weights=[0.299, 0.587, 0.114], axis=2).astype(np.uint8)


def rotate(image: np.array) -> np.array:
    return np.rot90(image, k=1, axes=(1, 0)).astype(np.uint8)


def mirror(image: np.array) -> np.array:
    return np.fliplr(image).astype(np.uint8)


def inverse(image: np.array) -> np.array:
    return (255 - image).astype(np.uint8)


def lighten(image: np.array, percentage: int) -> np.array:
    rate = percentage / 100

    def lit(pixel, rat=rate):
        res = pixel + pixel * rat
        if res >= 255:
            return 255
        else:
            return res

    vectorized_function = np.vectorize(lit)
    result = vectorized_function(image)
    return result.astype(np.uint8)


def darken(image: np.array, percentage: int) -> np.array:
    rate = percentage / 100

    def dark(pixel, rat=rate):
        res = pixel - pixel * rat
        if res <= 0:
            return 0
        else:
            return res

    vectorized_function = np.vectorize(dark)
    result = vectorized_function(image)
    return result.astype(np.uint8)
