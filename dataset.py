#
# dataset.py
# - Serialize and deserialize dataset.
#
from os.path import join, dirname
import tensorflow as tf
import glob


# Copied from tensorflow documentation.
def _int64_feature(value):
    """Wrapper for inserting int64 features into Example proto."""
    if not isinstance(value, list):
        value = [value]
    return tf.train.Feature(int64_list=tf.train.Int64List(value=value))


def _float_feature(value):
    """Wrapper for inserting float features into Example proto."""
    if not isinstance(value, list):
        value = [value]
    return tf.train.Feature(float_list=tf.train.FloatList(value=value))


def _floats_feature(value):
    return tf.train.Feature(float_list=tf.train.FloatList(value=value))


def _bytes_feature(value):
    """Wrapper for inserting bytes features into Example proto."""
    if not isinstance(value, list):
        value = [value]
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=value))


def _count(iterable):
    sum = 0
    for begin, end in iterable:
        sum += end - begin
    return sum


DATA_ROOT = join(dirname(__file__), 'dataset')
FONT_ROOT = join(dirname(__file__), 'fonts')
WIDTH = 32
HEIGHT = 32

# 0021 ~ 007E - Basic Latin
# 3130 ~ 318F - Hangul Compatibility Jamo, except 3130, 318F(unassigned) and 3164(not printable)
# AC00 ~ D7A3 - Hangul Syllables
_CHAR_RANGES = (
    (0x0021, 0x007F),
    (0x3131, 0x3164),
    (0x3165, 0x318F),
    (0xAC00, 0xD7A4)
)
MAX_CHARS = _count(_CHAR_RANGES)


def range_chars():
    '''
    Iterator for all characters used in dataset.
    '''
    for begin, end in _CHAR_RANGES:
        for ch in range(begin, end):
            yield chr(ch)


# Table mapped index (int) to label (str).
LABELS = {index : label for index, label in zip(range(MAX_CHARS), range_chars())}

# Table mapped label (str) to index (int).
INDEXES = {label : index for index, label in zip(range(MAX_CHARS), range_chars())}


def serialize(image, label):
    '''
    Serialize image and label to tfrecord.

    Args:
        image (numpy.ndarray):
        label (int):

    Returns:
        ... 
    '''
    sample, height, width, channel = image.shape

    example = tf.train.Example(features=tf.train.Features(feature={
        'image/width' : _int64_feature(width),
        'image/height' : _int64_feature(height),
        'image/channel' : _int64_feature(channel),
        'image/label' : _int64_feature(label),
        'image/data' : _floats_feature(image.flat)
    }))

    return example.SerializeToString()


_FEATURE_DESCRIPTION = {
    'image/width' : tf.io.FixedLenFeature([], tf.int64),
    'image/height' : tf.io.FixedLenFeature([], tf.int64),
    'image/channel' : tf.io.FixedLenFeature([], tf.int64),
    'image/label' : tf.io.FixedLenFeature([], tf.int64),
    'image/data' : tf.io.FixedLenSequenceFeature([], tf.float32, allow_missing=True)
}


def deserialize(raw_example):
    '''
    Deserialize image and label from string tensor.

    Args:
        raw_example: serialized tf.io.Example
    
    Returns:
        tuple of image and label.
    '''
    example = tf.io.parse_single_example(raw_example, _FEATURE_DESCRIPTION)

    width = example['image/width']
    height = example['image/height']
    channel = example['image/channel']
    label = example['image/label']
    data = example['image/data']

    return tf.reshape(data, (width, height, channel)), label


def _load(data_type):
    files = glob.glob(join(DATA_ROOT, data_type, '*.tfrecord'))

    return tf.data.TFRecordDataset(filenames=files, compression_type="GZIP").map(deserialize)


def load_train():
    '''
    Load train dataset.

    Returns:
        tf.data.Dataset contains train dataset.
    '''
    return _load('train')
    

def load_validation():
    '''
    Load validation dataset.

    Returns:
        tf.data.Dataset contains validation dataset.
    '''
    return _load('validation')


def load_test():
    '''
    Load test dataset.

    Returns:
        tf.data.Dataset contains test dataset.
    '''
    return _load('test')