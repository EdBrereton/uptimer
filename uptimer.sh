#!/bin/bash

HOME=/home/pi
BINDIR=$HOME/uptimer
VENVDIR=$BINDIR/env

cd $BINDIR
source $VENVDIR/bin/activate
$BINDIR/uptimer.py
