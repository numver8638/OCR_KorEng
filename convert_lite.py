#
# convert_lite.py
# - convert tensorflow model to tensorflow lite model.
#
import tensorflow as tf

def main(model_path, output_path):
    converter = tf.lite.TFLiteConverter.from_saved_model(model_path)

    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    converter.target_spec.supported_types = [tf.float16]

    with open(output_path, 'wb') as file:
        file.write(converter.convert())


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print("usage: python convert_lite.py model_path output_name")
    else:
        main(sys.argv[1], sys.argv[2])