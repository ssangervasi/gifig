"""
Basic tests.
"""
import os
import shutil
from os import path

import pytest
from gifig import process

TEST_DIR = path.abspath(path.join(__file__, '..', ))
IMAGE_OUT_DIR = path.join(TEST_DIR, 'output')
IMAGE_IN_DIR = path.join(TEST_DIR, 'images')
IMAGE_NAMES = (
    'bassman.gif',
    'partyhard.gif',
    'pooh.gif',
)


@pytest.fixture(scope='session')
def image_out_dir():
    shutil.rmtree(IMAGE_OUT_DIR, ignore_errors=True)
    os.mkdir(IMAGE_OUT_DIR)
    return IMAGE_OUT_DIR


@pytest.mark.parametrize('image_name', IMAGE_NAMES)
def test_open(image_name):
    gif = process.open_gif(path.join(IMAGE_IN_DIR, image_name))
    assert gif is not None
    gif.close()


@pytest.mark.parametrize('image_name', IMAGE_NAMES)
def test_copy(image_name, image_out_dir):
    gif = process.open_gif(path.join(IMAGE_IN_DIR, image_name))
    assert gif is not None
    gif.save(path.join(image_out_dir, image_name))
    gif.close()


@pytest.mark.skip
@pytest.mark.parametrize('image_name', IMAGE_NAMES)
def test_black_line(image_name, image_out_dir):
    gif = process.open_gif(path.join(IMAGE_IN_DIR, image_name))
    process.draw_black_line(gif)
    gif.save(path.join(image_out_dir, image_name))
    gif.close()
