#!/usr/bin/env bash

DATETIME=`date +%Y%m%d-%H%M%S`

source .venv/bin/activate

mkdir -p logs/$DATETIME models/$DATETIME

nohup python fit.py $DATETIME > logs/$DATETIME/tensorflow.log & disown
