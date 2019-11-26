#!/bin/sh
file=$1
cd ~/.hatch
sudo sh -c "PATH=$HATCHING:$PATH $HATCHING/hatchvm -loglevel=trace generate $file"
