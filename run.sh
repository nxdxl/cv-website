#!/bin/bash
docker run \
    --restart unless-stopped \
    -p 5002:5001 \
    -p 587:587 \
    -p 465:465 \
    -p 25:25 \
    -p 2525:2525 \
    --network host \
    --name cv-website \
    -h tom.keilers.com \
    cv-website
