#!/usr/bin/env bash
set -x
aws cloudformation describe-stacks --stack-name aws-sam-getting-started --region eu-west-1 --query "Stacks[].Outputs"