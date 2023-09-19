#!/bin/bash
docker run \
    --restart unless-stopped \
    -p 5002:5001 \
    -p 8081:8000 \
    -h tom.keilers.com \
    --name cv-website \
    cv-website
