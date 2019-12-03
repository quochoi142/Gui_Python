#!/bin/bash
USER=$1
HATCHING=/home/$USER/.hatch
export PATH=$HATCHING:$PATH
file=$2
cd ~/.hatch
sudo sh -c "PATH=$HATCHING:$PATH $HATCHING/hatchvm -loglevel=trace generate $file"
