#!/bin/bash

export DD_SITE='datadoghq.com'
export DD_LLMOBS_ML_APP='quickstart'
export DD_LLMOBS_ENABLED=1
export DD_ENV='dev'

DD_LLMOBS_ENABLED=1 DD_LLMOBS_ML_APP=quickstart \
DD_API_KEY=${DD_API_KEY} DD_SITE=${DD_SITE} \
DD_LLMOBS_AGENTLESS_ENABLED=1 ddtrace-run python $1

rm_carefully () {
  rm -i $1
}
