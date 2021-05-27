#
# datagen.py
# - Generate dataset for ML.
#
import glob
import multiprocessing as mp
import os
from os.path import join, dirname, basename, splitext
from itertools import repeat

import freetype as ft
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import dataset


def bitmap_generator(bitmap):
    '''
    Generate bitmap iterator of fixed width and height.

    Args:
        bitmap (freetype.Bitmap): The bitmap of the glyph.
    
    Returns:
        Gray scale pixel ranged [0, 255].
    '''
    start_width = int((dataset.WIDTH - bitmap.width) / 2)
    end_width = start_width + bitmap.width
    start_height = int((dataset.HEIGHT - bitmap.rows) / 2)
    end_height = start_height + bitmap.rows
    index = 0

    buffer = bitmap.buffer

    for y in range(dataset.HEIGHT):
        for x in range(dataset.WIDTH):
            if start_width <= x < end_width and start_height <= y < end_height:
                yield buffer[index]
                index += 1
            else:
                yield 0


def generate_data(data_type, font_file, batch_size):
    '''
    Generate dataset.

    Args:
        data_type (str): Kind of dataset. One of "train", "validation" and "test".
        font_file (str): Path of the font file.
        batch_size (int): Generation count of argumented image per glyph.
    '''
    IMAGE_GENERATOR = ImageDataGenerator(rotation_range=20,
                                         width_shift_range=0.1,
                                         height_shift_range=0.1,
                                         # zoom_range=[0.5, 0.8],
                                         rescale=1.0/255.0)
    
    face = ft.Face(font_file)
    face.set_pixel_sizes(32, 32)

    font_name, _ = splitext(basename(font_file))

    print("Generate {1} dataset from font '{0}'...".format(font_name, data_type))

    options = tf.io.TFRecordOptions(compression_type="GZIP")

    record_path = join(dataset.DATA_ROOT, data_type, '{font_name}.tfrecord'.format(font_name=font_name))
    os.makedirs(dirname(record_path), exist_ok=True)

    with tf.io.TFRecordWriter(record_path, options=options) as writer:
        for ch in dataset.range_chars():
            face.load_char(ch)

            image = np.fromiter(bitmap_generator(face.glyph.bitmap), int, count=dataset.WIDTH*dataset.HEIGHT)
            image.resize((1, dataset.WIDTH, dataset.HEIGHT, 1))

            augmented_image_generator = None

            if data_type != 'test':
                augmented_image_generator = IMAGE_GENERATOR.flow(image, batch_size=1)
            else:  # data_type == 'test'
                augmented_image_generator = (image / 255.0 for _ in repeat(0))

            for _ in range(batch_size):
                image = next(augmented_image_generator)
                writer.write(dataset.serialize(image, dataset.INDEXES[ch]))


    print("Generate {1} dataset from font '{0}'... done.".format(font_name, data_type))

if __name__ == '__main__':
    def data():
        for data_type, batch_size in ('train', 3), ('validation', 1), ('test', 1):
            for font_file in glob.glob(join(dataset.FONT_ROOT, '*.ttf')):
                yield data_type, font_file, batch_size

    with mp.Pool(processes=mp.cpu_count()) as pool:
        pool.starmap(generate_data, data())
