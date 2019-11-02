#!/usr/bin/env bash
set -x

# Retaining the non-empty bucket while deleting the stack
aws cloudformation delete-stack --stack-name aws-sam-getting-started --retain-resources MyBucket