#
# fit.py
# - Train model.
#
from datetime import datetime
import tensorflow as tf
from tensorflow.keras import layers, models, callbacks
import os
from os.path import dirname, exists, join
import multiprocessing as mp
import json

import dataset

PROJECT_ROOT = dirname(__file__)
MODELS_ROOT = join(PROJECT_ROOT, 'models')
LOGS_ROOT = join(PROJECT_ROOT, 'logs')
HYPERPARAMS_FILE = join(PROJECT_ROOT, 'hyperparams.json')

BATCH_SIZE = 32
EPOCHS = 50


def load_hyperparams():
    with open(HYPERPARAMS_FILE) as f:
        return json.load(f)


def fit(folder_name):
    hp = load_hyperparams()

    train_data = dataset.load_train().shuffle(1000).batch(BATCH_SIZE)
    validation_data = dataset.load_validation().shuffle(1000).batch(BATCH_SIZE)

    model = models.Sequential(layers=[
        layers.Conv2D(hp['conv2d_0_filters'], (3, 3), activation='relu', padding='same', input_shape=(32, 32, 1)),
        layers.Conv2D(hp['conv2d_1_filters'], (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(hp['dropout_0']),
        layers.Conv2D(hp['conv2d_2_filters'], (3, 3), activation='relu'),
        layers.Conv2D(hp['conv2d_3_filters'], (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(hp['dropout_1']),
        layers.Conv2D(hp['conv2d_4_filters'], (3, 3), activation='relu'),
        layers.Conv2D(hp['conv2d_5_filters'], (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(hp['dense_0_units'], activation='relu'),
        layers.Dropout(hp['dropout_2']),
        layers.Dense(hp['dense_1_units'], activation='relu'),
        layers.Dropout(hp['dropout_3']),
        layers.Dense(hp['dense_2_units'], activation='relu'),
        layers.Dense(dataset.MAX_CHARS, activation='softmax')
    ])

    model.summary()

    opt = tf.keras.optimizers.Adam(learning_rate=hp['learning_rate'])
    model.compile(optimizer=opt, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    
    model.fit(train_data,  
              epochs=EPOCHS, 
              validation_data=validation_data,
              verbose=2,
              callbacks=[
                  # Save log for tensorboard.
                  callbacks.TensorBoard(log_dir=join(LOGS_ROOT, folder_name), histogram_freq=1),
                  # Prevent overfitting.
                  callbacks.EarlyStopping(monitor='val_accuracy', mode='max', verbose=1, patience=5),
                  # Save checkpoint
                  callbacks.ModelCheckpoint(join(MODELS_ROOT, folder_name), monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')
                  # callbacks.LambdaCallback(on_epoch_end=log_confusion_matrix)
              ],
              workers=mp.cpu_count(),
              use_multiprocessing=True)

    test_data = dataset.load_test().shuffle(1000).batch(BATCH_SIZE)

    test_acc, test_loss = model.evaluate(test_data,
                                         verbose=2,
                                         callbacks=[
                                             callbacks.TensorBoard(log_dir=join(LOGS_ROOT, folder_name), histogram_freq=1)
                                         ],
                                         workers=mp.cpu_count(),
                                         use_multiprocessing=True)

    print("test_acc:", test_acc, "test_loss:", test_loss)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("usage: fit.py <folder_name>")
    elif not exists(HYPERPARAMS_FILE):
        print("hyperparams.json is not exist.")
    else:
        fit(sys.argv[1])
