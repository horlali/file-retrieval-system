#!/bin/sh

set -e

# Go to root folder
cd $(dirname $0)/..

NAME="File-Retrieval-System"
PROJECT_DIR="${PWD}/src"
MODULE_NAME="file_retrieval_system/client.py"

echo "Starting ${NAME} client..."

streamlit run ${PROJECT_DIR}/${MODULE_NAME} --server.port 8501
