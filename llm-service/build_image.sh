#!/usr/bin/bash

docker build -t localhost:32000/llm-service .
docker push localhost:32000/llm-service
