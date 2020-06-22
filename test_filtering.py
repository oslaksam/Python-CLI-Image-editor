from numpy.testing import assert_equal
from pytest import fixture

from filtering.filtering import *


@fixture
def image():
    return read_image('tests/lenna.png')


@fixture
def image_gaussian_blur():
    return read_image('tests/lenna_gaussian_blur.png')


@fixture
def image_gray(image):
    return np.average(image.astype(np.float), weights=[0.299, 0.587, 0.114], axis=2).astype(np.uint8)


@fixture
def image_gray_edge_detection():
    return read_image('tests/lenna_gray_edge_detection.png')


@fixture
def image_gaussian_blur3():
    return read_image('tests/lenna_blur3.png')


@fixture
def image_inverse():
    return read_image('tests/lenna_inverse.png')


@fixture
def image_rotate():
    return read_image('tests/lenna_rotate.png')


@fixture
def image_lit75():
    return read_image('tests/lenna_lit75.png')


@fixture
def image_dark50():
    return read_image('tests/lenna_dark50.png')


@fixture
def image_emboss():
    return read_image('tests/lenna_emboss.png')


@fixture
def image_sharp():
    return read_image('tests/lenna_sharp.png')


@fixture
def image_mirror():
    return read_image('tests/lenna_mirror.png')


@fixture
def image_dark50():
    return read_image('tests/lenna_dark50.png')


def test_gaussian_blur3(image, image_gaussian_blur3):
    assert_equal(apply_filter(image, approx_gaussian_blur_3_kernel), image_gaussian_blur3)


def test_image_inverse(image, image_inverse):
    assert_equal(inverse(image), image_inverse)


def test_identity_filter(image):
    assert_equal(apply_filter(image, identity_kernel), image)


def test_gaussian_blur(image, image_gaussian_blur):
    assert_equal(apply_filter(image, approx_gaussian_blur_5_kernel), image_gaussian_blur)


def test_gray_edge_detection(image_gray, image_gray_edge_detection):
    assert_equal(apply_filter(image_gray, edge_detection_kernel), image_gray_edge_detection)


def test_smile(image):
    assert_equal(apply_filter(image, identity_kernel), image)


def test_bw(image, image_gray):
    assert_equal((bw(image)), image_gray)


def test_darken50(image, image_dark50):
    assert_equal((darken(image, 50)), image_dark50)


def test_emboss(image, image_emboss):
    assert_equal((apply_filter(image, embossing_kernel)), image_emboss)


def test_lit75(image, image_lit75):
    assert_equal((lighten(image, 75)), image_lit75)


def test_mirror(image, image_mirror):
    assert_equal((mirror(image)), image_mirror)


def test_rotation(image, image_rotate):
    assert_equal((rotate(image)), image_rotate)


def test_sharp(image, image_sharp):
    assert_equal((apply_filter(image, sharpening_kernel)), image_sharp)


def chain_test(image, image_gray):
    assert_equal(bw(rotate(rotate(rotate(rotate(image))))), image_gray)
