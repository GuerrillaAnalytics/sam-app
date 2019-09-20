#!/usr/bin/env bash
pip install -r data-science-layer/requirements.txt -t .aws-sam//build/python/ --upgrade
zip -r9 .aws-sam/build/python.zip .aws-sam/build/python/
aws lambda publish-layer-version --layer-name data-science-layer --description "test layer for data science" --zip-file fileb://.aws-sam/build/python.zip --compatible-runtimes python3.7 --profile personal