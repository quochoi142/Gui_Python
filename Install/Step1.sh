#!/bin/sh
if [ $SUDO_USER ]; then USER=$SUDO_USER; else USER=`whoami`; fi



sudo sh -c "yes | sudo rm /var/lib/dpkg/lock"
sudo sh -c "yes | sudo dpkg --configure -a"


HATCHING=/home/$USER/.hatch

# Stop all HSB related process
sudo killall triage
sudo killall sandbox
sudo killall sandbox-net
sudo killall kwakd
sudo killall frontend
sudo killall hatchvmd

# Delete br0
sudo ip link delete br0 type bridge

# Create sandbox user if not existing (sandbox-net require user name "sandbox" for executing)
if getent passwd sandbox > /dev/null 2>&1; then
    echo "Sandbox user is existing"
else
    echo "Sandbox user has not existing yet, start to create"
    sudo adduser --disabled-password --gecos "" sandbox
fi


# clean haching dir
echo "[1/10]. Clean haching dir"
if [[ -d $HATCHING ]]; then
    rm -rf $HATCHING
fi
sudo -u $USER mkdir $HATCHING

# copy haching binary files
echo "[2/10]. Copy haching files"
# tar -C $HATCHING -xf ./hatching.tar
cp ./hatching $HATCHING
export PATH=$HATCHING:$PATH


if [[ ! -d $HATCHING/resources ]]; then
    sudo -u $USER mkdir $HATCHING/resources
fi
