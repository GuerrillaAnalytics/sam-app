#!/usr/bin/env bash
sam deploy --debug --template-file packaged.yaml --profile personal --capabilities CAPABILITY_IAM --stack-name aws-sam-getting-started --no-fail-on-empty-changeset
