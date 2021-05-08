#
# tune_hyper.py
# - Hyperparameter tuner
#
import tensorflow as tf
from tensorflow.keras import models, layers, optimizers, losses
import kerastuner as kt
import json
from os.path import dirname, join

import dataset

PROJECT_ROOT = dirname(__file__)
LOGS_ROOT = join(PROJECT_ROOT, 'logs/hyperparams')
HYPERPARAMS_FILE = join(PROJECT_ROOT, 'hyperparams.json')  # Must be synchonized with fit.py.

#
# Hyperparamerters constants
#
EPOCHS = 50
MIN_FILTERS = 32
MAX_FILTERS = 256
FILTER_STEP = 32
MIN_UNITS = 32
MAX_UNITS = 512
UNIT_STEP = 32
MIN_DROPOUT = 0.2
MAX_DROPOUT = 0.5
DROPOUT_STEP = 0.05


def model_builder(hp):
    '''
    Build model.

    Args:
        hp (kerastuner.HyperParameters) : hyperparameters
    '''
    # Hyperparameters to be tuned.
    conv2d_0 = hp.Int('conv2d_0_filters', min_value=MIN_FILTERS, max_value=MAX_FILTERS, step=FILTER_STEP)
    conv2d_1 = hp.Int('conv2d_1_filters', min_value=MIN_FILTERS, max_value=MAX_FILTERS, step=FILTER_STEP)
    conv2d_2 = hp.Int('conv2d_2_filters', min_value=MIN_FILTERS, max_value=MAX_FILTERS, step=FILTER_STEP)
    dense_0 = hp.Int('dense_0_units', min_value=MIN_UNITS, max_value=MAX_UNITS, step=UNIT_STEP)
    dense_1 = hp.Int('dense_1_units', min_value=MIN_FILTERS, max_value=MAX_FILTERS, step=FILTER_STEP)
    dropout_0 = hp.Float('dropout_0', min_value=MIN_DROPOUT, max_value=MAX_DROPOUT, step=DROPOUT_STEP)
    dropout_1 = hp.Float('dropout_1', min_value=MIN_DROPOUT, max_value=MAX_DROPOUT, step=DROPOUT_STEP)
    dropout_2 = hp.Float('dropout_2', min_value=MIN_DROPOUT, max_value=MAX_DROPOUT, step=DROPOUT_STEP)
    learning_rate = hp.Choice('learning_rate', [1e-3, 1e-4, 1e-5])

    model = models.Sequential(layers=[
        layers.Conv2D(filters=conv2d_0, kernel_size=(3, 3), activation='relu', input_shape=(32, 32, 1)),
        layers.Dropout(dropout_0),
        layers.Conv2D(filters=conv2d_1, kernel_size=(3, 3), activation='relu'),
        layers.Dropout(dropout_1),
        layers.Conv2D(filters=conv2d_2, kernel_size=(3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(dense_0, activation='relu'),
        layers.Dropout(dropout_2),
        layers.Dense(dense_1, activation='relu'),
        layers.Dense(dataset.MAX_CHARS, activation='softmax')
    ])

    model.compile(optimizer=optimizers.Adam(learning_rate=learning_rate),
                  loss=losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    return model


def save_hyperparams(hp):
    '''
    Save hyperparameters into HYPERPARAMS_FILE.
    
    Args:
        hp (kerastuner.HyperParameters) : hyperparameters
    '''
    with open(HYPERPARAMS_FILE, 'w') as f:
        json.dump({
            'conv2d_0_filters' : hp.get('conv2d_0_filters'),
            'conv2d_1_filters' : hp.get('conv2d_1_filters'),
            'conv2d_2_filters' : hp.get('conv2d_2_filters'),
            'dense_0_units' : hp.get('dense_0_units'),
            'dense_1_units' : hp.get('dense_1_units'),
            'dropout_0' : hp.get('dropout_0'),
            'dropout_1' : hp.get('dropout_1'),
            'dropout_2' : hp.get('dropout_2'),
            'learning_rate' : hp.get('learning_rate')
        }, f)


def main():
    train_data = dataset.load_train().shuffle(1000).batch(32)
    validation_data = dataset.load_validation().shuffle(1000).batch(32)

    tuner = kt.Hyperband(model_builder,
                         objective='val_accuracy',
                         max_epochs=EPOCHS,
                         factor=3,
                         directory=LOGS_ROOT)
    
    tuner.search(train_data, validation_data=validation_data, epochs=EPOCHS)

    best_hps = tuner.get_best_hyperparameters()[0]

    save_hyperparams(best_hps)


if __name__ == '__main__':
    main()