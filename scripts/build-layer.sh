#!/usr/bin/env bash
# Build a simple data science layer using some common
# python libraries
#
# see https://nordcloud.com/lambda-layers-for-python-runtime/

set -x

echo 'Setting correct target build path for zipping a Python lambda'
export PY_DIR=build/python/lib/python3.7/site-packages
mkdir -p $PY_DIR

echo 'Installing requirements into correct lambda path'
pip install -r data-science-layer/requirements.txt -t $PY_DIR

echo 'Zipping everything under the python folder inclusive'
cd build
rm -f data-science-layer.zip
zip -r9 data-science-layer.zip .
#aws lambda publish-layer-version --layer-name data-science-layer --description "test layer for data science" --zip-file fileb://.aws-sam/build/python.zip --compatible-runtimes python3.7 --profile personal