import tensorflow as tf
import preprocess
import cv2
import numpy as np
import dataset as ds
from PIL import ImageFont, ImageDraw, Image
from os.path import basename
import sys


def recognize(image_path):
    image = cv2.imread(image_path)

    height, width, _ = image.shape

    if height > 1024 or width > 1024:
        scale = 1024 / max(width, height)
        image = cv2.resize(image, (0,0), fx=scale, fy=scale)

    words = preprocess.preprocess_image(image)

    interpreter = tf.lite.Interpreter('model.tflite')
    interpreter.allocate_tensors()

    input_tensor = interpreter.get_input_details()[0]['index']
    output_tensor = interpreter.get_output_details()[0]['index']

    results = []
    for word, rect in words:
        word.resize((1, 32, 32, 1))
        interpreter.set_tensor(input_tensor, word)
        interpreter.invoke()

        res = interpreter.get_tensor(output_tensor)[0]
        idx = np.argmax(res)

        results.append((ds.LABELS[idx], res[idx] * 100.0, rect))

    return results

def main(image_path):
    font = ImageFont.truetype('fonts/NanumGothic.ttf', 12)
    image = Image.open(image_path)

    if image.width > 1024 or image.height > 1024:
        scale = 1024 / max(image.width, image.height)
    else:
        scale = 1

    draw = ImageDraw.Draw(image)

    for char, _, (x,y,w,h) in recognize(image_path):
        bbox = draw.textbbox((0,0), char, font=font)

        x /= scale
        y /= scale
        w /= scale
        h /= scale

        draw.rectangle((x,y, x+w, y+h), outline=(0,255,0))
        draw.text((x, y - bbox[3]), char, font=font, fill=(0,0,0))

    image.save(f'recognized-{basename(image_path)}.png')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('python recog.py <image>')