#!/bin/sh

set -e

# Go to root folder
cd $(dirname $0)/..

NAME="File-Retrieval-System"
PROJECT_DIR="${PWD}/src"
MODULE_NAME="file_retrieval_system/server.py"

echo "Starting ${NAME} server..."

python ${PROJECT_DIR}/${MODULE_NAME}
