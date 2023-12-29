#!/bin/bash

docker-compose -f docker-compose-app.yaml build

docker-compose -f docker-compose-app.yaml up -d

echo -e "\nApplication is accessible at: http://localhost:8080/"
