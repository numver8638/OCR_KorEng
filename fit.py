#
# fit.py
# - Train model.
#
from datetime import datetime
import tensorflow as tf
from tensorflow.keras import layers, models, callbacks
from os.path import dirname, exists, join
import multiprocessing as mp

import dataset

PROJECT_ROOT = dirname(__file__)
MODELS_ROOT = join(PROJECT_ROOT, 'models')
LOGS_ROOT = join(PROJECT_ROOT, 'logs')
BATCH_SIZE = 16
EPOCHS = 20

def fit(folder_name):
    hp = load_hyperparams()

    train_data = dataset.load_train().shuffle(1000).batch(BATCH_SIZE)
    validation_data = dataset.load_validation().shuffle(1000).batch(BATCH_SIZE)

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

    model.summary()

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

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
        fit(sys.argv[1])
