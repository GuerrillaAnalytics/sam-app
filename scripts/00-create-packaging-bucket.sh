#!/usr/bin/env bash
aws s3api create-bucket --bucket sam-app-pkg --region eu-west-1 --acl "private" --create-bucket-configuration LocationConstraint=eu-west-1