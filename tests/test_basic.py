"""
Basic tests.
"""
import os
import shutil
from os import path

import pytest
from gifig import Gif, transforms

TEST_DIR = path.abspath(path.join(__file__, '..', ))
IMAGE_EXAMPLE_DIR = path.join(TEST_DIR, 'images')
IMAGE_IN_DIR = path.join(TEST_DIR, 'temp_images')
IMAGE_OUT_DIR = path.join(TEST_DIR, 'output')
IMAGE_NAMES = (
    'bassman.gif',
    'partyhard.gif',
    'pooh.gif',
)


@pytest.fixture(scope='session')
def image_in_dir():
    shutil.rmtree(IMAGE_IN_DIR, ignore_errors=True)
    shutil.copytree(IMAGE_EXAMPLE_DIR, IMAGE_IN_DIR)
    return IMAGE_IN_DIR


@pytest.fixture(scope='session')
def image_out_dir():
    shutil.rmtree(IMAGE_OUT_DIR, ignore_errors=True)
    os.mkdir(IMAGE_OUT_DIR)
    return IMAGE_OUT_DIR


class TestGif(object):
    @pytest.mark.parametrize('image_name', IMAGE_NAMES)
    def test_init(self, image_name, image_in_dir):
        gif = Gif(path.join(image_in_dir, image_name))
        assert gif is not None
        assert gif.frames is not None

    @pytest.mark.parametrize('image_name', IMAGE_NAMES)
    def test_save_same_path(self, image_name, image_in_dir):
        gif = Gif(path.join(image_in_dir, image_name))
        gif.save()

    @pytest.mark.parametrize('image_name', IMAGE_NAMES)
    def test_save_new_path(self, image_name, image_in_dir, image_out_dir):
        gif = Gif(path.join(image_in_dir, image_name))
        gif.save(path.join(image_out_dir, image_name))


class TestTransforms(object):
    @pytest.mark.parametrize('image_name', IMAGE_NAMES)
    def test_greyscale(self, image_name, image_in_dir, image_out_dir):
        gif = Gif(path.join(image_in_dir, image_name))
        transforms.greyscale(gif)
        gif.save(path.join(image_out_dir, 'grey_' + image_name))

    @pytest.mark.parametrize('image_name', IMAGE_NAMES)
    def test_warpbox(self, image_name, image_in_dir, image_out_dir):
        gif = Gif(path.join(image_in_dir, image_name))
        transforms.warpbox(gif)
        gif.save(path.join(image_out_dir, 'warp_' + image_name))
