#!/bin/bash
USER=$1
HATCHING=/home/$USER/.hatch
export PATH=$HATCHING:$PATH





#remove opswat script
sudo sh -c "rm $HATCHING/scripts/installhook-x*"
sudo sh -c "rm $HATCHING/scripts/patch.ps1"

# setup kvm
echo "[6/10]. Install nessary package"
sudo setfacl -m u:$USER:rwx /dev/kvm

# setup network
echo "[7/10]. Start sandbox-net process"
sudo $HATCHING/sandbox-net $HATCHING/data &

if [ -e $HATCHING/resources/en_windows_server_2016_x64_dvd_9718492.iso ]
then
    sudo sh -c "mv $HATCHING/resources/en_windows_server_2016_x64_dvd_9718492.iso $HATCHING/resources/winserver2016x64.iso"
fi


# cd $HATCHING
# for filename in $HATCHING/config/*.yaml; do
#     sudo sh -c "PATH=$HATCHING:$PATH $HATCHING/hatchvm -loglevel=trace generate $filename"
# done




# arr_interface="$(ls /sys/class/net | awk -F: '$0 ~ "eno|ens|eth"') "
# HOST_NET_INTERFACE=($arr_interface[0])
# HOST_IPV4_ADRESS="$(/sbin/ifconfig $HOST_NET_INTERFACE | grep 'inet ' | awk '{ print $2}')"

# # prepare hatchvmd.example.yaml, avoid network conflict
# sed -i "s/10.0.0.0/10.6.0.0/g" $HATCHING/hatchvmd.example.yaml
# sed -i "s/#bind: localhost:8080/bind: localhost:8080/g" $HATCHING/hatchvmd.example.yaml

# # prepare frontend.conf
# sed -i "s/dsn: user=postgres dbname=triage password=root sslmode=disable/dsn: user=triage_frontend dbname=triage_frontend password=test sslmode=disable/g" $HATCHING/www/frontend.yaml
# sed -i "s/url: http:\/\/localhost:43588/url: http:\/\/$HOST_IPV4_ADRESS:43588/g" $HATCHING/www/frontend.yaml
# sed -i "s/key:/key: 'anwvBynbUmNJItHgtJMxB7jMm+bI6IWvjW42Nkpwk1BlXPXzVq\/AYsN9'/g" $HATCHING/www/frontend.yaml
# sed -i "s/url: https:\/\/hatchvmd.hatching.io/url: http:\/\/localhost:8080/g" $HATCHING/www/frontend.yaml

# # delete MD-core config if existing
# sed -i "s/# MD-core config://g" $HATCHING/www/frontend.yaml
# sed -i "s/mdcore://g" $HATCHING/www/frontend.yaml
# sed -i "s/  url: http:\/\/192.168.100.100:8008//g" $HATCHING/www/frontend.yaml



# # Export sandbox to outside
# sed -i "s/bind: localhost:9012/bind: $HOST_IPV4_ADRESS:9012/g" $HATCHING/www/frontend.yaml
# sed -i "s/url_root: http:\/\/localhost:9012/url_root: http:\/\/$HOST_IPV4_ADRESS:9012/g" $HATCHING/www/frontend.yaml
# # export VNC to outside
# sed -i "s/recorder: \"http:\/\/localhost:43588\/\"/recorder: \"http:\/\/$HOST_IPV4_ADRESS:43588\/\"/g" $HATCHING/data/triage/conf/triage.yaml
# sed -i "s/nohup .\/kwakd -bind localhost:43588/nohup .\/kwakd -bind $HOST_IPV4_ADRESS:43588/g" $HATCHING/hatching.sh
# sed -i "s/    display_addr: localhost/    display_addr: $HOST_IPV4_ADRESS/g" $HATCHING/data/sandbox.yaml

# sed -i "s/csrf: ''/csrf: 'dpLfnM0VwrKW6eEI+TQCgZvctZgIASUpkiVOk4jKWJ9D6lsgE4UyJKOQ'/g" $HATCHING/www/frontend.yaml
# sed -i "s/session: ''/session: '6\/5BQKQmxrkBhYiy8RhPgf0mrarMw0B1NHz5k64ZOOiCljTwCBidteJA'/g" $HATCHING/www/frontend.yaml

