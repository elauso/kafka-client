#!/bin/bash
set -e

# check build image
if [ "$1" != "--skip-build" ]
then
    docker image build -f Dockerfile.producer -t kafka-client-producer:0.0.1 . 
fi

# run producer-client
docker run --network="host" kafka-client-producer:0.0.1