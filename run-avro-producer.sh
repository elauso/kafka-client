#!/bin/bash
set -e

# check build image
if [ "$1" != "--skip-build" ]
then
    docker image build -f Dockerfile.avro_producer -t kafka-client-avro-producer:0.0.1 . 
fi

# run avro-producer-client
docker run --network="host" kafka-client-avro-producer:0.0.1