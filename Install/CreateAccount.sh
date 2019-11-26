#!/bin/sh
# create postgres account
sudo sh -c "sudo -u postgres createuser triage_frontend"
sudo sh -c "sudo -u postgres psql -c \"ALTER USER triage_frontend PASSWORD 'test';\""
sudo sh -c "sudo -u postgres psql -c \"DROP DATABASE triage_frontend;\""
sudo sh -c "sudo -u postgres psql -c \"CREATE DATABASE triage_frontend;\""
sudo sh -c "$HATCHING/frontend-cli -v -c $HATCHING/www/frontend.yaml migrations -dir $HATCHING/www/migrations/ up"
sudo sh -c "$HATCHING/frontend-cli -c $HATCHING/www/frontend.yaml setup-company -company $1 -email $2 -first-name $3 -last-name $4 -password $5 -phone $6"