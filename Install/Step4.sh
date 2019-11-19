#!/bin/sh
HATCHING=/home/$USER/.hatch
# config pcap

aa-disable /usr/sbin/tcpdump
setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump


sudo killall sandbox-net

# start hatching

cd $HATCHING
sudo sh -c "PATH=$HATCHING:$PATH $HATCHING/hatching.sh"