#!/bin/sh

cd $(dirname $0)/..

ARGS=""

if [ "$2" = "-s" ];
    then
        echo "test output will be printed to console"
        ARGS="-s"
fi

if [ "$1" = "--actions" ];
    then
        poetry run coverage run -m pytest ${ARGS}

else
poetry run coverage run -m pytest ${ARGS}
poetry run coverage report -m
fi
