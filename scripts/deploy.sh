#!/usr/bin/env bash
set -x
sam deploy --debug --template-file packaged.yaml --capabilities CAPABILITY_IAM --stack-name aws-sam-getting-started --no-fail-on-empty-changeset
