#
# fit.py
# - Train model.
#
import tensorflow as tf
from tensorflow.keras import layers, models
from os.path import join, dirname
import dataset

PROJECT_ROOT = dirname(__file__)
MODEL_ROOT = join(PROJECT_ROOT, 'model')


def fit():
    train_data = dataset.load_train().shuffle(1000)
    validation_data = dataset.load_validation().shuffle(1000)

    model = models.Sequential(layers=[
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(dataset.MAX_CHARS, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    model.fit(train_data, epochs=50, validation_data=validation_data, verbose=2)
    model.save(MODEL_ROOT)


if __name__ == '__main__':
    fit()