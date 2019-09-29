#!/usr/bin/env bash
set -x
sam package --output-template packaged.yaml --s3-bucket ga-sam-app
