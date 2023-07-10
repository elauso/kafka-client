#!/bin/bash
set -e

# check build image
if [ "$1" != "--skip-build" ]
then
    docker image build -f Dockerfile.consumer -t kafka-client-consumer:0.0.1 . 
fi

# run consumer
docker run --network="host" kafka-client-consumer:0.0.1