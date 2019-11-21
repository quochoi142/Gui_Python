#!/bin/sh
HATCHING=/home/$USER/.hatch






arr_interface="$(ls /sys/class/net | awk -F: '$0 ~ "eno|ens|eth"') "
HOST_NET_INTERFACE=($arr_interface[0])
HOST_IPV4_ADRESS="$(/sbin/ifconfig $HOST_NET_INTERFACE | grep 'inet ' | awk '{ print $2}')"

# prepare hatchvmd.example.yaml, avoid network conflict
sed -i "s/10.0.0.0/10.6.0.0/g" $HATCHING/hatchvmd.example.yaml
sed -i "s/#bind: localhost:8080/bind: localhost:8080/g" $HATCHING/hatchvmd.example.yaml

# prepare frontend.conf
sed -i "s/dsn: user=postgres dbname=triage password=root sslmode=disable/dsn: user=triage_frontend dbname=triage_frontend password=test sslmode=disable/g" $HATCHING/www/frontend.yaml
sed -i "s/url: http:\/\/localhost:43588/url: http:\/\/$HOST_IPV4_ADRESS:43588/g" $HATCHING/www/frontend.yaml
sed -i "s/key:/key: 'anwvBynbUmNJItHgtJMxB7jMm+bI6IWvjW42Nkpwk1BlXPXzVq\/AYsN9'/g" $HATCHING/www/frontend.yaml
sed -i "s/url: https:\/\/hatchvmd.hatching.io/url: http:\/\/localhost:8080/g" $HATCHING/www/frontend.yaml

# delete MD-core config if existing
sed -i "s/# MD-core config://g" $HATCHING/www/frontend.yaml
sed -i "s/mdcore://g" $HATCHING/www/frontend.yaml
sed -i "s/  url: http:\/\/192.168.100.100:8008//g" $HATCHING/www/frontend.yaml



# Export sandbox to outside
sed -i "s/bind: localhost:9012/bind: $HOST_IPV4_ADRESS:9012/g" $HATCHING/www/frontend.yaml
sed -i "s/url_root: http:\/\/localhost:9012/url_root: http:\/\/$HOST_IPV4_ADRESS:9012/g" $HATCHING/www/frontend.yaml
# export VNC to outside
sed -i "s/recorder: \"http:\/\/localhost:43588\/\"/recorder: \"http:\/\/$HOST_IPV4_ADRESS:43588\/\"/g" $HATCHING/data/triage/conf/triage.yaml
sed -i "s/nohup .\/kwakd -bind localhost:43588/nohup .\/kwakd -bind $HOST_IPV4_ADRESS:43588/g" $HATCHING/hatching.sh
sed -i "s/    display_addr: localhost/    display_addr: $HOST_IPV4_ADRESS/g" $HATCHING/data/sandbox.yaml

sed -i "s/csrf: ''/csrf: 'dpLfnM0VwrKW6eEI+TQCgZvctZgIASUpkiVOk4jKWJ9D6lsgE4UyJKOQ'/g" $HATCHING/www/frontend.yaml
sed -i "s/session: ''/session: '6\/5BQKQmxrkBhYiy8RhPgf0mrarMw0B1NHz5k64ZOOiCljTwCBidteJA'/g" $HATCHING/www/frontend.yaml

